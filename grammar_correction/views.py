from django.shortcuts import render

# Create your views here.


def correct_grammatical_mistake(request):
    meta = request.META
    print(meta)

    return True
