from django.shortcuts import render, HttpResponse

html_base = """

<h1> MI WEB PERSONAL</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de...</a></li>
    <li><a href="/portafolio/">Portafolio</a></li>
    <li><a href="/contacto/">Contacto</a></li>
</ul>
"""

# Create your views here.
# DESPLIEGA INORMACION -  VISUALIZA LA INTERACCION CON EL SISTEMA

# SE DEFINE EL METODO HOME O PAGINA PRINCIAPL DEL PROYECTO
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contacto(request):
    return render(request, "core/contacto.html")