from django import forms
from .models import *


class LaptopForm(forms.ModelForm):
   class Meta:
      model = Laptop
      fields = ('type' , 'price', 'status', 'room')

class DesktopForm(forms.ModelForm):
   class Meta:
      model = Desktop
      fields = ('type' , 'price', 'status', 'room')

class MobileForm(forms.ModelForm):
   class Meta:
      model = Mobile
      fields = ('type' , 'price', 'status', 'room')