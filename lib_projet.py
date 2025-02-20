import pandas as pd
import numpy as np
import scipy.optimize as so
from dataclasses import dataclass


def exemple_apports():
    return np.ndarray(np.array([75, 90, 225, 2000, 9, 800, 45]))


@dataclass
class besoins_journaliers:
    """Représente les catégories des aliments nécessaires aux besoins journaliers.

    Args :
    proteines (int): La quantité de protéines nécessaire en grammes.
    lipides (int): La quantité de lipides nécessaire en grammes.
    glucides (int): La quantité de glucides nécessaire en grammes.
    energie (int): La quantité d'énergie nécessaire en kcal.
    fer (int): La quantité de fer nécessaire en mg.
    calcium (int): La quantité de calcium nécessaire en mg.
    fibres (int): La quantité de fibres nécessaire en grammes.
    """

    proteines: int
    lipides: int
    glucides: int
    energie: int
    fer: int
    calcium: int
    fibres: int


def genere_beta(besoins_j: besoins_journaliers):
    """Permet de générer les besoins journaliers de Marie.

    Returns:
    Un tableau numpy contenant les besoins journaliers de Marie représentant
    respectivement les quantités de protéines, de lipides, de glucides,
    d'énergie, de fer, de calcium et de fibres nécessaires en grammes ou
    kcal/mg."""

    return np.array(
        [
            besoins_j.proteines,
            besoins_j.lipides,
            besoins_j.glucides,
            besoins_j.energie,
            besoins_j.fer,
            besoins_j.calcium,
            besoins_j.fibres,
        ]
    )


besoins_j = besoins_journaliers(
    proteines=75, lipides=90, glucides=225, energie=2000, fer=9, calcium=800, fibres=45
)


def genere_dataframe():
    """Permet de générer les apports des aliments.

    Returns:
    Un dataframe contenant les apports nutritionnels des aliments, où chaque
    ligne représente un aliment et chaque colonne représente une catégorie
    nutritionnelle."""

    aliments = pd.read_csv("Aliments.csv", sep=";", index_col=0)
    return aliments


def genere_A():
    """Permet de générer la transposée des apports des aliments.

    Returns:
    Un dataframe contenant les apports nutritionnels des aliments, où chaque
    ligne représente une catégorie nutritionnelle et chaque colonne
    représente un aliment."""

    A = np.array(genere_dataframe()).T
    return A


def genere_cout():
    """Permet d'obtenir la colonne des coûts.

    Returns:
    Un tableau contenant la colonne des coûts, représentant les coûts
    associés à chaque aliment."""

    B = genere_A()
    return B[-1]


def genere_coeff():
    """Permet d'obtenir les coefficients aux apports de chaque aliment.

    Returns:
    Un tableau contenant les valeurs associés aux apports de
    chaque aliment."""

    C = genere_A()
    return C[:-1]


def taille_matrice_c_bub(c=genere_cout(), a_ub=genere_coeff()):
    """Permet de vérifier la compatibilité des matrices de coût
    et de coefficient pour permettre l'optimisation."""

    if c.shape[0] != a_ub.shape[1]:
        raise ValueError(
            "Les matrices de coût et celle des coefficients doivent être compatibles"
        )


def resolution(beta=genere_beta(besoins_j)):
    """Permet de résoudre le problème sans marge."""

    if sum(beta) == 0:
        raise ValueError("Il faut au moins un des apports journaliers non nuls.")
    solution = so.linprog(genere_cout(), A_ub=-genere_coeff(), b_ub=-beta)
    A = solution.x
    (u,) = A.nonzero()
    REST = genere_dataframe().iloc[u, :]
    QTE = pd.DataFrame({"Quantités en g": 100 * A[A.nonzero()]}).set_index(
        genere_dataframe().iloc[u, :].index
    )
    return QTE


def resolution_avec_depassement_apports(
    beta=genere_beta(besoins_j), valeur=float
) -> pd.DataFrame:
    """Permet de résoudre le problème avec marge."""

    assert len(beta) == len(genere_coeff())
    if valeur > 1.0:
        raise ValueError("Veuillez renseigner les pourcentages en décimal.")
    solution = so.linprog(
        genere_cout(),
        A_ub=np.concatenate((-genere_coeff(), genere_coeff()), axis=0),
        b_ub=np.concatenate((-beta, beta * (1 + valeur)), axis=0),
    )
    A = solution.x
    (u,) = A.nonzero()
    REST = genere_dataframe().iloc[u, :]
    QTE = pd.DataFrame({"Quantités en g": 100 * A[A.nonzero()]}).set_index(
        genere_dataframe().index[u]
    )
    return QTE


def taille_matrice(beta=genere_beta):
    """Permet de vérifier si tous les apports journaliers ont bien
    été enregistrés."""

    if len(beta) != len(genere_coeff()):
        raise ValueError("Tous les apports journaliers n'ont pas été renseignés")


def satisfaction_variete_alimentaire(Beta=genere_beta(besoins_j)):
    """Permet de vérifier si le repas est assez varié."""

    nb_aliments = len(resolution(Beta).index)
    nb_aliments_uniques = 0
    if nb_aliments >= 2:
        nom_aliments = set()
        for aliment in resolution(Beta).index:
            debut = aliment.split()[0]
            nom_aliments.add(debut)
            nb_aliments_uniques = len(nom_aliments)
            if nb_aliments_uniques <= 2:
                raise ValueError("Il y a assez d'aliments, mais pas assez de variété")


def satisfaction_nombre_aliments(Beta=genere_beta(besoins_j)):
    """Permet de vérifier si le repas contient un nombre d'aliments
    supérieur ou égal à 2."""

    nb_aliments = len(resolution(Beta).index)
    if nb_aliments <= 2:
        raise ValueError("Il n'y a pas assez d'aliments, seulement 2 ou moins.")
