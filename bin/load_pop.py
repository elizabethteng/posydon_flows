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

df = pop.oneline[["S1_mass_i",
                  "S2_mass_i",
                  "orbital_period_i",
                  "S1_state_f",
                  "S2_state_f"]]

s1bh = df["S1_state_f"]=="BH" 
s2bh = df["S2_state_f"]=="BH" 
bbh_bool = s1bh.tolist() and s2bh.tolist()
df = df.assign(bbh = bbh_bool)

df.to_pickle(args.savename)