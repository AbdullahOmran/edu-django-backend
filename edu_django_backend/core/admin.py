from django.contrib import admin
from .models import User
from .models import (
    ContentCreator, Instructor, Course, Lesson, Question,
    QuestionOption, Exam, ExamQuestion, Student, Answer, Feedback,LessonNotes
)




admin.site.register(User)
# Register your models here.
@admin.register(ContentCreator)
class ContentCreatorAdmin(admin.ModelAdmin):
    pass

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    pass

@admin.register(LessonNotes)
class LessonNotesAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass

@admin.register(ExamQuestion)
class ExamQuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass