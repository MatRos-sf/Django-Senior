from django.shortcuts import render, redirect, get_object_or_404
from .forms import LisatZakupowForms
from .models import ListaZakupow
from .extraFunction import generationQrCode

from django.contrib import messages
# Create your views here.

def stronaGlowna(request):
    query = request.GET.get('q')
    if query :
        lista = ListaZakupow.objects.filter(miejscowosc__icontains=query)
    else:
        lista = ListaZakupow.objects.all()
    return render(request, 'main/home.html',{'lista': lista })


def utworz(request):

    if request.method == "POST":
        form = LisatZakupowForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LisatZakupowForms()
        
    return render(request, 'main/dodaj.html', {'form':form})

def edycja(request, id ):

    form = get_object_or_404(ListaZakupow,id=id)
    if form.realizcja == True:

        if request.method == 'POST':
            formNew = LisatZakupowForms(request.POST,instance=form)

            if formNew.is_valid():
                formNew.save()
            return redirect('home')
        else: #GET
            formNew=LisatZakupowForms(instance= form)

        return render(request, 'main/edit.html', {'form': formNew})

def info(request,id):

    lista = ListaZakupow.objects.get(id=id)
    generationQrCode(lista.id,lista.lista)

    if request.GET.get('mybtn'):
        lista.aktywne = False
        lista.realizacja = True
        lista.save()

    return render(request,'main/info.html',{'lista':lista })

def realizowane(request):
    realizes = ListaZakupow.objects.filter(realizacja=True)
    return render(request, 'main/realize.html', {'realizes': realizes})

def usun (request):

    if (request.GET.get('mybtn')):
        id = int(request.GET.get('mytextbox'))
        try:
            form = get_object_or_404(ListaZakupow, id=id )
        except:
            messages.error(request,' Nie ma takiego zlecenia ')
            return redirect('usun')

        if form.aktywne == False:
            if form.realizacja == True:
                form.delete()
                messages.info(request, 'Zlecenie zostało usunięte. ')
                return redirect('usun')
            else:
                messages.info(request,'Zlecenie nie jest realizowane.')
        else:
            messages.info(request, 'Nikt nie podjął się zlecenia wiec nie możesz usunąć je. ')

    return render(request, 'main/end.html')

def jakDziala(request):
    return render(request, 'main/how.html')