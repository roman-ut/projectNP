from django import template

register = template.Library()

@register.filter()
def censor(value):
   if not isinstance(value, str):
      raise ValueError('Нельзя цензурировать не строку')
   value = value.lower()
   exceptional_words = ['sometext', 'sometitle']
   for i in exceptional_words:
      value = value.replace(i, '*'*(len(i)-1))
      value = value.replace(i.capitalize(), '*'*len(i))
   return f'{value}'