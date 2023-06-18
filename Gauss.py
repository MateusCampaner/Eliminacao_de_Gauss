import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Gauss", page_icon=":crystal_ball:")

st.sidebar.title("Seleção de método")

metodos = ['📊 Gauss', '📈 Gauss - Seidel']
selecao_metodos = st.sidebar.selectbox("Escolha o seu método", metodos)

if selecao_metodos == '📊 Gauss':
    st.header("📊 Gauss")
else:
    st.header("📈 Gauss - Seidel")

tamanho_matriz = st.sidebar.number_input("Digite o tamanho da matriz:", min_value=2, value=3, step=1)

def gerar_matriz():
    matriz = np.zeros((tamanho_matriz, tamanho_matriz+1))
    for i in range(tamanho_matriz):
        for j in range(tamanho_matriz+1):
            matriz[i][j] = 0

    dataframe = pd.DataFrame(matriz)

    return dataframe

def calcular_gauss(matriz):
    n = len(matriz)
    iteracao = 0

    for i in range(n):
        
        if matriz[i][i] == 0:
            max_index = i
            max_value = 0
            for k in range(i+1, n):
                if abs(matriz[k][i]) > max_value:
                    max_value = abs(matriz[k][i])
                    max_index = k
            if max_index != i:
                matriz[[i, max_index]] = matriz[[max_index, i]]  

        pivo = matriz[i][i]
        if pivo == 0:
            raise ValueError("A matriz não pode ser calculada, um dos pivôs tem valor 0.")
            

        for j in range(i+1, n):
            fator = matriz[j][i] / pivo
            matriz[j] = matriz[j] - fator * matriz[i]
            iteracao = iteracao + 1

            st.write(f"Iteração {iteracao}")
            st.write(matriz)

    x = np.zeros(n)
    x[n-1] = matriz[n-1][n] / matriz[n-1][n-1]
    for i in range(n-2, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += matriz[i][j] * x[j]
        x[i] = (matriz[i][n] - soma) / matriz[i][i]

    return x

def calcular_gauss_seidel():
         
    return "Gauss-Seidel"

st.write("Matriz de valores")

df = gerar_matriz()
matriz_df = st.experimental_data_editor(df)

calcular = st.button("Calcular")

if selecao_metodos == '📊 Gauss':

    if calcular:
        matriz_valores = matriz_df.values
        try:
            resultado = calcular_gauss(matriz_valores)
            st.write("Resultados:")
            st.write(resultado)
        except ValueError as e:
            st.write("Erro:", str(e))

else:

    st.sidebar.number_input("Esolha o valor de epsilon", max_value= 0, min_value=-10, value=-1, step=1)

    st.sidebar.write("Escolha os valores do chute inicial das variáveis")
    vetor_valores_iniciais = np.zeros(tamanho_matriz)
    df_vetor_valores_iniciais = pd.DataFrame(vetor_valores_iniciais)
    vetor_df = st.sidebar.experimental_data_editor(df_vetor_valores_iniciais)

if calcular:
         
        resultados_gauss_seidel = calcular_gauss_seidel()
        st.write(resultados_gauss_seidel)