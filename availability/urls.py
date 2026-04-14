from django.urls import path
from .views import availability_view, book_slot

urlpatterns = [
    path('availability/', availability_view),
    path('book/', book_slot),   # ✅ ADD THIS
]