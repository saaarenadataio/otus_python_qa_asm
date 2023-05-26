"""
    Homework echo-server
"""

import socket
import http
import re

# vars
HOST = 'localhost'
PORT = 8099
end_of_stream = '\r\n\r\n'
http_response_hdr = (
    f"HTTP/1.1 200 OK\r\n"
    f"Server: python_daemon\r\n"
    f"Date: Wed, 26 Dec 1979 19:24:00 MSK\r\n"
    f"Content-Type: text/plain\r\n"
)

def http_response(data, address):
    res_status = '200 OK'
    if '?status=' in data:
        status = str(re.search(r'(?<=/\?status=)[^.\s]*', data).group(0))
        if status:
            for sts in http.HTTPStatus:
                if str(sts.value) == status:
                    res_status = status + ' ' + sts.phrase
                    break
    response = data.split('\r\n')
    request_method = response[0].split()[0]
#    print(f'met {request_method}', f'st {res_status}', f'dt {data}', f'ad {address}')
    response = [http_response_hdr, f'Request method: {request_method}', f'Request source: {str(address)}', f'Response status: {res_status}'] + response[2:-2]
    print(f"res {response}")
    return response

def handle_client(connection, address):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            print(f'Received: {data}')
            if not data:
                break
            client_data += data.decode()
            if end_of_stream in client_data:
                break
        #send response to client
        connection.send(('\r\n'.join(http_response(client_data, address))).encode() + f'\r\n'.encode())

def server_process():
    with socket.socket() as ss:
        ss.bind((HOST, PORT))
        print(f'Running server on {HOST}:{PORT}...')
        ss.listen()

        while True:
            (client_connection, client_address) = ss.accept()
            handle_client(client_connection, client_address)
            print(f'Sent data to {client_address}')

if __name__ == '__main__':
    server_process()
