import socket
import select
import json

with open('server_config.json') as server_config:
    config = json.load(server_config)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((config.get('IP'), config.get('PORT')))

server_socket.listen()

sockets_list = [server_socket]
clients = {}
msg_counter = 0


def receive_message(client_sock):
    try:
        message_header = client_sock.recv(config.get('HEADER_LENGTH'))

        if not len(message_header):
            return False

        message_len = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_sock.recv(message_len)}

    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user

            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} "
                  f"username: {user['data'].decode('utf-8')}")

        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f'Close connection from {clients[notified_socket]["data"].decode("utf-8")}')
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]

            print(f'Received [{msg_counter}] message from {user["data"].decode("utf-8")}: '
                  f'{message["data"].decode("utf-8")}')

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]

    msg_counter += 1
