from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/' , include('booking.urls')),
    path('ask/' , include("chatbot.urls")),
    path('user/' , include('user.urls')),
]
