import errno
import os
import signal
import socket

SERVER_ADDRESS = (HOST, port_number) = '', 9001
REQUEST_QUEUE_SIZE = 1024


def parse_request(packet):    			#parsing function
    st = "GET"
    if packet.find(st, 0, 3) != -1:    		# if search is true (GET is found)
		return True        		# return true
    else:
        return False        			# else return false
        

def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,
                os.WNOHANG
            )
        except OSError:
            return

        if pid == 0:
            return


def handle_request(client_connection):
    d = client_connection.recv(1024)        	# receive packet, store in variable
    if (parse_request(d) == True):        	# pass variable to be parsed
	with open ('PATH/TO/HTML/FILE', 'r') as myfile:		#REPLACE WITH PATH TO HTML FILE
	    data = myfile.read()            	# opens HTML, copies contents into variable
            client_connection.send('HTTP/1.0 200 OK\n')
            client_connection.send('Content-Type: text/html\n')
            client_connection.send('\n')
            client_connection.send(data)       # sends out HTML variable contents
    else:
        with open ('PATH/TO/ERROR/FILE', 'r') as myfile:	#REPLACE WITH PATH TO ERROR FILE
	    data = myfile.read()
        client_connection.send('HTTP/1.0 404 Not Found\n')
        client_connection.send('Content-Type: text/html\n')
        client_connection.send('\n')
        client_connection.send(data)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=port_number))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:
            listen_socket.close()
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else: 
            client_connection.close()

if __name__ == '__main__':
    serve_forever()
