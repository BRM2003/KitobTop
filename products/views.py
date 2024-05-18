from django.shortcuts import render
from django.http import JsonResponse
from users.models import Merchants
from .models import *
import json


def main_page(request):
    libraries = []
    stores = []
    try:
        libs = Merchants.objects.all().order_by('merchant_name')
        for lib in libs:
            books = Books.objects.filter(library=lib)
            for book in books:
                all_languages = book.languages.all()

                libraries.append({
                    'libraryName': lib.merchant_name,
                    'address': lib.address,
                    'location': lib.address,
                    'bookLanguages': get_langs(all_languages)
                })

        books2 = Books.objects.all()
        for book in books2:
            stores.append({
                'storeName': book.title,
                'address': book.library.all()[0].address,
                'location': book.library.all()[0].address,
                'price': book.price,
                'bookLanguages': get_langs(book.languages.all())
            })

    except Exception as e:
        print(str(e))
    # return render(request, 'Main/main_page.html', response)
    return JsonResponse({
            'libraries': libraries,
            'stores': stores
        })


def get_langs(list):
    langs = []
    try:
        for el in list:
            langs.append(el.language)
    except Exception as e:
        print('Error get_langs: ' + str(e))
    return langs

