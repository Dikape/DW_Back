from django.http import HttpResponse, JsonResponse
import requests
from math import sin, cos, sqrt, atan2, radians, asin

from investmap.models import ObjectCategory, InvestmentObject, InvestMapPoint
from geopy.distance import vincenty

def index(request):
    return HttpResponse('<h1>Home page of graduation work! Authors: Volodymyr Gorobyuk and Kasianchyk Dmytro</h1>'
                        '<p><a href="/api">Go to API</a></p>'
                        '<p><a href="/admin">Go to the admin page</a></p>')


def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, wt, val, obj_id = items[j - 1]
        for w in range(1, limit + 1):
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            item, wt, val, obj_id = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result


def math_algorithm(request):
    center_lat = request.POST.get('center_lat')
    center_lon = request.POST.get('center_lon')
    max_weight = request.POST.get('max_sum')
    categories_list = request.POST.get('categories')
    categories_id = [i[0] for i in categories_list]
    categories_costs = [i[1] for i in categories_list]

    categories = ObjectCategory.objects.filter(id__in=categories_id)
    objects_by_categories = {}

    distance_koef = 10

    result = {}
    for category in categories:
        invest_objects = category.investmentobject_set.filter()
        objects_price = {}
        for obj in invest_objects:
            points = obj.map_points.all()
            if points.count() == 1:

                obj_distance = vincenty((center_lat, center_lon), (points[0].map_lat, points[0].map_lon)).kilometers
                # print('price {0} distance {1}'.format(obj.price, obj_distance))
                objects_price[obj.id] = float(obj.price) + obj_distance*distance_koef

        objects_by_categories[category.id] = {k:v for k,v in objects_price.items() if v==min(objects_price.values())}
        # for obj in invest_objects:
        #     if obj.objects.fil
    items = ()
    i = 0
    for k,v in objects_by_categories.items():
        items += (k, int(list(v.values())[0]), categories_costs[i], list(v.keys())[0]),
        i+=1

    result_knapsack = knapsack01_dp(items, max_weight)

    result['result'] = [[i[0], i[3]] for i in result_knapsack]


    return JsonResponse(result, safe=False)