#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2014-09-17 18:25:00 ycopin>

"""
Calcul du PGCD de deux entiers
"""

__author__ = "Adrien Licari <adrien.licari@ens-lyon.fr>"

# Entiers dont on calcule le PGCD
a = 306
b = 756

# Test usuels : les nombres sont bien positifs et a > b
assert a > 0
assert b > 0
if (a < b):
    a, b = b, a                   # Interversion

a0, b0 = a, b                     # On garde une copie des valeurs originales

# On boucle jusqu'à ce que le reste soit nul, d'où la boucle while. Il
# faut etre sur que l'algorithme converge dans tous les cas!
while (b != 0):
    # On remplace a par b et b par le reste de la division euclidienne
    # de a par b
    a, b = b, a % b

print 'Le PGCD de', a0, 'et', b0, 'vaut', a  # On affiche le résultat
# Vérifications
print a0 // a, 'x', a, '=', (a0 // a * a)  # a//b: division euclidienne
print b0 // a, 'x', a, '=', (b0 // a * a)
