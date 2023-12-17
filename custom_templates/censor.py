from django import template
import re

register = template.Library()

@register.filter
def censor(value):
    censored_words = ['bad_word1', 'bad_word2']
    for word in censored_words:
        value = re.sub(r'\b{}\b'.format(word), '*', value, flags=re.IGNORECASE)
    return value