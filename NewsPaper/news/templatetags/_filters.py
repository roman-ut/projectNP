from django import template

register = template.Library()

@register.filter()
def censor(value):
   exceptional_words = ['sometext', 'sometitle']
   for i in exceptional_words:
      value = value.replace(i, '*')
   return f'{value}'