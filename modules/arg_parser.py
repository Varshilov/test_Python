# -*- coding: utf-8 -*-
from __future__ import print_function
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


class Arguments:
    def __init__(self):
        self.parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
        self.arg_input()
        self.args = self.parser.parse_args()
        self.n_dishes = self.set_n_dishes()
        self.products = self.set_products()
        self.last_cooked = self.set_last_cooked()
        self.dish_name = self.set_dish_name()
        # self.food_allergens = self._set_food_allergens()

    def arg_input(self):
        self.parser.add_argument("-n", "--number", type=int, help="store number of recipes", required=True)
        self.parser.add_argument("-l", "--last_cooked", action="store_true", help="choose from last cooked recipes")
        self.parser.add_argument("-p", "--products", type=str, nargs="+", help="choose particular product")
        self.parser.add_argument("-d", "--dish_name", type=str, help="store the name of the dish")

    def set_n_dishes(self):
        return self.args.number

    def set_products(self):
        return self.args.products

    def set_last_cooked(self):
        return self.args.last_cooked

    def set_dish_name(self):
        return self.args.dish_name

    # def _set_food_allergens(self):
    # return self.args.agents
