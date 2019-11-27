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
    c=0
    for i in range(len(chaine)):
        c = convert_1_input(chaine[i])
        for j in range(i+1, len(chaine)):
            if c < convert_1_input(chaine[j]):
                c = convert_1_input(chaine[i])*-1
        somme = c + somme

    return somme
