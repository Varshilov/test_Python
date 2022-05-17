from ChefProfile import ChefProfile


class RecipeBuilder:
    def __init__(self, recipe_id, dish_name=str, products=[], cooker=ChefProfile):
        self.id = recipe_id
        self.dish_name = dish_name
        self.products = products
        self.cooker = cooker
        # self.agents = []

    def __str__(self):
        return "{}\n{}\n{}\n{}\n" \
            .format(self.id, self.dish_name.encode("utf-8"),
                    "\n\t".join([product.__str__() for product in
                                 self.products]), self.cooker)
