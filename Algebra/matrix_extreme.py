import random
import copy
from fractions import  Fraction

def get_matrix(file_name="matrix_new.txt"):
    file = open(file_name, "r")
    A = []
    for line in file:
        A.append([Fraction(x) for x in line.split()])
    return A

def print_file(A, comment = ""):
    file = open("matrix_show.txt", "a")
    file.write("%s\n" % comment)
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

    # print(a)

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

def vector_series(A, alpha):
    N = matrix_plus_k_elementary(A, Fraction(-alpha, 1))

    addition_to_base = matrix_addition_to_base()
    ans = []

    for v in addition_to_base:
        ans.append([])
        curv = copy.copy(v)
        for i in range(50):
            ans[-1].append(curv)
            curv = matrix_vector_product(N, curv)
            
            not_null = False
            for it in curv:
                if it != 0:
                    not_null = True
            if not not_null:
                break
    return ans

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

def print_in_file(a, file):
    for item in a:
        file.write("%6s " % item)
    file.write("\n")

if __name__ == "__main__":

    ff = open("matrix_show.txt", "w")
    ff.close()

    alpha = [3, -5] # eigenvalues numbers

    a = get_matrix()
    A = transform_matrix(a)

    print_file(a, "Initial matrix")
    print_file(A, "Transformed matrix")

    for alpha_current in alpha:
        print_file([], "alpha = %i" % alpha_current)

        Ae0 = matrix_plus_k_elementary(A, Fraction(-alpha_current, 1))
        Ae = Ae0
        print_file(Ae0, "ker N0")

        fund_syst_array = []
        for cnt in range(50):
            fundamental_system = matrix_fundamental_system_of_solutions(Ae)
            if cnt == 0 or cnt > 0 and  not len(fund_syst_array[-1]) == len(fundamental_system):
                fund_syst_array.append(fundamental_system)
                print_file(fundamental_system, "fundamental_system Ker N^%i" % (cnt + 1))
                Ae = matrix_product(Ae, Ae0)
            else:
                break;

        chain = []
        for i in range(len(fund_syst_array) - 1, 0, -1):
            print("i = %i" % i)
            tmp = []
            for item_chain in chain:
                for item in item_chain:
                    tmp.append(item[-i-1])

            file_addition = open("addition.txt", "w")
            file_addition.write("%i %i\n" % (len(fund_syst_array[i - 1]) + len(tmp), len(fund_syst_array[i])))

            for item in fund_syst_array[i - 1]:
                print_in_file(item, file_addition)
            for item in tmp:
                print_in_file(item, file_addition)
            for item in fund_syst_array[i]:
                print_in_file(item, file_addition)
            file_addition.close()

            chain.append(vector_series(A, alpha_current))

            print_file([], "Chain #")
            for it in chain[-1]:
                print_file(it)
