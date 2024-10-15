import secrets
import random
import string
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from django.urls import reverse_lazy, reverse
from users.models import User
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.shortcuts import get_object_or_404, redirect
# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email_confirm/{token}/"
        send_mail(subject="Подтверждение почты",
                  message=f"Привет,перейди по ссылке для подтверждения почты{url}",
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email])
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


def generate_random_password(length=8):
    # Фун-ция кот.генерирует пароль

    # Определяем возможные символы для пароля
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''  # Создаем пустую строку для пароля
    # Генерируем пароль
    for i in range(length):
        random_char = random.choice(characters)  # Выбираем случайный символ
        password += random_char  # Добавляем его к паролю

    return password


def reset_password(request):
    # ф-ция восстановления, пароля зарегистрированного пользователя

    if request.method == 'POST':  # Мы проверяем, является ли метод запроса POST.
        email = request.POST.get('email')  # извлекаем email  из запроса

        try:
            user = User.objects.get(email=email)  # пытаемся получить пользователя по email
            new_password = generate_random_password()  # Генерация нового пароля через ф-цию
            user.password = make_password(new_password)  # Хеширование пароля
            user.save()

            # Отправка нового пароля на электронную почту
            send_mail(
                subject="Ваш новый пароль",
                message=f"Ваш новый пароль: {new_password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )
            # Перенаправление на страницу входа после успешного восстановления
            return redirect('users:login')

        # Обработка случая, когда пользователь не найден
        except User.DoesNotExist:
            return render(request, 'users/password_reset.html', {'error': 'Пользователь с таким email не найден.'})
    # Если метод запроса не POST, а GET мы просто отображаем форму для восстановления пароля.
    return render(request, 'users/password_reset.html')
