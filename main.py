# =================================  TESTY  ===================================
# Testy do tego pliku zostały podzielone na dwie kategorie:
#
#  1. `..._invalid_input`:
#     - Sprawdzające poprawną obsługę nieprawidłowych danych wejściowych.
#
#  2. `..._correct_solution`:
#     - Weryfikujące poprawność wyników dla prawidłowych danych wejściowych.
# =============================================================================
import numpy as np
import numpy.polynomial.polynomial as nppoly
import math


def roots_20(coef: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    if type(coef)==np.ndarray and coef.ndim==1: 
        noise = np.random.random_sample(np.size(coef))
        coef_add=coef+(noise*1e-10)
        roots=nppoly.polyroots(coef_add)
        return coef_add, roots   
    else:
        return None
"""Funkcja wyznaczająca miejsca zerowe wielomianu funkcją
    `nppoly.polyroots()`, najpierw lekko zaburzając wejściowe współczynniki 
    wielomianu (N(0,1) * 1e-10).

    Args:
        coef (np.ndarray): Wektor współczynników wielomianu (n,).

    Returns:
        (tuple[np.ndarray, np. ndarray]):
            - Zaburzony wektor współczynników (n,),
            - Wektor miejsc zerowych (m,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
 

def frob_a(coef: np.ndarray) -> np.ndarray | None:
    if type(coef)==np.ndarray and coef.ndim==1 and len(coef)>1: 
        m=len(coef)
        last=coef[m-1]
        row=[]
        for i in range (0,m-1):
            row.append(-(coef[i]/last))   
        print(row)
        A=np.zeros((m-2,m-1))
        np.fill_diagonal(A[:, 1:], 1)
        A_new = np.vstack([A, row])
        return A_new
    else:
        return None


"""Funkcja służąca do wyznaczenia macierzy Frobeniusa na podstawie
    współczynników jej wielomianu charakterystycznego:
    w(x) = a_n*x^n + a_{n-1}*x^{n-1} + ... + a_2*x^2 + a_1*x + a_0

    Testy wymagają poniższej definicji macierzy Frobeniusa (implementacja dla 
    innych postaci nie jest zabroniona):
    F = [[       0,        1,        0,   ...,            0],
         [       0,        0,        1,   ...,            0],
         [       0,        0,        0,   ...,            0],
         [     ...,      ...,      ...,   ...,          ...],
         [-a_0/a_n, -a_1/a_n, -a_2/a_n,   ..., -a_{n-1}/a_n]]

    Args:
        coef (np.narray): Wektor współczynników wielomianu (n,).

    Returns:
        (np.ndarray): Macierz Frobeniusa o rozmiarze (n,n).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """

def is_nonsingular(A: np.ndarray) -> bool | None:
    if type(A)==np.ndarray and A.ndim==2 and A.shape[0]==A.shape[1]:
        if np.linalg.det(A) !=0:
            return True 
        else:
            return False

    else:
        return None
    """Funkcja sprawdzająca czy podana macierz NIE JEST singularna. Przy
    implementacji należy pamiętać o definicji zera maszynowego.

    Args:
        A (np.ndarray): Macierz (n,n) do przetestowania.

    Returns:
        (bool): `True`, jeżeli macierz A nie jest singularna, w przeciwnym 
            wypadku `False`.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    pass
