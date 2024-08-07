from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.shortcuts import get_object_or_404


class UserManager(BaseUserManager):

    def create_user(self, email, phone_number, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        if not phone_number:
            raise ValueError(_("The phone number must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email,phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, phone_number, password, **extra_fields)


class User(AbstractUser):
    """
    Custom user model that supports using email instead of username
    """
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
        ('content_creator', 'Content Creator'),
        ('parent', 'Parent/Guardian'),
    ]
    id = models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(verbose_name=_("phone number"),max_length=20,unique= True, help_text='Enter phone number')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    role_assigned_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.email
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notes = models.ManyToManyField('Lesson',through='LessonNotes')
    
    def __str__(self):
        return self.user.email
    
class ContentCreator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class Instructor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    instructor_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    photo = models.ImageField(upload_to='instructors/photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.instructor_name

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        instructor = get_object_or_404(Instructor, instructor_name=self.instructor_id)
        return f'{self.course_name} By {instructor.instructor_name}'

class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    data = models.TextField()
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to='lessons/photos/', null=True, blank=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title
    
class LessonNotes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson= models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_notes")
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural  = 'lesson notes'
    
    def __str__(self):
        return f'Note by {self.student} on {self.lesson}'

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=50)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    content_creator_id = models.ForeignKey(ContentCreator, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class QuestionOption(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)

class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam_date = models.DateField()
    exam_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class ExamQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)



class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    answer = models.CharField(max_length=100, null=True)

class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content_creator_id = models.ForeignKey(ContentCreator, on_delete=models.SET_NULL, null=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    difficulty_level = models.CharField(max_length=50)

class RandomExamManager(models.Manager):
    def create_random_exam(self,exam_type, course_id, num_questions=10):
        # Create a new exam
        exam = self.create(
            exam_date=timezone.now(),
            exam_type=exam_type,
            created_at=timezone.now()
        )

        # Get random questions for the course
        questions = Question.objects.order_by('?')[:num_questions]

        # Add questions to the exam
        for question in questions:
            ExamQuestion.objects.create(
                exam_id=exam,
                question_id=question
            )

        return exam

class RandomExam(Exam):
    objects = RandomExamManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created and instance.role == 'student':
        Student.objects.create(user=instance)
