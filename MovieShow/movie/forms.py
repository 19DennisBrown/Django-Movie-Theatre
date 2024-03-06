from django import forms

from .models import Movie, bookedMovie

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('category', 'name', 'description', 'price', 'image',)
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
class bookedMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('isBooked', 'name', 'description', 'price',)
        widgets = {
            
            'isBooked': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
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
class updateBookedMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('isBooked', 'name', 'description', 'price',)
        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'isBooked': forms.Textarea(attrs={
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
        model = Movie
        fields = ('name', 'description', 'price', 'image',)
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

