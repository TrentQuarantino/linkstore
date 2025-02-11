from asyncio_simple_http_server import *
import asyncio
import json
import tempfile
#from stock_map import mapping
from_ext = "extension.json"
# File where you store data 'the database' so to speak
database_json = "test_dyn_local.json"
#stocco = "CRWD"
#database_json2 = f"../json/{stocco}.json"
# Function to read the data from 'the database'
def read_database(thefile):# = database_json):
    with open(thefile) as database:
        data = json.load(database)
        return data
# Function to write the data to 'the database'
def write_database(data_to_write, thefile):
    with open(thefile, "w") as database:
        json.dump(data_to_write, database)

class DbHandler:
    @uri_pattern_mapping('/(.*)', method='OPTIONS')
    def test_options(self):
        pass
    # ============ Read all data from database =======================
    @uri_mapping('/test-get')
    def test_get(self):
       data = read_database()
       return data
    # ============= CREATE a new resource (Insert) ==================== 
    @uri_mapping('/test-post', method='POST')
    def test_post(self, body):
        data = read_database()    
        data.append(body)

        write_database(data)

        print('you insert:', body)
        #return body
    # ============== UPDATE a  resource (Patch) =======================  
    @uri_mapping('/test-update', method='PATCH')
    def test_update(self, body):
        data = read_database()
        for file_stock in data:
            if file_stock['title'] == body['title']:
                file_stock.update(body)

        write_database(data)
        print('updated:',body)
        #return body  
    # =============== DELETE a resource ================================
    @uri_mapping('/test-delete', method='DELETE')
    def test_delete(self, body):
        data = read_database()
        for file_stock in data:
            if file_stock['title'] == body:
                data.remove(file_stock)

        write_database(data)
        print('deleted:',body)
        #return body
    # =============== Request data for charts ===========================
    @uri_mapping('/test-request', method='POST')
    def test_request(self, body):
        #stock = mapping(body)
        #database_json2 = f"../json/{stock}.json"
        #data = read_database(database_json2)
        #return data
        pass
    # =================== prova ============================
    @uri_mapping('/rebugi', method='CULO')
    def rebugi(self):
        return 'rebbu'
    
    @uri_mapping('/rebugi', method='POST')
    def rebugi2(self, body):
        #print(body)
        #from_ext = body
        write_database(body, from_ext)
        #print(data)
        #print('dal browser',from_ext)
        data = read_database(from_ext)
        print(data)
        return 'rebbuDUE'
    @uri_mapping('/rebugi3', method='GET')
    def rebugi3(self):
       data = read_database(from_ext)
       #print(data)
       
       return data
    
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

# https://sureshchandrasekar.substack.com/p/coming-soon