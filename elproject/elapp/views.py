import http
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView, FormView, TemplateView
from .models import elModel
from django.urls import reverse_lazy
import requests
from bs4 import BeautifulSoup
import selenium
from django.shortcuts import render
from .forms import VenueForm
from django.http import HttpResponseRedirect
import elscrapy
# Create your views here.

posted_data = {
    'text':''
}
class englishlist(ListView):
    template_name='list.html'
    model=elModel

class englishdetail(DetailView):
    template_name= 'detail.html'
    model= elModel

# class englishform(FormView):
#     template_name = 'form.html'
#     form_class = inputform
#     success_url = reverse_lazy('list')
#    def form_valid(self, form):
#         posted_data['word'] = form.data.get('word')
#         return super().form_valid(form)
 
def add_venue(request):
    submitted = False
    if request.method =='POST':
        form = VenueForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/list/')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'form.html', {'form':form, 'submitted':submitted})

# class englishform(TemplateView):
#     def __init__(self):
#         self.params = {
#             'Message':'単語を入力してください。',
#             'form':forms.Contact_Form(),
#         }
#     def get(self, request):
#         return render(request, 'form.html', context=self.params)

#     def post(self, request):
#         if request.method =='POST':
#             self.params['form'] = forms.Contact_Form(request.POST)

#             if self.params['form'].is_valid():
#                 self.params['form'].save(commit=True)
#                 self.params['Message'] = '入力情報が送信されました。'
#         return render(request, 'form.html', context=self.params)

class englishcreate(CreateView):
    template_name= 'create.html'
    model=elModel
    fields = ('word', 'priority', 'duedate')
    # items = elModel.objects.get(word = 'word')
    # print(items)
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
