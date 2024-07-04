from rest_framework.pagination import PageNumberPagination

class LessonPagination(PageNumberPagination):
    page_size = 10  # Number of lessons per page
    page_size_query_param = 'page_size'
    max_page_size = 100