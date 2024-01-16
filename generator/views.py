from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    nums = []
    for i in range(1, 101):
        nums.append(i)
    return render(request, 'generator/home.html', {'nums': nums})

def generator(request):
    character = list('abcdefghijklmnopqrstuvwxyz')
    uChar = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lchar = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        val = len(character)
        for c in range(val):
            character.append(character[c].upper())
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()+-_:/\\?|,.'))
    if request.GET.get('numbers'):
        character.extend(list('01234567890123456789'))

    random.shuffle(character)

    length = int(request.GET.get('length'))
    password = []
    val = []

    for it in range(1000):
        temp = ''
        if request.GET.get('uppercase'):
            temp+=random.choice(uChar)
        else:
            temp+=random.choice(lchar)
        for i in range(length-1):
            temp+=random.choice(character)
        lower, upper, num, special = 0, 0, 0, 0
        for i in temp:
            if i>='a' and i<='z':
                lower+=1
            elif i>='A' and i<='Z':
                upper+=1
            elif i>='0' and i<='9':
                num+=1
            else:
                special+=1
        tos = [lower, upper, num, special]
        tos.sort()
        val.append((tos[3]-tos[0], it))
        password.append(temp)
    val.sort()
    return render(request, 'generator/password.html', {'password': password[val[0][1]]})

def about(request):
    return render(request, 'generator/about.html')