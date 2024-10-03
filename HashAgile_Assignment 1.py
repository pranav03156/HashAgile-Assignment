import pandas as pd
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(
    ["http://localhost:9200"],  
    http_auth=('elastic', 'password'),  
    scheme="http",
    port=9200,
)

index_name = "employee_data"
mapping = {
    "mappings": {
        "properties": {
            "Name": {"type": "text"},
            "Age": {"type": "integer"},
            "Department": {"type": "text"},
            "Salary": {"type": "float"},
            "Country": {"type": "text"}
        }
    }
}

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=mapping)
    print(f"Index '{index_name}' created successfully.")
else:
    print(f"Index '{index_name}' already exists.")

file_path = 'kaggle_emp_data.csv'
df = pd.read_csv(file_path)

def generate_actions(dataframe):
    for _, row in dataframe.iterrows():
        yield {
            "_index": index_name,
            "_source": {
                "Name": row["Name"],
                "Age": row["Age"],
                "Department": row["Department"],
                "Salary": row["Salary"],
                "Country": row["Country"]
            }
        }


helpers.bulk(es, generate_actions(df))
print("Data indexed successfully.")

