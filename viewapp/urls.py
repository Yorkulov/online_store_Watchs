from django.urls import path
from django.views.generic import TemplateView
from .views import WatchView, CreateWatchView, watchDetail, DeleteWatchView, UpdateWatchView, WatchBuyView, WatchRegisterView, CommentView, AdminPageView

urlpatterns = [
    path('', WatchView.as_view(), name="home_page_view"),
    path('admin-panel/', AdminPageView.as_view(), name="admin_page"),
    path('product/', WatchView.as_view(template_name="pages/product.html"), name="product_page_view"),
    # path('contact/', ContactView.as_view(), name="contact_page_view"),
    path('watch/<int:pk>/comment', CommentView.as_view(), name="comments"),
    path('watch/<int:pk>/', watchDetail, name="watch_detail"),
    path('create/', CreateWatchView.as_view(), name="create_watch"),
    path('delete/<int:pk>/', DeleteWatchView.as_view(), name="delete_watch"),
    path('update/<int:pk>/', UpdateWatchView.as_view(), name="update_watch"),
    path('watch/<int:pk>/register/', WatchRegisterView.as_view(), name="watch_register"),
    path('watch/<int:pk>/register/buy/', WatchBuyView.as_view(), name="watch_buy"),
]
