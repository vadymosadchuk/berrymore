from datetime import datetime

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from app.models import Visit
from app.reports import ReportDaily


def view_report_index(request):
    today = datetime.now().strftime('%Y-%m-%d')
    return HttpResponseRedirect(reverse('report_daily', args=[f'{today}_{today}']))


def view_report_daily(request, date):
    report = ReportDaily(date).get_report()
    return render(request, 'app/report_daily.html', context=report)


def view_report_visit(request, visit_id):
    visit = Visit.objects.filter(id=visit_id).first()
    error = None if visit else 'visit does not exist'

    return render(request, 'app/report_visit.html', context={
        'visit': visit,
        'error': error,
    })
