from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from events_site.managers import CustomUserManager


class CustomUser(AbstractUser):
    birthdate = models.DateField(_("date of birth"), null=True)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    title = models.CharField(_("title"), max_length=150)
    text = models.TextField(_("text"))
    date = models.DateTimeField(_("date"))
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    participants = models.ManyToManyField(CustomUser, _('participants'))

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return f"{self.title} {self.date}"

