import os
a = ['SERVER_SSH_PRIV_KEY', 'SERVER_SSH_USER', 'SERVER_ADDRES']
# exit()
sep = "\n"
for b in a:
    print(f"\n{b}\n")
    val = os.environ[b]
    if sep in val:
        lines = val.split(sep)
        lines = list(map(lambda x: x[:-1], lines))
        for line in lines:
            print(line)
    else:
        print(os.environ[b][:-1])
