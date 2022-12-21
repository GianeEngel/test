# -*- coding: utf-8 -*-
"""
Codigo para fazer a predicao a partir do modelo treinado.
versao giane.sav
Tipo: floresta randomica

@author: mirkos@gmail.com
"""

import joblib
import streamlit as st
import pandas as pd

gravidade = ['Leve','Moderada','Grave']
nome = 'giane.sav'
modelo = joblib.load(nome)
st.title('Preditor de gravidade COVID-19')
siri = 0
aisi = 0
nlr = 0
plr = 0
sii = 0
rdw = st.number_input('RDW (%)',min_value=(10),max_value=(9000))
leu = st.number_input('Leukocytes (x109/L)',min_value=(1),max_value=(270))
lin = st.number_input('Lymphocytes (x109/L)')
mon = st.number_input('Monocytes (x109/L)')
neu = st.number_input('Neutrophils (x109/L)',min_value=(1),max_value=(35))
pcr = st.number_input('PCR (mg/dL)')
pla = st.number_input('Plaquetas (x109/L)')#
satO = st.selectbox('Saturation Oximetry',('<95','>=95'))
if satO == '<95':
    sat=0
else:
    sat=1
dbm2 = st.selectbox('Diabetes Mellitus type 2',('NO','YES'))
if dbm2=='Nao':
    dm2 = 0
else:
    dm2 = 1

if st.button('Calculos'):
    #nlr = st.number_input('NLR.1')
    if lin == 0:
        nlr = 0
        plr = 0
        aisi = 0
    elif mon == 0:
        siri = 0
    else:
        siri = nlr/float(mon)
        #aisi = st.number_input('AISI.1')
        aisi = (float(neu)*int(pla)*float(mon))/float(lin)
        nlr = float(neu)/float(lin)
        #plr = st.number_input('PLR.1')
        plr = float(pla)/float(lin)
        #sii = st.number_input('SII.1')
        sii = plr/float(neu)
        #siri = st.number_input('SIRI.1')
# if mon == 0:
 #       siri = 0
  #  else:
   #    siri = nlr/float(mon)
    #aisi = st.number_input('AISI.1')
    #   aisi = (float(neu)*int(pla)*float(mon))/float(lin)
    
    st.write('NLR:',nlr)
    limit_float = round(nlr, 2)
    print('NOVO-NLR:',limit_float)
    st.write('PLR:',plr)
    st.write('SII:',sii)
    st.write('SIRI:',siri)
    st.write('AISI:',aisi)

pac = [rdw,leu,neu,pcr,sat,dm2,nlr,plr,sii,siri,aisi]
pred = modelo.predict([pac])

if st.button('Analyze'):
    indice = float(pred)
    st.write('Gravidade pred:',gravidade[float(pred)])
    if indice == 0:
        st.image('low-risk.png')
    else:
        if indice==1:
            st.image('moderate-risk.png')
        else:
            st.image('high-risk.png')

