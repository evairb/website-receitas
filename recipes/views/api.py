from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from tag.models import Tag
from recipes.serializers import TagSerializer

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


@api_view()
def recipe_api_list(request):
    recipes = Recipe.objects.get_published()[:10]
    serializer = RecipeSerializer(
        instance=recipes,
        many=True,
        context={'request': request}
    )
    return Response(serializer.data)


@api_view()
def recipe_api_detail(request, pk):
    recipes = get_object_or_404(
        Recipe.objects.get_published(),
        pk=pk
    )
    serializer = RecipeSerializer(
        instance=recipes,
        many=False,
        context={'request': request}
    )
    return Response(serializer.data)


@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )
    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={'request': request}
    )
    return Response(serializer.data)
