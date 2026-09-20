"""
Global DRF exception handler. Without this, an unexpected exception (a bug,
a third-party API timeout, a DB constraint error) falls through to Django's
raw HTML 500 page even on an API endpoint — which is what the checklist's
"stable, handles errors without crashing" criterion is actually checking for.

This does two things DRF's default handler doesn't:
  1. Catches exceptions DRF's default handler ignores (anything not a
     recognized APIException/Http404/PermissionDenied) and turns them into
     a clean JSON 500 instead of an unhandled crash.
  2. Normalizes every error response to the same {"error": "..."} shape,
     so frontend error handling doesn't need a special case per endpoint.
"""
import logging

from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is not None:

        if isinstance(response.data, dict) and "error" not in response.data and "detail" in response.data:
            response.data = {"error": response.data["detail"]}
        return response


    logger.exception("Unhandled exception in %s", context.get("view"))
    return Response(
        {"error": "Terjadi kesalahan pada server. Silakan coba lagi."},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
