from django.contrib import admin

from .models import Recipe, Ingredient, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}


class IngredientAdmin(admin.ModelAdmin):
    # TODO: use djfractions for quantity field
    #fields = ('name', 'recipe', 'order')
    list_display = ('name', 'recipe', 'place')


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0
    fields = ['quantity', 'units', 'name', 'place']

    def get_extra(self, request, obj=None, **kwargs):
        '''Make it so no extra lines show if object already exists.'''
        if obj:
            return 0
        return self.extra

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'book_page']
    inlines = [IngredientInline]
    prepopulated_fields = {'slug':('title', )}


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
