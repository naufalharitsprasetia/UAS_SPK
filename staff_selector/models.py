from django.db import models


class Alternatif(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Kriteria(models.Model):
    SIFAT_CHOICES = [
        ("benefit", "Benefit"),
        ("cost", "Cost"),
    ]
    nama = models.CharField(max_length=100)
    bobot = models.FloatField()
    sifat = models.CharField(max_length=10, choices=SIFAT_CHOICES)

    def __str__(self):
        return self.nama


class Nilai(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE)
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE)
    nilai = models.FloatField()

    class Meta:
        unique_together = ("alternatif", "kriteria")
