from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form=ContactForm()
    if request.method =='POST':
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid:
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            # Enviamos el mensaje y redirecionamos
            email=EmailMessage(subject="Nuevo Email Caffeteira contacto",
                               body="De: {} <{}>\n\n Escribio:\n\n{}".format(name,email,content),
                               from_email="no-contestar@inbox.mailtrap.io",
                               to=["stiverueda1995@gmail.com"],
                               reply_to=[email])
            try:
                email.send()
                # se envio el correo
                return redirect(reverse('contact')+"?ok")
            except:
                # lastimosamente no se envio el correo
                import traceback
                traceback.print_exc()
                return redirect(reverse('contact')+"?fail")
    return render(request,"contact/contact.html",{"forms":contact_form})
