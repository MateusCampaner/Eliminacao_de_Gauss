import numpy as np
import streamlit as st

def gerar_matriz(size):
    matrix = np.zeros((size, size+1))
    for i in range(size):
        for j in range(size+1):
            matrix[i][j] = np.random.randint(10)  # Você pode ajustar o intervalo dos valores aqui

    return matrix

def resolver_matriz(matrix):
    size = matrix.shape[0]

    # Eliminação de Gauss
    for i in range(size):
        if matrix[i][i] == 0:
            raise ValueError("A matriz não pode ter zeros na diagonal principal.")

        for j in range(i+1, size):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(size+1):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    # Retrosubstituição
    x = np.zeros(size)
    for i in range(size-1, -1, -1):
        x[i] = matrix[i][size] / matrix[i][i]
        for j in range(i-1, -1, -1):
            matrix[j][size] -= matrix[j][i] * x[i]

    return x

def main():
    size = st.sidebar.number_input("Digite o tamanho da matriz:", min_value=1, value=3, step=1)

    if st.sidebar.button("Gerar matriz"):
        matrix = gerar_matriz(int(size))
        st.write("Matriz gerada:")
        st.write(matrix)

        try:
            solution = resolver_matriz(matrix)
            st.write("Solução encontrada:")
            st.write(solution)
        except ValueError as e:
            st.write("Erro:", str(e))

if __name__ == "__main__":
    main()