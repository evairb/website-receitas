from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrom_browser
import time
from recipes.tests.test_recipe_base import RecipeMixing


class RecipeBaseFunctionalTest(StaticLiveServerTestCase, RecipeMixing):
    def setUp(self):
        self.browser = make_chrom_browser()
        return super().setUp()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=3):
        time.sleep(seconds)
