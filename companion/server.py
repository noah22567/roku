import socket
from companion.packages.utils import gen_response, handle_command

server_address = ('localhost', 8350)


def serve(server_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(1)
    print("listening for requests")
    while True:
        connection, client_address = sock.accept()
        print("{} has connected".format(client_address))
        print('waiting for request')
        try:
            while True:
                data = connection.recv(1024)
                if len(data) > 10:
                    print("Received request: {}".format(data.decode('utf-8')))
                    connection.sendall(b'{"status":200,"message":"Successfully received request."}')
                    print("Sent Success message to client {}".format(client_address))
                    command = handle_command(data,client_address)
                    print("Command successfully executed ")# takes data from client returns endpoints for command
                    if command == SyntaxError.__name__:
                        print("Could not process request due to SyntaxError")
                        connection.sendall(b'{"status":422,"message":"Invalid syntax."}')
                    elif command == "InternalError":#will add threading with timer for timed out and a try clause for timedout
                        print("Could not process request due to InternalError")
                        connection.sendall(b'{"status":500,"message":"Internal Error."}')
                    elif command == "ValueError":  # will add threading with timer for timed out and a try clause for timedout
                        print("ValueError Could not find that command.")
                        connection.sendall(b'{"status":500,"message":"Value Error."}')
                    elif command == "ValueError":  # will add threading with timer for timed out and a try clause for timedout
                        print("ValueError Could not find the device.")
                        connection.sendall(b'{"status":422,"message":"Value Error."}')
                    elif command:
                        print("Can handle request generating response")
                        print("Inserting command into response")
                        print("command: ", command)
                        command_request = gen_response(command)
                        print("Response Generated")
                        print(command_request)
                        connection.sendall(command_request)
                        print("Sending command")

                    else:
                        print("Unknown Error")
                        connection.sendall(b'{"status":500,"message":"Internal Error."}')
                else:
                    continue

        except:
            print("Reestablishing..")
            continue
if __name__=="__main__":
    serve(server_address)