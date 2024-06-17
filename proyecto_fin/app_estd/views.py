from django.shortcuts import render

# Create your views here.
def ver_home(request):
    return render(request,"home.html")


def ver_jugadores(request):


    return render(request,"jugadores.html")

def ver_nosotros(request):
    return render(request,"nosotros.html")

#por jugador

def defensa_central(request):
    # trate todas las estadisticas posisiocn sea defensa central
    
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
