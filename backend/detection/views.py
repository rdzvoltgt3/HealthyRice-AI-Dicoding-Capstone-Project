from django.core.exceptions import ValidationError
from django.core.validators import get_available_image_extensions
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from diseases.models import Disease
from .ml_engine import run_inference
from .models import Detection
from .serializers import (
    DetectionCreateSerializer,
    DetectionHistorySerializer,
    DetectionResultSerializer,
)

MAX_UPLOAD_SIZE_MB = 10


def validate_uploaded_image(file_obj):

    ext = file_obj.name.rsplit(
        ".", 1)[-1].lower() if "." in file_obj.name else ""
    if ext not in get_available_image_extensions():
        raise ValidationError(f"Unsupported file type: .{ext}")
    if file_obj.size > MAX_UPLOAD_SIZE_MB * 1024 * 1024:
        raise ValidationError(f"File too large. Max {MAX_UPLOAD_SIZE_MB}MB.")


class DetectionViewSet(viewsets.ModelViewSet):
    """
    POST   /api/detections/          -> upload photo, run inference, save+return result
    GET    /api/detections/          -> Riwayat Deteksi (history), supports ?disease=<slug>
    GET    /api/detections/<id>/     -> single result (for 'Redirect to Prediction Disease page')
    DELETE /api/detections/<id>/     -> 'Hapus' button
    """
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        qs = Detection.objects.filter(
            user=self.request.user).select_related("predicted_disease")
        disease_slug = self.request.query_params.get("disease")
        if disease_slug:
            qs = qs.filter(predicted_disease__slug=disease_slug)
        return qs

    def get_serializer_class(self):
        if self.action == "create":
            return DetectionCreateSerializer
        if self.action == "list":
            return DetectionHistorySerializer
        return DetectionResultSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_file = serializer.validated_data["image"]

        try:
            validate_uploaded_image(image_file)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


        result = run_inference(image_file)
        image_file.seek(0)  

        if result["is_uncertain"]:
          
            return Response(
                {
                    "is_uncertain": True,
                    "reason": result.get("reason"),
                    "confidence": result["confidence"],
                    "message": result["message"],
                },
                status=status.HTTP_200_OK,
            )

        try:
            disease = Disease.objects.get(slug=result["label"])
        except Disease.DoesNotExist:
            return Response(
                {"error": f"Model returned unknown label '{result['label']}'. Seed the diseases table first."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

      
        detection = serializer.save(
            user=request.user,
            predicted_disease=disease,
            confidence=result["confidence"],
            inference_time_ms=result["inference_time_ms"],
        )

        return Response(DetectionResultSerializer(detection, context={"request": request}).data, status=201)
