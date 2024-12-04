from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
# Connection details
PUBLIC_IP = "18.132.73.146"
USERNAME = "consultants"
PASSWORD = "WelcomeItc@2022"
DB_NAME = "testdb"
PORT = "5432"
ENCODED_PASSWORD = quote_plus(PASSWORD)

database_url = f"postgresql://{USERNAME}:{ENCODED_PASSWORD}@{PUBLIC_IP}:{PORT}/{DB_NAME}"

#Create an engine
engine=create_engine(database_url)
#Read data from Mysql
import pandas as pd
#df= pd.read_sql("accounts1",con=engine)
#print(df)
db1=pd.read_csv("C:\\Users\\adurg\\Downloads\\people_data.csv")
db1.to_sql('addresses', con=engine, if_exists="replace", index=False)