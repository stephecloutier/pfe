from django.core.exceptions import ValidationError
import re

def validate_ean(value):
    pattern = re.compile("^[0-9]{13}$")
    if not pattern.match(value):
        raise ValidationError(
            ('Le code EAN doit être numérique et composé de 13 chiffres.'),
            code='invalid_ean_number')