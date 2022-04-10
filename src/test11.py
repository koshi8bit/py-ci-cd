import os
import sys

# exit()
sep = "\n"
args = sys.argv[1:]
print("Args:", args)
for b in args:
    print(f"\n{b}")
    val = os.environ[b]
    if sep in val:
        lines = val.split(sep)
        lines = list(map(lambda x: x[:-1], lines))
        for line in lines:
            print(line)
    else:
        print(os.environ[b][:-1])
