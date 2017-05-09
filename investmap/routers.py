from rest_framework import routers

from investmap import viewsets

router = routers.SimpleRouter()
# Register viewsets in router
router.register(r'objects', viewsets.InvestMapObjectViewSet, 'InvestMapObject')
router.register(r'object_points', viewsets.InvestMapPointViewSet, 'InvestMapPoint')
router.register(r'holders', viewsets.ObjectHolderViewSet, 'ObjectHolder')

