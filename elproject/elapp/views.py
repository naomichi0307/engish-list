import http
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView
from .models import elModel
from django.urls import reverse_lazy


# Create your views here.
class englishlist(ListView):
    template_name='list.html'
    model=elModel

class englishdetail(DetailView):
    template_name= 'detail.html'
    model= elModel

class englishcreate(CreateView):
    template_name= 'create.html'
    model=elModel
    fields = ('word', 'priority', 'duedate')
    success_url = reverse_lazy('list')

class englishdelete(DeleteView):
    template_name = 'delete.html'
    model=elModel
    success_url= reverse_lazy('list')

class englishupdate(UpdateView):
    template_name = 'update.html'
    model = elModel
    fields = ('word', 'priority', 'duedate')
    success_url = reverse_lazy('list')