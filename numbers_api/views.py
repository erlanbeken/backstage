from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import Log
from time import gmtime, strftime


def difference(request):
    n = request.GET.get('number', False)

    if not n:
        raise Http404('<N> parameter required')

    if not n.isdigit():
        raise Http404('<N> parameter must be an integer')

    n = int(n)

    if n < 0 or n > 100:
        raise Http404('<N> must be greater that 0 and less than 100')

    try:
        entry = Log.objects.get(number=n)
        entry.occurrences += 1
    except Log.DoesNotExist:
        entry = Log()
        entry.do_calc(n)

    entry.save()

    result = {
        "datetime"    : strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        "value"       : entry.value,
        "number"      : n,
        "occurrences" : entry.occurrences
    }
    return JsonResponse(result)


def index(request):
    return render(request, 'index.html', {})