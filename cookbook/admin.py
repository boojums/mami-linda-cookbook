from django.contrib import admin

from .models import Recipe, Ingredient, Category



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}


# TODO: save multiple ingredients at once in the admin form
class IngredientAdmin(admin.ModelAdmin):
    # TODO: use djfractions for quantity field
    #fields = ('name', 'recipe', 'order')
    list_display = ('name', 'recipe', 'place')


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title', )}


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
