from rest_framework import serializers

from diseases.models import Disease
from diseases.serializers import DiseaseListSerializer
from .models import Detection


class DetectionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detection
        fields = ["id", "image"]
        read_only_fields = ["id"]


class DetectionResultSerializer(serializers.ModelSerializer):

    disease = DiseaseListSerializer(source="predicted_disease", read_only=True)

    class Meta:
        model = Detection
        fields = ["id", "image", "disease", "confidence",
                  "inference_time_ms", "created_at"]


class DetectionHistorySerializer(serializers.ModelSerializer):

    disease = DiseaseListSerializer(source="predicted_disease", read_only=True)

    class Meta:
        model = Detection
        fields = ["id", "image", "disease", "confidence", "created_at"]
