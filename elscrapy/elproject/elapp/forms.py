
from django import forms
from .models import elModel, Newword
from django.forms import ModelForm
# class inputform(forms.Form):
#     # model = elModel
#     # fields = ('word', 'priority', 'duedate')
#     # labels = {
#     #     'word':'検索単語',
#     #     'priority':'優先',
#     #     'duedate':'登録日',
#     # }

#     word = forms.CharField(max_length = 30)

class VenueForm(ModelForm):
    class Meta:
        model = Newword
        fields = ('word','date')