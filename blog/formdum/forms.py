from django.forms import Form
from django import forms


class DummForm(Form):
    text = forms.CharField(label='Отзыв', max_length=10, min_length=3)
    grade = forms.IntegerField(label='Оценка', max_value=10, min_value=1)
    image = forms.FileField(label='Фото', required=False)
