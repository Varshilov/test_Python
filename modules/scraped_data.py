class ScrapedDAta:
    def __init__(self):
        self.scraped_data_list = []

    def add_recipe(self, recipe):
        self.scraped_data_list.append(recipe)

    def export_to_google_sheets(self):
        pass

    def export_to_file(self):
        pass

    def __str__(self):
        return "Recipes:\n\n{}".format("\n".join([recipe.__str__() for recipe in self.scraped_data_list]))

