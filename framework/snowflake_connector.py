import snowflake.connector
import pandas as pd
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

SNOWFLAKE_CONN_PARAMS = config["snowflake"]

class SnowflakeConnector:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = snowflake.connector.connect(
            user=SNOWFLAKE_CONN_PARAMS["user"],
            password=SNOWFLAKE_CONN_PARAMS["password"],
            account=SNOWFLAKE_CONN_PARAMS["account"],
            warehouse=SNOWFLAKE_CONN_PARAMS["warehouse"],
            database=SNOWFLAKE_CONN_PARAMS["database"],
            schema=SNOWFLAKE_CONN_PARAMS["schema"]
        )

    def fetch_data(self, query):
        if not self.conn:
            self.connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return pd.DataFrame(data, columns=columns)
        finally:
            cursor.close()

    def close(self):
        if self.conn:
            self.conn.close()
