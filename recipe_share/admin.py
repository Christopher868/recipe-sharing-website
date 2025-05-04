from django.contrib import admin
from .models import CustomerMessage, UserRecipe, RecipeCategory

# Register your models here.
class UserRecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'created_by')

admin.site.register(RecipeCategory)
admin.site.register(CustomerMessage)
admin.site.register(UserRecipe, UserRecipeAdmin)