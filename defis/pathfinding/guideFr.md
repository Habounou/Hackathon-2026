# Guide du Défi Labyrinthe

## Niveau 1 : Trouver un Chemin
- Trouver n'importe quel chemin de S à E
- Éviter les murs (#)
- **Stamina :** Illimité
- **Objectif :** Atteindre simplement la fin (n'importe quel chemin fonctionne)

## Niveau 2 : Navigation de Base
- Trouver un chemin de S à E
- Éviter les murs (#)
- **Stamina :** 77
- **Objectif :** Aller du début à la fin avec le 'stamina' donné

## Niveau 3 : Coûts de Terrain
- `.` sol = 1 stamina
- `~` eau = 200 stamina
- `X` boue = 30000 stamina
- **Stamina :** 93 513
- **Objectif :** Aller du début à la fin avec le 'stamina' donné

## Niveau 4 : Portails
- Tous les mécaniques du Niveau 3
- `P` portail vous téléporte : (x,y) → (y,x)
- **Stamina :** 61 490
- **Objectif :** Aller du début à la fin avec le 'stamina' donné

## Niveau 5 : Points de Contrôle
- Tous les mécanismes des Niveaux 3 & 4
- Points de contrôle `C`
- **Objectif :** Chemin optimal du début à la fin en passant par les points de contrôle

---

**Mouvements :** `U` (haut), `D` (bas), `L` (gauche), `R` (droite)

**Soumettre :** Suite de mouvements sous forme de chaîne, ex. `"RRDDLLUURR"`

---

## Tester Votre Solution

Utilisez la fonction `test()` dans `ressources/gui.py` pour valider vos mouvements :

```python
from ressources.gui import test

# Test sans affichage (validation rapide)
result = test(maze=INPUT_MAZE, moves="RRDDLLUURR", level=1, delay=0, display=False)
print(result)  # True si réussi, False sinon

# Test avec affichage (retour visuel, sons et stamina)
# Quand display=True, gardez delay > 0 pour la lisibilité (ex. 200-500ms)
# Sinon (display=False), gardez delay=0 pour les tests rapides
result = test(maze=INPUT_MAZE, moves="RRDDLLUURR", level=1, delay=200, display=True)
```

**Paramètres :**
- `maze`: Disposition du labyrinthe (chaîne)
- `moves`: Séquence de mouvements (chaîne de U/D/L/R)
- `level`: Numéro du niveau (1–5)
- `delay`: Millisecondes entre les étapes (0 sans affichage, 200–500 avec affichage)
- `display`: False pour sans affichage, True pour visualisation pygame avec HUD et sons

**Retour :** `True` si toutes les conditions sont remplies (fin atteinte, stamina ≥ 0, coût ≤ limite, points de contrôle visités), `False` sinon

---

## Commandes du Mode Affichage Interactif

Quand `display=True`, vous pouvez également **contrôler le robot avec votre clavier** :

- **Touches Fléchées :** Déplacer haut, bas, gauche, droite (↑ ↓ ← →)
- **Touche B :** Annuler le dernier mouvement
- Cela vous permet d'explorer et résoudre de manière interactive dans la fenêtre d'affichage
