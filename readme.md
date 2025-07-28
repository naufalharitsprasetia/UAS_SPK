# Project Akhir Mata Kuliah SPK
(Sistem Pendukung Keputuan)
Studi Kasus : "Pemilihan Calon Staff PPTIK Universitas Darussalam Gontor"
oleh : 
- Naufal Harits Prasetia / 432022611051
- Mukhammad Shobikh / 432022611047
  
## Tutorial :    
```bash
python -m venv venv # buat virtual enviroment

venv\Scripts\activate     # Windows
source venv/bin/activate # macOS/Linux:

pip install django pandas numpy # install packages

python manage.py migrate # migrasi tabel-tabel database

python manage.py createsuperuser # perintah untuk membuat Akun untuk masuk ke admin dashboard

python manage.py runserver # jalankan, dan buka di route '/admin'
```

## Route
- {server:host}/admin : untuk input data Alternatif,Kriteria,Nilai
- {server:host}/hasil : untuk melihat hasil keputusan berdasarkan metode WP
