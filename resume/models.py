from django.db import models


class Formation(models.Model):
    diplôme = models.CharField(max_length=60)
    date_obtention = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.diplôme} {self.date_obtention}"


class ExperiencePro(models.Model):
    entreprise = models.CharField(max_length=60)
    job = models.CharField(max_length=30)
    début = models.DateTimeField(auto_now=False, auto_now_add=False)
    fin = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.entreprise} {self.job}"
