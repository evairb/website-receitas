from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from tag.models import Tag
from recipes.serializers import TagSerializer
from rest_framework import status

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


@api_view(http_method_names=['get', 'post'])
def recipe_api_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.get_published()[:10]
        serializer = RecipeSerializer(
            instance=recipes,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )


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
