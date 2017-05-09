from django.db import models

from django.contrib.auth.models import User


# PROJECT_TYPES = [
#     ('fb', 'Приміщення'),
#     ('fa', 'Ділянка'),
#     ('cp', 'Інвестиційний проект')
# ]

OBJECT_TYPES = [
    (0, 'Приміщення'),
    (1, 'Ділянка')
]


class ObjectHolder(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва')
    address = models.CharField(max_length=100, verbose_name='Адреса')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'investmap_holders'


class InvestMapObject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва')
    description = models.CharField(max_length=1000, verbose_name='Опис')
    price = models.CharField(max_length=16, verbose_name='Ціна')
    address = models.CharField(max_length=100, verbose_name='Адреса')
    metrics = models.CharField(max_length=50, verbose_name='Площа')
    contacts = models.CharField(max_length=100, verbose_name='Контакти')
    object_holder = models.ForeignKey(ObjectHolder, verbose_name='Власник')
    # project_type = models.CharField(max_length=2, choices=PROJECT_TYPES,
    #                                 default=PROJECT_TYPES[0], verbose_name='Тип об\'єкту')
    object_type = models.IntegerField(choices=OBJECT_TYPES, default=0, verbose_name='Тип об\'єкта')

    # image = models.ImageField(upload_to='investmap/', verbose_name='')


    @property
    def lat_lng(self):
        query = InvestMapPoint.objects.filter(investmap_object=self)
        count = query.count()
        result = []
        if count == 1:
            result = query.first().lat_lng()
        elif count > 1:
            result = [coordinate.lat_lng() for coordinate in query]
        return result
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'investmap_objects'


class InvestMapPoint(models.Model):
    investmap_object = models.ForeignKey(InvestMapObject, on_delete=models.CASCADE)
    map_lon = models.CharField(max_length=64)
    map_lat = models.CharField(max_length=64)

    def lat_lng(self):
        return {'lat': float(self.map_lat), 'lng': float(self.map_lon)}

    class Meta:
        db_table = 'investmap_points'


class InvestMapLog(models.Model):
    investmap_object = models.ForeignKey(InvestMapObject, on_delete=models.SET_NULL, null=True)
    data_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operation = models.CharField(max_length=32)
    ip_address = models.CharField(max_length=32)

    class Meta:
        db_table = 'investmap_logs'


