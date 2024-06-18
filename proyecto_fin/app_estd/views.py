from django.shortcuts import render
from .models import jugadores_collection

# Create your views here.
def ver_home(request):
    return render(request,"home.html")

def ver_jugadores(request):
    jugadores = list(jugadores_collection.find({}, {
        "Name": 1, "Position": 1, "team": 1, "MarkeValue": 1, "Nationality": 1, "_id": 0
    }))
    return render(request, "jugadores.html", {'jugadores': jugadores})

def ver_nosotros(request):
    return render(request,"nosotros.html")

#por jugador

def defensa_central(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    
    return render(request, 'jd_defensa_central.html')


def delantero_centro(request):
    id = request.GET.get('id', '')
    # recibir los datos de id y insertarlos en el html
    #print("Mensaje recibido:", id)
    return render(request, 'jd_delantero_centro.html')

def extremo_derecho(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    return render(request, 'jd_extremo_derecho.html')

def extremo_izquierdo(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    return render(request, 'jd_extremo_izquierdo.html')

def lateral_derecho(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    return render(request, 'jd_lateral_derecho.html')

def lateral_izquierdo(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    return render(request, 'jd_lateral_izquierdo.html')

def mediapunta(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    return render(request, 'jd_mediapunta.html')

def mediocampista_ofensivo(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    return render(request, 'jd_mediocentro_ofensivo.html')

def pivote(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    return render(request, 'jd_pivote.html')

def portero(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    return render(request, 'jd_portero.html')

def mediocentro(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    return render(request, 'jd_mediocentro.html')
