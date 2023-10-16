from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Paginas
from .forms import Escoger


# Create your views here.
def sing_up(request):
    if request.method == 'GET':
        return render(request, 'sesion/sing_up.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'sesion/sing_up.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'})
        return render(request, 'sesion/sing_up.html', {
            'form': UserCreationForm,
            'error': 'Las contrasenas no coinciden'
        })

def sing_in(request):
    if request.method == 'GET':
        return render(request, 'sesion/sing_in.html', {"form": AuthenticationForm()})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'sesion/sing_in.html', {"form": AuthenticationForm(), "error": "Username or password is incorrect."})
        else:
            login(request, user)
            return main(request)

def singout(request):
    logout(request)
    return main(request)

def Crear_categorias(request):
    categorias = {
        "BALENCIAGA": {
            "BALENCIAGA": request.user.BALENCIAGA,
            "DIOR": request.user.DIOR,
            "GUCCI": request.user.GUCCI,
            "PRADA": request.user.PRADA,
            "VERSACE": request.user.VERSACE,
        },
        "DIOR": {
            "BALENCIAGA": request.user.BALENCIAGA,
            "DIOR": request.user.DIOR,
            "GUCCI": request.user.GUCCI,
            "PRADA": request.user.PRADA,
            "VERSACE": request.user.VERSACE,
        },
        "GUCCI": {
            "BALENCIAGA": request.user.BALENCIAGA,
            "DIOR": request.user.DIOR,
            "GUCCI": request.user.GUCCI,
            "PRADA": request.user.PRADA,
            "VERSACE": request.user.VERSACE,
        },
        "PRADA": {
            "BALENCIAGA": request.user.BALENCIAGA,
            "DIOR": request.user.DIOR,
            "GUCCI": request.user.GUCCI,
            "PRADA": request.user.PRADA,
            "VERSACE": request.user.VERSACE,
        },
        "VERSACE": {
            "BALENCIAGA": request.user.BALENCIAGA,
            "DIOR": request.user.DIOR,
            "GUCCI": request.user.GUCCI,
            "PRADA": request.user.PRADA,
            "VERSACE": request.user.VERSACE,
        },
    }
    return categorias

def obtener_categorias_principales(categorias, potencia=20, num_categorias=5):
    # Crear matriz de transición
    matriz_visitas = []

    # Recorrer los subdiccionarios
    for sub_diccionario in categorias.values():
        valores = list(sub_diccionario.values())
        matriz_visitas.append(valores)

    # Crear el vector de visitas
    vector_visitas = [sum(fila) for fila in matriz_visitas]

    # Crear la matriz de transición
    matriz_transicion = [[valor / vector_visitas[i] for valor in fila] for i, fila in enumerate(matriz_visitas)]
    #print(matriz_visitas)
    #print(matriz_transicion)
    
    def elevar_matriz(matriz, n):
        # Verificar si la matriz es cuadrada
        if len(matriz) != len(matriz[0]):
            raise ValueError("La matriz debe ser cuadrada para poder elevarla a una potencia")

        # Crear una copia de la matriz original
        matriz_elevada = matriz[:]

        # Realizar la multiplicación repetida
        for _ in range(1, n):
            matriz_elevada = multiplicar_matrices(matriz_elevada, matriz)

        return matriz_elevada

    def multiplicar_matrices(matriz1, matriz2):
        filas1 = len(matriz1)
        columnas1 = len(matriz1[0])
        columnas2 = len(matriz2[0])

        resultado = []
        for i in range(filas1):
            fila_resultado = []
            for j in range(columnas2):
                suma = 0
                for k in range(columnas1):
                    suma += matriz1[i][k] * matriz2[k][j]
                fila_resultado.append(suma)
            resultado.append(fila_resultado)

        return resultado

    matriz_elevada = elevar_matriz(matriz_transicion, potencia)
    print(matriz_elevada)
    fila0 = matriz_elevada[0]
    numeros_extraidos = [round(num, 4) for num in fila0]

    numeros_mayores = sorted(numeros_extraidos, reverse=True)[:num_categorias]
    posiciones_numeros_mayores = [numeros_extraidos.index(num) for num in numeros_mayores]

    diccionario_numeros_mayores = {}
    categorias_lista = list(categorias.keys())

    for i in range(len(numeros_mayores)):
        posicion = posiciones_numeros_mayores[i]
        clave = categorias_lista[posicion]
        diccionario_numeros_mayores[clave] = numeros_mayores[i]

    return list(diccionario_numeros_mayores.keys())

def main(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            buscador = request.POST.get('buscador')
            if buscador:
                buscador = buscador.lower()
                user = request.user
                if 'balenciaga' in buscador:
                    user.BALENCIAGA += 1
                elif 'dior' in buscador:
                    user.DIOR += 1
                elif 'gucci' in buscador:
                    user.GUCCI += 1
                elif 'prada' in buscador:
                    user.PRADA += 1
                elif 'versace' in buscador:
                    user.VERSACE += 1
                user.save()

        u = Crear_categorias(request)
        pg = obtener_categorias_principales(u)
        print(pg)
        mayor = pg[:2]
        banner1 = mayor[0]
        banner2 = mayor[1]
        print(banner1)
        print(banner2)
        return render(request, 'main/inicio.html', {'pg': pg, 'mayor': mayor, 'banner1': banner1, 'banner2': banner2})
    else:
        return sing_in(request)








