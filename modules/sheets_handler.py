# -*- coding: utf-8 -*-
import os.path
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

FIRST = 0
AUTH_SCOPES = ["https://www.googleapis.com/auth/drive"]


# REMOVE BEFORE FLIGHT REMOVE BEFORE FLIGHT REMOVE BEFORE FLIGHT
class Recipe(object):
    def __init__(self):
        self.title = ""
        self.products = list
        self.preparation_method = ""
        self.number_of_cooks = 0
        self.likes = ""
        self.chef_popularity = 0
        self.unique_products_length = 0
        self.identical_products_length = 0


# REMOVE BEFORE FLIGHT REMOVE BEFORE FLIGHT REMOVE BEFORE FLIGHT
# REMOVE BEFORE FLIGHT REMOVE BEFORE FLIGHT REMOVE BEFORE FLIGHT
test_recipe = Recipe()
test_recipe.title = "Test Title"
test_recipe.products = [
    "Test Product 1 - Test Amount 1",
    "Test Product 2 - Test Amount 2",
    "Test Product 3 - Test Amount 3"
]
test_recipe.preparation_method = "Test Preparation Method - Cook, Boil, Fry, Bake, But It's Still Not A Cake :("


# REMOVE BEFORE FLIGHT REMOVE BEFORE FLIGHT REMOVE BEFORE FLIGHT


def authorize_to_api(scope):
    """Authorize Scraper API to the Google APIs suite (Drive)"""
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file(
            "token.json", scope)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            application_flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", scope)
            credentials = application_flow.run_local_server(port=0)
        with open("token.json", mode="w") as token:
            token.write(credentials.to_json())
    print "Authorization successful!"
    return credentials


def handle_spreadsheet(credentials):
    """Check for the existence of Scraper's results spreadsheet
     and create if missing"""
    try:
        service_drive = build(serviceName="drive", version="v3", credentials=credentials)
        print "Connection to GoogleDrive established!"
        search_results = service_drive.files().list(q="name='ScraperResults'").execute()
        files = search_results.get("files")
        if files:
            file_ = files[FIRST]
            print "File: {0} exists!".format(file_.get("name"))
        else:
            file_body = {'name': 'ScraperResults', 'mimeType': 'application/vnd.google-apps.spreadsheet'}
            file_ = service_drive.files().create(body=file_body, fields="id").execute()
            print "File: ScraperResults created!"
        return file_.get("id")
    except HttpError as err:
        print "Error: {0}".format(err)


def handle_values(recipe):
    """Parse data from Recipe object to ValueRange object"""
    products_str = ""
    for product in recipe.products:
        products_str += product
    values = [
        [
            u"Заглавие:", recipe.title
        ],
        [
            u"Продукти:", products_str
        ],
        [
            u"Начин на приготвяне", recipe.preparation_method
        ],
        [
            time.asctime()
        ]
    ]
    return values


def upload_to_sheets(credentials, sheet_id, values):
    """Upload ValueRange object data to GoogleSheet's spreadsheet"""
    try:
        service_sheets = build(serviceName="sheets", version="v4", credentials=credentials)
        values_body = {"values": values}
        sheet = service_sheets.spreadsheets().values().append(
            spreadsheetId=sheet_id, range="Лист1!A:A",
            valueInputOption="RAW", insertDataOption="INSERT_ROWS",
            body=values_body).execute()
        print('{0} cells appended.'.format(sheet
                                           .get('updates')
                                           .get('updatedCells')))
    except HttpError as err:
        print "Error: {0}".format(err)


usr_creds = authorize_to_api(AUTH_SCOPES)
spreadsheet_id = handle_spreadsheet(usr_creds)
values_table = handle_values(test_recipe)
upload_to_sheets(usr_creds, spreadsheet_id, values_table)
