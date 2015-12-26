import django_filters
from .models import Recipe

class RecipeFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_type='icontains')

	class Meta:
		model = Recipe
		fields = ['title', 'category', 'serves']

