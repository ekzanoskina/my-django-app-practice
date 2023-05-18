from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# def monday(request):
#     return HttpResponse("watch tv")
#
# def tuesday(request):
#     return HttpResponse("walk with a dog")

dct_week_days = {
    'monday': 'в понедельник я жалею себя',
    'tuesday': 'во вторник - глазею в пропасть',
    'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
    'thursday': 'в четверг - зарядка',
    'friday': 'ужин с собой, нельзя снова его пропускать',
    'saturday': 'в субботу - борьба с презрением к себе',
    'sunday': 'в воскресенье - иду на рождество'
}

def what_to_do(request, day_of_week: str):

    if day_of_week.lower() in dct_week_days:
        return HttpResponse(dct_week_days[day_of_week.lower()])
    return HttpResponseNotFound(f'{day_of_week} - такого дня недели нет.')

def what_to_do_by_number(request, day_of_week: int):
    if 0 < day_of_week < 8:
        days = list(dct_week_days)
        name_day = days[day_of_week - 1]
        new_url = reverse('day-number', args=(name_day,))
        return HttpResponseRedirect(new_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {day_of_week}')