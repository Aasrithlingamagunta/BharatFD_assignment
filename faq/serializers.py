from rest_framework import serializers
from django.utils.html import strip_tags
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()

    def get_answer(self, obj):
        return strip_tags(obj.answer)  # Remove HTML tags from CKEditor content

    class Meta:
        model = FAQ
        fields = ["question", "answer"]
