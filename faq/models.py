from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi Translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali Translation
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Ensures translations are generated automatically if not provided.
        """
        if not self.pk:  # Only translate if it's a new object
            if not self.question_hi:
                self.question_hi = translator.translate(self.question, dest='hi').text
            if not self.question_bn:
                self.question_bn = translator.translate(self.question, dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        """Returns the translated question based on the language parameter."""
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        return translations.get(lang, self.question)  # Default to English

    def __str__(self):
        return self.question
