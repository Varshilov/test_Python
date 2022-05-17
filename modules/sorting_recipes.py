# -*- coding: utf-8 -*-
class Sorting:
    recipes = []

    def sort_asc_by_unique_products(self):
        """Sorts the recipes ascending by number of unique products"""
        sort_data = list(
            sorted(
                self.recipes,
                key=lambda x: (x.calculate_unique_products(x.products), x.calculate_identical_products(x.products)),
                reverse=False,
            )
        )
        for item in sort_data:
            print(item)

    def sort_desc_by_unique_products(self):
        """Sorts the recipes descending by number of unique products"""
        sort_data = list(
            sorted(
                self.recipes,
                key=lambda x: (x.calculate_unique_products(x.products), x.calculate_identical_products(x.products)),
                reverse=True,
            )
        )
        for item in sort_data:
            print(item)

    def sort_by_most_often_cooked(self):
        """Sorts the recipes descending by most often cooked dishes"""
        sort_data = list(
            sorted(
                self.recipes,
                key=lambda x: x.number_of_cooks,
                reverse=True,
            )
        )
        for item in sort_data:
            print(item)

    def sort_by_most_liked_dish(self):
        """Sorts the recipes descending by most liked dishes"""
        sort_data = list(
            sorted(
                self.recipes,
                key=lambda x: x.likes,
                reverse=True,
            )
        )
        for item in sort_data:
            print(item)

    def sort_by_chef_popularity(self):
        """Sorts the recipes descending by chef popularity"""
        sort_data = list(
            sorted(
                self.recipes,
                key=lambda x: x.chef_popularity,
                reverse=True,
            )
        )
        for item in sort_data:
            print(item)
