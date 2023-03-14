#CONFIGUTACIÓN

from config import Config as conf

__all__ =['Tb', 'Config']

# OPEN 
#establish database connection

class Config(object):
    driver='ODBC Driver 17 for SQL Server'
    username='',
    password='',
    server='SURUBI037'
    database='CAPEX'
    Trusted_Connection='yes'
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"

