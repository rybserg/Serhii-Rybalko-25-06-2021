from rest_framework import serializers
from emails.models import Email
from users.api.serializers import UserDisplaySerializer


class EmailSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Email
        exclude = ["is_read", "is_spam", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y %H:%M")


class EmailDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    sender = UserDisplaySerializer(read_only=True)
    receiver = UserDisplaySerializer(read_only=True)

    class Meta:
        model = Email
        exclude = ["is_read", "is_spam", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y %H:%M")


class PersonalEmailSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Email
        exclude = ["updated_at"]
        read_only_fields = ('is_read', 'is_spam')

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def validate_receiver(self, value):
        if self.context['request'].user.id == int(self.context['request'].data.get("receiver")):
            raise serializers.ValidationError("The recipient must not be the same as the sender")
        return value


class PersonalEmailMarkSerializer(serializers.ModelSerializer):

    is_read = serializers.BooleanField(required=False)
    is_spam = serializers.BooleanField(required=False)

    class Meta:
        model = Email
        fields = ('is_read', 'is_spam')

    def validate(self, data):
        if "is_read" not in data and "is_spam" not in data:
            raise serializers.ValidationError("Fields is_read or is_spam are required.")
        return data





