import numpy as np
from .models import Alternatif, Kriteria, Nilai


def hitung_wp():
    alternatif_qs = Alternatif.objects.all()
    kriteria_qs = Kriteria.objects.all()
    total_bobot = sum(k.bobot for k in kriteria_qs)

    kriteria_data = []
    for k in kriteria_qs:
        wj = k.bobot / total_bobot
        kriteria_data.append(
            {
                "id": k.id,
                "sifat": k.sifat,
                "bobot": wj,
            }
        )

    hasil = []

    for alt in alternatif_qs:
        nilai_qs = Nilai.objects.filter(alternatif=alt)
        S = 1
        for k in kriteria_data:
            nilai = nilai_qs.get(kriteria_id=k["id"]).nilai
            if k["sifat"] == "cost":
                nilai = 1 / nilai
            S *= pow(nilai, k["bobot"])
        hasil.append({"nama": alt.nama, "S": S})

    total_S = sum(h["S"] for h in hasil)
    for h in hasil:
        h["V"] = h["S"] / total_S

    hasil.sort(key=lambda x: x["V"], reverse=True)
    return hasil
