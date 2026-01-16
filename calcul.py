def addition(n1,n2):
    return n1 + n2

def soustraction(n1,n2):
    return n1 - n2

def division(n1,n2):
    return n1 / n2

def multiplication(n1,n2):
    return n1 * n2

def calcul_prioriteMA(n1,n2,n3):
    resultat=n1 * n2 + n3
    return resultat

def calcul_prioriteMS(n1,n2,n3):
    resultat= n1 * n2 - n3
    return resultat

def calcul_prioriteMD(n1,n2,n3):
    resultat=n1*n2/n3
    return resultat

def calcul_priorite_parentheseAM(n1,n2,n3):
    resultat=(n1 + n2) * n3
    return resultat

def calcul_priorite_parentheseSM(n1,n2,n3):
    resultat=(n1 - n2) * n3
    return resultat

def calcul_prioriteM(n1,n2,n3):
    resultat= n1 * n2 * n3
    return resultat

def calcul_prioriteD(n1,n2,n3):
    resultat= n1 / n2 / n3
    return resultat

def calcul_priorite_parentheseSD(n1,n2,n3):
    resultat=(n1 - n2) / n3
    return resultat

def calcul_priorite_parentheseAD(n1,n2,n3):
    resultat=(n1 + n2) / n3
    return resultat

