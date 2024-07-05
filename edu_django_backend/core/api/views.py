from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from ..models import (
    ContentCreator, Instructor, Course, Lesson, Question,
    QuestionOption, Exam, ExamQuestion, Student, Answer, Feedback
)
from .paginations import LessonPagination
from .serializers import (
    ContentCreatorSerializer, InstructorSerializer, CourseListSerializer,CourseDetailSerializer,
    LessonListSerializer, QuestionSerializer, QuestionOptionSerializer,LessonDetailSerializer,
    ExamSerializer, ExamQuestionSerializer, StudentSerializer, AnswerSerializer,
    FeedbackSerializer
)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class Register(APIView):

    def post(self, request, format=None):
        """
        Register a new user
        """
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors,status=status.HTTP_201_CREATED)



# class ContentCreatorListCreateView(generics.ListCreateAPIView):
#     serializer_class = ContentCreatorSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return ContentCreator.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class ContentCreatorDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ContentCreatorSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return ContentCreator.objects.filter(user=self.request.user)

# class InstructorListCreateView(generics.ListCreateAPIView):
#     serializer_class = InstructorSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Instructor.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class InstructorDetailView(generics.RetrieveAPIView):
#     serializer_class = InstructorSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Instructor.objects.filter(user=self.request.user)

class CourseListView(generics.ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Course.objects.all()

class CourseDetailView(generics.RetrieveAPIView):
#     serializer_class = CourseDetailSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Course.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        lessons = Lesson.objects.filter(course_id=course)
        
        paginator = LessonPagination()
        paginated_lessons = paginator.paginate_queryset(lessons, request)
        lesson_serializer = LessonListSerializer(paginated_lessons, many=True)
        
        course_serializer = CourseDetailSerializer(course)
        response_data = course_serializer.data
        response_data['lessons'] = paginator.get_paginated_response(lesson_serializer.data).data
        
        return Response(response_data)



class LessonDetailView(generics.RetrieveAPIView):
    serializer_class = LessonDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Lesson.objects.all()


    def get_serializer_context(self):
        context = super().get_serializer_context()
        student = get_object_or_404(Student, user=self.request.user)
        context['student'] = student
        return context

# class QuestionListCreateView(generics.ListCreateAPIView):
#     serializer_class = QuestionSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Question.objects.filter(content_creator_id__user=self.request.user)

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Question.objects.filter(content_creator_id__user=self.request.user)

# class QuestionOptionListCreateView(generics.ListCreateAPIView):
#     serializer_class = QuestionOptionSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return QuestionOption.objects.filter(question_id__content_creator_id__user=self.request.user)

class QuestionOptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionOptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return QuestionOption.objects.filter(question_id__content_creator_id__user=self.request.user)

class ExamListCreateView(generics.ListCreateAPIView):
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Exam.objects.filter(course_id__instructor_id__user=self.request.user)

class ExamDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Exam.objects.filter(course_id__instructor_id__user=self.request.user)

# class ExamQuestionListCreateView(generics.ListCreateAPIView):
#     serializer_class = ExamQuestionSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return ExamQuestion.objects.filter(exam_id__course_id__instructor_id__user=self.request.user)

# class ExamQuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ExamQuestionSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return ExamQuestion.objects.filter(exam_id__course_id__instructor_id__user=self.request.user)

# class StudentListCreateView(generics.ListCreateAPIView):
#     serializer_class = StudentSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Student.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = StudentSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Student.objects.filter(user=self.request.user)

class AnswerListCreateView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Answer.objects.filter(student_id__user=self.request.user)

class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Answer.objects.filter(student_id__user=self.request.user)

# class FeedbackListCreateView(generics.ListCreateAPIView):
#     serializer_class = FeedbackSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Feedback.objects.filter(content_creator_id__user=self.request.user)

# class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = FeedbackSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Feedback.objects.filter(content_creator_id__user=self.request.user)