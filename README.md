# Penning
Une particule dans un piège de Penning : modélisation de sa trajectoire.

## Les différents fichiers
- main.cpp : programme en C++ qui effectue les calculs de la trajectoire et renvoie les positions successives en fonction du temps de la particule dans un fichier penning.res
- display.py : programme Python qui trace la trajectoire dans l'espace à 3 dimensions en fonction du temps.
- 1D_display.py : programme Python qui trace la position en x, y et z de la particule en fonction du temps dans trois graphes différents.
- rk4.cpp et rk4.hpp : fichiers contenant l'implémentation de la fonction RK4 en C++, utilisée par penning.cpp
- launch.sh : exécutable contenant les instructions pour exécuter le programme et afficher les graphes en une seule commande "./launch.sh". 

## Informations d'exécution
Avant d'exécuter le programme, il convient de construire l'exécutable avec la commande "chmod +x launch.sh". Il suffit ensuite de taper "./launch.sh".

## GitHub
Le dépôt GitHub de ce projet se trouve à l'adresse suivante : "https://github.com/gbogopolsky/Penning".

