from modules.scraped_data import ScrapedDAta
from modules.gotvach_scraper import GotvachScraper
from modules.sorting_recipes import Sorting

scraper = GotvachScraper()
scraper.set_recipes()
stored_data = ScrapedDAta()

for recipe in scraper.recipes:
    stored_data.add_recipe(recipe)
print(stored_data)

