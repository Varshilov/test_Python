


def sort_by_recipe_rating_ascending(self):
    self.recipe_storage = sorted(self.recipe_storage,
                                 key=lambda r: r.rating,
                                 reverse=False)