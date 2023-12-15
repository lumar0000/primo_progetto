from django.shortcuts import render

# Create your views here.

def view_a(request):
    context = {
        'materie' : ["Matematica","Italiano","Inglese","Storia","Geografia"],
    }
    return render(request, "view_a.html", context)

def view_b(request):
    context = {
        'voti' :  {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
        'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
        'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    return render(request, "view_b.html", context)

def view_c(request):
    voti :  {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
        'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
        'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    tot = 0
    media = {}
    i = 0
    
    for chiave in voti:
        for materia in voti[chiave]:
            tot += materia[1]
        media[chiave] = tot/len(voti[chiave])
        tot = 0
        i += 1

    
    context = {
        'media' : media
    }
    return render(request, "view_c.html", context)

def view_d(request):
    max = 0
    min = 10
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
        'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
        'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    for chiave in voti:
        for materia in voti[chiave]:
            if(max < materia[1]):
                max = materia[1]
            if(min > materia[1]):
                min = materia[1]

    minmax = {max:[[],[]],min:[[],[]]}

    for chiave in voti:
        for materia in voti[chiave]:
            if(materia[1] == max):
                minmax[max][1].append(materia[0])
                if(chiave not in minmax[max][0]):
                    minmax[max][0].append(chiave)
            elif(materia[1] == min):
                minmax[min][1].append(materia[0])
                if(chiave not in minmax[min][0]):
                    minmax[min][0].append(chiave)

    
    context = {
        'minmax' : minmax
    }
    return render(request, "view_d.html", context)