from typer import Typer
from .lib_projet import (
    besoins_journaliers,
)
from projet_sc.visualisation import bj_to_table, res_to_table
from rich import print

app = Typer()


@app.command()
def start():
    """Génère des besoins journaliers"""
    bj = besoins_journaliers(
        proteines=80,
        lipides=85,
        glucides=230,
        energie=2200,
        fer=9,
        calcium=900,
        fibres=50,
    )
    print(bj_to_table(bj))


@app.command()
def solve():
    """Génère la résolution"""
    bj = besoins_journaliers(
        proteines=80,
        lipides=85,
        glucides=230,
        energie=2200,
        fer=9,
        calcium=900,
        fibres=50,
    )
    print(res_to_table(bj))


if __name__ == "__main__":
    app()
