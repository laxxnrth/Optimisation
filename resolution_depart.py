import pandas as pd
import numpy as np
import scipy.optimize as so
from dataclasses import dataclass

Al = pd.read_csv("Aliments.csv", sep=";", index_col=0)

# QUESTION 1

A = np.array(Al).T

coeff = A[:-1]
z_ori = A[-1]
print(z_ori)
beta = np.array([75, 90, 225, 2000, 9, 800, 45])


RESULT = so.linprog(z_ori, A_ub=-coeff, b_ub=-beta)

# Valeurs réalisant l'optimum
A = RESULT.x

# Coût du repas
print(RESULT.fun)


(u,) = A.nonzero()
REST = Al.iloc[u, :]
print(REST)
QTE = pd.DataFrame({"Quantités en g": 100 * A[A.nonzero()]}).set_index(
    Al.iloc[u, :].index
)
print(QTE)

# QUESTION 2

RESULT_b = so.linprog(
    z_ori,
    A_ub=np.concatenate((-coeff, coeff), axis=0),
    b_ub=np.concatenate((-beta, 1.1 * beta), axis=0),
    method="simplex",
)

B = RESULT_b.x
(v,) = B.nonzero()
REST = Al.iloc[v, :]
print(REST)
QTE = pd.DataFrame({"Quantités en g": 100 * B[B.nonzero()]}).set_index(
    Al.iloc[v, :].index
)
print(QTE)

# Coût du repas
print(RESULT_b.fun)