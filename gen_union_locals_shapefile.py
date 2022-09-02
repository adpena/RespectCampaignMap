import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.colors import ListedColormap

district_boundaries = gpd.read_file("/Users/adpena/PycharmProjects/RespectCampaignMap/DistrictsFinal.geojson")

district_boundaries.geom_type.head()
