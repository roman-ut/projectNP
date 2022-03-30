from django import template

register = template.Library()

@register.filter()
def censor(value):
   value = value.lower()
   exceptional_words = ['sometext', 'sometitle']
   for i in exceptional_words:
      value = value.replace(i, '*'*len(i))
      value = value.replace(i.capitalize(), '*'*len(i))
   return f'{value}'