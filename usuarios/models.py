# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

class CustomUser(User):
    username_validator = ASCIIUsernameValidator()


# Create your models here.
