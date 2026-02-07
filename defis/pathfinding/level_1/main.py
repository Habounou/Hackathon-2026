"""
NIVEAU 1 : Trouver un Chemin
==============================
Objectif : Trouver n'importe quel chemin du départ S à l'arrivée E
Stamina : Illimité
"""

from pathlib import Path
from ressources.gui import test

# Charger le labyrinthe
inputMaze = Path('ressources/assets/maze.txt').read_text().strip('\n')

# Votre solution : séquence de mouvements (U/D/L/R)
mySolution = "VOTRE_SOLUTION_ICI"

# ============================================
# TEST
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("NIVEAU 1 : Trouver un Chemin")
    print("=" * 50)
    
    # Test rapide
    result = test(maze=inputMaze, moves=mySolution, level=1, display=False)
    
    if result:
        print("✅ SUCCÈS !")
    else:
        print("❌ Échec")
    
    # Test avec visualisation
    print("\n🎮 Visualisation...")
    test(maze=inputMaze, moves=mySolution, level=1, delay=200, display=True)
