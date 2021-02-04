"""
Definition of forms.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView
from django.db import transaction
from django.db import models
from django.forms import ModelForm

#Import Models
from django.db import models
from django.forms import ModelForm
from .models import ComicInput
from .models import Series_Choices

## Authentication Form ####
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
## User Registration Form ##
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First name is required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last name is required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

        
##############Comic  Input Forms###############
class ComicInputForm(forms.ModelForm):
    class Meta:
        model = ComicInput
        fields = '__all__'

##############Comic  Edit Forms################

class editform(forms.ModelForm):
    #Series = forms.ChoiceField(choices=Series_Choices)
    
    class Meta:
        model=ComicInput
        fields ='__all__'

###################### Collection View Filters #######################

class TitleChoiceField(forms.Form):
 
    class Meta:
        model = ComicInput
        fields = ('Title','uid',)
    
    titles = forms.ModelChoiceField(queryset =ComicInput.objects.all())

    ###over ride the Form init to include the uid, so that only the user's items can be used to populate the filters##
    def __init__(self, uid=None, *args, **kwargs):
        super(TitleChoiceField, self).__init__(*args, **kwargs)
        self.user = uid
        usrqry = ComicInput.objects.filter(uid=self.user).values_list('Title', flat=True).distinct().order_by('Title')
        
        self.fields['titles'].queryset=usrqry
      
class NotesChoiceField(forms.Form):

    class Meta:
        model = ComicInput
        fields = ('SellingNotes','uid',)
    
    sellingnotes = forms.ModelChoiceField(queryset =ComicInput.objects.all())

    ###over ride the Form init to include the uid, so that only the user's items can be used to populate the filters##
    def __init__(self, uid=None, *args, **kwargs):
        super(NotesChoiceField, self).__init__(*args, **kwargs)
        self.user = uid
        usrqry = ComicInput.objects.filter(uid=self.user).values_list('SellingNotes', flat=True).distinct().order_by('SellingNotes')
        
        self.fields['sellingnotes'].queryset=usrqry

class PublisherChoiceField(forms.Form):

    class Meta:
        model = ComicInput
        fields = ('Publisher','uid',)
    
    publisher = forms.ModelChoiceField(queryset =ComicInput.objects.all())

    ###over ride the Form init to include the uid, so that only the user's items can be used to populate the filters##
    def __init__(self, uid=None, *args, **kwargs):
        super(PublisherChoiceField, self).__init__(*args, **kwargs)
        self.user = uid
        usrqry = ComicInput.objects.filter(uid=self.user).values_list('Publisher', flat=True).distinct().order_by('Publisher')
        self.fields['publisher'].queryset=usrqry

class CategoryChoiceField(forms.Form):

    class Meta:
        model = ComicInput
        fields = ('Category','uid',)
    
    category = forms.ModelChoiceField(queryset =ComicInput.objects.all())

    ###over ride the Form init to include the uid, so that only the user's items can be used to populate the filters##
    def __init__(self, uid=None, *args, **kwargs):
        super(CategoryChoiceField, self).__init__(*args, **kwargs)
        self.user = uid
        usrqry = ComicInput.objects.filter(uid=self.user).values_list('Category', flat=True).distinct().order_by('Category')
        
        self.fields['category'].queryset=usrqry


     
