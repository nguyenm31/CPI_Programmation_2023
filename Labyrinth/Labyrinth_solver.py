import json
from collections import deque

def formatTiles(fileName : str) -> list:
    file = open(fileName)

    labyrinth_data = json.load(file)
    tiles = labyrinth_data["tiles"]

    formatted_tiles = [
        [tile[0]["a"], tile[0]["r"], tile[0]["c"], tile[1]["type"].split('.')[-1]]
        for tile in tiles
    ]

    # Start and End points
    start = [labyrinth_data["start"]["a"], labyrinth_data["start"]["r"], labyrinth_data["start"]["c"], "START"]
    end = [labyrinth_data["end"]["a"], labyrinth_data["end"]["r"], labyrinth_data["end"]["c"], "END"]

    # Accessing specific information from the tiles
    for formatted_tile in formatted_tiles:
        if formatted_tile[0] == start[0] and formatted_tile[1] == start[1] and formatted_tile[2] == start[2]:
            formatted_tile[3] = 'START'
        if formatted_tile[0] == end[0] and formatted_tile[1] == end[1] and formatted_tile[2] == end[2]:
            formatted_tile[3] = 'END'

    file.close()
    return formatted_tiles
    
def checkIfEnd(tile : list) -> bool:
    return tile[3] == 'END'
    

def findIndex(a : int, r : int, c : int, tiles : list) -> int:
    for i in range(len(tiles)):
        if tiles[i][0] == a and tiles[i][1] == r and tiles[i][2] == c:
            return i
    return None

def findVisitableNeighbour(tile, labyrinth, visited_tiles):
    a = tile[0]
    r = tile[1]
    c = tile[2]

    # Define the six possible neighbors in hexagonal coordinates
    neighbors = [
        [a, r, c + 1],  # Top-right
        [1 - a, r- (1-a), c+a],      # Right
        [1 - a, r - (1-a), c-(1-a)],  # Bottom-right
        [a, r, c - 1],  # Bottom-left
        [1 - a, r+a, c-(1-a)],      # Left
        [1 - a, r + a, c+a]   # Top-left
    ]

    for n in neighbors:
        for l in labyrinth:
            if l[0] == n[0] and l[1] == n[1] and l[2] == n[2] and l[3] != 'WALL' and l not in visited_tiles: 
                return l
    return None

def getStart(labyrinth : list):
    for tile in labyrinth:
        if tile[3] == 'START':
            return tile
        
def solutionFormat(list : list) -> str:
    strVersion = ''
    for l in list:
        strVersion += str(tuple(l[0:3]))
        strVersion += '\n'
    return strVersion
        

if __name__ == '__main__':
    dificultyPaths = ['/easy', '/intermediate', '/hard', '/extreme']
    pathLabyrinth = './labyrinths'
    pathSolutions = './solutions'
    # labyrinth = formatTiles("./labyrinths/easy/labyrinth_00.json")

    
    def findPath(fileName : str):
        visitedTiles = [] # Contains index in list 'tiles' of visited tiles
        path = deque()
        labyrinth = formatTiles(fileName)

        # def isVisited(index : int) -> bool:
        #     return labyrinth[index] in visitedTiles     
        
        currentTile = getStart(labyrinth)
        visitedTiles.append(currentTile)
        path.append(currentTile)

        while not checkIfEnd(currentTile):
            tileToVisit = findVisitableNeighbour(currentTile, labyrinth, visitedTiles)
            if tileToVisit == None :
                # Rebrousse chemin
                path.pop()
                currentTile = path[-1]
                if currentTile == None:
                    return -1

            else :
                visitedTiles.append(tileToVisit)
                path.append(tileToVisit)
                currentTile = tileToVisit

        return list(path)

    for dificulty in dificultyPaths :
        for level in range(100) :
            levelStr = str(level)
            if level < 10:
                levelStr = '0' + str(level)

            filePath = pathLabyrinth + dificulty + '/labyrinth_' + levelStr + '.json'
            solution = findPath(filePath)

            solutionStr = solutionFormat(solution)
            solutionPath = pathSolutions + dificulty + '/labyrinth_' + levelStr + '.txt'

            with open(solutionPath, 'w') as txt_file:
                txt_file.write(solutionStr)




        

   #  print(solutionFormat(findPath("./labyrinths/easy/labyrinth_00.json")))

    # print('\n\n===============================================\n\n')
    # print(findVisitableNeighbour(labyrinth[2], labyrinth, visitedTiles))

    # print('\n\n===============================================\n\n')
    # print(isVisited(findIndex(1, -1, 1, labyrinth)))
