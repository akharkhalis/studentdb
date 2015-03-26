# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def journal(request):

    journal = (
        {'id': 1,
        'name': u'Марк Хархаліс',
        'ticket': 235,
        },
        {'id': 2,
        'name': u'Юлія Ліпко',
        'ticket': 2123,
        },
        {'id': 3,
        'name': u'Антон Хархаліс',
        'ticket': 12345,
        },
        )
    return render(request, 'students/journal.html',
        {'journal': journal})

