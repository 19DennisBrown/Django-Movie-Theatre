from django import forms

from .models import MovieDetails, bookedMovie

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewMovieForm(forms.ModelForm):
    class Meta:
        model = MovieDetails
        fields = ('name', 'description', 'price', 'created_by')
        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
         
           
        }


class EditMovieForm(forms.ModelForm):
    class Meta:
        model = MovieDetails
        fields = ('name', 'description', 'price',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

