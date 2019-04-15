from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABctJ8FnzuuS8I728cmDwOplcpjwcV3LLj2GCPbmO8nTzHHf6ZeK9fzcxr4aqc5Tz5rTPNmXvnqdo9lG-NMb5MDcmPkRFvwULxp05YH8OMMIFrDD6BCLCmwabQwr7A9wkGrO1lt02l1l3ZGeozhmatbKBbudjfWWHp-6x_q6oBp8wvJwkk='

if __name__ == "__main__":
    f = Fernet(key)
    print(f.decrypt(message))