#Define C2 server IP and Port in last line of script
import socket
import ssl
import sys
import select

def ssl_netcat(host, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Wrap the socket with SSL
        context = ssl.create_default_context()
        ssl_sock = context.wrap_socket(sock, server_hostname=host)

        # Connect to the host
        ssl_sock.connect((host, port))
        print(f"Connected to {host}:{port} with SSL/TLS")

        # Interactive loop: read from stdin and socket
        while True:
            # Use select to wait for input from either stdin or socket
            read_sockets, _, _ = select.select([sys.stdin, ssl_sock], [], [])

            for s in read_sockets:
                if s == ssl_sock:
                    # Data from remote host
                    data = ssl_sock.recv(4096)
                    if not data:
                        print("\nConnection closed by remote host.")
                        return
                    sys.stdout.write(data.decode(errors='ignore'))
                    sys.stdout.flush()
                else:
                    # Data from user input
                    user_input = sys.stdin.readline()
                    if user_input.strip().lower() == 'exit':
                        print("Closing connection...")
                        ssl_sock.close()
                        return
                    ssl_sock.sendall(user_input.encode())

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ssl_netcat("172.16.42.1", 443)
