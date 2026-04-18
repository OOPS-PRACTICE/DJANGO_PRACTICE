from django import forms
# from .models import ProjectTypes

# class ProjectTypesForm(forms.Form):
#     project_type = forms.ModelChoiceField(
#         queryset=ProjectTypes.objects.all(), label="Select Project Type"
#     )


class ProjectTypesForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="Project Type Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )