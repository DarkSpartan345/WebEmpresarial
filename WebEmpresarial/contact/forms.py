from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="Nombre",required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':"Escriba su nombre"}),min_length=3,max_length=100)
    email=forms.EmailField(label="Correo",required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':"Escriba su correo"}),min_length=3,max_length=100)
    content=forms.CharField(label="contenido",required=True,widget=forms.Textarea(
        attrs={'class':'form-control','rows':3,'placeholder':"Escriba su mensaje"}),min_length=10,max_length=1000)