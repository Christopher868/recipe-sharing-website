from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth import logout
from .forms import LoginForm, CreateUserForm, ChangeUser, CreateRecipe
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import CustomerMessage, UserRecipe, RecipeCategory
import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.paginator import Paginator


# View for loading the homepage
def home(request):
    categories = RecipeCategory.objects.all()
    most_liked = UserRecipe.objects.order_by('-likes')[:10]
    return render(request, 'home.html', {'categories': categories, 'recipes':most_liked})


# View for loading login page and logging user into their account
def login_user(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request, "Successfully logged in!")
                    return redirect(request.META.get('HTTP_REFERER', '/'))
                else:
                    form.add_error(None, "Invalid username or password!")
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})


# View for logging out a user
def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect(request.META.get('HTTP_REFERER', '/'))


# View for loading register page and registering a new user
def register_user(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                messages.success(request, "Account Successfully Created! You have been logged in.")
                return redirect("homepage")
        else:
            form = CreateUserForm()

        return render(request, 'register.html', {'form': form})


# View for editing profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved successfully!')
            return redirect('homepage')
    else:
        form = ChangeUser(instance=request.user)
    return render(request, 'edit-profile.html', {'form': form})


# View for changing password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'New password saved!')
            return redirect('edit-profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change-password.html', {'form': form})


# View for storing customer messages
@require_POST
def contact(request):
        email = request.POST.get('email')
        message= request.POST.get('message')
        date = datetime.date.today()
        CustomerMessage.objects.create(email=email, message=message, date=date)
        messages.success(request, 'Message Sent!')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    

# View for page that allows users to create recipes
@login_required
def create_recipe(request):
    if request.method =='POST':
        form = CreateRecipe(request.POST, request.FILES)
        if form.is_valid:
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            messages.success(request, "Successfully created new recipe!")
            return redirect('create-recipe')
    else: 
        form = CreateRecipe()  
    return render(request, 'create-recipe.html', {'form': form})


# View for page that displays recipes
def recipes(request, filter):
    if filter != 'All':
        recipes = UserRecipe.objects.filter(recipe_category__name=filter)
    else:
        recipes = UserRecipe.objects.all()
    categories = RecipeCategory.objects.all()
    paginator = Paginator(recipes, 10)

    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)
    
    return render(request, 'recipes.html', {'filter':filter, 'categories': categories, 'recipes': recipes})


# Filters recipes by categories
def filter_recipes(request):
    filter = request.GET.get('category')

    return redirect('recipes', filter=filter)


# View for page that allows you to view the specifics of a recipe
def view_recipe(request, recipe_id):
    from_search = request.GET.get('from') == 'search'
    user = request.user
    recipe = get_object_or_404(UserRecipe, id=recipe_id)
    return render(request, 'view-recipe.html', {'recipe': recipe, 'user': user, 'from_search': from_search})


# View that displays recipes the user has created
def my_recipes(request):
    user = request.user
    filter = request.POST.get('category')
    recipes = get_list_or_404(UserRecipe, created_by=user)
    if request.method == 'POST':
        if filter != None or filter != 'All':
            recipes = UserRecipe.objects.filter(recipe_category__name=filter, created_by=user)

    paginator = Paginator(recipes, 10)

    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)
        
    categories = RecipeCategory.objects.all()
    return render(request, 'my-recipes.html', {'recipes':recipes, 'categories':categories, 'filter':filter})


# View for editing a recipe
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(UserRecipe, id=recipe_id)
    if recipe.created_by == request.user:
        if request.method == 'POST':
            form =CreateRecipe(request.POST, instance=recipe)
            if form.is_valid():
                form.save()
                messages.success(request, 'Changes Saved!')
                return redirect ('view-recipe', recipe_id=recipe.id)
        else:
            form = CreateRecipe(instance=recipe)
    else:
        messages.success(request, 'Only the creator of a recipe can edit it!')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'edit-recipe.html', {'recipe': recipe, 'form': form})


# View for deleting a recipe
def delete_recipe(request, recipe_id):
    recipe = UserRecipe.objects.get(id=recipe_id)
    if request.user == recipe.created_by:
        recipe.delete()
        messages.success(request, 'Recipe successfully deleted!')
        return redirect('homepage')
    else:
        messages.success(request, 'Recipe can only be deleted by creator!')
        return redirect('homepage')


# View for liking a post 
@login_required
@require_POST
def like_post(request):
    recipe_id = request.POST.get('recipe_id')
    recipe = UserRecipe.objects.get(id=recipe_id)

    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)
        liked = False
    else:
        recipe.likes.add(request.user)
        liked = True
    
    return JsonResponse({'liked': liked, 'likes_count': recipe.total_likes()})


# View for displaying user search results
def search(request):
    category = request.GET.get('category')
    query = request.GET.get('search')
    print(query)
    
    if category == 'recipe-name':
        recipes = UserRecipe.objects.filter(recipe_name__contains=query)
    elif category == 'author-name':
        recipes = UserRecipe.objects.filter(created_by__username__icontains=query)
    
    paginator = Paginator(recipes, 10)

    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)
    
    return render(request, 'search.html', {'recipes': recipes, 'query': query, 'category': category})
