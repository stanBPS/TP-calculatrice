def convert(lettre_rommaine):
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


def convert_add2(chaineLettreRomaine):
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
