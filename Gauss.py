import numpy as np
import streamlit as st

st.set_page_config(page_title="Gauss", page_icon=":crystal_ball:")
st.header("Eliminação de Gauss")

st.sidebar.title("Seleção de Sistema Linear")

metodo = st.sidebar.selectbox(
    "Escolha o seu método",
    ('Gauss', 'Gauss - Seidel'))

def gerar_matriz(size):
        matrix = np.zeros((size, size+1))
        for i in range(size):
            for j in range(size+1):
                matrix[i][j] = np.random.randint(10)  # Você pode ajustar o intervalo dos valores aqui

        return matrix
    
def main():
    size = st.sidebar.number_input("Digite o tamanho da matriz:", min_value=1, value=3, step=1)

    if st.sidebar.button("Gerar matriz"):
        matrix = gerar_matriz(int(size))
        st.write("Matriz gerada:")
        st.write(matrix)

if __name__ == "__main__":
    main()


if metodo == 'Gauss':
    st.write('Você selecionou Gauss.')

else:
    st.write("Você selecionou Gauss - Seidel")



