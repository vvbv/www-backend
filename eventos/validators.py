from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
def validate_date_before_now(date):
    if date <= timezone.now():
        raise ValidationError(
            _('La fecha de inicio del evento no puede ser menor a la fecha actual')
        )