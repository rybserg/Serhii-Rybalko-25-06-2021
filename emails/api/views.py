from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from emails.api.permissions import IsSenderOrReadOnly
from emails.api.serializers import EmailSerializer, PersonalEmailSerializer, PersonalEmailMarkSerializer
from emails.models import Email


class EmailCreateAPIView(generics.CreateAPIView):
    serializer_class = EmailSerializer


class EmailDestroyAPIView(generics.DestroyAPIView):
    queryset = Email.objects.all()


class PersonalEmailViewSet(viewsets.ModelViewSet):

    queryset = Email.objects.all().order_by("-created_at")
    serializer_class = PersonalEmailSerializer
    permission_classes = [IsAuthenticated, IsSenderOrReadOnly]

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))

        if self.request.query_params.get('spam'):
            queryset = queryset.filter(is_spam=True)
        if self.request.query_params.get('read'):
            queryset = queryset.filter(is_read=True)
        if self.request.query_params.get('sent'):
            queryset = queryset.filter(sender=self.request.user)
        if self.request.query_params.get('received'):
            queryset = queryset.filter(receiver=self.request.user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class PersonalEmailMarkAPIView(APIView):

    serializer_class = PersonalEmailMarkSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        email = get_object_or_404(Email, pk=pk, receiver=self.request.user)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if "is_spam" in request.data:
                email.is_spam = request.data.get("is_spam")
            if "is_read" in request.data:
                email.is_read = request.data.get("is_read")
            email.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


