from rest_framework import serializers
from .models import Disease


class DiseaseSerializer(serializers.ModelSerializer):

    symptoms = serializers.SerializerMethodField()
    treatment = serializers.SerializerMethodField()
    prevention = serializers.SerializerMethodField()

    class Meta:
        model = Disease
        fields = [
            "id", "slug", "name", "scientific_name",
            "short_description", "description", "cause",
            "symptoms", "details", "treatment", "prevention",
            "sources", "risk_level", "image",
        ]

    def get_symptoms(self, obj):
        return obj.steps_as_list("symptoms")

    def get_treatment(self, obj):
        return obj.steps_as_list("treatment_steps")

    def get_prevention(self, obj):
        return obj.steps_as_list("prevention_steps")


class DiseaseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disease
        fields = ["id", "slug", "name", "description", "short_description", "risk_level", "image"]
