from rest_framework import serializers
from django.utils import timezone

from live.models import FuzzingRun


class FuzzingRunSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    start_time = serializers.DateTimeField(required=False, default=timezone.now)
    lastupdate_time = serializers.DateTimeField(required=False, default=timezone.now)

    iterations_per_sec = serializers.IntegerField(required=False)
    iterations_overall = serializers.IntegerField(required=False)

    crash_count = serializers.IntegerField(required=False)
    latest_crash = serializers.DateTimeField(required=False, default=timezone.now)

    path_count = serializers.IntegerField(required=False)
    latest_path = serializers.DateTimeField(required=False, default=timezone.now)

    title = serializers.CharField(required=False, max_length=200)
    text = serializers.CharField(required=False)


    def create(self, validated_data):
        """
        Create and return a new `FuzzingRun` instance, given the validated data.
        """
        return FuzzingRun.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `FuzzingRun` instance, given the validated data.
        """
        instance.lastupdate_time = validated_data.get('lastupdate_time', instance.lastupdate_time)

        instance.iterations_per_sec = validated_data.get('iterations_per_sec', instance.iterations_per_sec)
        instance.iterations_overall = validated_data.get('iterations_overall', instance.iterations_overall)

        instance.crash_count = validated_data.get('crash_count', instance.crash_count)
        instance.latest_crash = validated_data.get('latest_crash', instance.latest_crash)

        instance.path_count = validated_data.get('path_count', instance.path_count)
        instance.latest_path = validated_data.get('latest_path', instance.latest_path)

        instance.save()
        return instance
