from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = "sponsors"
urlpatterns = [
    path(
        "sponsors/<owner>/<repo>.svg",
        cache_page(views.SponsorshipView.TTL)(views.SponsorshipView.as_view()),
        name="sponsors",
    )
]
