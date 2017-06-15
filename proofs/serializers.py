from rest_framework import serializers

from proofs.models import ProofTopic, Tag, Proof, Upvote, Downvote

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProofTopic
        fields = ('id', 'name', 'popularity', 'user')

class ProofSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Proof
        fields = ('id', 'topic', 'content', 'slug', 'popularity', 'user')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'popularity', 'slug')

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ('user', 'proof')

class DownvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downvote
        fields = ('user', 'proof')
