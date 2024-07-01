from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['Age','Experience','Income','Family','CCAvg','Education','Mortgage','CDAccount','OnlineAccount']
