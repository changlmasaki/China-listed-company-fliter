from django.http import HttpResponse
from django.shortcuts import render
from .models import List
from collections import defaultdict


# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

    # x_data = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    # y_data = [5, 20, 36, 10, 10, 20]

    # return render(request, 'insert_table.html', {'x_data': x_data, 'y_data': y_data})


def demo(request):
    dict_company = defaultdict(int)
    for i in List.objects.all():
        dict_company[i.abbr] += 1
    # print(dict_company)
    dict_company = sorted(dict_company.items(), key=lambda item: item[1], reverse=True)[:10]
    x_data = [x[0] for x in dict_company]
    # print(x_data)

    dict_province = defaultdict(int)
    for i in List.objects.all():
        dict_province[i.province] += 1
    # print(dict_province)
    dict_province = sorted(dict_province.items(), key=lambda item: item[1], reverse=True)[:800]
    y1_data = [x[0] for x in dict_province]
    y2_data = [x[1] for x in dict_province]

    dict_example = {}

    for i in range(len(y1_data)):
        name = y1_data[i]
        value = y2_data[i]
        dict_example[i] = {"name": name, "value": value}

    #for x in dic_example.keys():
        #print(dic_example[x])

    dict_example = [x[1] for x in dict_example.items()]

    #####################################################################################

    dict_job = defaultdict(int)
    for i in List.objects.all():
        dict_job[i.job_category] += 1

    dict_job = sorted(dict_job.items(), key=lambda item: item[1], reverse=True)[:800]
    z1_data = [x[0] for x in dict_job]
    z2_data = [x[1] for x in dict_job]

    dict_example2 = {}

    for i in range(len(z1_data)):
        name2 = z1_data[i]
        value2 = z2_data[i]
        dict_example2[i] = {"name": name2, "value": value2}

    dict_example2 = [x[1] for x in dict_example2.items()]

    #####################################################################################
    table = List.objects.all()[:800]

    return render(request, 'insert_table.html', {'x_data': x_data, 'y_data': dict_example, 'table': table})
