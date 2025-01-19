#before running need to do the below in terminal

#gcloud init
#gcloud auth application-default login
from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()

query = "select * from `data-analytics1-437123.avocado_data.avocado_prices`; "
#print(query)
df = client.query(query).to_dataframe()

print(df)
