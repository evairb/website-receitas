from django.urls import reverse, resolve  # type: ignore
from recipes.views import site
from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewsTeste(RecipeTestBase):
    # Testes da Category
    def test_recipe_category_template_dont_not_load_recipes_not_published(self):  # noqa
        """Test category is_published False dont show"""
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id':recipe.category.id})) # noqa

        self.assertEqual(response.status_code, 404)

    def test_recipe_category_templates_loads_recipes(self):
        needed_title = 'This is a category test'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1, )))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func.view_class, site.RecipeListViewCategory)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
