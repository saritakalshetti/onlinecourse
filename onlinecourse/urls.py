from django.urls import path
from . import views

urlpatterns = [
    path(
        "course/<int:course_id>/exam/",
        views.show_exam_result,
        name="show_exam_result"
    ),
    path(
        "course/<int:course_id>/submit/",
        views.submit,
        name="submit"
    ),
]