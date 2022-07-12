from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate, Poll, Choice

import datetime

# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'elections/index.html')


def areas(request, area):
    today = datetime.datetime.now()
    try :
        poll = Poll.objects.get(area = area, start_date__lte = today, end_date__gte=today) # get에 인자로 조건을 전달해줍니다.
        candidates = Candidate.objects.filter(area = area) # Candidate의 area와 매개변수 area가 같은 객체만 불러오기
    except:
        poll = None
        candidates = None
    context = {'candidates': candidates,
               'area' : area,
               'poll' : poll }
    return render(request, 'elections/area.html', context)