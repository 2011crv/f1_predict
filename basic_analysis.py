import fastf1 
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd
import os
import sys

try:
    fastf1.Cache.enable_cache(sys.path[0]+"/fastf1_cache")
except:
    os.makedirs(sys.path[0]+"/fastf1_cache")
    fastf1.Cache.enable_cache(sys.path[0]+"/fastf1_cache")


#input 
year = 2025
location = 'Miami'
session = 'Q'

#get session

race = fastf1.get_session(year,location,session)
race.load(weather=True)

df=race.laps
