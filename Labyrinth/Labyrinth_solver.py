import json

def formatTiles(fileName : str) -> list:
    file = open(fileName)

    labyrinth_data = json.load(file)
    tiles = labyrinth_data["tiles"]

    formatted_tiles = [
        [tile[0]["a"], tile[0]["r"], tile[0]["c"], tile[1]["type"].split('.')[-1]]
        for tile in tiles
    ]

    start = [labyrinth_data["start"]["a"], labyrinth_data["start"]["r"], labyrinth_data["start"]["c"], "START"]
    end = [labyrinth_data["end"]["a"], labyrinth_data["end"]["r"], labyrinth_data["end"]["c"], "END"]

    for formatted_tile in formatted_tiles:
        if formatted_tile[0] == start[0] and formatted_tile[1] == start[1] and formatted_tile[2] == start[2]:
            formatted_tile[3] = 'START'
        if formatted_tile[0] == end[0] and formatted_tile[1] == end[1] and formatted_tile[2] == end[2]:
            formatted_tile[3] = 'END'

    file.close()
    return formatted_tile

def getAdjacents():

def isVisited():
    
def checkIfEnd() -> bool: