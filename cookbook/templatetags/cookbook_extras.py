from django import template
from cookbook.models import Category

register = template.Library()

@register.inclusion_tag('cookbook/cats.html')
def get_category_list(cat=None):
	# TODO: ordering
	return {'cats': Category.objects.all(), 'act_cat': cat}