"""Tests Quoridor

Ce module contient des tests unitaires pour le projet Quoridor.
"""
from quoridor import formater_damier, formater_jeu, formater_légende

# Réussi
def test_formater_légende_pour_une_nouvelle_partie():
    joueurs = [
        {"nom": "Robin", "murs": 10, "pos": [5, 1]},
        {"nom": "Alfred", "murs": 10, "pos": [5, 9]},
    ]

    attendu = (
        "Légende:\n"
        "   1=Robin,  murs=||||||||||\n"
        "   2=Alfred, murs=||||||||||\n"
    )

    résultat = formater_légende(joueurs)

    assert résultat == attendu, "Échec du test de formater_légende pour une nouvelle partie"

# Réussi
def test_formater_damier_pour_une_nouvelle_partie():
    joueurs = [
        {"nom": "Robin", "murs": 10, "pos": [5, 1]},
        {"nom": "Alfred", "murs": 10, "pos": [5, 9]},
    ]
    murs = {
        "horizontaux": [],
        "verticaux": [],
    }

    attendu = (
        "   -----------------------------------\n"
        "9 | .   .   .   .   2   .   .   .   . |\n"
        "  |                                   |\n"
        "8 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "7 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "6 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "5 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "4 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "3 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "2 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "1 | .   .   .   .   1   .   .   .   . |\n"
        "--|-----------------------------------\n"
        "  | 1   2   3   4   5   6   7   8   9\n"
    )

    résultat = formater_damier(joueurs, murs)
    assert résultat == attendu, "Échec du test de formater_damier pour une nouvelle partie"

# Réussi
def test_formater_jeu_pour_une_nouvelle_partie():
    état = {
        "joueurs": [
            {"nom": "Robin", "murs": 10, "pos": [5, 1]},
            {"nom": "Alfred", "murs": 10, "pos": [5, 9]},
        ],
        "murs": {
            "horizontaux": [],
            "verticaux": [],
        },
    }

    attendu = (
        "Légende:\n"
        "   1=Robin,  murs=||||||||||\n"
        "   2=Alfred, murs=||||||||||\n"
        "   -----------------------------------\n"
        "9 | .   .   .   .   2   .   .   .   . |\n"
        "  |                                   |\n"
        "8 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "7 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "6 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "5 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "4 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "3 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "2 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "1 | .   .   .   .   1   .   .   .   . |\n"
        "--|-----------------------------------\n"
        "  | 1   2   3   4   5   6   7   8   9\n"
    )

    résultat = formater_jeu(état)

    assert résultat == attendu, "Échec du test de formater_jeu pour une nouvelle partie"

# Réussi
def test_formater_jeu_pour_une_partie_avancée():
    état = {
        "joueurs": [
            {"nom": "Alfred", "murs": 7, "pos": [5, 5]},
            {"nom": "Robin", "murs": 3, "pos": [8, 6]},
        ],
        "murs": {
            "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
            "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]],
        }
    }

    attendu = (
        "Légende:\n"
        "   1=Alfred, murs=|||||||\n"
        "   2=Robin,  murs=|||\n"
        "   -----------------------------------\n"
        "9 | .   .   .   .   .   .   .   .   . |\n"
        "  |                                   |\n"
        "8 | .   .   .   .   .   . | .   .   . |\n"
        "  |        ------- -------|-------    |\n"
        "7 | . | .   .   .   .   . | .   .   . |\n"
        "  |   |                               |\n"
        "6 | . | .   .   .   .   . | .   2   . |\n"
        "  |    -------            |           |\n"
        "5 | .   .   . | .   1   . | .   .   . |\n"
        "  |           |                       |\n"
        "4 | .   .   . | .   .   .   .   .   . |\n"
        "  |            -------                |\n"
        "3 | .   .   .   .   . | .   .   .   . |\n"
        "  |                   |               |\n"
        "2 | .   .   .   .   . | .   .   .   . |\n"
        "  |                                   |\n"
        "1 | .   .   .   .   .   .   .   .   . |\n"
        "--|-----------------------------------\n"
        "  | 1   2   3   4   5   6   7   8   9\n"
    )

    résultat = formater_jeu(état)

    assert résultat == attendu, "Échec du test de formater_jeu pour une partie avancée"



if __name__ == "__main__":
    test_formater_légende_pour_une_nouvelle_partie()
    print("Test de formater_légende pour une nouvelle partie réussi")
    test_formater_damier_pour_une_nouvelle_partie()
    print("Test de formater_damier pour une nouvelle partie réussi")
    test_formater_jeu_pour_une_nouvelle_partie()
    print("Test de formater_jeu pour une nouvelle partie réussi")
    test_formater_jeu_pour_une_partie_avancée()
    print("Test de formater_jeu pour une partie avancée réussi")
