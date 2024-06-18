from django.shortcuts import render
from .models import jugadores_collection

# Create your views here.
def ver_home(request):
    return render(request,"home.html")

def ver_jugadores(request):
    jugadores = list(jugadores_collection.find({}, {
        "Name": 1, "Position": 1, "team": 1, "MarkeValue": 1, "Nationality": 1, "_id": 0
    }))
    print(f"Colección:", jugadores)
    return render(request, "jugadores.html", {'jugadores': jugadores})

def ver_nosotros(request):
    return render(request,"nosotros.html")

#por jugador

def defensa_central(request):
    # trate todas las estadisticas posisiocn sea defensa central
    # id = request.GET.get('id')
    # print(f"id: {id}")
    return render(request, 'jd_defensa_central.html')

def delantero_centro(request):
    return render(request, 'jd_delantero_centro.html')

def extremo_derecho(request):
    return render(request, 'jd_extremo_derecho.html')

def extremo_izquierdo(request):
    return render(request, 'jd_extremo_izquierdo.html')

def lateral_derecho(request):
    return render(request, 'jd_lateral_derecho.html')

def lateral_izquierdo(request):
    return render(request, 'jd_lateral_izquierdo.html')

def mediapunta(request):
    return render(request, 'jd_mediapunta.html')

def mediocampista_ofensivo(request):
    return render(request, 'jd_mediocentro_ofensivo.html')

def pivote(request):
    return render(request, 'jd_pivote.html')

def portero(request):
    return render(request, 'jd_portero.html')

def mediocentro(request):
    return render(request, 'jd_mediocentro.html')
