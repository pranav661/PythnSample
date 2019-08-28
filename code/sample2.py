import pandas as pd
import sys
import code.sample as samp

print('starting execution')
print('starting execution 4')

workspace = sys.argv[1]
print(workspace)

masterpath = workspace + "\Master.xlsx"
print(masterpath)

samp.getpath(masterpath)
