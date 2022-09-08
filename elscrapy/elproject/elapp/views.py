from dataclasses import dataclass, fields
from distutils.core import run_setup
import http
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView, FormView, TemplateView
from .models import elModel,Newword
from django.urls import reverse_lazy
import requests
import bs4
from selenium import webdriver
from django.shortcuts import render
from .forms import VenueForm
from django.http import HttpResponseRedirect
import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
import os, signal
from scrapy.utils.project import get_project_settings
from django.db.models import F
# Create your views here.

posted_data = {
    'text':''
}

# class WordSpider(scrapy.Spider):
#     name = 'word'
#     allowed_domains = ['ejje.weblio.jp']
#     # start_urls = ['http://ejje.weblio.jp/content/']
  

#     def __init__(self, query='', *args, **kwargs):
#         super(WordSpider, self).__init__(*args, **kwargs)
#         #self.user_agent = 'custom-user-agent'
#         self.start_urls = ['https://ejje.weblio.jp/content/' + query]



#     def parse(self, response):
       
#         # item=ElscrapyItem()
#         # item['word']=response.xpath('//*[@id="summary"]/div[2]/p/span[2]/text()').get().replace('\n', '').strip()
#         # yield item
        
#         word=response.xpath('//*[@id="summary"]/div[2]/p/span[2]/text()').get().replace('\n', '').strip()
#         #loader = ItemLoader(item = ElscrapyItem(), response=response)
#         #loader.add_xpath('word', '//*[@id="summary"]/div[2]/p/span[2]/text()')
#         #yield loader.load_item()
#         yield{
#             'word':word
#         }
def get_word(query: str) -> str:
    resp = requests.get(f'https://ejje.weblio.jp/content/{query}', headers={
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    })
    resp.raise_for_status()
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    return soup.find(class_='content-explanation').get_text(strip=True)
class englishlist(ListView):
    template_name='list.html'
    model= Newword

class englishdetail(DetailView):
    template_name= 'detail.html'
    model= Newword

# class englishform(FormView):
#     template_name = 'form.html'
#     form_class = inputform
#     success_url = reverse_lazy('list')
#    def form_valid(self, form):
#         posted_data['word'] = form.data.get('word')
#         return super().form_valid(form)
 
# def add_venue(request):
#     submitted = False
#     if request.method =='POST':
#         form = VenueForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['word']#入力した単語
#             queryset = Newword.objects.filter(word = name)
#             print(queryset)
#             if queryset.exists():
#                 #dataclass
#                 pass
#             else:
#                 #print(name)
#                 # process = CrawlerProcess({
#                 # 'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#                 # })
#                 process = CrawlerProcess(get_project_settings())
#                 process.crawl(WordSpider, query=name)
#                 process.start() # the script will block here until the crawling is finished
#                 #process.join()
#                 form.save()
                
#             return HttpResponseRedirect('/list/')
#     else:
#         form = VenueForm
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'form.html', {'form':form, 'submitted':submitted})

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
def add_venue(request):
    submitted = ('submitted' in request.GET)
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            if not Newword.objects.filter(word=word).exists():
                explanation = get_word(word)
                # (do something with `explanation` probably?)
                print(explanation)
                form.save()
                result = Newword.objects.get(word=word)
                result.mean = explanation
                result.save()

            else:
                print(word)
                result = Newword.objects.get(word=word)
                result.useful = result.useful + 1
                result.save()
            return HttpResponseRedirect('/list/')
    else:
        form = VenueForm()

    return render(request, 'form.html', {'form': form, 'submitted': submitted})
class englishcreate(CreateView):
    template_name= 'create.html'
    model=Newword
    fields = ('word', 'priority', 'date')
    # items = elModel.objects.get(word = 'word')
    # print(items)
    success_url = reverse_lazy('list')

class englishdelete(DeleteView):
    template_name = 'delete.html'
    model=Newword
    success_url= reverse_lazy('list')

class englishupdate(UpdateView):
    template_name = 'update.html'
    model = Newword
    fields = ('word', 'priority', 'date')
    success_url = reverse_lazy('list')
