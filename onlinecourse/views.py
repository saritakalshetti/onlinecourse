from django.shortcuts import render, get_object_or_404
from .models import Course, Question, Choice, Submission


def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = course.question_set.all()

    score = 0
    results = []

    if request.method == "POST":
        for question in questions:
            selected_choice_id = request.POST.get(
                f"question_{question.id}"
            )

            selected_choice = None

            if selected_choice_id:
                selected_choice = get_object_or_404(
                    Choice,
                    id=selected_choice_id,
                    question=question
                )

                if selected_choice.is_correct:
                    score += 1

                Submission.objects.create(
                    question=question,
                    choice=selected_choice
                )

            results.append({
                "question": question,
                "selected_choice": selected_choice,
                "correct_choice": question.choice_set.filter(
                    is_correct=True
                ).first(),
            })

    return render(
        request,
        "course/exam_result.html",
        {
            "course": course,
            "score": score,
            "total": questions.count(),
            "results": results,
        }
    )


def show_exam_result(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = course.question_set.all()

    return render(
        request,
        "course/exam.html",
        {
            "course": course,
            "questions": questions,
        }
    )