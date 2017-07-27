#!/usr/bin/env python3

# Usage:
#  import auth_api
#  s = auth_api.connect("127.0.0.1", 8999)
#  auth_api.auth(s, "root", "toor")
#  auth_api.has_access_to(s, "/some/path")

import socket

def connect(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    return s

def send_command(s, cmd):
    # print("> " + cmd)
    s.send(cmd.encode('utf-8'))
    data = s.recv(1024)
    # print(data)
    return data

def auth(s, username, password):
    data = send_command(s, "AUTH : " + username + " " + password + "\n")
    return data == b'success\n'

def has_access_to(s, path):
    data = send_command(s, "USER HAS ACCESS TO : write " + path + "\n")
    return data == b'success\n'

if __name__ == "__main__":
    s = connect("127.0.0.1", 8999)
    if auth(s, "root", "toor"):
        print("Connected with root:toor")
    else:
        print("Failed to connect")
        exit(1)

    if has_access_to(s, "/tmp"):
        print("You have access to /tmp")
    else:
        print("You don't have access to /tmp")
