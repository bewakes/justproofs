from django.contrib import admin
from proofs.models import User, Proof, Tag, ProofTopic

# Register your models here.

admin.site.register(User)
admin.site.register(Proof)
admin.site.register(Tag)
admin.site.register(ProofTopic)
