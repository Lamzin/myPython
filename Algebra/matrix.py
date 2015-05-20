import random
import copy
#import decimal
from fractions import  Fraction

def get_matrix(file_name="matrix_new.txt"):
    file = open(file_name, "r")
    A = []
    for line in file:
        A.append([Fraction(x) for x in line.split()])
    return A

def print_file(A):
    file = open("matrix_show.txt", "a")
    for i in range(len(A)):
        for j in range(len(A[i])):
            file.write("%6s " % Fraction.limit_denominator(A[i][j]))
        file.write("\n")
    file.write("\n\n")

def transform_matrix(A):
    n = len(A)
    a = [[A[i][j] for j in range(n)] for i in range(n)]

    cnt = 10
    file_report = open("transform_report_new.txt", "w")
    for i in range(n):
        for count in range(cnt):
            j = random.randint(0, n - 1)
            if i == j:
                break
            kk = Fraction(random.randint(-1, 1))
            if not kk == 0:
                for g in range(n):
                    a[i][g] += kk * a[j][g]
                    a[g][j] -= kk * a[g][i]
                file_report.write("(line: ) %i += (%i)%i\n" % (i, kk, j))
                file_report.write("(column: ) %i -= (%i)%i\n" % (j, kk, i))

    return a

def matrix_product(A, B):
    n = len(A)
    C = []
    for i in range(n):
        C.append([])
        for j in range(n):
            C[i].append(Fraction(0, 1))
            for g in range(n):
                C[i][j] += A[i][g] * B[g][j]
    return C

def matrix_plus_k_elementary(A, k):
    ans = [[A[i][j] for j in range(len(A))] for i in range(len(A))]
    for i in range(len(A)):
        ans[i][i] += k
    return ans

def matrix_fundamental_system_of_solutions(A):
    n = len(A)
    a = [[A[i][j] for j in range(n)] for i in range(n)]
    used = [[False, -1] for x in range(n)]

    print(a)

    ii = 0
    for variable in range(n):
        index = -1
        for i in range(ii, n):
            if a[i][variable].numerator != 0:
                index = i
                break
        if index != -1:
            used[variable] = [True, ii]
            a[ii], a[index] = a[index], a[ii]
            k = a[ii][variable]
            for g in range(n):
                a[ii][g] /= k

            for i in range(n):
                if i == ii:
                    continue
                if a[i][variable].numerator != 0:
                    kk = a[i][variable]
                    for j in range(n):
                        a[i][j] -= kk * a[ii][j]
            ii += 1

    ans = []
    for i in range(n):
        if not used[i][0]:
            ans.append([])
            for j in range(n):
                if i == j:
                    ans[-1].append(Fraction(1, 1))
                else:
                    ans[-1].append(-a[used[j][1]][i] if used[j][0] else Fraction(0, 1))
                    pass
    return ans

def matrix_addition_to_base():
    file = open("addition.txt", "r")
    n, m = [int(x) for x in file.readline().split()]
    a = [[Fraction(x) for x in line.split()] for line in file]
    a_copy = copy.deepcopy(a)
    dimV = len(a[0])
    used = [False for x in range(len(a))]

    for variable in range(dimV):
        index = -1
        for i in range(len(a)):
            if a[i][variable].numerator != 0 and not used[i]:
                index = i
                break

        if index != -1:
            used[index] = True
            k = a[index][variable]
            for g in range(dimV):
                a[index][g] /= k
                pass
            for ii in range(len(a)):
                if index == ii:
                    continue
                if a[ii][variable].numerator != 0:
                    kk = a[ii][variable]
                    for g in range(dimV):
                        a[ii][g] -= kk * a[index][g]

    file.close()
    file = open("addition_answer.txt", "w")

    ans = []
    file.write("Addition:\n")
    for i in range(n, len(used)):
        if used[i]:
            ans.append(a_copy[i])
            file.write(" ".join([str(item) for item in a_copy[i]]))
            file.write("\n")
    return ans

def matrix_vector_product(A, v):
    n = len(A)
    C = []
    for i in range(n):
        C.append(Fraction(0, 1))
        for g in range(n):
            C[i] += A[i][g] * v[g]
    return C

def vector_series():
    A = get_matrix()
    N = matrix_plus_k_elementary(A, Fraction(-1, 1))

    addition_to_base = matrix_addition_to_base()

    file = open("series_answer.txt", "w")
    for v in addition_to_base:
        curv = copy.copy(v)
        for i in range(5):
            file.write(" ".join([str(it) for it in curv]))
            file.write(" =>\n")
            curv = matrix_vector_product(N, curv)
        file.write("\n\n")

def matrix_transposed(A):
    n = len(A)
    aT = [[A[j][i] for j in range(n)] for i in range(n)]
    return aT

def matrix_invers(A):
    n = len(A)
    a = copy.deepcopy(A)
    for i in range(n):
        for j in range(n):
            a[i].append(Fraction(0))
        a[i][i + n] = Fraction(1)

    used = [False for x in range(n)]
    for variable in range(n):
        index = -1
        for i in range(n):
            if a[i][variable].numerator != 0 and not used[i]:
                index = i
                break
        if index != -1:
            used[variable] = True
            a[variable], a[index] = a[index], a[variable]
            kk = a[variable][variable]
            for g in range(2*n):
                a[variable][g] /= kk
            for i in range(n):
                if i == variable or a[i][variable].numerator == 0:
                    continue
                kk = a[i][variable]
                for g in range(2*n):
                    a[i][g] -= kk * a[variable][g]

    invers = [[a[i][j + n] for j in range(n)] for i in range(n)]
    return invers

def check_jordan_base():
    A = get_matrix("matrix_input.txt")
    St = get_matrix()
    S = matrix_transposed(St)
    print_file(S)

    S_invers = matrix_invers(S)
    print_file(S_invers)

    product = matrix_product(matrix_product(S_invers, A), S)
    print_file(product)

if __name__ == "__main__":

    # A = get_matrix()
    # atr = transform_matrix(A)
    # print_file(atr)

    #vector_series()
    #matrix_addition_to_base()

    #vector_series()
    #matrix_addition_to_base()


    #A = get_matrix()
    #N = matrix_plus_k_elementary(A, Fraction(-2))

    check_jordan_base()

    # vector_series()

    # a = get_matrix()
    #
    # print_file(a)
    # Ae0 = matrix_plus_k_elementary(a, Fraction(-1, 1))
    # print_file(Ae0)
    #
    # Ae = Ae0
    # for cnt in range(5):
    #     fundamental_system = matrix_fundamental_system_of_solutions(Ae)
    #     print_file(fundamental_system)
    #     Ae = matrix_product(Ae, Ae0)
