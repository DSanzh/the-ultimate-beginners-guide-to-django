from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == 'POST':
        registerUser()
    else:
        return render(request, 'accounts/signup.html')

def registerUser():
    print('register user')