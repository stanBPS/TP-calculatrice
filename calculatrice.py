def convert_1_input(lettre_rommaine):
    if lettre_rommaine == 'I':
        return 1
    elif lettre_rommaine == 'V':
        return 5
    elif lettre_rommaine == 'X':
        return 10
    elif lettre_rommaine == 'L':
        return 50
    elif lettre_rommaine == 'C':
        return 100
    elif lettre_rommaine == 'D':
        return 500
    elif lettre_rommaine == 'M':
        return 1000


def convert_same_add2(chaineLettreRomaine):
    """"
    if chaineLettreRomaine == 'II':
        return 2
    elif chaineLettreRomaine == 'VV':
        return 10
    elif chaineLettreRomaine == 'XX':
        return 20
    elif chaineLettreRomaine == 'LL':
        return 100
    elif chaineLettreRomaine == 'CC':
        return 200
    elif chaineLettreRomaine == 'DD':
        return 1000
    elif chaineLettreRomaine == 'MM':
        return 2000
    """
    for l in chaineLettreRomaine:
        return convert_1_input(l) * 2


def convert_same_caract_n(chaine):
    somme = 0
    for l in chaine:
        somme = somme + convert_1_input(l)
    return somme


def convert_add(chaine):
    somme = 0
    for l in chaine:
        somme = somme + convert_1_input(l)
    return somme


def soustraction_2_caract(chaine):
    somme = 0
    c = 0  # sauvegarde valeur de la lettre n-1 de la chaine
    for i in range(len(chaine)):
        c = convert_1_input(chaine[i])
        for j in range(i + 1, len(chaine)):
            if c < convert_1_input(chaine[j]):
                c = convert_1_input(chaine[i]) * -1
        somme = c + somme
    return somme


def soustraction_n_caract(chaine):
    somme = 0
    c = 0
    for i in range(len(chaine)):
        c = convert_1_input(chaine[i])
        for j in range(i + 1, len(chaine)):
            if c < convert_1_input(chaine[j]):
                c = convert_1_input(chaine[i]) * -1
        somme = c + somme
    return somme


def calculatrice(operator, chaine1, chaine2):
    resultat = 0
    nombre1 = soustraction_n_caract(chaine1)
    nombre2 = soustraction_n_caract(chaine2)

    if operator == '+':
        resultat = nombre1 + nombre2
    elif operator == '-':
        resultat = nombre1 - nombre2
    elif operator == '*':
        resultat = nombre1 * nombre2
    elif operator == '/':
        resultat = nombre1 / nombre2
    return resultat


def convert_1_to_roman(num):
    if num == 1:
        return 'I'
    elif num == 5:
        return 'V'
    elif num == 10:
        return 'X'
    elif num == 50:
        return 'L'
    elif num == 100:
        return 'C'
    elif num == 500:
        return 'D'
    elif num == 1000:
        return 'M'

""""
def return_plus_petit(num)
    list_roman_letter = [['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]
    for i in range(len(list_roman_letter)):
        if num <= l[i][1]:


def convert_to_roman_n_add(num):
    list_roman_letter = [['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]
    i = num #1006
    res = 0
    while i != 0:
        res = i/10

"""

