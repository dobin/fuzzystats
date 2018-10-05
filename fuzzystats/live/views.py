from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .serializers import FuzzingRunSerializer
from .models import FuzzingRun


# WWW

def fuzzingrun_list(request):
    fuzzingruns = FuzzingRun.objects.order_by('start_time')
    return render(request, 'live/fuzzingrun_list.html', { 'fuzzingruns': fuzzingruns })


def fuzzingrun_latest(request):
    fuzzingrun = FuzzingRun.objects.latest('id')
    return render(request, 'live/fuzzingrun_latest.html', { 'fuzzingrun': fuzzingrun })


# REST

@api_view(['GET', 'POST'])
def fuzzingrun_list(request):
    """
    List all code fuzzingruns, or create a new fuzzingrun.
    """
    if request.method == 'GET':
        fuzzingruns = FuzzingRun.objects.all()
        serializer = FuzzingRunSerializer(fuzzingruns, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FuzzingRunSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def fuzzingrun_detail(request, pk):
    """
    Retrieve, update or delete a code fuzzingrun.
    """
    try:
        fuzzingrun = FuzzingRun.objects.get(pk=pk)
    except FuzzingRun.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FuzzingRunSerializer(fuzzingrun)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FuzzingRunSerializer(fuzzingrun, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        fuzzingrun.delete()
        return HttpResponse(status=204)
