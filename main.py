""" nombre de caracteres similaires et joints présent dans une chaine de caractères """
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(1100)
#### Fonctions secondaires



def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne
    de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)"""
    # votre code ici
    liste=[]
    i=0
    while i != len(s) :
        n=1
        while i+n<len(s) and s[i]==s[i+n] :
            n+=1
        ev=(s[i],n)
        liste.append(ev)
        i+=n
    return liste


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de
    caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    # cas de base
    if not s :
        return []
    # recherche nombre de caractères identiques au premier
    # appel récursif
    n=1

    while n<len(s) and s[0]==s[n] :
        n+=1
    return [(s[0],n)] + artcode_r(s[n:])
#### Fonction principale


def main():
    """fonction main"""
    #print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
