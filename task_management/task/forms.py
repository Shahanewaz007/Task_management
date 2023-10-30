from django import forms
from .models import Task


CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

class TaskForm(forms.Form):
    
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a description'}),)
    due_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datepicker'}),)
    priority = forms.ChoiceField(choices=CHOICES)

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'due_date', 'priority', 'photo']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a description'}),
#             'due_date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
#             'priority': forms.Select(attrs={'class': 'form-control'}),
#         }