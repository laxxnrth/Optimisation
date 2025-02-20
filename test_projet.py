from projet_sc.lib_projet import (
    taille_matrice_c_bub,
    taille_matrice,
    resolution,
    resolution_avec_depassement_apports,
    satisfaction_variete_alimentaire,
    satisfaction_nombre_aliments,
)
import pytest
import numpy as np


def test_taille_matrice_c_bub():
    """Teste si la taille de la matrice de coût est conforme."""
    cout = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
    with pytest.raises(ValueError):
        taille_matrice_c_bub(c=cout)


def test_taille_matrice():
    """Teste si la taille de la matrice beta regroupant les besoins journaliers est conforme."""
    beta = np.array([70, 90, 200, 50, 18, 90, 100, 2000, 9])
    with pytest.raises(ValueError):
        taille_matrice(beta)


def test_resolution():
    """Teste erreur lorsque la somme des apports renseignés est nulle."""
    exemple = np.array([0, 0, 0, 0, 0, 0, 0])
    with pytest.raises(ValueError):
        resolution(beta=exemple)


def test_resolution_avec_depassement_apports():
    """Teste avec un beta différent et une valeur supérieure à 1"""
    beta_2 = np.array([100, 200, 400, 3000, 30, 1500, 70])
    with pytest.raises(ValueError):
        resolution_avec_depassement_apports(beta=beta_2, valeur=3)


def test_satisfaction_variete_alimentaire():
    """Teste si le régime alimentaire est varié."""
    beta = np.array([100, 200, 400, 3000, 30, 1500, 70])
    with pytest.raises(ValueError):
        satisfaction_variete_alimentaire(Beta=beta)


def test_satisfaction_nombre_aliments():
    """Teste si le nombre d'aliments proposés est supérieur ou égale à 2."""
    beta = np.array([1, 8, 15, 1, 7, 5, 5])
    with pytest.raises(ValueError):
        satisfaction_nombre_aliments(Beta=beta)
