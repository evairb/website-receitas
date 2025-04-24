from django.urls import reverse, resolve  # type: ignore
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeDetailViewsTeste(RecipeTestBase):
    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, views.RecipeDetail)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_templates_loads_recipes(self):
        needed_title = 'This is a detail test - It load one recipe'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:recipe',kwargs={'pk': 1}))  # noqa
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)
