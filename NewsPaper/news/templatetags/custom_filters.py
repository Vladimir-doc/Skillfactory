from django import template

register = template.Library()

@register.filter()
def censor(value):
    bad_words = ['год', 'момент', 'сегодня', 'имена', 'сторонники', 'здания', 'пистолета', 'талибам', 'позор', 'протестующие']

    for b_word in bad_words:
        for word in value.split():
            if word.lower().count(b_word) and len(word) > len(b_word):
                value = value.replace(word, f'{word[0]}{"*" * (len(word) - 1)}')
    return value