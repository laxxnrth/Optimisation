# Projet Supply Chain
## Sujet 2 - Régime Alimentaire

### Rappel du sujet
On utilisera les données contenues dans le fichier Aliments.csv dans la suite.

Marie estime ses besoins journaliers de la manière suivante :
- 2000 Kcal
- 75g de Protéines
- 225g de Glucides
- 90g de Lipides
- 9mg de Fer
- 800mg de Calcium
- 45g de Fibres
1) Comment doit-elle satisfaire ses besoins si elle veut minimiser son budget?
2) Comment procéder si elle ne veut pas dépasser de plus de 10% les apports journaliers?

## Contenu du code
Dans un premier temps :
- Résolution du problème selon besoins journaliers de Marie dans `resolution_depart.py`

Dans un second temps :
- Résolution du problème de manière généralisée sous forme de librairie dans `lib_projet.py`
- Mise en place des tests dans `test_projet.py`
    - Vérification de la validation des tests
- Création de `visualisation.py` nous facilitant la visualisation lors de l'utilisation de l'interface ligne de commande
- Création de `__main__.py` pour l'interface ligne de commande
- Remplissage des docstrings
- Mise en place d'un formateur de code :
   - Installation de black via `py -m pip install black`
    - Application de black via `py -m black ./projet_sc/lib_projet.py ./tests/test_projet.py`
- Mise en place d'un typechecker :
    - Installation de mypy via `py -m pip install mypy`
    - Application de mypy via `py -m mypy ./projet_sc/lib_projet.py ./tests/test_projet.py`
- Mise en place d'un linter :
    - Installation de ruff via `py -m pip install ruff`
    - Application de ruff via `py -m ruff ./projet_sc/lib_projet.py ./tests/test_projet.py`

Interface en ligne :
![](img\Interface1.JPG)
![](img\Interface2.JPG)
