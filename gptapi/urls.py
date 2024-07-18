from django.urls import path
from .views import GPTResponseView

urlpatterns = [
    path('gpt/', GPTResponseView.as_view(), name='get_gpt_response'),
]
