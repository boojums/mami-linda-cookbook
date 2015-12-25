from django.db import models
from django.template.defaultfilters import slugify

class Tag(models.Model):
    # TODO: tags for different things?
    pass

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
    category = models.ForeignKey(Category)
    serves = models.IntegerField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    instructions = models.TextField()
    preptime = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    recipe = models.ForeignKey(Recipe)
    # TODO: use latest djfractions with DecimalFractionField
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
        ('qt', 'quart')
        )

    units = models.CharField(max_length=40, 
                             choices=units_choices,
                             null=True, blank=True)
    place = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        #unique_together = 
        pass