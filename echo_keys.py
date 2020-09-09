#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# Q&D python script to echo information from downloaded key csv file
# in a useable format.
# Author: Erik Vermeer
# Date:   Sep 2019
import os
import re
import sys

# Check if file was given.
if len(sys.argv) == 1:
    print('ERROR   - no file given', file=sys.stderr)
    sys.exit(1)
else:
    keyf = sys.argv[1]

# Check if file is accessible.
if not os.path.isfile(keyf):
    print(f'ERROR   - file {keyf} not found or accessible', file=sys.stderr)
    sys.exit(1)

# Open the file and extract the relevant line.
try:
    with open(keyf, 'r') as fh:
        wanted = (fh.read().splitlines())[1]
except Exception as why:
    print('ERROR   - opening {}: {}'.format(keyf, str(why)), file=sys.stderr)
    sys.exit(1)

# Print out information.
(key, value) = re.split(',', wanted)
print(f'export AWS_ACCESS_KEY_ID="{key}"')
print(f'export AWS_SECRET_ACCESS_KEY="{value}"')
print('export AWS_REGION=eu-central-1')
