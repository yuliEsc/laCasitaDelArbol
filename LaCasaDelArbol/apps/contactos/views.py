from django.shortcuts import render,redirect
from .forms import ContactoForm
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.http import  HttpResponse
# Create your views here.
def contacto(request):
    formulario_contacto = ContactoForm()

    if request.method =="POST":
        formulario_contacto = ContactoForm(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            mail=request.POST.get("mail")
            contenido=request.POST.get("contenido")
            
            email=EmailMessage(" Mensaje desde la App Django ",
            "El usuario con nombre {} con la direcion electronica {} escribe lo siguiente:\n\n {}".format(nombre,mail,contenido),
            "",["casita.arbol@hotmail.com"],reply_to=[mail])
            
            try:
                email.send()
                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")
        
    return render(request,'contacto.html',{'formulario':formulario_contacto})
