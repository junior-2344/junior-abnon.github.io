from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    # receiving a post request from the form 
    if request.method == "POST":
        # instaciating a from if the from is valid
        form = UserCreationForm(request.POST)

        if form.is_valid(): # validating extracting data from the form
            # from.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
