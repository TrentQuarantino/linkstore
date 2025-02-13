from asyncio_simple_http_server import *
import asyncio
import json

# the fake db 'the database'
from_ext = "extension.json"
# ===========================================================
# Function to read the data from 'the database'
def read_database(thefile):# = database_json):
    with open(thefile) as database:
        data = json.load(database)
        return data
# ===========================================================
# Function to write the data to 'the database'
def write_database(data_to_write, thefile):
    with open(thefile, "w") as database:
        json.dump(data_to_write, database)

# ===========================================================
class DbHandler:
    @uri_pattern_mapping('/(.*)', method='OPTIONS')
    def test_options(self):
        pass
    
# ===========================================================  
# Get data from Chrome  
    @uri_mapping('/from_chrome', method='POST')
    def from_chrome(self, body):
        #print(body)
        #from_ext = body
        write_database(body, from_ext)
        #print(data)
        #print('dal browser',from_ext)
        data = read_database(from_ext)
        print(data)
# ============================================================
# Send data to the App Linkstore
    @uri_mapping('/to_app', method='GET')
    def to_app(self):
       data = read_database(from_ext)
       #print(data)      
       return data
# ============================================================   
async def main():
    # Create an instance of the HTTP Server
    http_server = HttpServer()

    # Register one or more handlers
    http_server.add_handler(DbHandler())

    # Enable CORS
    http_server.add_default_response_headers({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*'
    })

    # Start the server and serve/wait forever
    await http_server.start('localhost', 8888) # or '127.0.0.1'
    print(f'Serving on {http_server.bind_address_description()}')
    await http_server.serve_forever()

if __name__== '__main__':
    asyncio.run(main())

