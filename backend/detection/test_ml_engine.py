from django.test import TestCase

from diseases.models import Disease
from .ml_engine import _CLASSES, _REJECT_LABELS, _normalize_label


class LabelNormalizationTests(TestCase):

    def test_brown_spot_normalizes_to_hyphenated_slug(self):
        self.assertEqual(_normalize_label("brown_spot"), "brown-spot")

    def test_single_word_labels_are_unchanged(self):
        for label in ["blast", "blight", "healthy", "scald", "tungro"]:
            self.assertEqual(_normalize_label(label), label)

    def test_every_model_class_matches_a_seeded_disease(self):
        Disease.objects.bulk_create([
            Disease(slug="blast", name="Blast"),
            Disease(slug="blight", name="Blight"),
            Disease(slug="brown-spot", name="Brown Spot"),
            Disease(slug="healthy", name="Healthy"),
            Disease(slug="scald", name="Scald"),
            Disease(slug="tungro", name="Tungro"),
        ])
        db_slugs = set(Disease.objects.values_list("slug", flat=True))

        for raw_label in _CLASSES:
            if raw_label in _REJECT_LABELS:
                continue  
            normalized = _normalize_label(raw_label)
            self.assertIn(
                normalized, db_slugs,
                f"Model label '{raw_label}' (normalized: '{normalized}') has no matching Disease — "
                f"this is exactly the bug that broke brown_spot. Run `python manage.py check_labels`.",
            )

    def test_reject_labels_are_not_required_to_have_a_disease(self):

        if "not_rice" in _CLASSES:
            self.assertIn("not_rice", _REJECT_LABELS)
