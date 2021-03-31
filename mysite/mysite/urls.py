from django.contrib import admin
from django.urls import include, path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]

