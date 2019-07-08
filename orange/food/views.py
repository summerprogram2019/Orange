from django.shortcuts import render
from food.models import Food

# Create your views here.
def add_food(request):
    return render(request, 'food/add_food.html')

def view_all_food(request):

    args = {
        'foods' : Food.objects.all()
    }

    return render(request, 'food/view_all_food.html', args)

def view_food(request, id):

    args = {
        'food' : Food.objects.get(pk=id)
    }

    return render(request, 'food/view_food.html', args)
