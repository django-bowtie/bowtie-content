from django import forms
from widgets import BowtieContentWidget


class BowtieContentFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        self.widget = BowtieContentWidget()
        super(BowtieContentFormField, self).__init__(*args, **kwargs)

