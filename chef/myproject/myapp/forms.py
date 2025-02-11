from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'start_date', 'end_date',
            'breakfast_day1', 'snack_day1', 'dinner_day1', 'total_calories_day1',
            'breakfast_day2', 'snack_day2', 'dinner_day2', 'total_calories_day2',
            'breakfast_day3', 'snack_day3', 'dinner_day3', 'total_calories_day3',
            'breakfast_day4', 'snack_day4', 'dinner_day4', 'total_calories_day4',
            'breakfast_day5', 'snack_day5', 'dinner_day5', 'total_calories_day5'
        ]
