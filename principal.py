import streamlit as st
import pandas as pd

st.title('Predição de gravidade COVID a partir de Prontuário')
st.header('(c)2022 - Giane Engel / Mirkos Martins')

genero = st.selectbox('Selecione o gênero do paciente:',('masculino','feminino'))
idade = st.number_input('Digite a idade do paciente:',min_value=1,max_value=150,step=1)
RDW = st.number_input('RDW (%)',value=0.0,min_value=0.0,max_value=50.0,step=0.1)
leucocitos = st.number_input('Leucocitos (x109/L)',step=0.1)
monocitos = st.number_input('Monócitos (x109/L)',step=0.001)
linfocitos = st.number_input('Linfócitos (x109/L)',step=0.001)
plaquetas = st.number_input('Plaquetas (x109/L)',step=1000)
neutrofilos = st.number_input('Neutrófilos (x109/L)',step=0.001)
if st.button('Calcular NLR/PLR/SII/SIRI/AISI'):
  nlr = neutrofilos/linfocitos
  plr = plaquetas/linfocitos
  sii = plr/neutrofilos
  siri = nlr/monocitos
  aisi = (neutrofilos*plaquetas*monocitos)/linfocitos
  st.write('NLR: '+str(nlr))
  st.write('PLR: '+str(plr))
  st.write('SII: '+str(sii))
  st.write('SIRI: '+str(siri))
  st.write('AISI: '+str(aisi))
