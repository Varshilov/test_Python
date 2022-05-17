# coding=utf-8
import requests
from bs4 import BeautifulSoup


class ChefProfile:
    def __init__(self, base_url, agent):
        self.base_url = base_url
        self.agent = agent
        self.cooker_name = self.filter_cooker_name()
        self.cooker_hats = self.k_filter(self.filter_hats())
        self.likes = self.k_filter(self.filter_likes())
        self.cooked_recipe = self.k_filter(self.filter_cooked_recipe())

    def filter_cooker_name(self):
        link = requests.get(self.base_url, headers=self.agent)
        soup = BeautifulSoup(link.content, "lxml")
        cooker_name = soup.find("div", {"class": "aub"}).select_one("a", href=False).text
        return cooker_name

    def filter_hats(self):
        link = requests.get(self.base_url, headers=self.agent)
        soup = BeautifulSoup(link.content, "lxml")
        cooker_hats = soup.find("div", {"class": "aub"}).select_one("span.icb-hat").text
        return cooker_hats

    def filter_likes(self):
        link = requests.get(self.base_url, headers=self.agent)
        soup = BeautifulSoup(link.content, "lxml")
        likes = soup.find("div", {"class": "aub"}).select_one("span.icb-hrt").text
        return likes

    def filter_cooked_recipe(self):
        link = requests.get(self.base_url, headers=self.agent)
        soup = BeautifulSoup(link.content, "lxml")
        cooked_recipe = soup.find("div", {"class": "aub"}).select_one("span.icb-plt").text
        return cooked_recipe

    @staticmethod
    def k_filter(str_recipe_info):
        k_flag = False
        if u"k" in str_recipe_info:
            k_flag = True
        in_number = float("".join(number for number in str_recipe_info if number.isdigit()))
        if k_flag:
            in_number *= 1000
        return in_number

    def get_cooker_rating(self):
        cooker_rating = (self.cooker_hats + self.likes + self.cooked_recipe) // 3
        return cooker_rating

    def __eq__(self, other):
        if self.get_cooker_rating() == other.get_ratings():
            return True
        return False

    def __lt__(self, other):
        if self.get_cooker_rating() < other.get_ratings():
            return True
        return False

    def __gt__(self, other):
        if self.get_cooker_rating() > other.get_ratings():
            return True
        return False

    def __str__(self):
        return "Cooker name: {}\nCooker hats: {}\tCooker likes: {}\tnum of cooked recipe: {}\nCooker Rating: {}" \
            .format(self.cooker_name.encode("utf-8"),
                    self.cooker_hats, self.likes, self.cooked_recipe,
                    self.get_cooker_rating())
