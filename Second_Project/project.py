# Miguel Borges Ribeiro, 79085
# Rodrigo Andre Moreira Bernardo, 78942
# Grupo al067
#

from janela_sopa_letras import *

################################################################################
#                              FUNCOES GERAIS

def inverte_string(s):
    """
    inverte_string: string --> string
    inverte_string(string) recebe uma string e inverte-a, ou seja, devolve a
    mesma string, lida da direita para esquerda.
    """
    nova_string = ''
    for i in range(len(s)-1,-1,-1):
        nova_string = nova_string + s[i]
    return nova_string

def maiuscula(lst):
    """
    maiuscula: lista de strings --> lista de strings
    maiuscula(lst) recebe uma lista de strings e devolve a mesma lista de
    strings, cada uma com os seus caracteres na forma maiuscula.
    """
    for i in range(len(lst)):
        lst[i] = string_maiuscula(lst[i])
    return lst

def string_maiuscula(string):
    """
    string_maiuscula: string --> string
    string_maiuscula(string) recebe uma string e devolve a mesma string com os
    seus caracteres na forma maiuscula.
    """
    nova_string = ''
    for car in string:
        nova_string = nova_string + car_maiusculo(car)
    return nova_string

def car_maiusculo(car):
    """
    car_maiusculo: string --> string
    car_maiusculo(car) recebe um caracter e devolve o mesmo caracter na
    forma maiuscula.
    """
    if 'A' <= car <= 'Z':
        return car
    elif 'a' <= car <= 'z':
        return chr(ord(car) - abs(ord('A') - ord('a')))
    else:
        raise ValueError('car_maiusculo: caracter invalido')

################################################################################
#                                TIPO DIRECAO

# RECONHECEDORES

def e_direcao(arg):
    """
    e_direcao: universal --> logico
    e_direcao(arg) tem o valor verdadeiro se arg for do tipo direcao e falso
    caso contrario.
    """
    return arg in ('N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW')

def e_norte(arg):
    """
    e_norte: direcao --> logico
    e_norte(arg) tem o valor verdadeiro se arg for o elemento 'N' e falso caso
    contrario.
    """
    return arg == 'N'

def e_sul(arg):
    """
    e_sul: direcao --> logico
    e_sul(arg) tem o valor verdadeiro se arg for o elemento 'S' e falso caso
    contrario.
    """
    return arg == 'S'

def e_leste(arg):
    """
    e_leste: direcao --> logico
    e_sul(arg) tem o valor verdadeiro se arg for o elemento 'E' e falso caso
    contrario.
    """
    return arg == 'E'

def e_oeste(arg):
    """
    e_oeste: direcao --> logico
    e_oeste(arg) tem o valor verdadeiro se arg for o elemento 'W' e falso caso
    contrario.
    """
    return arg == 'W'

def e_nordeste(arg):
    """
    e_nordeste: direcao --> logico
    e_nordeste(arg) tem o valor verdadeiro se arg for o elemento 'NE' e falso
    caso contrario.
    """
    return arg == 'NE'

def e_noroeste(arg):
    """
    e_noroeste: direcao --> logico
    e_noroeste(arg) tem o valor verdadeiro se arg for o elemento 'NW' e falso
    caso contrario.
    """
    return arg == 'NW'

def e_sudeste(arg):
    """
    e_sudeste: direcao --> logico
    e_sudeste(arg) tem o valor verdadeiro se arg for o elemento 'SE' e falso
    caso contrario.
    """
    return arg == 'SE'

def e_sudoeste(arg):
    """
    e_sudoeste: direcao --> logico
    e_sudoeste(arg) tem o valor verdadeiro se arg for o elemento 'SW' e falso
    caso contrario.
    """
    return arg == 'SW'

#TESTES

def direcoes_iguais(d1, d2):
    """
    direcoes_iguais: direcao x direcao --> logico
    direcoes_iguais(d1, d2) devolve o valor verdadeiro se as direcoes d1 e d2
    forem iguais e falso caso contrario.
    """
    return d1 == d2

# OUTRAS OPERACOES

def direcao_oposta(d):
    """
    direcao_oposta: direcao --> direcao
    direcao_oposta(d) devolve a direcao oposta a d de acordo com a rosa dos
    ventos.
    """
    return roda_direcao(d,4)

def roda_direcao(d,n):
    """
    roda_direcao: direcao x inteiro positivo --> direcao
    roda_direcao(d,n) devolve o resultado da aplicacao de uma rotacao de menos
    45 graus a direcao d, n vezes.
    """

    def roda_direcao_aux(d):
        """
        roda_direcao_aux: direcao --> direcao
        roda_direcao_aux(d) devolve o resultado da aplicacao de uma rotacao de
        menos 45 graus a direcao d.
        """
        if e_norte(d):
            return 'NE'
        elif e_nordeste(d):
            return 'E'
        elif e_leste(d):
            return 'SE'
        elif e_sudeste(d):
            return 'S'
        elif e_sul(d):
            return 'SW'
        elif e_sudoeste(d):
            return 'W'
        elif e_oeste(d):
            return 'NW'
        elif e_noroeste(d):
            return 'N'

    if n == 0:
        return d
    elif n == 1:
        return roda_direcao_aux(d)
    elif n > 1:
        return roda_direcao(roda_direcao_aux(d),n-1)

################################################################################
#                              TIPO COORDENADA

# CONSTRUTOR

def coordenada(l,c,d):
    """
    coordenada: int positivo x int positivo x direcao --> coordenada
    coordenada(l, c, d) devolve a coordenada referente a  posicao (l,c) e
    direcao d.
    """
    if ( isinstance(l,int)
       and isinstance(c,int)
       and e_direcao(d)
       and l >= 0
       and c >= 0 ):
        return (l,c,d)
    else:
        raise ValueError('coordenada: argumentos invalidos')

# SELETORES

def coord_linha(c):
    """
    coord_linha: coordenada --> inteiro positivo
    coord_linha(c) tem como valor a linha da coordenada.
    """
    return c[0]

def coord_coluna(c):
    """
    coord_coluna: coordenada --> inteiro positivo
    coord_coluna(c) tem como valor a coluna da coordenada.
    """
    return c[1]

def coord_direcao(c):
    """
    coord_direcao: coordenada --> direcao
    coord_direcao(c) tem como valor a direcao da coordenada.
    """
    return c[2]

# RECONHECEDORES

def e_coordenada(arg):
    """
    e_coordenada: universal --> logico
    e_coordenada(arg) tem o valor verdadeiro se arg for do tipo coordenada, e
    falso caso contrario.
    """
    return (isinstance(arg,tuple)
           and len(arg) == 3
           and isinstance(arg[0],int)
           and isinstance(arg[1],int)
           and e_direcao(arg[2])
           and arg[0] >= 0
           and arg[1] >= 0 )

# TESTES

def coordenadas_iguais(c1,c2):
    """
    coordenadas_iguais: coordenada x coordenada --> logico
    coordenadas_iguais(c1, c2) devolve o valor verdadeiro se as coordenadas c1 e
    c2 forem iguais, e falso caso contrario.
    """
    return c1 == c2

# OUTRAS OPERACOES

def coordenada_string(c):
    """
    coordenada_string: coordenada --> string
    coordenada_string(c) devolve a representacao externa de c.
    """
    return '(' + str(coord_linha(c))\
               + ', '\
               + str(coord_coluna(c))\
               + ')-'\
               + str(coord_direcao(c))

def roda_coord(g,c,n):
    """
    roda_coord: grelha x coordenada x inteiro positivo --> coordenada
    roda_coord(g,c,n) devolve o resultado da aplicacao de um rotacao de menos 90
    graus a coordenada c segundo a grelha g, n vezes.
    """

    def roda_coord_aux(g,c):
        """
        roda_coord_aux: grelha x coordenada --> coordenada
        roda_coord_aux(g,c) devolve a coordenada que resulta da aplicacao de uma
        rotacao de menos 90 graus a coordenada c segundo a grelha g.
        """
        return coordenada(coord_coluna(c),\
                          grelha_nr_linhas(g)-1-coord_linha(c),\
                          roda_direcao(coord_direcao(c),2))
    if n == 0:
        return c
    elif n == 1:
        return roda_coord_aux(g,c)
    elif n > 1:
        return roda_coord(roda_grelha(g,1),roda_coord_aux(g,c),n-1)

################################################################################
#                                TIPO GRELHA

# CONSTRUTOR

def grelha(lst):
    """
    grelha: lista de strings --> grelha
    grelha(lst) tem como valor uma grelha m x n, em que m e o numero de
    elementos da lista lst e n o numero de caracteres de cada
    string na lista.
    """
    erro = 'grelha: argumentos invalidos'
    if isinstance(lst,list) and lst != []:
        for elem in lst:
            if not ( isinstance(elem,str) and len(elem) == len(lst[0]) ):
                raise ValueError(erro)
        return maiuscula(lst)
    else:
        raise ValueError(erro)

# SELETORES

def grelha_nr_linhas(g):
    """
    grelha_nr_linhas: grelha --> inteiro positivo
    grelha_nr_linhas(g) devolve o numero de linhas da grelha g.
    """
    return len(g)

def grelha_nr_colunas(g):
    """
    grelha_nr_colunas: grelha --> inteiro positivo
    grelha_nr_colunas(g) devolve o numero de colunas da grelha g.
    """
    return len(g[0])

def grelha_elemento(g,l,c):
    """
    grelha_elemento: grelha x int positivo x int positivo --> string
    grelha_elemento(g,l,c) devolve o caracter que esta na posicao (l,c) da
    grelha g.
    """
    if l < grelha_nr_linhas(g) and c < grelha_nr_colunas(g):
        return g[l][c]
    else:
        raise ValueError('grelha_elemento: argumentos invalidos')

def grelha_linha(g,c):
    """
    grelha_linha: grelha x coordenada --> string
    grelha_linha(g,c) devolve a cadeia de caracteres que corresponde a linha
    definida segundo a direcao dada pela coordenada c, e que inclui a posicao
    dada pela mesma coordenada.
    """

    def vertical(g,c):
    #esta funcao, tal como a funcao horizontal, podia receber um inteiro
    #(neste caso correspondente a coluna) em vez de uma coordenada.
    #No entanto, como as funcoes diagonais necessitam de uma coordenada, assim
    #foi feito para esta, de tal modo que as suas chamadas sejam realizadas de
    #forma identica e o codigo seja de mais facil entendimento.
        """
        vertical: grelha x coordenada --> string
        vertical(g,c) devolve a cadeia de caracteres correspondente aos
        elementos da grelha g presentes na coluna a que corresponde a coordenada
        c, de cima para baixo.
        """
        string = ''
        for linha in range(grelha_nr_linhas(g)):
            string = string + grelha_elemento(g,linha,coord_coluna(c))
        return string

    def horizontal(g,c):
        """
        horizontal: grelha x coordenada --> string
        horizontal(g,c) devolve a cadeia de caracteres correspondente aos
        elementos da grelha g presentes na linha a que corresponde a coordenada
        c, da esquerda para a direita.
        """
        return vertical(roda_grelha(g,1),roda_coord(g,c,1))

    def diagonal(g,c):
        """
        diagonal: grelha x coordenada --> string
        diagonal(g,c) devolve a cadeia de caracteres correspondente aos
        elementos da grelha g presentes na diagonal de sentido sudeste e que
        passa pela coordenada c.
        """
        d = diag_correspond(g,c)
        linha = coord_linha(d)
        string = ''
        for c in range(coord_coluna(d), grelha_nr_colunas(g)):
            if linha < grelha_nr_linhas(g):
                string = string + grelha_elemento(g,linha,c)
                linha = linha + 1
        return string

    def diagonal_oposta(g,c):
        """
        diagonal_oposta: grelha x coordenada --> string
        diagonal_oposta(g,c) devolve a cadeia de caracteres correspondente aos
        elementos da grelha g presentes na diagonal de sentido nordeste e que
        passa pela coordenada c.
        """
        return diagonal(roda_grelha(g,1),roda_coord(g,c,1))

    direcao = coord_direcao(c)
    if not ((0 <= coord_linha(c) < grelha_nr_linhas(g))
       and (0 <= coord_coluna(c) < grelha_nr_colunas(g))):
        raise ValueError('grelha_linha: argumentos invalidos')
    elif e_sul(direcao):
        return vertical(g,c)
    elif e_norte(direcao):
        return inverte_string(vertical(g,c))
    elif e_leste(direcao):
        return horizontal(g,c)
    elif e_oeste(direcao):
        return inverte_string(horizontal(g,c))
    elif e_sudeste(direcao):
        return diagonal(g,c)
    elif e_noroeste(direcao):
        return inverte_string(diagonal(g,c))
    elif e_nordeste(direcao):
        return diagonal_oposta(g,c)
    elif e_sudoeste(direcao):
        return inverte_string(diagonal_oposta(g,c))

# RECONHECEDORES

def e_grelha(arg):
    """
    e_grelha: universal --> logico
    e_grelha(arg) tem o valor verdadeiro se arg for do tipo grelha e falso caso
    contrario.
    """
    if isinstance(arg,list) and list != []:
        for elem in arg:
            if not ( isinstance(elem,str)
                     and len(elem) == len(arg[0])
                     and elem == string_maiuscula(elem) ):
                return False
        return True
    else:
        return False

# TESTES

def grelhas_iguais(g1,g2):
    """
    grelhas_iguais: grelha x grelha --> logico
    grelhas_iguais(g1,g2) devolve o valor verdadeiro se as grelhas forem iguais,
    e falso caso contrario.
    """
    return g1 == g2

# OUTRAS OPERACOES

def diag_correspond(g,c):
    """
    diag_correspond: grelha x coordenada --> coordenada
    diag_correspond(g,c) devolve a coordenada resultado da projecao segundo o
    sentido noroeste da coordenada c nos limites da grelha g, e que
    define a diagonal com sentido sudeste que passa por c.
    Por exemplo, se c for a coordenada de um elemento pertencente a diagonal
    principal da grelha, diag_correspond(g,c) devolve a coordenada (0,0,'SE').
    """
    if coord_linha(c) > coord_coluna(c):
        return coordenada(coord_linha(c) - coord_coluna(c),0,'SE')
    else:
        return coordenada(0,coord_coluna(c) - coord_linha(c),'SE')

def roda_grelha(g,n):
    """
    roda_grelha: grelha x int --> grelha
    roda_grelha(g) devolve o resultado da aplicacao de uma rotacao de menos 90
    graus a grelha g, n vezes.
    """

    def roda_grelha_aux(g):
        """
        roda_grelha_aux: grelha --> grelha
        roda_grelha(g) devolve o resultado da aplicacao de uma rotacao de menos
        90 graus a grelha g.
        """
        nova_grelha = []
        for coluna in range(grelha_nr_colunas(g)):
            nova_grelha = nova_grelha + \
                [inverte_string(grelha_linha(g,coordenada(0,coluna,'S')))]
        return grelha(nova_grelha)

    if n == 0:
        return g
    elif n == 1:
        return roda_grelha_aux(g)
    elif n > 1:
        return roda_grelha(roda_grelha_aux(g),n-1)

################################################################################
#                               TIPO RESPOSTA

# CONSTRUTOR

def resposta(lst):
    """
    resposta: lista de tuplos(string, coordenada) --> resposta
    resposta(lst) tem como valor a resposta que contem cada um dos tuplos que
    compoem a lista lst.
    """
    erro = 'resposta: argumentos invalidos'
    if isinstance(lst,list):
        for elem in lst:
            if  not ( isinstance(elem,tuple)
                     and len(elem) == 2
                     and isinstance(elem[0],str)
                     and len(elem[0]) != 0
                     and e_coordenada(elem[1]) ):
                raise ValueError(erro)
        return lst
    else:
        raise ValueError(erro)

# SELETORES

def resposta_elemento(res,n):
    """
    resposta_elemento: resposta x inteiro positivo --> tuplo(string, coordenada)
    resposta_elemento(res,n) devolve o enesimo elemento da resposta res.
    """
    if 0 <= n < resposta_tamanho(res):
        return res[n]
    else:
        raise ValueError('resposta_elemento: argumentos invalidos')

def resposta_tamanho(res):
    """
    resposta_tamanho: resposta --> inteiro positivo
    resposta_tamanho(res) devolve o numero de elementos da resposta res.
    """
    return len(res)

# MODIFICADORES

def acrescenta_elemento(r,s,c):
    """
    acrescenta_elemento: resposta x string x coordenada --> resposta
    acrescenta_elemento(r,s,c) devolve a resposta r com mais um elemento - o
    tuplo (s, c).
    """
    return r + [(s,c)]

# RECONHECEDORES

def e_resposta(arg):
    """
    e_resposta: universal --> logico
    e_resposta(arg) tem o valor verdadeiro se arg for do tipo resposta, e falso
    caso contrario.
    """
    if isinstance(arg,list):
        for elem in arg:
            if  not ( isinstance(elem,tuple)
                     and len(elem) == 2
                     and isinstance(elem[0],str)
                     and len(elem[0]) != 0
                     and e_coordenada(elem[1]) ):
                return False
        return True
    else:
        return False

# TESTES

def respostas_iguais(r1,r2):
    """
    respostas_iguais: resposta x resposta --> logico
    respostas_iguais(r1,r2) devolve o valor verdadeiro se as respostas r1 e r2
    contiverem os mesmos tuplos, e falso caso contrario.
    """
    return resposta_string(r1) == resposta_string(r2)

# OUTRAS OPERACOES

def resposta_string(res):
    """
    resposta_string: resposta --> string
    resposta_string(res) devolve a representacao externa da resposta res.
    """
    res = ordena_resposta(res)
    string = '['

    for i in range(resposta_tamanho(res)):
        string = string + '<'\
                        + resposta_elemento(res,i)[0]\
                        + ':'\
                        + coordenada_string(resposta_elemento(res,i)[1])\
                        + '>, '

    return string[:-2] + ']'    # string[:-2] para retirar a ultima virgula

def ordena_resposta(res):
    """
    ordena_resposta: resposta --> resposta
    ordena_resposta(res) devolve a resposta recebida ordenada alfabeticamente.
    """
    lst_elem = []
    tamanho_res = resposta_tamanho(res)

    for n in range(tamanho_res):
            lst_elem = lst_elem + \
                [(resposta_elemento(res,n)[0],resposta_elemento(res,n)[1])]

    maior_indice = tamanho_res - 1
    troca = True

    while troca:
        troca = False
        for n in range(maior_indice):
            if lst_elem[n][0] > lst_elem[n+1][0]:
                lst_elem[n], lst_elem[n+1] = lst_elem[n+1], lst_elem[n]
                troca = True
        maior_indice = maior_indice - 1

    return resposta(lst_elem)

def junta_respostas(*res):
    """
    junta_respostas: *resposta --> resposta
    junta_resposta(*res) devolve a resposta resultado de juntar todos os
    elementos das respostas fornecidas numa unica resposta.
    """
    res_junta = resposta([])
    for r in range(len(res)):
        for n in range(resposta_tamanho(res[r])):
            res_elem = resposta_elemento(res[r],n)
            res_junta = acrescenta_elemento(res_junta,res_elem[0],res_elem[1])
    return res_junta

################################################################################
#                                 PRINCIPAL

def sopa_letras(ficheiro):
    """
    sopa_letras: string --> resposta
    sopa_letras(ficheiro) tem como resultado a resposta ao puzzle descrito em
    ficheiro.
    """

    def palavras_a_procurar(sopa):
        """
        palavras_a_procurar: lista de strings --> lista de strings
        palavras_a_procurar(sopa) recebe uma lista de strings proveniente da
        leitura de um ficheiro de sopa de letras e devolve as palavras a
        procurar nessa sopa.
        """
        lista_de_palavras = []
        palavras = sopa[1]

        for i in range(len(palavras)-1,-1,-1):
            if palavras[i] in ' \n':
                lista_de_palavras = lista_de_palavras + [palavras[i+1:]]
                palavras = palavras[:i]
            elif palavras[i] == ',':
                palavras = palavras[:i]

        return maiuscula(lista_de_palavras[1:])

    def grelha_sopa(sopa):
        """
        grelha_sopa: lista de strings --> grelha
        grelha_sopa(sopa) recebe uma lista de strings proveniente da leitura de
        um ficheiro de sopa de letras e devolve a grelha correspondente a sopa.
        """
        sopa_de_letras = sopa[2:]

        for linha in range(len(sopa_de_letras)):
            string = ''
            for car in sopa_de_letras[linha]:
                if car not in ' \n':
                    string = string + car
            sopa_de_letras[linha] = string

        return grelha(sopa_de_letras)

    fich = open(ficheiro, 'r')
    lst_linhas = fich.readlines()
    fich.close()

    lista_de_palavras = palavras_a_procurar(lst_linhas)
    sopa_de_letras = grelha_sopa(lst_linhas)

    res = ordena_resposta(
            procura_palavras_todas_direcoes(sopa_de_letras,lista_de_palavras))

    janela = janela_sopa_letras(ficheiro)
    janela.mostra_palavras(res)
    janela.termina_jogo()

    return res

def procura_palavras_todas_direcoes(g,palavras):
    """
    procura_palavras_todas_direcoes: grelha x lista de strings --> resposta
    procura_palavras_todas_direcoes(g,palavras) devolve a resposta resultado da
    procura em todas as direcoes pelas palavras fornecidas na grelha g.
    """
    return junta_respostas(
           procura_palavras_numa_direcao(g,palavras,'N'),
           procura_palavras_numa_direcao(g,palavras,'S'),
           procura_palavras_numa_direcao(g,palavras,'E'),
           procura_palavras_numa_direcao(g,palavras,'W'),
           procura_palavras_numa_direcao(g,palavras,'NE'),
           procura_palavras_numa_direcao(g,palavras,'NW'),
           procura_palavras_numa_direcao(g,palavras,'SE'),
           procura_palavras_numa_direcao(g,palavras,'SW') )

def procura_palavras_numa_direcao(g,palavras,d):
    """
    procura_palavras_numa_direcao: grelha x lista de strings x direcao -->
                                         --> resposta
    procura_palavras_numa_direcao(g,palavras,d) devolve a resposta resultado da
    procura, segundo a direcao d, pelas palavras fornecidas na grelha g.
    """

    def procura_vertical_horizontal(g_aux,palavras,d):
        """
        procura_vertical_horizontal: grelha x lista de strings x direcao -->
                                           --> resposta
        procura_vertical_horizontal(g,palavras,d) devolve a resposta resultado
        da procura na vertical e na horizontal pelas palavras fornecidas na
        grelha g.
        """
        res = resposta([])
        if e_norte(d) or e_sul(d):
            for col in range(grelha_nr_colunas(g_aux)):
                c = coordenada(0,col,d)
                for p in palavras:
                    if p in grelha_linha(g_aux,c):
                        achada = acha_coord(g_aux,p,c)
                        if not grelhas_iguais(g_aux,g):
                            achada = roda_coord(g_aux,achada,3)
                        res = acrescenta_elemento(res,p,achada)
            return res
        else:
            g_rodada, d_rodada = roda_grelha(g_aux,1), roda_direcao(d,2)
            return procura_vertical_horizontal(g_rodada,palavras,d_rodada)

    def procura_diagonal(g_aux,palavras,d):
        """
        procura_diagonal: grelha x lista de strings x direcao --> resposta
        procura_diagonal(g,palavras,d) devolve o resultado da procura na
        diagonal (qualquer sentido) pelas palavras fornecidas na grelha g.
        """
        if e_sudeste(d) or e_noroeste(d):
            res = resposta([])
            for p in palavras:
                for l in range(grelha_nr_linhas(g_aux)):
                    c = coordenada(l,0,d)
                    if p in grelha_linha(g_aux,c):
                        achada = acha_coord(g_aux,p,c)
                        if not grelhas_iguais(g_aux,g):
                            achada = roda_coord(g_aux,achada,3)
                        res = acrescenta_elemento(res,p,achada)
                for col in range(1,grelha_nr_colunas(g_aux)):
                    c = coordenada(0,col,d)
                    if p in grelha_linha(g_aux,c):
                        achada = acha_coord(g_aux,p,c)
                        if not grelhas_iguais(g_aux,g):
                            achada = roda_coord(g_aux,achada,3)
                        res = acrescenta_elemento(res,p,achada)
            return res
        else:
            g_rodada, d_rodada = roda_grelha(g_aux,1), roda_direcao(d,2)
            return procura_diagonal(g_rodada,palavras,d_rodada)

    if e_norte(d) or e_sul(d) or e_leste(d) or e_oeste(d):
        return procura_vertical_horizontal(g,palavras,d)
    elif e_sudeste(d) or e_sudoeste(d) or e_nordeste(d) or e_noroeste(d):
        return procura_diagonal(g,palavras,d)

def acha_coord(g,palavra,c):
    """
    acha_coord: grelha x string x coordenada --> coordenada
    acha_coord(g,palavra,c) devolve a coordenada da palavra encontrada na linha
    da grelha g definida pela coordenada c.
    """
    def acha_coord_sul(g,c):
        """
        acha_coord_sul: grelha x coordenada --> coordenada
        acha_coord_sul(g,c) devolve a coordenada da palavra encontrada na linha
        da grelha g definida pela coordenada c quando o sentido definido em c e
        sul.
        """
        return coordenada(i,coord_coluna(c),coord_direcao(c))

    def acha_coord_norte(g,c):
        """
        acha_coord_norte: grelha x coordenada --> coordenada
        acha_coord_norte(g,c) devolve a coordenada da palavra encontrada na
        linha da grelha g definida pela coordenada c quando o sentido definido
        em c e norte.
        """
        rodada = roda_grelha(g,2)
        achada = acha_coord_sul(rodada,roda_coord(g,c,2))
        return roda_coord(rodada,achada,2)

    def acha_coord_leste(g,c):
        """
        acha_coord_leste: grelha x coordenada --> coordenada
        acha_coord_leste(g,c) devolve a coordenada da palavra encontrada na
        linha da grelha g definida pela coordenada c quando o sentido definido
        em c e leste.
        """
        rodada = roda_grelha(g,1)
        achada = acha_coord_sul(rodada,roda_coord(g,c,1))
        return roda_coord(rodada,achada,3)

    def acha_coord_oeste(g,c):
        """
        acha_coord_oeste: grelha x coordenada --> coordenada
        acha_coord_oeste(g,c) devolve a coordenada da palavra encontrada na
        linha da grelha g definida pela coordenada c quando o sentido definido
        em c e oeste.
        """
        rodada = roda_grelha(g,3)
        achada = acha_coord_sul(rodada,roda_coord(g,c,3))
        return roda_coord(rodada,achada,1)

    def acha_coord_sudeste(g,c):
        """
        acha_coord_sudeste: grelha x coordenada --> coordenada
        acha_coord_sudeste(g,c) devolve a coordenada da palavra encontrada na
        linha da grelha g definida pela coordenada c quando o sentido definido
        em c e sudeste.
        """
        c = diag_correspond(g,c)
        if coord_linha(c) < coord_coluna(c):
            return coordenada(i,i + coord_coluna(c),coord_direcao(c))
        elif coord_linha(c) > coord_coluna(c):
            return coordenada(i + coord_linha(c),i,coord_direcao(c))
        else:
            return coordenada(i,i,coord_direcao(c))

    def acha_coord_noroeste(g,c):
        """
        acha_coord_noroeste: grelha x coordenada --> coordenada
        acha_coord_noroeste(g,c) devolve a coordenada da palavra encontrada na
        linha da grelha g definida pela coordenada c quando o sentido definido
        em c e noroeste.
        """
        rodada = roda_grelha(g,2)
        achada = acha_coord_sudeste(rodada,roda_coord(g,c,2))
        return roda_coord(rodada,achada,2)

    def acha_coord_nordeste(g,c):
        """
        acha_coord_nordeste: grelha coordenada --> coordenada
        acha_coord_nordeste(g,c) devolve a coordenada da palavra encontrada na
        linha da grelha g definida pela coordenada c quando o sentido definido
        em c e nordeste.
        """
        rodada = roda_grelha(g,1)
        achada = acha_coord_sudeste(rodada,roda_coord(g,c,1))
        return roda_coord(rodada,achada,3)

    def acha_coord_sudoeste(g,c):
        """
        acha_coord_sudoeste: grelha x coordenada --> coordenada
        acha_coord_sudoeste(g,c) devolve a coordenada da palavra encontrada na
        linha da grelha g definida pela coordenada c quando o sentido definido
        em c e sudoeste.
        """
        rodada = roda_grelha(g,3)
        achada = acha_coord_sudeste(rodada,roda_coord(g,c,3))
        return roda_coord(rodada,achada,1)

    linha = grelha_linha(g,c)
    direcao = coord_direcao(c)
    for i in range(len(linha)):
        if palavra not in linha[i+1:]:
            if e_sul(direcao):
                return acha_coord_sul(g,c)
            elif e_norte(direcao):
                return acha_coord_norte(g,c)
            elif e_leste(direcao):
                return acha_coord_leste(g,c)
            elif e_oeste(direcao):
                return acha_coord_oeste(g,c)
            elif e_sudeste(direcao):
                return acha_coord_sudeste(g,c)
            elif e_noroeste(direcao):
                return acha_coord_noroeste(g,c)
            elif e_nordeste(direcao):
                return acha_coord_nordeste(g,c)
            elif e_sudoeste(direcao):
                return acha_coord_sudoeste(g,c)
