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
rdw = st.number_input('RDW (%)',min_value=(10),max_value=(9000))
leu = st.number_input('Leukocytes (x109/L)',min_value=(0.1),max_value=(270))
lin = st.number_input('Lymphocytes (x109/L)',min_value=(0.1))#
mon = st.number_input('Monocytes (x109/L)',min_value=(0.1))#
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
#nlr = st.number_input('NLR.1')
nlr = int(neu)/int(lin)
#plr = st.number_input('PLR.1')
plr = int(pla)/int(lin)
#sii = st.number_input('SII.1')
sii = plr/int(neu)
#siri = st.number_input('SIRI.1')
siri = nlr/int(mon)
#aisi = st.number_input('AISI.1')
aisi = (int(neu)*int(pla)*int(mon))/int(lin)
st.write('NLR:',nlr)
st.write('PLR:',plr)
st.write('SII:',sii)
st.write('SIRI:',siri)
st.write('AISI:',aisi)
pac = [rdw,leu,neu,pcr,sat,dm2,nlr,plr,sii,siri,aisi]
pred = modelo.predict([pac])




if st.button('Analyze'):
    indice = int(pred)
    st.write('Gravidade pred:',gravidade[int(pred)])
    if indice == 0:
        st.image('low-risk.png')
    else:
        if indice==1:
            st.image('moderate-risk.png')
        else:
            st.image('high-risk.png')
    
