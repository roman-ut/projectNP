from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Post


class NewsForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Post
        fields = ['title', 'text', 'auth',
                  'check_box']  # не забываем включить галочку в поля иначе она не будет показываться на странице!