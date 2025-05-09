from django.db import models

class Editora(models.Model):
    name = models.CharField(max_length=100)
    site = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.name}"

