import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
driver = '{ODBC Driver 17 for SQL Server}'
server = 'background-server.database.windows.net' 
database = 'background' 
username = 'azureuser' 
password = 'User1234'
encrypt = 'yes'
trust_server_certificate = 'no'
connection_timeout = '30'

connection_string = 'Driver={};Server={};Database={};Uid={};Pwd={};Encrypt={};TrustServerCertificate={};Connection Timeout={};'.format(
    driver, server, database, username, password, encrypt, trust_server_certificate, connection_timeout
)

search_query = 'SELECT * FROM FEATURE'

cnxn = pyodbc.connect(connection_string)
cursor = cnxn.cursor()
#Sample select query
result = cursor.execute(search_query).fetchall()
print(result)
cnxn.close()