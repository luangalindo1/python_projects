# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 08:37:56 2022

@author: luanfabiomg
"""

import pandas as pd
import numpy as np
from statistics import variance

#lendo os dados
decathlon = pd.read_csv("Decathlon.csv", sep=",")
#vista dos dados
decathlon.head()

#renomeando as colunas
decathlon.columns = ["Athlets", "100m", "Long Jump", "Shot Put", "High Jump",
                     "400m", "110m Hurdle", "Discus", "Pole Vault",
                     "Javeline", "1500m", "Rank", "Points", "Competition"]

#definindo os atributos a serem analisados
features = ['100m', 'Long Jump', 'Shot Put', 'High Jump', '400m', 
           '110m Hurdle', 'Discus', 'Pole Vault', 'Javeline',
           '1500m', 'Points']

Athlet_Decastar = decathlon.loc[:12, ['Athlets']].values
Decastar = decathlon.loc[:12, features].values

Athlet_Olympic = decathlon.loc[13:, ['Athlets']].values
Olympic = decathlon.loc[13:, features].values

#variância

hdm_dec = Decastar[:,0]
lj_dec = Decastar[:,1]
sp_dec = Decastar[:,2]
hj_dec = Decastar[:,3]
fhdm_dec = Decastar[:,4]
hdtm_dec = Decastar[:,5]
dc_dec = Decastar[:,6]
pl_dec = Decastar[:,7]
jl_dec = Decastar[:,8]
tdm_dec = Decastar[:,9]
pt_dec = Decastar[:,10]

var_dec = np.array([variance(hdm_dec), variance(lj_dec), variance(sp_dec),
                    variance(hj_dec), variance(fhdm_dec), variance(hdtm_dec),
                    variance(dc_dec), variance(pl_dec), variance(jl_dec),
                    variance(tdm_dec), variance(pt_dec)])


hdm_ol = Olympic[:,0]
lj_ol = Olympic[:,1]
sp_ol = Olympic[:,2]
hj_ol = Olympic[:,3]
fhdm_ol = Olympic[:,4]
hdtm_ol = Olympic[:,5]
dc_ol = Olympic[:,6]
pl_ol = Olympic[:,7]
jl_ol = Olympic[:,8]
tdm_ol = Olympic[:,9]
pt_ol = Olympic[:,10]

var_ol = np.array([variance(hdm_ol), variance(lj_ol), variance(sp_ol),
                    variance(hj_ol), variance(fhdm_ol), variance(hdtm_ol),
                    variance(dc_ol), variance(pl_ol), variance(jl_ol),
                    variance(tdm_ol), variance(pt_ol)])

#correlação

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

target_dec = label_encoder.fit_transform(Athlet_Decastar)
target_dec = pd.DataFrame(target_dec, columns=['Athlets'])
base_dec = decathlon.iloc[:13, 1:11]
base_dec = pd.concat([base_dec, target_dec], axis=1)
correl_dec = base_dec.corr()





