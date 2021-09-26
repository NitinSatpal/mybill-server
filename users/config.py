from django.db import models


class ProfileType(models.IntegerChoices):
    PERSONAL = 1
    BUSINESS = 2
