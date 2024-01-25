from django.shortcuts import render
from .models import Post
# Create your views here.

# posts = [
#     {
#         "author": 'Abnon',
#         'title': "Blog 1",
#         'content': 'dsfg3rltuixgn b stitrlw34nbt srt ltugw',
#         'date_posted': "December 3 2023"
#     },
#     {
#         "author": 'junior',
#         'title': "Blog 2",
#         'content': 'dsfg3rltuixgn b stitrlw34nbt srt ltugw',
#         'date_posted': "December 3 2023"
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all() #unparking the dictionary from the database for rendurin inside the html
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
