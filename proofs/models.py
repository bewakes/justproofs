import re
from django.db import models

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.core import validators
from django.utils import timezone

from django_extensions.db.fields import AutoSlugField

from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self,  email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given  email and password.
        """
        current_time = timezone.now()
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=current_time,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,  email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_staffuser(self,  email, password=None, **extra_fields):
        return self._create_user(email, password, True, False,
                                 **extra_fields)

    def create_superuser(self,  email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile", "name", ]

    name = models.CharField("Name", max_length=200, blank=False)
    email = models.EmailField("email address", blank=False, unique=True)
    slug = AutoSlugField(populate_from="email")
    is_staff = models.BooleanField("staff status", default=False, help_text=_(
        "Designates whether the user can log into this admin site."))
    is_active = models.BooleanField("Active", default=True, help_text=_(
        "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."))
    mobile = models.CharField(null=False, blank=False, max_length=14,
                              validators=[
                                  validators.RegexValidator(re.compile(r"^([+][9][7][7][9][678][0-9]{8}|[9][678][0-9]{8})$"), (
                                      "Required. either +9779xxxxxxxxx or 9xxxxxxxxx. Enter a valid mobile."), "invalid")
                              ])
    created_by = models.ForeignKey(
        "self", null=True, default=None, on_delete=models.SET_NULL)
    is_mobile_verified = models.BooleanField(
        null=False, blank=False, default=False)
    reset_value = models.CharField(max_length=100, null=True, blank=True)

    created_on = models.DateTimeField("Created Date", auto_now_add=True)
    modified_on = models.DateTimeField("Modified Date", auto_now=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)
    deleted_on = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=False,
        default=None
    )

    objects = UserManager()

    def get_short_name(self):
        return self.name

class ProofTopic(models.Model):
    """
    Title of the proof. Title is separate model because single topic can have
    many proofs
    """
    name = models.CharField(max_length=300)
    popularity = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    Tag for proofs
    """
    name = models.CharField(max_length=40)
    popularity = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Proof(models.Model):
    """
    Main proof model
    """
    topic = models.ForeignKey(ProofTopic)
    content = models.TextField()
    slug = AutoSlugField(populate_from='topic')
    tags =  models.ManyToManyField(Tag, related_name='proofs')
    popularity = models.FloatField(default=0)

    def __str__(self):
        return self.topic.name


class Upvote(models.Model):
    """
    Upvotes for a proof
    """
    user = models.ForeignKey(User)
    proof = models.ForeignKey(Proof)

class Downvote(models.Model):
    """
    Downvotes for a proof
    """
    user = models.ForeignKey(User)
    proof = models.ForeignKey(Proof)
