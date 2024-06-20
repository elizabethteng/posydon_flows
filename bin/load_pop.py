from posydon.popsyn.synthetic_population import Population
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('--gridfile', default="IF/burstSFR/fiducial/1e+00_Zsun_population.h5",help='',type=str)
parser.add_argument('--savename', default="bbh_data.pkl",help='',type=str)
args = parser.parse_args()

path = "/projects/b1119/briel/popsyn/240618_grids/240618/"

pop = Population(path + args.gridfile,verbose=True)

m1 = pop.oneline["S1_mass_i"]
m2 = pop.oneline["S2_mass_i"]
p = pop.oneline["orbital_period_i"]

fstate1 = pop.oneline["S1_state_f"]
fstate2 = pop.oneline["S2_state_f"]

bbh = np.logical_and(fstate1=="BH",fstate2=="BH")

data = {"m1" : m1,
          "m2" : m2,
          "p" : p,
          "BBH" : bbh
         }

df = pd.Dataframe(data)

df.to_pickle(args.savename)