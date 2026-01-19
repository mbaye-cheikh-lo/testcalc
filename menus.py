from calcul import *

FICHIER_HISTORIQUE = "historique.txt"

def sauvegarder_historique(ligne):
    with open(FICHIER_HISTORIQUE, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")

def afficher_historique_fichier():
    try:
        with open(FICHIER_HISTORIQUE, "r", encoding="utf-8") as f:
            print("\n--- Historique (fichier) ---")
            print(f.read())
    except FileNotFoundError:
        print("Historique vide.")


def menu():
    print("\n 1 - Calcul simple")
    print("2 - calcul avec priorite")
    print("3 - Afficher l'historique")
    print("4 - Quitter")
    return input("Votre choix:")

historique=[]

while True:

    choix=menu()
    
    if choix=="1":
        n1=float(input("saisir n1:"))
        op=input("saisir op (+ - / *):")
        n2=float(input("saisir n2:"))

        if op == "+":
            resultat=addition(n1,n2)
        elif op == "-":
            resultat=soustraction(n1,n2)
        elif op == "*":
            resultat=multiplication(n1,n2)
        elif op == "/":
            resultat=division(n1,n2)
         
        else:
            print("Operation invalide:")
            ligne = f"{n1} {op} {n2} = {resultat}"
            historique.append(ligne)
            sauvegarder_historique(ligne)
            historique.append(f"{n1} {op} {n2}= {resultat}")
    
    elif choix=="2":
        n1=float(input("saisir n1:"))
        op1=input("saisir premier opérateur:")
        n2=float(input("saisir n2:"))
        op2=input("saisir deuxieme operateur:")
        n3=float(input("saisir n3:"))

        if op1=="*" and op2=="+":
            resultat=calcul_priorite_parentheseAM(n1,n2,n3)
        elif op1=="*" and op2=="-":
            resultat=calcul_priorite_parentheseSM(n1,n2,n3)
        elif op1=="+" and op2=="/":
            resultat=calcul_priorite_parentheseAD(n1,n2,n3)
        elif op1=="-" and op=="/":
            resultat=calcul_priorite_parentheseSD(n1,n2,n3)
        else:
            print("Combinaison invalide")
            continue

        print("resultat combinaison:",resultat)
        ligne = f"{n1} {op1} {n2} {op2} {n3} = {resultat}"
        historique.append(ligne)
        sauvegarder_historique(ligne)

    elif choix=="3":
        afficher_historique_fichier()

    elif choix=="4":
        break

    else:
        print("choix invalide")
