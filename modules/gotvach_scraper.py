# -*- coding: utf-8 -*-
from __future__ import print_function
import requests
from bs4 import BeautifulSoup
from arg_parser import Arguments
# from modules.product import Product
from ChefProfile import ChefProfile
from product_builder import ProductBuilder
from recipe_builder import RecipeBuilder


class GotvachScraper:
    GOTVACH_URL = "https://recepti.gotvach.bg/?kw="

    agent = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.127 Safari/537.36'
    }

    def __init__(self):
        self.args = Arguments()
        self.dishes_count = self.args.n_dishes
        self.url_by_products = self.set_url_by_products()
        self.url_by_last_cooked = self.set_url_by_last_cooked()
        self.url_by_recipe = self.set_url_by_recipe()
        self.recipes = []

    def set_url_by_products(self):
        urls = []
        page_url = self.GOTVACH_URL
        if self.args.products:
            product_url = "%20".join(self.args.products)
            page_url += product_url

        page = requests.get(page_url, headers=self.agent)
        soup = BeautifulSoup(page.content, "lxml")
        results = soup.find(id="searchRecipes")
        recipes_names = results.find_all("a", class_="title")
        for title in recipes_names:
            link_url = title["href"]
            urls.append(link_url)
        return urls

    def set_recipes_by_product(self):
        products_list = []

        try:
            for number in range(0, self.dishes_count):
                url = self.url_by_products[number]
                page = requests.get(url, headers=self.agent)
                soup = BeautifulSoup(page.content, "lxml")
                result = soup.find(id="content")
                for item in range(len(result.find("ul"))):
                    new_product = ProductBuilder(result.find("ul").find_all("li")[item].text)
                    products_list.append(new_product)

                recipe_title = result.find_all("h1")[0].text
                new_cooker = ChefProfile(base_url=url, agent=self.agent)
                recipe = RecipeBuilder(recipe_id=number, dish_name=recipe_title, products=products_list,
                                       cooker=new_cooker)
                self.recipes.append(recipe)
                # print(self.recipes[i])
        except IndexError:
            print("No more recipes with these parameters!")

    def set_url_by_last_cooked(self):
        urls = []
        url_last_cooked = "https://recepti.gotvach.bg/cook"
        page = requests.get(url_last_cooked, headers=self.agent)
        soup = BeautifulSoup(page.content, "lxml")
        results = soup.find(id="lastCook")
        recipes_names = results.find_all("a", class_="title")
        for name in recipes_names:
            link_url = name["href"]
            urls.append(link_url)
        return urls

    def set_recipes_by_last_cooked(self):
        products_list = []

        try:
            for number in range(0, self.dishes_count):
                url = self.url_by_last_cooked[number]
                page = requests.get(url, headers=self.agent)
                soup = BeautifulSoup(page.content, "lxml")
                result = soup.find(id="content")

                for item in range(len(result.find("ul"))):
                    new_product = ProductBuilder(result.find("ul").find_all("li")[item].text)
                    products_list.append(new_product)

                recipe_title = result.find_all("h1")[0].text
                new_chef = ChefProfile(base_url=url, agent=self.agent)
                recipe = RecipeBuilder(recipe_id=number, dish_name=recipe_title, products=products_list,
                                       cooker=new_chef)
                self.recipes.append(recipe)
                # print(self.recipes[i])
        except IndexError:
            print("Can`t find any more recipes with the given params!")

    def set_url_by_recipe(self):

        urls = []
        page_url = self.GOTVACH_URL
        if self.args.dish_name:
            page_url += self.args.dish_name
        page = requests.get(page_url, headers=self.agent)
        soup = BeautifulSoup(page.content, "lxml")
        results = soup.find(id="searchRecipes")
        recipes_names = results.find_all("a", class_="title")
        for name in recipes_names:
            link_url = name["href"]
            urls.append(link_url)
        return urls

    def set_recipes_by_recipe_name(self):
        products_list = []

        try:
            for number in range(0, self.dishes_count):
                url = self.url_by_recipe[number]
                page = requests.get(url, headers=self.agent)
                soup = BeautifulSoup(page.content, "lxml")
                result = soup.find(id="content")

                for item in range(len(result.find("ul"))):
                    new_product = ProductBuilder(result.find("ul").find_all("li")[item].text)
                    products_list.append(new_product)

                recipe_title = result.find_all("h1")[0].text
                new_cooker = ChefProfile(base_url=url, agent=self.agent)
                recipe = RecipeBuilder(recipe_id=number, dish_name=recipe_title, products=products_list,
                                       cooker=new_cooker)
                self.recipes.append(recipe)
                # print(self.recipes[i])
        except IndexError:
            print("Can`t find any more recipes with the given params!")

    def set_recipes_by_agents_urls(self):
        pass

    def set_recipes_by_agents(self):
        pass

    def set_recipes(self):
        if self.args.products:
            self.set_recipes_by_product()
        if self.args.last_cooked:
            self.set_recipes_by_last_cooked()
        if self.args.dish_name:
            self.set_recipes_by_recipe_name()

