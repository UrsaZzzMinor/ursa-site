#from django.views.generic.base import View
from django.shortcuts import render_to_response


def show_about(request):
    return render_to_response('About.html')


def show_gallery(request):
    return render_to_response('Gallery.html', {'a': [1, 2, 3]}) 


def show_photo(request, name):
    return render_to_response('photo.html',
                              {'photo': 'img/' + name + '.jpg'})