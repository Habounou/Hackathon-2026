# Tile properties per level
TILES = {
    '#': {
        'name': 'wall',
        'cost': float('inf'),
        'levels': [1, 2, 3, 4, 5]
    },
    '.': {
        'name': 'ground',
        'cost': 1,
        'levels': [1, 2, 3, 4, 5]
    },
    '~': {
        'name': 'water',
        'cost': 200,
        'levels': [3, 4, 5]
    },
    'X': {
        'name': 'mud',
        'cost': 30000,
        'levels': [3, 4, 5]
    },
    'P': {
        'name': 'portal',
        'cost': 1,  # base cost, destination terrain added
        'teleports': True,
        'levels': [4, 5]
    },
    'C': {
        'name': 'checkpoint',
        'cost': 1,
        'levels': [5]
    },
    'S': {
        'name': 'start',
        'cost': 1,
        'levels': [1, 2, 3, 4, 5]
    },
    'E': {
        'name': 'end',
        'cost': 1,
        'levels': [1, 2, 3, 4, 5]
    }
}



# Rendering rules per level
def getDisplayChar(char, level):
    """Returns what character to display based on level"""
    if char not in TILES:
        return char
    return char

# Terrain cost per level
def getFieldCost(char, level):
    """Returns movement cost for a tile at given level"""
    if level <= 2:
        # Level 1 & 2: all terrain costs 1 (walls still block)
        return 1 if char != '#' else float('inf')
    return TILES.get(char, {}).get('cost', 1)

def getName(char):
    """Returns the name of a tile character"""
    return TILES.get(char, {}).get('name', 'unknown')