"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
from api import débuter_partie, jouer_coup, lister_parties
from quoridor import (analyser_commande, formater_jeu, formater_les_parties,
                      récupérer_le_coup)

# Mettre ici votre secret récupérer depuis le site de PAX
SECRET = "493162ca-e829-48c5-9e94-3d43b9497375"
analyser_commande()

if __name__ == "__main__":
    args = analyser_commande()
    #print(args.idul)
    #print(vars(args))
    if args.parties:
        parties = lister_parties(args.idul, SECRET)
        print(formater_les_parties(parties))
    else:
        id_partie, état = débuter_partie(args.idul, SECRET)
        while True:
            # Afficher la partie
            print(formater_jeu(état))
            # Demander au joueur de choisir son prochain coup
            type_coup, position = récupérer_le_coup()
            # Envoyez le coup au serveur
            try:
                id_partie, état = jouer_coup(
                id_partie,
                type_coup,
                position,
                args.idul,
                SECRET,)
            except RuntimeError as RE:
                print(RE)
                print()
                #pass
