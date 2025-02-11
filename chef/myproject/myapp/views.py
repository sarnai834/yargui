from django.shortcuts import render, redirect
from .models import Food  
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from .models import Food, FoodMenu
from django.db.models import Q
from .models import Food  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def some_view(request):
    if not request.user.groups.filter(name='Web Users').exists():
        return HttpResponse("You don't have permission to access this page.")
    return render(request, 'home.html')
def logout_view(request):
    logout(request)  # Clears the session and logs the user out
    return redirect('/') 
def show(request):
    return render(request,"home.html")

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        ingredients = request.POST['ingredients']
        calories = request.POST['calories']
        serving_size = request.POST['serving_size']
        Food.objects.create(name=name, ingredients=ingredients, calories=calories, serving_size=serving_size)
        return redirect('food_list')
    return render(request, 'add_food.html')

def food_list(request):
    query = request.GET.get('query', '')  # Get the search query from the GET request
    foods = Food.objects.all()  # Get all foods by default

    # If there's a search query, filter the food list
    if query:
        foods = foods.filter(name__icontains=query)  # Filter foods by name (case-insensitive)

    # Prepare context to pass to the template
    context = {
        'foods': foods,
        'query': query
    }

    return render(request, 'food_list.html', context)

def add_menu(request):
    return render(request, 'add_menu.html')

from django.shortcuts import render

def menu_list(request):
    # Logic to fetch menu items, etc.
    return render(request, 'menu_list.html')


from django.shortcuts import render
from .models import MealMenu

from django.shortcuts import render
from .models import MealMenu
from datetime import datetime

def menu_search(request):
    query_set = MealMenu.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            query_set = query_set.filter(date__range=[start_date, end_date])
        except ValueError:
            pass  # Хэрэв буруу форматтай бол хайлт хийхгүй

    return render(request, 'menu_search.html', {'meal_menus': query_set})

def calculate_calories(request):
    return render(request, 'calculate_calories.html')
