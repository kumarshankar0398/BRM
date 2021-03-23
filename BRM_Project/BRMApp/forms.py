from django import forms

class NewBookForm(forms.Form):
    title=forms.CharField(label='Book Title',max_length=100)
    price=forms.FloatField(label='Book Price')
    author=forms.CharField(label='Book Author',max_length=100)
    publisher=forms.CharField(label='Book Publisher',max_length=100)

class SearchForm(forms.Form):
    title=forms.CharField(label='Book Title',max_length=100)
