from rest_framework import serializers

from proofs.models import ProofTopic, Tag, Proof, Upvote, Downvote

class TopicSerialier(serializers.ModelSerializer):
    class Meta:
        model = ProofTopic
        fields = ('name', 'popularity')

class ProofSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Proof
        fields = ('topic', 'content', 'slug', 'popularity')

class TagSerialiezer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'popularity')

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = (user, proof)

class DownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downvote
        fields = (user, proof)
