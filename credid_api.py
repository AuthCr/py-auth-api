#!/usr/bin/env python3

# Usage:
#  import credid_api
#  s = credid_api.connect("127.0.0.1", 8999)
#  credid_api.auth(s, "root", "toor")
#  credid_api.has_access_to(s, "write", "/some/path")

import socket

def connect(ip, port):
    api = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    api.connect((ip, port))
    return api

def send_command(api, cmd, options):
    query = cmd + "\n"
    api.send(query.encode('utf-8'))
    data = api.recv(1024)
    # print(data)
    return data

def is_success(data):
    return data == b'success\n'

def auth(api, username, password, options = {}):
    return send_command(api, "AUTH : " + username + " " + password, options)

def user_has_access_to(api, username, perm, path, options = {}):
    return send_command(api, "USER HAS ACCESS TO : " + username + " " + perm + " " + path, options)

def group_add(api, group, perm, resource, options = {}):
    return send_command(api, "GROUP ADD : " + group + " " + perm + " " + resource, options)

def group_remove(api, group, resource, options = {}):
    return send_command(api, "GROUP REMOVE : " + group + " " + resource, options)

def group_list(api, options = {}):
    return send_command(api, "GROUP LIST", options)

def group_list_perms(api, group, options = {}):
    return send_command(api, "GROUP LIST PERMS : " + group, options)

def group_get_perm(api, group, resource, options = {}):
    return send_command(api, "GROUP GET PERM : " + group + " " + resource, options)

def user_list(api, options = {}):
    return send_command(api, "USER LIST", options)

def user_add(api, username, password, options = {}):
    return send_command(api, "USER ADD : " + username + " " + password, options)

def user_remove(api, username, options = {}):
    return send_command(api, "USER REMOVE : " + username, options)

def user_add_group(api, username, group, options = {}):
    return send_command(api, "USER ADD GROUP : " + username + " " + group, options)

def user_remove_group(api, username, group, options = {}):
    return send_command(api, "USER REMOVE GROUP : " + usernae + " " + group, options)

def user_list_groups(api, username, options = {}):
    return send_command(api, "USER LIST GROUPS : " + username, options)

def user_change_password(api, username, newpassword, options = {}):
    return send_command(api, "USER CHANGE PASSWORD : " + username + " " + newpassword, options)
