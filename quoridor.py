"""Module Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
    * formater_légende - Formater la représentation graphique du damier.
    * formater_damier - Formater la représentation graphique de la légende.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
"""
import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut «idul» représentant l'idul du joueur
                   et l'attribut «parties» qui est un booléen True/False.
    """
    parser = argparse.ArgumentParser()

    parser = argparse.ArgumentParser(
                    description = 'Quoridor')

    parser.add_argument('idul', help = 'IDUL du joueur')
    parser.add_argument('-p', '--parties', action='store_true', help = "Lister les parties existantes")

    return parser.parse_args()


def formater_légende(joueurs):
    
    """Formater la représentation graphique de la légende.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.

    Returns:
        str: Chaîne de caractères représentant la légende.
    """
    nom1 = joueurs[0].get('nom') + ','
    nom2 = joueurs[1].get('nom') + ','
    #print(nom1)
    #print(nom2)

    lon = max(len(nom1), len(nom2))

    murs1 = joueurs[0].get('murs')
    murs2 = joueurs[1].get('murs')

    m1 = ('|' * murs1)
    m2 = ('|' * murs2)

    l1 = f'   1={nom1:{lon}} murs=' + m1
    l2 = f'   2={nom2:{lon}} murs=' + m2

    chaine = 'Légende:' + '\n' + l1 + '\n' + l2 + '\n'
    return chaine


def formater_damier(joueurs, murs):
    """Formater la représentation graphique du damier.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.
        murs (dict): Dictionnaire représentant l'emplacement des murs.

    Returns:
        str: Chaîne de caractères représentant le damier.
    """
    # Initialisation du damier vide
    ld = '   ' + ('-' * 35)
    lf = '--|' + ('-' * 35)
    ll = ' '.join([' ', '|', '1', ' ', '2', ' ', '3', ' ', '4', ' ', '5', ' ', '6', ' ', '7', ' ', '8', ' ', '9'])
    lvide = ' '.join([' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'])
    ls = []
    chaine = ''

    for i in range(9):
        ls.append(' '.join([str(i+1),'|', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', '|']))

    damier = [ld]
    for element in reversed(ls):
        damier.append(element)
        damier.append(lvide)
    del(damier[-1])
    damier.append(lf)
    damier.append(ll)

    # Traitement des joueurs
    cter = 1
    for i in joueurs:
        position = i.get('pos')
        temp = list(damier[20 - (position[1] * 2) - 1])
        temp[position[0]*4] = str(cter)
        damier[20 - (position[1] * 2) - 1] = ''.join(temp)
        cter += 1
    
    # Traitement des murs horizontaux
    if len(murs.get('horizontaux')) > 0:
        for i in murs.get('horizontaux'):
            ind_list = [4*i[0]-1, 4*i[0], 4*i[0]+1, 4*i[0]+2, 4*i[0]+3, 4*i[0]+4, 4*i[0]+5]
            temp = list(damier[20 - (i[1] * 2)])
            for idx in ind_list:
                temp[idx] = '-'
            damier[20 - (i[1] * 2)] = ''.join(temp)

    # Traitement des murs verticaux
    if len(murs.get('verticaux')) > 0:
        for i in murs.get('verticaux'):
            temp2 = []
            ind_list = [20 - (i[1] * 2) - 1, 20 - (i[1] * 2) - 2, 20 - (i[1] * 2) - 3]

            for j in ind_list:
                temp2.append(list(damier[j]))
            
            for k in range(len(ind_list)):
                temp2[k][4*i[0] - 2] = '|'
                damier[ind_list[k]] = ''.join(temp2[k])

    # Formatage du damier
    for i in damier:
        chaine += i + '\n'
    
    return chaine


def formater_jeu(état):
    """Formater la représentation graphique d'un jeu.

    Doit faire usage des fonctions formater_légende et formater_damier.

    Args:
        état (dict): Dictionnaire représentant l'état du jeu.

    Returns:
        str: Chaîne de caractères représentant le jeu.
    """
    legend = formater_légende(état['joueurs'])
    game = formater_damier(état['joueurs'], état['murs'])
    state = legend + game
    return state

def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): Liste des parties

    Returns:
        str: Représentation des parties
    """

    chaine = ''
    cter = 1
    for i in test:
        line = str(cter) + ' : ' + i['date'] + ', ' + i['joueurs'][0] + ' vs ' + i['joueurs'][1]
        if i['gagnant'] is None:
            line = ''.join([line, '\n'])
        else:
            line = ''.join([line,', gagnant: ', i['gagnant']])
        chaine += line
        cter += 1
    return chaine


def récupérer_le_coup():
    """Récupérer le coup

    Returns:
        tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
    Examples:
        Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):
        Donnez la position où appliquer ce coup (x,y): 2,6
    """
    while True:
        type = input('Quel type de coup voulez-vous jouer? (\'D\', \'MH\', \'MV\') ?')
        if (type == 'D') or (type == 'MH') or (type == 'MV'):
            break
        else:
            print('Type erroné, veuillez entrer un type de coup valide.')

    while True:
        position = input('Donnez la position où appliquer ce coup (x,y) :').split(',')
        if len(position) != 2:
            print('Position invalide, veuillez entrer une position valide.')
        elif isinstance(int(position[0]), int) and isinstance(int(position[1]), int) and 1 <= int(position[0]) <= 9 and 1 <= int(position[1]) <= 9:
            break
        else:
            print('Position invalide, veuillez entrer une position valide.')

    return (type, [int(position[0]), int(position[1])])


