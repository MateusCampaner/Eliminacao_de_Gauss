import streamlit as st
import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = np.copy(x0)

    for _ in range(max_iter):
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        if np.linalg.norm(A @ x - b) < tol:
            break

    return x

def main():
    st.title("Resolução de Matriz por Gauss-Seidel")

    # Inputs
    st.header("Entradas")
    n = st.number_input("Tamanho da matriz quadrada (n x n)", min_value=1, value=3, step=1)
    A = np.zeros((n, n))
    b = np.zeros(n)
    x0 = np.zeros(n)
    for i in range(n):
        for j in range(n):
            A[i][j] = st.number_input(f"A[{i+1}, {j+1}]", value=0.0)
        b[i] = st.number_input(f"b[{i+1}]", value=0.0)
        x0[i] = st.number_input(f"x0[{i+1}]", value=0.0)
    tol = st.number_input("Tolerância", value=1)
    max_iter = st.number_input("Número máximo de iterações", min_value=1, value=100, step=1)

    # Resolução
    if st.button("Resolver"):
        x = gauss_seidel(A, b, x0, tol, max_iter)
        st.header("Saída")
        st.write("Solução encontrada:")
        st.write(x)

if __name__ == "__main__":
    main()