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

    name = models.CharField(max_length=100)
    recipe_category = models.ForeignKey(RecipeCategory, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='recipe-images/', default='', null=True, blank=True)
    difficulty = models.CharField(max_length=13, choices=difficulty_options)
    instructions = models.TextField(validators=[MaxLengthValidator(1000)], help_text="Max Characters 1000 | Please make sure instructions are clear and easy to understand!")
    equipment = models.TextField(validators=[MaxLengthValidator(500)], help_text="Max Characters 500 | Please make sure equipment list is easy to understand!")
    created_at = models.DateField(auto_now_add=True, editable=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', editable=False, null=True)

    def __str__(self):
        if self.created_by is None:
            return f"{self.name} {self.created_at}"
        else:
            return f"{self.created_by} {self.name} {self.created_at}"
        

