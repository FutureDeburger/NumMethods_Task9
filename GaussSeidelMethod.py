
def gauss_seidel(A, b, eps, max_iterations=1000):
    n = len(A)
    x = [0.0] * n

    for iteration in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        if all(abs(x_new[i] - x[i]) < eps for i in range(n)):
            return x_new
        x = x_new

    print("Достигнуто максимальное количество итераций.")
    return x


if __name__ == '__main__':
    epsilon = 1e-6

    SLE_A = [[2.47, 0.65, -1.88],
             [1.34, 1.17, 2.54],
             [0.86, -1.73, -1.08]]

    SLE_B = [1.24,
             2.35,
             3.15]

    solution = gauss_seidel(SLE_A, SLE_B, epsilon)
    print(solution)


    test_a = [[10, 1, 1],
             [2, 10, 1],
             [2, 2, 10]]

    test_b = [12, 13, 14]

    test_solution = gauss_seidel(test_a, test_b, epsilon)
    print(test_solution)