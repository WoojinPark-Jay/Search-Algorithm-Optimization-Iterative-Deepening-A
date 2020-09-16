
### In this part of hw , I refer the most of the webpage's code part from below : 
### https://stackoverflow.com/questions/13888566/python-basemap-drawgreatcircle-function/14154584#14154584
import os
import conda

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib

from mpl_toolkits.basemap import Basemap
import numpy as np
import pandas as pd
m = Basemap(projection='cyl', lon_0=0, resolution='c')

m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary(fill_color='aqua')

location = pd.read_csv('Location_coordinates.csv')

loc = {}
for a, b in location.iterrows():
    loc[b['Location']] = (b['Latitude'], b['Longitude'])
    
print(loc)

network = [ ("St. Stephan's Cathedral,  Austria", 'Stockholm,  Sweden'),
           ('Stockholm,  Sweden', 'Tallinn,  Estonia' ),
           ('Tallinn,  Estonia', 'Shanghai,  China'),
           ('Shanghai,  China', 'Itsukushima Shrine,  Japan'),
           ('Itsukushima Shrine,  Japan','Brisbane,  Australia'),
           ('Brisbane,  Australia','Montreal,  Canada'),
           ('Montreal,  Canada','Teide,  Spain'),
           ('Teide,  Spain','Edinburgh,  Scotland'),
           ('Edinburgh,  Scotland','Brugge,  Belgium'),
           ('Brugge,  Belgium',"St. Stephan's Cathedral,  Austria")           
           ]


for s, t in network:
    la1, lo1 = loc[s]
    la2, lo2 = loc[t]
    line, = m.drawgreatcircle(lo1, la1, lo2, la2, lw=3)

    p = line.get_path()
    
    cp = np.where(np.abs(np.diff(p.vertices[:, 0])) > 199)[0]
    if cp:
        cp = cp[0]

        nv = np.concatenate(
                                   [p.vertices[:cp, :], 
                                    [[np.nan, np.nan]], 
                                    p.vertices[cp+1:, :]]
                                   )
        p.codes = None
        p.vertices = nv
