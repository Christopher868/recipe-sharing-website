from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MaxLengthValidator

# Model for storing customer messages
class CustomerMessage(models.Model):
    email = models.EmailField(max_length=100)
    message = models.TextField(validators=[MaxLengthValidator(500)], help_text="Max Characters 500")
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.email} ({self.date})"



# Model for recipe categories
class RecipeCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category-images/', default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Recipe categories"

    def __str__(self):
        return self.name


# Model for user created recipes
class UserRecipe(models.Model):

    difficulty_options = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    recipe_name = models.CharField(max_length=100, help_text='Please give your recipe a good name | Max Characters 100')
    recipe_category = models.ForeignKey(RecipeCategory, on_delete=models.SET_NULL, null=True, help_text='Please choose category for your recipe')
    recipe_picture = models.ImageField(upload_to='recipe-images/', default='', null=True, blank=True, help_text="Please take a good picture of recipes final product and include it here")
    recipe_difficulty = models.CharField(max_length=13, choices=difficulty_options, help_text="Please choose difficulty that matches your recipe the best")
    instructions = models.TextField(validators=[MaxLengthValidator(2000)], help_text="Please carefully explain instructions for your recipe | Please use to enter to go down a line to between each step | Max Characters 2000")
    required_equipment = models.TextField(validators=[MaxLengthValidator(1000)], help_text="Please include that tools will be needed for this recipe | Please use enter to go down a line between in each piece of equipment | Max Characters 1000")
    created_at = models.DateField(auto_now_add=True, editable=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', editable=False, null=True)

    def __str__(self):
        if self.created_by is None:
            return f"{self.recipe_name} {self.created_at}"
        else:
            return f"{self.created_by} {self.recipe_name} {self.created_at}"
        

