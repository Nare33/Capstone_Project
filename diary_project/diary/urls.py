from django.urls import path
from .views import UserCreate, UserLogin, EntryListCreate, EntryRetrieveUpdateDestroy, EntryHistory

urlpatterns = [
    path('users/', UserCreate.as_view()),
    path('login/', UserLogin.as_view()),
    path('entries/', EntryListCreate.as_view()),
    path('entries/<int:pk>/', EntryRetrieveUpdateDestroy.as_view()),
    path('history/', EntryHistory.as_view()),
]
