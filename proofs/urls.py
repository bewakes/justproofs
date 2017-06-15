from django.conf.urls import url, include
from django.contrib import admin
from proofs.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'topics', ProofTopicViewSet)
router.register(r'proofs', ProofViewset)
router.register(r'tags', TagViewset)

urlpatterns = [
    url(r'^$', home),
    url(r'^api/', include(router.urls)),
]
