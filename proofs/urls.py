from django.conf.urls import url
from django.contrib import admin
from proofs.views import *

urlpatterns = [
    url(r'^', home)
]
