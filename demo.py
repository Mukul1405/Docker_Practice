import os
import sys

os.environ['key'] = sys.argv[1]
print(os.environ['key'])