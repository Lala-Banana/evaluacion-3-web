from django.shortcuts import render

# Create your views here.
def inicio(request):
    context = {}
    return render(request, 'tienda/inicio.html', context)