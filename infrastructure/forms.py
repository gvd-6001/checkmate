from django.forms import ModelForm

from .models import Panel, NVR


class PanelAddForm(ModelForm):
    class Meta:
        model = Panel
        fields = '__all__'


class NvrAddForm(ModelForm):
    class Meta:
        model = NVR
        fields = '__all__'
