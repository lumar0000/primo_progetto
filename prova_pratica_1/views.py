from django.shortcuts import render
import random
# Create your views here.
def view_a(request):
    var1 = random.randint(1,10)
    var2 = random.randint(1,10)
    var3 = var1+var2
    context = {
        'var1' : var1,
        'var2' : var2,
        'var3' : var3,
    }
    return render(request, "minmax.html", context)

def view_b(request):
    media = 0
    list1 = []
    while(list1.__len__()<30) : 
        i = random.randint(1,10)
        list1.append(i)
        media += i
    media = media/30
    
    context = {
        'var1' : list1,
        'media' : media,
    }
    return render(request, "media.html", context)

def view_c(request):
    voti = {'studente1':8, 'studente2':7, 'studente3':5}
    context = {
        'voti' : voti
    }
    return render(request, "voti.html", context)

def index_prova_1(request):
    return render(request, "index_prova_1.html")

