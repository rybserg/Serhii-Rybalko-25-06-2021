from django.urls import include, path
from rest_framework.routers import DefaultRouter

from emails.api import views as emails_views

router = DefaultRouter()
router.register(r"personal-emails", emails_views.PersonalEmailViewSet)

urlpatterns = [

    path("emails/",
         emails_views.EmailCreateAPIView.as_view(),
         name="email-create"),

    path("emails/<int:pk>/",
         emails_views.EmailDestroyAPIView.as_view(),
         name="email-destroy"),

    path("", include(router.urls)),

    path("personal-emails/<int:pk>/mark/",
         emails_views.PersonalEmailMarkAPIView.as_view(),
         name="personal-email-mark"),

]
