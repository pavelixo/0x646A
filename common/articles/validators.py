from django.core import validators
from django.utils.crypto import get_random_string
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError


@deconstructible
class TitleValidator(validators.RegexValidator):
    regex = r"^[a-zA-Z\s]+$"
    message = "Enter a valid product name (only letters and spaces allowed)."


@deconstructible
class UploadToValidator:
    def __call__(self, instance, filename):
        """
        Generates the new filename using a random string and file extension.
        """

        mark = get_random_string(16).lower()  # Generates a random string
        return f"articles/articles.{mark}.md"  # Returns the new file name