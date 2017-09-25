from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
def validate_date_start_event_before_now(date):
    if date <= timezone.now():
        raise ValidationError(
            _('La fecha de inicio del evento no puede ser menor a la fecha actual')
        )
def validate_now_before_date_finish_event(date):
    if timezone.now() >= date:
        raise ValidationError(
            _('La fecha de finalizacion del evento ya ha pasado, no puede editarlo')
        )