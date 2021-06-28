from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer
from emails.api.serializers import EmailDetailSerializer
from users.models import CustomUser
from emails.models import Email
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.generics import get_object_or_404


class UserEmailListAPIView(generics.ListAPIView):
    serializer_class = EmailDetailSerializer

    def get_queryset(self):
        get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        queryset = Email.objects.filter(Q(sender__pk=self.kwargs['pk']) | Q(receiver__pk=self.kwargs['pk']))

        sent = self.request.query_params.get('sent')
        if sent is not None:
            queryset = queryset.filter(sender__pk=self.kwargs['pk'])

        received = self.request.query_params.get('received')
        if received is not None:
            queryset = queryset.filter(receiver__pk=self.kwargs['pk'])

        return queryset.order_by("id")


class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserDisplaySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        search = self.request.query_params.get('search')
        if search is not None and len(search):
            queryset = queryset.filter(username__startswith=search)
        return queryset
