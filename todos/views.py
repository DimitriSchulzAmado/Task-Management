from django.shortcuts import render

def home(request):
    ''' what need to do when the view is executed '''
    return render(request, 'todos/home.html')
