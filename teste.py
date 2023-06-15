import streamlit as st
import numpy as np

def generate_matrix(size):
    # Criar a matriz
    matrix = np.zeros((size, size+1))

    # Preencher a matriz com valores aleatórios
    for i in range(size):
        for j in range(size+1):
            matrix[i][j] = np.random.randint(10)  # Você pode ajustar o intervalo dos valores aqui

    return matrix

# Interface do Streamlit
def main():
    st.title("Gerador de Matriz")

    size = st.number_input("Digite o tamanho da matriz:", min_value=1, value=3, step=1)

    if st.button("Gerar matriz"):
        matrix = generate_matrix(int(size))
        st.write("Matriz gerada:")
        st.write(matrix)

if __name__ == "__main__":
    main()