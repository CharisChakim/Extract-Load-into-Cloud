#load then extract data from .json in GCS --> load data to bigquery
import json
import os
from google.cloud import storage, bigquery

# Menyiapkan informasi koneksi GCS dan BigQuery
gcs_bucket_name = os.getenv('BUCKET_NAME')
gcs_blob_name = 'try_task1.json'
bigquery_project_id = os.getenv('PROJECT_ID')
bigquery_dataset_id = 'try_dataset'
bigquery_table_id = 'try_table'

# Fungsi untuk memuat data ke GCS
def load_to_gcs(data, bucket_name, blob_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(json.dumps(data), content_type='application/json')

# Fungsi untuk mengekstrak data dari GCS
def extract_from_gcs(bucket_name, blob_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    data = json.loads(blob.download_as_text())
    return data

# Fungsi untuk memuat data ke BigQuery
def load_to_bigquery(data, project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    table = client.get_table(table_ref)

    rows_to_insert = [(item['id'],item['nama'], item['gender'],item['created_at']) for item in data]

    errors = client.insert_rows(table, rows_to_insert)

    if errors:
        print(f'Errors occurred: {errors}')
    else:
        print('Data successfully loaded to BigQuery.')

# Contoh data
sample_data = [
    {'id': 1,'nama': 'naruto','gender' : 'male','created_at' : '2023-11-10 08:00:00'},
    {'id': 2,'nama': 'zoro','gender' : 'male','created_at' : '2023-11-10 08:00:00'},
    {'id': 3,'nama': 'sakura','gender' : 'female','created_at' : '2023-11-10 08:00:00'},
    {'id': 4,'nama': 'cibi','gender' : 'female','created_at' : '2023-11-10 08:00:00'},
    {'id': 5,'nama': 'sasuke','gender' : 'male','created_at' : '2023-11-10 08:00:00'} 
]

# Memuat data ke GCS
load_to_gcs(sample_data, gcs_bucket_name, gcs_blob_name)
print("Upload to GCS . . .")

# Mengekstrak data dari GCS
extracted_data = extract_from_gcs(gcs_bucket_name, gcs_blob_name)
print("Exctracting data . . .")

# Memuat data yang diekstrak ke BigQuery
load_to_bigquery(extracted_data, bigquery_project_id, bigquery_dataset_id, bigquery_table_id)
