from django.shortcuts import render, HttpResponseRedirect
from web.forms import VentaForm
from web.models import Venta
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
        if request.method =='POST':
            form = VentaForm(request.POST)

            if form.is_valid():
                    contact_form = Venta.objects.create(**form.cleaned_data)
                    messages.success(request, "La informacion se guardo correctamente !")
                    return HttpResponseRedirect('/')
            else:
                    messages.error(request, "La informacion no se pudo guardar !")
                    return HttpResponseRedirect('/')
        else:
            form = VentaForm()
    
        return render(request, 'index.html', {'form': form})
@login_required
def listado(request):
        ventas = Venta.objects.all()
        return render(request, 'listado.html', {'ventas': ventas})
