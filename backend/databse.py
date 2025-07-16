import pyodbc as p

def connect_db():
    try:
        connection = p.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};' +
        'SERVER=LAPTOP-9QRP48GA;' +
        'DATABASE=registros;' +
        'Trusted_Connection=yes;' 
        )

        #'DRIVER={ODBC Driver 17 for SQL Server};'+
        #'SERVER=LAPTOP-9QRP48GA;'+
        #'DATABASE=registros;'+
        #                             'Trusted_Connection=yes;'

        print("Connecting to the database...")
        return connection

    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    

connect_db()