import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def is_valid_time_format(time_str):
    # The pattern for checking the time format "HH:MM"
    time_pattern = re.compile(r'^([01]\d|2[0-3]):([0-5]\d)$')

    return bool(time_pattern.match(time_str))


def validate_working_hours(value):
    if not isinstance(value, dict):
        raise ValidationError(_('Invalid format for working hours'))

    expected_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for day in expected_days:
        if day not in value:
            raise ValidationError(_(f'Missing {day} in working hours'))

        if "open" not in value[day] or "close" not in value[day]:
            raise ValidationError(_(f'Invalid structure for {day} in working hours'))

        if not is_valid_time_format(value[day]["open"]) or not is_valid_time_format(value[day]["close"]):
            raise ValidationError(_(f'Invalid time format for {day} in working hours'))
