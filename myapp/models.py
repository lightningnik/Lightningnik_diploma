# myapp/models.py

from django.db import models

class Diploma(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='diplomas/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title