from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, forms.BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-comfort"


class ProductForm(forms.ModelForm, StyleFormMixin):
    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data.get("name")
        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"Название не должно содержать {word}")
            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")
        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"Описание не должно содержать {word}")
            return cleaned_data


class VersionForm(forms.ModelForm, StyleFormMixin):
    class Meta:
        model = Version
        fields = "__all__"
