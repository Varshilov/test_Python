# WEB SCRAPER

# I. Summary
The purpose of this project is to make a python scraper and get n-number recipes from https://recepti.gotvach.bg, 
then to sort the data based on given criteria, such as: product(s), dish name, last cooked 
and allergens. After that we have to extract the gathered data, sort it and 
upload the file to Google sheet. The data must be presented with graphical tables.

## II. Requirements
To successfully run the project you need to install all the modules from the requirements.txt file.
If a pop-up "install requirements.txt" from PyCharm doesn't show you can install it with the $ pip install -r requirements.txt
command from the venv terminal
-beautifulsoup4==4.9.3
-certifi==2021.10.8
-chardet==4.0.0
-mock==3.0.5
-numpy==1.16.6
-pandas==0.24.2
-requests==2.27.1
-urllib3==1.26.9
-lxml==4.8.0
The web scraper is build in python2.7 and run under venv
 to install python 2.7 - sudo apt install python2-minimal
 to install pip - sudo python2 get-pip.py
 to install venv - pip2 install virtualenv



## III. Usage
 
The script is used to gather data from https://recepti.gotvach.bg/.
You can write the following command in your terminal:
  ```
  python main.py [-h] [-a <allergens>]
                 [-n <number of dishes>] [-l <last cooked>]
                 [-n <number of dishes>] [-p <products>]
                 [-n <number of dishes>] [-d <dish>] 
  ```
About the optional arguments:
  * -h,                    show this help message and exit
  * -n <number of dishes>  give number of dishes as an input
  * -a <allergens>         give list of allergens as an input
  * -l <last cooked>       give input search criteria option "last cooked"
  * -p <products>          give a list of products as a search criteria
  * -d <dish>              give a name of a dish as a search criteria  
  ...

an example of how to start the program will be:
  -     python main.py -n 5 -p domati
        python main.py -n 3 -d omlet
        python main.py -n 4 -l (for last cooked, no need to specify)
  
## IV.Overall requirements
    Tests, documentation, OOP design

## V.Technical Details:
Technical Details:
    ArgParser implementation - get user input and parse it as an arguments
    Scraping - get data from https://recepti.gotvach.bg/, the script uses request and Beautiful Soup
    Data collector implementation - accepts and organize parsed data in JSON format
    Data sender implementation - provide API to send the data to Google Sheets
    Tests implementation

// todo sorting by wanted criteria
// todo extracting to json
// todo importing json go Google Sheets
// todo put some comments to clarify the workflow