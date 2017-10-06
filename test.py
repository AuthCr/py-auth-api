#!/usr/bin/env python3
# Test

if __name__ == "__main__":
    import credid_api
    api = credid_api.connect("127.0.0.1", 8999)
    # Auth
    r = credid_api.auth(api, "root", "toor")
    if credid_api.is_success(r) == True:
        print("Connected with root:toor")
    else:
        print("Failed to connect\n" + str(r))
        exit(1)
    # Perm test
    r = credid_api.user_has_access_to(api, "root", "write", "/tmp")
    if credid_api.is_success(r) == True:
        print("You have access to /tmp")
    else:
        print("You don't have access to /tmp\n" + str(r))
