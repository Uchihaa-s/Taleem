from django.contrib import admin
from django.urls import path

from Questions.views import QuestionListView, QuestionDetailView, ConversationView, AnswerView, QuestionsCreationView

urlpatterns = [
                  path('', QuestionListView.as_view(),name="Feed"),
                  path('<int:pk>/', QuestionDetailView.as_view(),name="question_view"),
                  path('answer/<int:pk>/', AnswerView.as_view(),name="answer_view"),
                  path('Conversation/<int:pk>/', ConversationView.as_view(),name="Comment_view"),
                  path('Question_creation/', QuestionsCreationView.as_view(),name="QuestionsCreationView"),
              ]