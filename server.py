import socket
import json

from data_processing import *

sock = socket.socket()
sock.bind(('127.0.0.1', 9090))

while True:
    sock.listen(1)
    conn, address = sock.accept()
    data = conn.recv(10000)
    server_answer = "{}"
    print("\nNew connection")
    if not data:
        server_answer = {"success": False}
        print("No data received")
    else:
        data_encoded = True
        received_data = json.loads(data.decode('utf-8'))
        try:
            print("Client login:", received_data["login"])
        except:
            data_encoded = False
            server_answer = {"success": False}
            print("none")

        if data_encoded:
            print("Action:", received_data["action"])
            if not received_data["auth"]:
                action = received_data["action"]

                if action == "get_my_diagnoses":
                    server_answer = get_user_diagnoses(received_data["login"])
                    result = "Success" if server_answer["success"] else "Failed"
                    print("Result", result)

                elif action == "get_all_users":
                    server_answer = get_all_users()
                    result = "Success" if server_answer["success"] else "Failed"
                    print("Result", result)

                elif action == "add_new_user":
                    server_answer = add_new_user(received_data["user_data"])
                    print("Result", server_answer["success"])

            else:
                server_answer = authorize_user(received_data["login"], received_data["password"])
                result = "Success" if server_answer["success"] else "Failed"
                print("Result:", result)
                print("Role:", server_answer["role"])

    conn.sendall(json.dumps(server_answer).encode('utf-8'))
    print("Close connection")
sock.close()
