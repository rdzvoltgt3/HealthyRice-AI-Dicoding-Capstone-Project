from django.db import models


class Disease(models.Model):
    class RiskLevel(models.TextChoices):
        NONE = "none", "Tidak ada risiko"
        LOW = "low", "Risiko Rendah"
        MEDIUM = "medium", "Risiko Sedang"
        HIGH = "high", "Risiko Tinggi"

    slug = models.SlugField(unique=True)  
    name = models.CharField(max_length=100)  
    scientific_name = models.CharField(max_length=150, blank=True)
    short_description = models.CharField(max_length=255, blank=True)  
    description = models.TextField(blank=True)  # full "Tentang Penyakit" paragraph(s)
    cause = models.TextField(blank=True)
    symptoms = models.TextField(blank=True) 
    details = models.TextField(blank=True)
    treatment_steps = models.TextField(blank=True)  
    prevention_steps = models.TextField(blank=True) 
    sources = models.JSONField(default=list, blank=True)  # [{"title": ..., "url": ...}, ...]
    risk_level = models.CharField(max_length=10, choices=RiskLevel.choices, default=RiskLevel.MEDIUM)
    image = models.ImageField(upload_to="diseases/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def steps_as_list(self, field_name):
        raw = getattr(self, field_name) or ""
        return [line.strip() for line in raw.splitlines() if line.strip()]
