from django.forms import ModelForm

from .models import Branch


class BranchAddForm(ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
