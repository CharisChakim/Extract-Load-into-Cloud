# TASK 1
task hari ini.
buat script python untuk extract data dari file .json yang ada di GCS --> load data yang sudah di extract ke bigquery

example:

file json di gcs = [
    {"name": "djamier", "age": 20},
    {"name": "elon musk", "age": 30}
]

table di big query =
name            age
djamier         20
elon musk    30

# Ans
Pertama kita buat project dan bucket di GCP sebagai wadah yang akan kita gunakan dalam task ini.

![Alt text](image.png)

![Alt text](image-1.png)

Buat dataset table di bigquery

![Alt text](image-3.png)

Buat tabel sesuai data yang akan kita inputkan

![Alt text](image-4.png)

Buat file .env sesuai nama project dan bucket yang kita buat 

![Alt text](image-2.png)

Login ke akun GCP menggunakan google cloud shell SDK dan pastikan project yang aktif telah sesuai dengan yang akan kita kerjakan

![Alt text](image-5.png)

Jalankan file .env sebelum menjalankan file python

![Alt text](image-6.png)

Jalankan file python task1_charis.py

![Alt text](image-7.png)

Cek data via UI cloud

![Alt text](image-8.png)

![Alt text](image-9.png)

#END





 