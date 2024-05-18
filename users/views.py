from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import Admins


def authentication(request):
    response = {}
    try:
        if request.method == 'POST':
            print(request.POST)

            if request.POST['type'] == 'sign-in':
                user = sign_in(request, {
                    'username': request.POST['username'],
                    'password': request.POST['password']
                })
            else:
                user = sign_up(request, {
                    'username': request.POST['username'],
                    'email': request.POST['email'],
                    'password': request.POST['password']
                })

            if 'error' not in user:
                page_return = get_page_return(request.POST, user)
                print(page_return)
                return redirect(page_return)
            else:
                response['error'] = user['error']
        else:
            if request.user.is_authenticated:
                return redirect('main_page')
    except Exception as e:
        print('Error in authentication: ' + str(e))
        response['error'] = 'Error: ' + str(e)
    return render(request, 'authenticate/sign_in(up).html', response)


def is_user_exist(request, username, password):
    return authenticate(request, username=username, password=password)


def sign_in(request, data):
    result = {}
    try:
        user = is_user_exist(request, data['username'], data['password'])
        if user is not None:
            login(request, user)
            result['user'] = user
        else:
            result['error'] = 'Username or Password is incorrect'
    except Exception as e:
        print('Error in sign_in: ' + str(e))
        result['error'] = 'Something went wrong: ' + str(e)
    finally:
        return result


def sign_up(request, data):
    return is_user_exist(request, data['username'], data['password'])


def get_page_return(request, user):
    try:
        if 'page_return' in request:
            page_return = request['page_return']
            if page_return == '':
                if Admins.objects.filter(user__user__username=user).exists():
                    return 'admin'
                else:
                    return 'main_page'
            else:
                return page_return
        else:
            if Admins.objects.filter(user__user__username=user).exists():
                return 'admin'
            else:
                return 'main_page'
    except Exception as e:
        print('Error in get_page_return: ' + str(e))
        return 'Error in get_page_return: ' + str(e)

