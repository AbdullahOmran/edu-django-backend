
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import Register
from .views import (
    # ContentCreatorListCreateView, ContentCreatorDetailView,
    # InstructorListCreateView, 
    # InstructorDetailView,
    
    CourseListView, 
    CourseDetailView,
    # LessonListCreateView,
     LessonDetailView,
     LessonNotesUpdateView,
    # QuestionListCreateView, 
    QuestionDetailView,
    # QuestionOptionListCreateView, 
    QuestionOptionDetailView,
    ExamListCreateView, ExamDetailView,
    LoadUserView,
    # ExamQuestionListCreateView,
    #  ExamQuestionDetailView,
    # StudentListCreateView, StudentDetailView,
    AnswerListCreateView,
     AnswerDetailView,
    # FeedbackListCreateView, FeedbackDetailView
)
schema_view = get_schema_view(
    openapi.Info(
        title="Edu API Documentation",
        default_version='v1',
        description="My API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('auth/register/',Register.as_view(), name = 'auth-register' ),
    path('auth/login/',MyTokenObtainPairView.as_view(), name = 'auth-login' ),
    path('auth/refresh/',TokenRefreshView.as_view(), name = 'auth-refresh' ),
    path('auth/verify/',TokenVerifyView.as_view(), name = 'auth-verify' ),
    path('auth/load-user/',LoadUserView.as_view(), name = 'auth-load-user' ),
    # path('auth/token/',MyTokenObtainPairView.as_view(), name = 'auth-token' ),
    # path('auth/logout/',TokenRefreshView.as_view(), name = 'token-refresh' ),
    # path('auth/forgot-password/',TokenRefreshView.as_view(), name = 'token-refresh' ),
    # path('auth/reset-password/',TokenRefreshView.as_view(), name = 'token-refresh' ),
    # path('contentcreators/', ContentCreatorListCreateView.as_view(), name='contentcreator-list-create'),
    # path('contentcreators/<uuid:pk>/', ContentCreatorDetailView.as_view(), name='contentcreator-detail'),
    # path('instructors/', InstructorListCreateView.as_view(), name='instructor-list-create'),
    # path('instructors/<uuid:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<uuid:pk>/', CourseDetailView.as_view(), name='course-detail'),
    # path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lesson/<uuid:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('lesson-notes/<uuid:pk>/update/', LessonNotesUpdateView.as_view(), name='lesson-notes-update'),
    # path('questions/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('questions/<uuid:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    # path('questionoptions/', QuestionOptionListCreateView.as_view(), name='questionoption-list-create'),
    path('questionoptions/<uuid:pk>/', QuestionOptionDetailView.as_view(), name='questionoption-detail'),
    path('exams/', ExamListCreateView.as_view(), name='exam-list-create'),
    path('exams/<uuid:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    # path('examquestions/', ExamQuestionListCreateView.as_view(), name='examquestion-list-create'),
    # path('examquestions/<uuid:pk>/', ExamQuestionDetailView.as_view(), name='examquestion-detail'),
    # path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    # path('students/<uuid:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('answers/', AnswerListCreateView.as_view(), name='answer-list-create'),
    path('answers/<uuid:pk>/', AnswerDetailView.as_view(), name='answer-detail'),
    # path('feedbacks/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
    # path('feedbacks/<uuid:pk>/', FeedbackDetailView.as_view(), name='feedback-detail'),
]
