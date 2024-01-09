# Turtles Crossing Game

Ce projet est un jeu "Turtles Crossing" développé en Python utilisant le module Turtle pour créer une interface graphique simple ainsi que la POO.

## Présentation du jeu

"Turtles Crossing" est un jeu où le joueur contrôle une tortue pour traverser une route sans se faire heurter par les voitures. Le joueur remporte le niveau en traversant et en atteignant l'autre côté de la route.

## Contenu du projet

### Fichiers inclus :

- `main.py`: Le fichier principal du jeu qui initialise l'interface graphique, crée les éléments du jeu (joueur, voitures) et gère la logique du jeu.
- `player.py`: Contient la classe Player qui définit les caractéristiques et mouvements du joueur (la tortue).
- `car_manager.py`: Ce fichier contient la classe CarManager qui gère la création et le mouvement des voitures.
- `scoreboard.py`: Définit la classe Scoreboard pour afficher le niveau actuel et gérer la fin du jeu.

### Installation et configuration :
- Python 3.9.6
- Aucune installation de modules supplémentaires n'est nécessaire. Le jeu utilise uniquement le module Turtle intégré à Python.

## Comment jouer ?

Exécutez le fichier `main.py` pour démarrer le jeu.
- Utilisez la touche flèche du "Haut" pour déplacer la tortue vers le haut et traverser la route. Vous pouvez choisir la touche liée à l'exécution de la fonction faisant avancer la tortue en modifiant cette ligne de code:
```python
screen.onkeypress(fun=player.move, key="Up")
```
- Évitez les voitures en mouvement. Si la tortue est touchée, le jeu se termine et affiche "GAME OVER".
- Atteindre l'autre côté de la route augmente le niveau affiché à l'écran.
- Plus le niveau augmente, plus les voitures se déplacent rapidement

## Aperçu de l'Interface

![Game Screenshot](/assets/playground.png)

## Remarques
- Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.
