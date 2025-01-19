#before running need to do the below in terminal

#gcloud init
#gcloud auth application-default login
from google.cloud import bigquery
import pandas as pd
import pandas_gbq as pd_gbq

client = bigquery.Client()
project_id = 'data-analytics1-437123'

fin = open('avocado_query.sql')
query_in = fin.read()
pd_gbq.read_gbq(query_in, project_id)
#print(query)
#df = client.query(query).to_dataframe()

#print(df)
