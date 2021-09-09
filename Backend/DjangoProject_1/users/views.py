from django.shortcuts import render, redirect
# importing django forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# defining a function for registration
def register(request):
    # the form is only given if a post request is made else it is a blank return
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #checks if form data is valid. If true then gets the username
        if form.is_valid():
            username = form.cleaned_data.get('username')
            #gives a flash msg when an account is created
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
    # the {'form': form} part is used for accessing form content from within the reg template

