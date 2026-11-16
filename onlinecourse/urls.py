from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # ex: /onlinecourse/5/
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    # ex: /enroll/5/
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Route for submit view
    path('<int:course_id>/submit/', views.submit, name="submit"),

    # Route for show_exam_result view
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name="exam_result"),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```[cite: 1]

---

### Next Steps to Finalize and Push to GitHub:
1. Replace the code inside your `onlinecourse/urls.py` file with the code above and save it[cite: 1].
2. Open your terminal and push all your completed code files (`models.py`, `admin.py`, `views.py`, and `urls.py`) to GitHub[cite: 1]:
   ```bash
   git add .
   git commit -m "Add submit and exam_result URL paths"
   git push origin main
   ```[cite: 1]
   *(When prompted for your password, paste your GitHub Personal Access Token).*

Once pushed, all your GitHub URL submissions (Tasks 1, 2, 4, 5, and 6) and screenshots (Tasks 3 and 7) will be fully in place for a passing grade!