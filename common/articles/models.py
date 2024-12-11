from django.db import models
from django.utils.text import slugify
from .validators import TitleValidator, UploadToValidator


class Article(models.Model):
    title_validator = TitleValidator()
    title = models.CharField(max_length=256, unique=True, validators=[title_validator])
    
    upload_to_validator = UploadToValidator()
    content = models.FileField(upload_to=upload_to_validator)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "common_articles"
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
