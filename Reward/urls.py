from django.urls import path

from Reward.views import TransactionListView, TransactionCreateView, RewardCreateView

urlpatterns = [
    path('', TransactionListView.as_view()),
    path('create/', TransactionCreateView.as_view(),name="Transaction_create_view"),
    path('Reward/<int:pk>/', RewardCreateView.as_view(),name="Reward_create_view"),
]