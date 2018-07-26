from django.shortcuts import render, redirect, get_object_or_404
from .models import Clients
from .forms import ClientForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def clients(request):
    clients = Clients.objects.all()
    return render(request, 'clients.html', {'clients': clients})


@login_required
def client_new(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clients')
    else:
        return render(request, 'client_new.html', {'form': form})


@login_required
def client_update(request, id):
    client = get_object_or_404(Clients, pk=id)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('clients')
    else:
        return render(request, 'client_new.html', {'form': form})


@login_required
def client_delete(request, id):
    client = get_object_or_404(Clients, pk=id)
    if request.method == 'POST':
        client.delete()
        return redirect('clients')
    else:
        return render(request, 'client_delete_confirm.html', {'client': client})

