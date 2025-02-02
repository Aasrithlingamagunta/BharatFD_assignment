from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer


def get_faqs(request):
    """
    Fetch FAQs with caching.
    """
    lang = request.GET.get("lang", "en")

    cached_data = cache.get(f"faqs_{lang}")
    if cached_data:
        return JsonResponse({"faqs": cached_data})

    faqs = FAQ.objects.all()
    faq_data = [
        {
            "question": faq.get_translated_question(lang),
            "answer": faq.answer
        }
        for faq in faqs
    ]

    cache.set(f"faqs_{lang}", faq_data, timeout=600)
    return JsonResponse({"faqs": faq_data})


def interactive_faq_view(request):
    """
    Interactive FAQ Web Page.
    """
    return render(request, "faq/interactive.html")
