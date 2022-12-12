import pyodbc
server = 'sql-estudo.database.windows.net'

driver = '{ODBC Driver 17 for SQL Server}'

database = 'db-estudos'

username = 'thayane.bitencourt@blueshift.com.br'

Authentication='ActiveDirectoryInteractive'

port = '1433'

conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)#+';PWD='+password)

cursor = conn.cursor()