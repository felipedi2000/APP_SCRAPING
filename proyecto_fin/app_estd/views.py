from django.shortcuts import redirect, render
from bson import ObjectId
from .models import jugadores_collection

# Create your views here.
def ver_home(request):
    return render(request,"home.html")

def ver_jugadores(request):
    jugadores = list(jugadores_collection.find({}, {
        "Name": 1, "Position": 1, "team": 1, "MarkeValue": 1, "Nationality": 1, "id": 1
    }))
    return render(request, "jugadores.html", {'jugadores': jugadores})

def ver_nosotros(request):
    return render(request,"nosotros.html")

#por jugador
def defensa_central(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"interceptions": 1,"accuratePassesPercentage": 1,"aerialDuelsWon": 1,"accurateLongBalls": 1, "dribbledPast": 1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_defensa_central.html',{'jugador': jugador})

def delantero_centro(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"successfulDribbles": 1,"totalShots": 1,"bigChancesMissed": 1, "offsides": 1,"shotsOnTarget": 1,"aerialDuelsWon": 1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_delantero_centro.html',{'jugador': jugador})

def extremo_derecho(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"successfulDribbles": 1,"totalShots": 1,"bigChancesCreated": 1, "shotsOnTarget": 1,"keyPasses": 1,"accurateCrosses": 1,"accuratePassesPercentage": 1, "bigChancesMissed":1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_extremo_derecho.html',{'jugador': jugador})

def extremo_izquierdo(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"successfulDribbles": 1,"totalShots": 1,"bigChancesCreated": 1, "shotsOnTarget": 1,"keyPasses": 1,"accurateCrosses": 1,"accuratePassesPercentage": 1, "bigChancesMissed":1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_extremo_izquierdo.html',{'jugador': jugador})

def lateral_derecho(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"interceptions": 1,"clearances": 1,"accuratePassesPercentage": 1, "accurateCrosses": 1,"successfulDribbles": 1,"keyPasses": 1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_lateral_derecho.html',{'jugador': jugador})

def lateral_izquierdo(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"interceptions": 1,"clearances": 1,"accuratePassesPercentage": 1, "accurateCrosses": 1,"successfulDribbles": 1,"keyPasses": 1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_lateral_izquierdo.html',{'jugador': jugador})

def mediapunta(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"successfulDribbles": 1,"totalShots": 1,"bigChancesCreated": 1, "shotsOnTarget": 1,"keyPasses": 1,"accuratePassesPercentage": 1, "bigChancesMissed":1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_mediapunta.html',{'jugador': jugador})

def mediocampista_ofensivo(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"successfulDribbles": 1,"totalShots": 1,"bigChancesCreated": 1, "shotsOnTarget": 1,"keyPasses": 1,"accuratePassesPercentage": 1, "bigChancesMissed":1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_mediocentro_ofensivo.html',{'jugador': jugador})

def pivote(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"successfulDribbles": 1,"totalShots": 1,"bigChancesCreated": 1, "shotsOnTarget": 1,"keyPasses": 1,"accuratePassesPercentage": 1, "bigChancesMissed":1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_pivote.html',{'jugador': jugador})

def portero(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"goalsConcededOutsideTheBox": 1,"saves": 1,"totalDuelsWon": 1, "goalsConcededInsideTheBox": 1,"savedShotsFromInsideTheBox": 1,"savedShotsFromOutsideTheBox": 1, "highClaims":1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_portero.html',{'jugador': jugador})

def mediocentro(request):
    id = request.GET.get('id', '')
    print("Mensaje recibido:", id)
    jugador_id = int(id)
    jugador = jugadores_collection.find_one({"id": jugador_id},{
        "Name": 1, "Nationality": 1, "Age": 1, "team": 1, "Number": 1, "MarkeValue": 1, "Position": 1, "goals": 1, "yellowCards": 1, "redCards": 1, "minutesPlayed": 1, "assists": 1,"interceptions": 1,"clearances": 1,"accurateLongBalls": 1, "accuratePassesPercentage": 1
    })
    print(f"jugador:{jugador}")
    return render(request, 'jd_mediocentro.html',{'jugador': jugador})


def jugadorBuscar(request):
    params = request.GET.get('id').split('&')
    claves = ['Posicion', 'min', 'max', 'jugador', 'equipo']
    dic = dict(zip(claves, params))
    print(dic)
    # falta hacer consulta en mongo
    jugadores=list([])
    
    return render(request, "jugadores.html",{'jugadores': jugadores}) 