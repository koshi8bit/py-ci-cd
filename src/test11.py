import os
a = ['SERVER_SSH_PRIV_KEY', 'SERVER_SSH_USER', 'SERVER_ADDRES']
for b in a:
    print(os.environ[b][:-1])
