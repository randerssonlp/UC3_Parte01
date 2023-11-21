from django.shortcuts import render, HttpResponse
# Create your views here.
homehtml = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="vienport" content="width=device-width, initial-scale=1.0" />
<title>Examen UC3</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans&display=swap">
</head>
<style>
    body {
      margin: 0;
      font-family: 'Open Sans', sans-serif; 
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }

    header {
      background-color: #f0f0f0;
      text-align: center;
      padding: 10px 0;
    }

    .Logo img {
      width: 50%;
    }

    nav {
      background-color: yellow;
      padding: 10px 0;
    }

    .nav-inner {
      list-style: none;
      padding: 0;
      margin: 0;
      text-align: center;
    }

    .nav-item {
      display: inline-block;
      margin: 0 15px;
    }

    .nav-item a {
      text-decoration: none; 
      color: #000; 
    }

    main {
      flex: 1;
    }

    footer {
      background-color: #808080;
      color: #fff;
      text-align: center;
      padding: 10px 0;
      margin-top: auto; 
    }
  </style>
<body>
<header>
<div class="Logo">
<img src="https://www.untels.edu.pe/images/logo.png" alt="untels logo" />
</div>
<nav>
<ul class="nav-inner">
<li class="nav-item"><a href="/inicio">Inicio</a></li>
<li class="nav-item"><a href="/primos/1/10">Primos[a,b]</a></li>
<li class="nav-item"><a href="/examen">Examen</a></li>
</ul>
</nav>
</header>
</body>
</html>
"""
footer = """
<footer>
  <div class="content">UNTELS - LP3 - LOPEZ_MAMANI_MORENO - 20/11/2023</div>
</footer>
"""
 
def home(request):
    return HttpResponse(homehtml+footer)

# lista=['Legislación Informática', 
#       'Dinámica de Sistemas',
#       'Ingeniería de Requerimientos',
#       'Algoritmos de Computación Gráfica',
#       'Lenguaje de Programación III',
#       'Microprocesadores',
#       'Gestión de Procesos de Negocios']

# def mostrar_cursos(request):
#     materias_html="<h1>Lista de Cursos de Ingeniería de Sistemas</h1><ul>"
    
#     for materia in lista:
#         materias_html+=f"<li>{materia}</lia>" 
#     materias_html+="</ul>"
    
#     return HttpResponse(homehtml+materias_html+footer)

# def mostrar_primos(request, a, b):
#     a = int(a)
#     b = int(b)

#     # Manejo del caso en que a > b
#     if a > b:
#         a, b = b, a

#     primos_html = f"<h1>Números primos entre {a} y {b}</h1><ul>"
    
#     for num in range(max(2, a), b + 1):
#         es_primo = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
#         if es_primo:
#             primos_html += f"<li>{num}</li>"
#     primos_html += "</ul>"

#     return HttpResponse(homehtml + primos_html + footer)

# estudiantes = [
#     {"nombre": "Lopez Puris Raúl Andersson", "github": "https://github.com/randerssonlp/UC3_Parte01.git"},
#     {"nombre": "Moreno Menacho Facundo Rafael ", "github": "https://github.com/Facundo08/UC3_Parte02.git"},
#     {"nombre": "Mamani Avalos Melany Irma", "github": "https://github.com/MelanyMamani1/UC3_Parte03.git"},
# ]
# def mostrar_examen(request):
    examen_html = "<h1>Lista de estudiantes y enlaces de GitHub</h1><ul>"
    
    for estudiante in estudiantes:
        examen_html += f"<li>{estudiante['nombre']}: <a href='{estudiante['github']}'>{estudiante['github']}</a></li>"
    
    examen_html += "</ul>"

    return HttpResponse(homehtml + examen_html + footer)