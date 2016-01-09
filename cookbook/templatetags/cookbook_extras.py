from django import template
from cookbook.models import Category

register = template.Library()


@register.inclusion_tag('cookbook/cats.html')
def get_category_list(cat=None):
    cats = sorted(Category.objects.all(), key=lambda a: a.first_page())
    return {'cats': cats,
            'act_cat': cat}
