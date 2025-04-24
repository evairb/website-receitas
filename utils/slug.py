from django.utils.text import slugify
from recipes.models import Recipe


def generate_unique_slug(title):
    slug = slugify(title)
    original_slug = slug
    counter = 1
    while Recipe.objects.filter(slug=slug).exists():
        slug = f"{original_slug}-{counter}"
        counter += 1
    return slug
