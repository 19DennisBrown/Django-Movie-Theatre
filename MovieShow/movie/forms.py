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
           
            # 'created_by': forms.InlineForeignKeyField(attrs={
            #     'class': INPUT_CLASSES
            # }),
           
          
           
        }
# class bookedMovieForm(forms.ModelForm):
#     class Meta:
#         model = bookedMovie
#         fields = ('isBooked', 'title', 'description', 'cost',)
        # widgets = {
            
        #     'isBooked': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'title': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'description': forms.Textarea(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'cost': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
           
        # }
# class updateBookedMovie(forms.ModelForm):
#     class Meta:
#         model = bookedMovie
#         fields = ('isBooked', 'title', 'description', 'cost',)
#         widgets = {
            
#             'title': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'isBooked': forms.Textarea(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'description': forms.Textarea(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'cost': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
           
#         }

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

