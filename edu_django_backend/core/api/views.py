from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import generics, permissions
from ..models import (
    ContentCreator, Instructor, Course, Lesson, Question,
    QuestionOption, Exam, ExamQuestion, Student, Answer, Feedback
)
from .serializers import (
    ContentCreatorSerializer, InstructorSerializer, CourseSerializer,
    LessonSerializer, QuestionSerializer, QuestionOptionSerializer,
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
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Course.objects.all()

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Course.objects.filter(instructor_id__user=self.request.user)

# class LessonListCreateView(generics.ListCreateAPIView):
#     serializer_class = LessonSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Lesson.objects.filter(course_id__instructor_id__user=self.request.user)

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Lesson.objects.filter(course_id__instructor_id__user=self.request.user)

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