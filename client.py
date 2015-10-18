__author__ = 'Alexander Black'
import socket
import select
import sys


def prompt():
    sys.stdout.write("> ")
    sys.stdout.flush()


class Client(object):
    def __init__(self):
        self.host = sys.argv[1]
        self.port = int(sys.argv[2])
        self.sock = None
        self.connect_to_server()

    def connect_to_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(2)
        # connect to remote host
        try:
            self.sock.connect((self.host, self.port))
        except:
            print 'Unable to connect'
            sys.exit()

        print 'Connected to remote host. Start sending messages'
        prompt()
        self.wait_for_messages()

    def wait_for_messages(self):
        while 1:
            socket_list = [sys.stdin, self.sock]

            # Get the list sockets which are readable
            read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

            for sock in read_sockets:
                # incoming message from remote server
                if sock == self.sock:
                    data = sock.recv(4096)
                    if not data:
                        print '\nDisconnected from chat server'
                        sys.exit()
                    else:
                        # print data
                        sys.stdout.write(data)
                        prompt()

                # user entered a message
                else:
                    msg = sys.stdin.readline()
                    self.sock.send(msg)
                    prompt()


if __name__ == '__main__':
    client = Client()
