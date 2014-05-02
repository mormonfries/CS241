import math
from priorityqueue import PriorityQueue

LAT_COST = 10
DIAG_COST = 14

class MapTile (object):

    def __init__(self, coords, g, h, terrain, parent):
        self.coords = coords
        self.g = g
        self.h = h
        self.terrain = terrain
        self.parent = parent

    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.f() < other.f()

    def locatedAt(self, coords):
        return self.coords[0] == coords[0] and self.coords[1] == coords[1]


def mandistance(start, end):
    """ manhattan distance from start to end """
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

def terraintype(mapdata, width, height, coords):
    return mapdata[coords[0] + coords[1]*width]

def north ( cur ):
    return [cur[0], cur[1] - 1]

def south ( cur ):
    return [cur[0], cur[1] + 1]

def east ( cur ):
    return [cur[0] + 1, cur[1]]

def west ( cur ):
    return [cur[0] - 1, cur[1]]

def northwest(cur):
    return [cur[0] - 1, cur[1] - 1]

def northeast(cur):
    return [cur[0] + 1, cur[1] - 1]

def southwest(cur):
    return [cur[0] - 1, cur[1] + 1]

def southeast(cur):
    return [cur[0] + 1, cur[1] + 1]

def onMap( cur, width, height):
    if cur[0] >= 0 and cur[0] < width and cur[1] >= 0 and cur[1] < height:
        return True
    else:
        return False

def find(mapdata, width, height, start, end):
    """ mapdata is a one-dimensional list of values, start and end are vectors of size 2 """
    # WRITE THIS FUNCTION

    open = PriorityQueue()
    closed = []
    curTile = MapTile(start, None, None, None, None)
    print(width, height, start, end)

    while curTile.coords != end:
        if onMap(curTile.coords, width, height):
            n = north(curTile.coords)
            nter = terraintype(mapdata, width, height, n)
            ntile = MapTile(n, LAT_COST, mandistance(n, end), nter, curTile)
            if nter and (ntile not in closed):
                print(ntile)
                open.insert(ntile)

            s = south(curTile.coords)
            ster = terraintype(mapdata, width, height, s)
            stile = MapTile(s, LAT_COST, mandistance(s, end), ster, curTile)
            if ster and (stile not in closed):
                print(stile)
                open.insert(stile)

            e = east(curTile.coords)
            eter = terraintype(mapdata, width, height, e)
            etile = MapTile(e, LAT_COST, mandistance(e, end), eter, curTile)
            if eter and (etile not in closed):
                print(etile)
                open.insert(etile)

            w = west(curTile.coords)
            wter = terraintype(mapdata, width, height, w)
            wtile = MapTile(w, LAT_COST, mandistance(w, end), wter, curTile)
            if wter and (wtile not in closed):
                print(wtile)
                open.insert(wtile)

            nw = northwest(curTile.coords)
            nwter = terraintype(mapdata, width, height, nw)
            nwtile = MapTile(nw, DIAG_COST, mandistance(nw, end), nwter, curTile)
            if nwter and (nwtile not in closed):
                print(nwtile)
                open.insert(nwtile)

            ne = northeast(curTile.coords)
            neter = terraintype(mapdata, width, height, ne)
            netile =  MapTile(ne, DIAG_COST, mandistance(ne, end), neter, curTile)
            if neter and (netile not in closed):
                print(netile)
                open.insert(netile)

            sw = southwest(curTile.coords)
            swter = terraintype(mapdata, width, height, sw)
            swtile = MapTile(sw, DIAG_COST, mandistance(sw, end), swter, curTile)
            if swter and (swtile not in closed):
                print(swtile)
                open.insert(swtile)

            se = southeast(curTile.coords)
            seter = terraintype(mapdata, width, height, se)
            setile = MapTile(se, DIAG_COST, mandistance(se, end), seter, curTile)
            if seter and (setile not in closed):
                print(setile)
                open.insert(setile)

        closed.append(curTile)
        print(open)
        curTile = open.remove()

    path = []
    if curTile.coords == end:
        while curTile.parent is not None:
            path.append(curTile.parent)
            curTile = curTile.parent
        print(path)