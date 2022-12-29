import numpy as np
import pandas as pd
import os
from glob import glob


root = r'G:\Groups\GIS\Data\Download_Data\USEPA\TRI\TRI_BasicDataFiles'
outroot = r'G:\Groups\GIS\Data\Download_Data\USEPA\TRI\TRI_BasicDataFiles\combined'


csvlist = glob(os.path.join(root, '*.csv'))
for c in range(0, len(csvlist)-1):
    print(c+1)
    # initialize combining csv1 and csv2
    if c == 0:
        df1 = pd.read_csv(csvlist[c], low_memory=False)
        df2 = pd.read_csv(csvlist[c+1], low_memory=False)
        dfc = pd.concat([df1, df2])
    else:
        # then only read the second csv and combine it with the merged first two
        df2 = pd.read_csv(csvlist[c+1], low_memory=False)
        dfc = pd.concat([dfc, df2])


# export to csv
dfc.to_csv(os.path.join(outroot, 'tri_us.csv'))