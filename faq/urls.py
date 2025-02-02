from django.urls import path
from .views import get_faqs, interactive_faq_view

urlpatterns = [
    path("api/faqs/", get_faqs, name="api_faqs"),
    path("", interactive_faq_view, name="interactive_faq"),
]
