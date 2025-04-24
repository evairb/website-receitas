from django.http import Http404
from django.views import View
from recipes.models import Recipe
from authors.forms import AuthorRecipeForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardRecipe(View):
    def get_recipe(self, id=None):
        recipe = None

        if id is not None:
            recipe = Recipe.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id,
            ).first()

            if not recipe:
                raise Http404()

        return recipe

    def render_recipe(self, context):
        return render(
            self.request, 'authors/pages/dashboard_recipe.html',
            context=context
        )

    def get(self, request, id=None):
        recipe = self.get_recipe(id)

        form = AuthorRecipeForm(instance=recipe)

        context = {
            'form': form,
        }
        return self.render_recipe(context)

    def post(self, request, id=None):
        print(id)
        recipe = self.get_recipe(id)

        form = AuthorRecipeForm(
            data=self.request.POST or None,
            files=self.request.FILES or None,
            instance=recipe
        )

        context = {
            'form': form,
        }

        if form.is_valid():
            recipe = form.save(commit=False)

            recipe.author = self.request.user
            recipe.preparation_steps_is_html = False
            recipe.is_published = False

            recipe.save()

            messages.success(
                self.request, 'Sua receita foi salva com sucesso!'
            )

            return redirect(
                reverse('authors:dashboard_recipe_edit', args=(recipe.id,))
            )
        return self.render_recipe(context)


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardRecipeDelete(DashboardRecipe):
    def post(self, *args, **kwargs):
        recipe = self.get_recipe(self.request.POST.get('id'))
        recipe.delete()
        messages.success(self.request, 'Deleted successfully')
        return redirect(reverse('authors:dashboard'))
