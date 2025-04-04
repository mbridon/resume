from django.forms import DateInput, ModelForm, TextInput
from .models import ExperiencePro, Formation


class ExperienceProForm(ModelForm):
    class Meta:
        model = ExperiencePro
        fields = ["entreprise", "job", "début", "fin"]
        widgets = {
            "début": DateInput(attrs={"type": "date"}),
            "fin": DateInput(attrs={"type": "date", "required": False})
        }


class FormationForm(ModelForm):
    class Meta:
        model = Formation
        fields = ["diplôme", "date_obtention"]
        widgets = {
            "date_obtention": DateInput(attrs={"type": "date", "required": False})
        }