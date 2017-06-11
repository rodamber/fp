# Miguel Borges Ribeiro, aluno numero 79085
# Rodrigo Andre Moreira Bernardo, aluno numero 78942
# Grupo 35

def encripta(N, i, j):
    """
    encripta: int x int x int --> int
    encripta(N, i, j) devolve a mensagem N encriptada,
    usando o i-esimo e j-esimo primos.
    """
    n = (n_esimo_primo(i) - 1) * (n_esimo_primo(j) - 1)
    m = n_esimo_primo(i) * n_esimo_primo(j)
    e = calcula_e(n)
    if N >= m:
        raise ValueError("encripta: a mensagem tem de ser inferior a " + str(m))
    return  N**e % m

def decifra(C, i, j):
    """
    decifra: int x int x int --> int
    decifra(C, i, j) devolve a mensagem a mensagem original, N, a partir da
    mensagem encriptada, C, e dos i-esimo e j-esimo primos.
    """
    n = (n_esimo_primo(i) - 1) * (n_esimo_primo(j) - 1)
    m = n_esimo_primo(i) * n_esimo_primo(j)
    d = calcula_d(calcula_e(n),n)
    if C >= m:
        raise ValueError("decifra: a mensagem tem de ser inferior a " + str(m))
    return C**d % m

def n_esimo_primo(n):
    """
    n_esimo_primo: int --> int
    n_esimo_primo(n) devolve o n-esimo primo (primo de ordem n).
    """
    ordem, num = 0, 1
    while ordem < n:
        num += 1
        if primo(num):
            ordem += 1
    return num


def primo(num):
    """
    primo: int --> boolean
    primo(num) devolve True se o numero for primo e False se nao for primo.
    """
    div = 2
    if num == 1:
        return False
    elif num == 2:
        return True

    while num % div != 0:
        if div > num**0.5:
            return True
        div = div + 1

    return False

def calcula_e(n):
    """
    calcula_e: int --> int
    calcula_e(n) devolve o menor inteiro entre 1 e n que seja co-primo de n.
    """

    e = 2

    while mdc(e,n)!=1:
        mdc(e,n)
        e = e + 1
    return e

def calcula_d(e, n):
    """
    calcula_d: int x int --> int
    calcula_d(e, n) devolve o menor inteiro d em que se verifica a igualdade
    d * e = 1 + k * n, sendo k um numero inteiro.
    """

    d, k = 0, 0.5 #numero decimal arbitrario para k

    while int(k) != k:
        d = d + 1
        k = (d * e - 1)/n
    return d

def mdc(a, b):
    """
    mdc: int x int --> int
    mdc(a, b) devolve o maximo divisor comum de dois numeros inteiros.
    """

    while b != 0:
        a, b = b, a%b
    return a
