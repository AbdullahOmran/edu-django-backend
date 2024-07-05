from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from ..models import (
    User,ContentCreator, Instructor, Course, Lesson, Question,
    QuestionOption, Exam, ExamQuestion, Student, Answer, Feedback,LessonNotes
)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name    
        token['last_name'] = user.last_name    
        # ...

        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password','phone_number', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'created_at']

class LessonNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonNotes
        fields = '__all__'
class LessonDetailSerializer(serializers.ModelSerializer):
    note = LessonNotesSerializer(source="lesson_notes", many=True)
    class Meta:
        model = Lesson
        fields = '__all__'
        
class ContentCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCreator
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['instructor_name', 'photo']

class CourseListSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(source='instructor_id', read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'instructor', 'course_name', 'description','created_at']

class CourseDetailSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(source='instructor_id', read_only=True)
    lessons = LessonListSerializer(source='lesson_set', many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'instructor', 'course_name', 'description','created_at','lessons']



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class ExamQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamQuestion
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
