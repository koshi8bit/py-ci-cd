import os
a = ['SERVER_SSH_PRIV_KEY', 'SERVER_SSH_USER', 'SERVER_ADDRES']
sep = "\n"
for b in a:
    val = os.environ[b]
    print(sep in val)
    if sep in val:
        lines = val.split(sep)
        print(lines)
        lines = list(map(lambda x: x[:-1], lines))
        for line in lines:
            print(line)
    else:
        print(os.environ[b][:-1])
