from rest_framework.routers import DefaultRouter

from .views import BookViewSet, OrderViewSet 

router = DefaultRouter()

router.register(r'books', BookViewSet)
router.register(r'orders', OrderViewSet) 

urlpatterns = router.urls