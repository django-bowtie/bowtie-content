from django.db import models
from django.utils.six import with_metaclass, text_type
from django.utils.translation import ugettext_lazy as _

from content import BowtieContent
from forms import BowtieContentFormField


class SirTrevorField(with_metaclass(models.SubfieldBase, models.Field)):
    description = _("TODO")

    def get_internal_type(self):
        return 'TextField'

    def formfield(self, **kwargs):
        defaults = {
            'form_class': BowtieContentFormField
        }
        defaults.update(kwargs)
        return super(SirTrevorField, self).formfield(**defaults)

    def to_python(self, value):
        return BowtieContent(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        return text_type(value)
