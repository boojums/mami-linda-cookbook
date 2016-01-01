from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

class Tag(models.Model):
    # TODO: tags for different things?
    name = models.CharField(max_length=128, unique=True, default='')

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, default='')
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    alt_title = models.CharField(max_length=128, blank=True, null=True)
    book_page = models.IntegerField()
    category = models.ForeignKey(Category)
    serves = models.IntegerField(blank=True, null=True)
    serves_upper = models.IntegerField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    # For easy autosplitting of copypasted ingredients lists
    blob_ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField()
    preptime = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


def createIngredients(sender, instance, created, **kwargs):
    ''' Create ingredients from blob if it isn't empty.'''
    # TODO: This isn't very pretty, probably a better way with 
    # forms. How do the admin inline forms do it?
    if instance.blob_ingredients and instance.blob_ingredients != '':
        Ingredient.objects.filter(recipe=instance).delete()
        ingredients = instance.blob_ingredients.split('\r\n')
        for elem in ingredients:
            Ingredient.objects.create(name=elem, recipe=instance)
        instance.blob_ingredients = ''
        instance.save()
       

signals.post_save.connect(createIngredients, sender=Recipe)

# TODO: unique place + recipe?
class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    recipe = models.ForeignKey(Recipe)
    # TODO: use latest djfractions with DecimalFractionField?
    quantity = models.DecimalField(null=True, blank=True, 
                                   max_digits=10, 
                                   decimal_places=5)
    units_choices = (
        ('tsp', 'teaspoon'),
        ('tbl', 'tablespoon'),
        ('cup', 'cup'),
        ('oz', 'ounce'),
        ('lb', 'pound'),
        ('dash', 'dash',),
        ('can', 'can'),
        ('qt', 'quart'),
        ('g', 'grams'),
        ('ml', 'millileters'),
        ('l', 'liters')
        )

    units = models.CharField(max_length=40, 
                             choices=units_choices,
                             null=True, blank=True)

    place = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.place:
            existing_places = Ingredient.objects.filter(recipe=self.recipe)\
                                                .order_by('-place')
            if existing_places:
                self.place = existing_places[0].place + 1
            else:
                self.place = 1
        super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        quantity = '{:.2f}'.format(self.quantity) if self.quantity else ''
        units = self.units if self.units else ''
        # TODO: pretty repr with proper fraction quantities
        return '{} {} {}'.format(quantity, units, self.name)

    class Meta:
        #unique_together = 
        pass