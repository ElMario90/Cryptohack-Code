from pwn import remote
import json
from Crypto.Util.number import long_to_bytes
import base64
import codecs

def receive_json(conn):
    data_line = conn.recvline()
    return json.loads(data_line.decode())

def send_json(conn, payload):
    encoded_payload = json.dumps(payload).encode()
    conn.sendline(encoded_payload)

def decode_payload(encoding_type, data):
    if encoding_type == "base64":
        return base64.b64decode(data).decode('utf-8')
    elif encoding_type == "hex":
        return bytes.fromhex(data).decode('utf-8')
    elif encoding_type == "rot13":
        return codecs.decode(data, 'rot_13')
    elif encoding_type == "bigint":
        return long_to_bytes(int(data, 16)).decode('utf-8')
    elif encoding_type == "utf-8":
        return ''.join(chr(c) for c in data)
    else:
        raise ValueError(f"Unknown encoding type: {encoding_type}")

def main():
    server_host = 'socket.cryptohack.org'
    server_port = 13377
    conn = remote(server_host, server_port)

    for _ in range(100):
        message = receive_json(conn)
        encoding_type = message["type"]
        encoded_data = message["encoded"]
        decoded_data = decode_payload(encoding_type, encoded_data)
        response = {"decoded": decoded_data}
        send_json(conn, response)

    final_message = receive_json(conn)
    print(f"Flag: {final_message['flag']}")

if __name__ == "__main__":
    main()
