
def Gaussian_method(sle):

    i1 = sle[0]
    i2 = sle[1]
    i3 = sle[2]
    print_orig_sle = f'Оригинальная СЛАУ:\n{i1}\n{i2}\n{i3}\n'

    i2_hatch = list(x + y for x, y in zip(list(_ * (-i2[0]/i1[0]) for _ in i1), i2))
    i3_hatch = list(x + y for x, y in zip(list(_ * (-i3[0]/i1[0]) for _ in i1), i3))
    print_first_dec = f'Первое вычитание:\n{i1}\n{i2_hatch}\n{i3_hatch}\n'

    i3_hatch_hatch = list(x + y for x, y in zip(list(_ * (-i3_hatch[1]/i2_hatch[1]) for _ in i2_hatch), i3_hatch))
    print_second_dec = f'Второе вычитание:\n{i1}\n{i2_hatch}\n{i3_hatch_hatch}\n'

    x3 = i3_hatch_hatch[3] / i3_hatch_hatch[2]
    x2 = (i2_hatch[3] - i2_hatch[2] * x3) / i2_hatch[1]
    x1 = (i1[3] - i1[1] * x2 - i1[2] * x3) / i1[0]

    list_of_approximate_roots = [x1, x2, x3]
    #print(f'Полученные приближённые корни: {list_of_approximate_roots}')

    return list_of_approximate_roots, print_orig_sle, print_first_dec, print_second_dec

def find_epsilon(sle, apr_roots):

    A = [x[:-1] for x in sle]
    B = [x[-1] for x in sle]

    Ax0 = [[a * x0 for a, x0 in zip(row, apr_roots)] for row in A]
    eps = [b - sum(ax0) for b, ax0 in zip(B, Ax0)]  # невязка для приближенного решения x0

    return eps

def find_delta(orig_sle, eps):

    A = [x[:-1] for x in orig_sle]
    new_sle = [a + [b] for a, b in zip(A, eps)]

    return Gaussian_method(new_sle)[0]

def find_x(approx_roots, amends):
    list_x = [x0 + d for x0, d in zip(approx_roots, amends)]
    return list_x

def check_roots(orig_sle, orig_roots):
    A = [x[:-1] for x in orig_sle]
    B = [sum(a*x for a,x in zip(row, orig_roots)) for row in A]
    return B

if __name__ == '__main__':

    SLE = [[2.47, 0.65, -1.88, 1.24],
           [1.34, 1.17, 2.54, 2.35],
           [0.86, -1.73, -1.08, 3.15]]

    approximate_roots = Gaussian_method(SLE)[0]
    epsilon = find_epsilon(SLE, approximate_roots)
    amendments = find_delta(SLE, epsilon)
    roots = find_x(approximate_roots, amendments)
    check = check_roots(SLE, roots)

    print(Gaussian_method(SLE)[1])
    print(Gaussian_method(SLE)[2])
    print(Gaussian_method(SLE)[3])
    print(f'Полученные приближённые корни: {approximate_roots}')
    print(f'Невязка для приближенного решения x0: {epsilon}')
    print(f'Значения поправок: {amendments}')
    print(f'Значения корней: {roots}')
    print(f'Проверка подстановкой: {check}')