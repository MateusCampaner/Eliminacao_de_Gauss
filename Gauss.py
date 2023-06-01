import numpy as np
import matplotlib as mt
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gauss", page_icon=":crystal_ball:")
st.header("Eliminação de Gauss")

def eliminacao_gauss(matriz):
    n = len(matriz) 
    
    for i in range(n): 
        pivo = matriz[i][i] 
        
        if pivo == 0: 
            raise ValueError("Ops, verifique o valor do pivô indicado")
        
        matriz[i] = matriz[i] / pivo 
        
        print("Matriz intermediária após a normalização da linha", i + 1)
        print(matriz)
        print()
        
        for j in range(i+1, n): 
            multiplicador = matriz[j][i] 
            matriz[j] = matriz[j] - multiplicador * matriz[i] # 
        
        print("Matriz intermediária após a atualização das linhas abaixo do pivô", i + 1)
        print(matriz)
        print()
    
    return matriz


st.sidebar.title("Seleção de Sistema Linear")

metodo = st.sidebar.selectbox(
    "Escolha o seu método",
    ('Gauss', 'Gauss - Seidel'))

rows = st.sidebar.number_input("Número de linhas da matriz", min_value=1, value=3)
cols = rows

if metodo == 'Gauss':
    st.write('Você selecionou Gauss.')
else:
    st.write("Você selecionou Gauss - Seidel")

st.write(f"Número de linhas e colunas selecionadas: {rows}")

data = [[st.sidebar.number_input(f"Valor [{i+1},{j+1}]", key=f"value_{i}_{j}", value=0.0) for j in range(cols)] for i in range(rows)]
df = pd.DataFrame(data, index=range(1, rows + 1), columns=range(1, cols + 1))
edited_df = st.experimental_data_editor(df)


