from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Ascii
# Create your views here.
import ascii_magic

#
# def home(request):
#     if request.user.is_authenticated:
#         user = request.user
#         if request.method == 'POST':
#             file = request.POST.get('file')
#             print(user)
#             print(file)
#
#             asciii = Ascii(user=user, image=file)
#             asciii.save()
#             print(asciii.image.url)
#             image = ascii_magic.from_image_file(f'C://Users//user//developer//talantblog//static//img/{asciii.image.url}')
#             ascii_magic.to_html_file('../templates/ascii/magic.html', image)
#     return render(request, 'ascii/home.html')
