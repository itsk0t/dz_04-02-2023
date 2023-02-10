from .models import Imprisoned
from django.forms import ModelForm


class ImprisonedForm(ModelForm):
    class Meta:
        model = Imprisoned
        fields = [
            'name',
            'last_name',
            'patronymic',
            'article',
            'time_start',
            'period',
            'block',
            'cell',
            'note_about_behavior'
        ]