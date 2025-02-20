"""Description

Conversion de besoins_journaliers vers une table Rich.
"""

from projet_sc.lib_projet import (
    besoins_journaliers,
    genere_beta,
    resolution,
)
from rich.table import Table


def bj_to_table(besoins_journaliers: besoins_journaliers) -> Table:
    """Convertit les besoins journaliers en une table Rich.

    Args:
        besoins_journaliers: Les besoins journaliers à convertir.

    Returns:
        Table: La table Rich correspondant aux besoins journaliers.
    """
    resultat = Table(title="Besoins journaliers")
    resultat.add_column("Besoins")
    resultat.add_column("Quantités")
    resultat.add_row("Protéines", f"{besoins_journaliers.proteines}")
    resultat.add_row("Lipides", f"{besoins_journaliers.lipides}")
    resultat.add_row("Glucides", f"{besoins_journaliers.glucides}")
    resultat.add_row("Energie", f"{besoins_journaliers.energie}")
    resultat.add_row("Fer", f"{besoins_journaliers.fer}")
    resultat.add_row("Calcium", f"{besoins_journaliers.calcium}")
    resultat.add_row("Fibres", f"{besoins_journaliers.fibres}")
    return resultat


def res_to_table(besoins_journaliers: genere_beta) -> Table:
    """Convertit la resolution en une table Rich.

    Args:
        besoins_journaliers: Les besoins journaliers à convertir.

    Returns:
        Table: La table Rich correspondant à la résolution.
    """
    resultat = Table(title="Satisfaction des besoins en minimisant le coût")
    resultat.add_column("Besoins")
    resultat.add_column("Quantités")
    resultat.add_column("Les aliments proposés sont")
    resultat.add_row("Protéines", f"{besoins_journaliers.proteines}", f"{resolution()}")
    resultat.add_row("Lipides", f"{besoins_journaliers.lipides}")
    resultat.add_row("Glucides", f"{besoins_journaliers.glucides}")
    resultat.add_row("Energie", f"{besoins_journaliers.energie}")
    resultat.add_row("Fer", f"{besoins_journaliers.fer}")
    resultat.add_row("Calcium", f"{besoins_journaliers.calcium}")
    resultat.add_row("Fibres", f"{besoins_journaliers.fibres}")
    return resultat

