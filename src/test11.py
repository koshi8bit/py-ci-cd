import os
import sys

# exit()
sep = "\n"
for b in sys.argv[1:]:
    print(f"\n{b}")
    val = os.environ[b]
    if sep in val:
        lines = val.split(sep)
        lines = list(map(lambda x: x[:-1], lines))
        for line in lines:
            print(line)
    else:
        print(os.environ[b][:-1])
