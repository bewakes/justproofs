from django.shortcuts import render
from django.views import View
from proofs.models import User, Tag, Proof, Upvote, Downvote, ProofTopic
from proofs.serializers import *

from rest_framework import viewsets

# Create your views here.

def home(request):
    return render(request, 'index.html', {})


class ProofTopicViewSet(viewsets.ModelViewSet):
    """ viewset for proof topics """
    queryset = ProofTopic.objects.all()
    serializer_class = TopicSerializer

class ProofViewset(viewsets.ModelViewSet):
    """ viewset for proofs """
    queryset = Proof.objects.all()
    serializer_class = ProofSerializer

class TagViewset(viewsets.ModelViewSet):
    """ viewset for tags """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
