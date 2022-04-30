from django.forms import ModelForm, BooleanField   # Импортируем true-false поле


from .models import Post, Author, Category


class NewsForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Post
        fields = ['title', 'text', 'auth', 'postCategory',
                  'check_box']


class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


class SubscribeForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']
