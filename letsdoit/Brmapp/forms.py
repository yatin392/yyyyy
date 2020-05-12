from django import forms

class newbookform(forms.Form):
    title=forms.CharField(max_length=100,label='Title')
    author=forms.CharField(max_length=100,label='author')
    price=forms.FloatField(label='price')
    publisher=forms.CharField(max_length=100,label='publisher')
class searchform(forms.form):
    title=forms.CharField(label='Title')
