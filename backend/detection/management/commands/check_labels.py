from django.core.management.base import BaseCommand

from diseases.models import Disease
from detection.ml_engine import _CLASSES, _REJECT_LABELS, _normalize_label


class Command(BaseCommand):
    """
    Run this after swapping in a new model or labels.json — catches label/
    slug mismatches (like brown_spot vs brown-spot) before they show up as
    a live 500 for a real user.

    Classes listed in labels.json's "reject_labels" (e.g. "not_rice") are
    intentionally excluded from the Disease check — they're not diagnoses,
    the view discards them before any DB lookup happens.

        python manage.py check_labels
    """
    help = "Verify every non-reject class in labels.json maps to an existing Disease.slug."

    def handle(self, *args, **options):
        db_slugs = set(Disease.objects.values_list("slug", flat=True))
        problems = []
        reject_count = 0

        for raw_label in _CLASSES:
            if raw_label in _REJECT_LABELS:
                reject_count += 1
                continue
            normalized = _normalize_label(raw_label)
            if normalized not in db_slugs:
                problems.append((raw_label, normalized))

        checked = len(_CLASSES) - reject_count

        if not problems:
            self.stdout.write(self.style.SUCCESS(
                f"All {checked} disease label(s) map to a seeded Disease. OK."
            ))
            if reject_count:
                self.stdout.write(f"({reject_count} reject label(s) skipped: {sorted(_REJECT_LABELS)})")
            return

        self.stdout.write(self.style.ERROR(f"{len(problems)} label(s) do not match any Disease.slug:"))
        for raw_label, normalized in problems:
            self.stdout.write(f"  model label '{raw_label}' -> normalized '{normalized}' -> NOT FOUND in DB")
        self.stdout.write(self.style.WARNING(
            "Fix by either seeding a Disease with that slug, or adjusting "
            "_normalize_label() in detection/ml_engine.py."
        ))
