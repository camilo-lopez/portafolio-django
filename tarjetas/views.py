from django.shortcuts import render

# Create your views here.
def sumar(request):

    a = 1
    b = 2
    c = a + b
    context = {
        "c":c,
        "a":a,
        "b":b,
    }
    return render(request, 'resultado.html', context)
