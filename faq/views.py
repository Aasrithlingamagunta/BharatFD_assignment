from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer


@api_view(["GET"])
def get_faqs(request):
    lang = request.GET.get("lang", "en")
    cache_key = f"faqs_{lang}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return Response(cached_data)

    faqs = FAQ.objects.all()
    data = [
        {
            "question": faq.get_translated_question(lang),
            "answer": faq.answer,
            "created_at": faq.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for faq in faqs
    ]
    cache.set(cache_key, data, timeout=300)
    return Response(data)
