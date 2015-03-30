# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):

    students = (
        {'id': 1,
        'first_name': u'Марк',
        'last_name': u'Хархаліс',
        'ticket': 235,
        'image': 'img/MK.jpg'},
        {'id': 2,
        'first_name': u'Юлія',
        'last_name': u'Ліпко',
        'ticket': 2123,
        'image': 'img/JL.jpg'},
        {'id': 3,
        'first_name': u'Антон',
        'last_name': u'Хархаліс',
        'ticket': 12345,
        'image': 'img/AK.jpg'},
        )
    return render(request, 'students/students_list.html',
        {'students': students})
def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups

def groups_list(request):
    groups = (
        {'id': 1, 
        'title': u'хмх 11',
        'leader': u'Марк Хархаліс'},
        {'id': 2,
        'title': u'хмх 12',
        'leader': u'Юлія Ліпко'},
        {'id': 3,
        'title': u'хмх 13',
        'leader': u'Антон Хархаліс'},
        )
    return render(request, 'students/groups_list.html',
        {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)