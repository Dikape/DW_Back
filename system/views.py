from django.http import HttpResponse
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
        item, wt, val = items[j - 1]
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
            item, wt, val = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result


def math_algorithm(request):
    center_lat1 = 32.33
    center_lon1 = 49.2
    distance_price = 9
    categories = ObjectCategory.objects.filter(id__in=[2,3,4,5])
    objects_by_categories = {}
    for category in categories:
        invest_objects = category.investmentobject_set.filter()
        objects_price = {}
        for obj in invest_objects:
            points = obj.map_points.all()
            if points.count() == 1:

                obj_distance = vincenty((center_lat1, center_lon1), (points[0].map_lat, points[0].map_lon)).kilometers
                # print('price {0} distance {1}'.format(obj.price, obj_distance))
                objects_price[obj.id] = float(obj.price) + obj_distance*distance_price

        objects_by_categories[category.title] = {k:v for k,v in objects_price.items() if v==min(objects_price.values())}
        # for obj in invest_objects:
        #     if obj.objects.fil
    items = ()
    costs = [10, 12, 20, 15]
    i = 0
    for k,v in objects_by_categories.items():
        items += (k, int(list(v.values())[0]), costs[i]),
        i+=1

    result = knapsack01_dp(items, 10000)
    print(result)



    return HttpResponse(result)