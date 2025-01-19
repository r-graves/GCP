#before running need to do the below in terminal
#note that this version currently errors out as I can't carry a temp query

#gcloud init
#gcloud auth application-default login
from google.cloud import bigquery
import pandas as pd
import pandas_gbq as pd_gbq


project_id = 'data-analytics1-437123'
client = bigquery.Client(project=project_id)



fin = open('avocado_query.sql')
query = fin.read()

client.query(query)

#query2 = open('avocado_query_perm.sql')
#query3 = query2.read()
#df = client.query(query3).to_dataframe()

#print(df)



#fin2 = open('avocado_query_perm.sql')
#query_in2 = fin2.read()
#client.query(query_in2)
#pd_gbq.read_gbq(query_in, project_id)
#print(query)
#df = client.query(query).to_dataframe()

#print(df)
