from posydon.popsyn.synthetic_population import Population
import pandas as pd

path = "/projects/b1119/briel/popsyn/240618_grids/240618/IF/burstSFR/alpha_0.2/1e+00_Zsun_population.h5"
pop = Population(path,verbose=True)

m1 = pop.oneline["S1_mass_i"]
m2 = pop.oneline["S2_mass_i"]
p = pop.oneline["orbital_period_i"]

fstate1 = pop.oneline["S1_state_f"]
fstate2 = pop.oneline["S2_state_f"]

bbh = np.logical_and(fstate1==fstate2 ,fstate1=="BBH")

data = {"m1" : m1,
          "m2" : m2,
          "p" : p,
          "BBH" : bbh
         }

df = pd.Dataframe(data)

df.to_pickle("test_bbh_data.pkl")