## this author wishes to acknowledge the
## contributions of darren redmond & karl mahon

## imports required
#import pandas as pandas
#import numpy as numpy
#import csv
from haversine import distance 

## define starting/finishing point
northPole = (90,0)
## set weight limit
weightLimit = 1000
## set sleigh weight
sleighWeight = 10

class Sleigh(object):

    ## load file & strip whitespace
    @staticmethod
    def fileLoader(fileName):
        ## do not read-in header of csv file
        file = open(fileName).readlines()[1:]
        #next(file, None)
        ## lambda is computationally easier
        ## map transforms to a list (because lambda doesn't know it is a list)
        file = map(lambda x:x.strip().split(","), file)
        ## return list of file lines
        return file

    
    ## count number of lines in file
    @staticmethod
    def CountNumberOfLines(fileName):
        file = sleigh.fileLoader(fileName)
        ## return length of file
        return len(file)
    

    ## segment each line of file
    ## parse to floats
    @staticmethod
    def createCoordsList(fileName):
        file = sleigh.fileLoader(fileName)
        giftsList= []
        ## iterate & sub-divide each line
        for line in file:
            strlatitude = line[1]
            latitude = float(strlatitude)
            strlongitude = line[2]
            longitude = float(strlongitude)
            coords = (latitude, longitude)
            ## add coords to end of list
            giftsList.append(coords)
        ## return list of gifts
        return giftsList
        
    
    ## start at north pole
    ## map distance from haversine
    ## pump shortestRoute through reducer -> overallDistance
    @staticmethod
    def shortestRoute(list):
        shortestRoute = map(lambda x: distance(northPole, x), list)
        overallDistance = reduce(lambda x,y: x + y, shortestRoute)
        ## return shortest & overall
        return (shortestRoute, overallDistance)
    
    def shortestPath(currentLocation, places):
        nearestDistance = 20000
        nearestPlace = None
        for place in places:
            placeDistance = distance(currentLocation, place)
            if placeDistance < nearestDistance:
                nearestDistance = placeDistance
                nearestPlace = place
                ## retune nearestPlace & nearestDistance
                return (nearestPlace, nearestDistance)
            

    def routePlanner(currentLocation, places):
        route = []
        overallDistance = 0
        while 0 < len(places):
            the_place = shortestPath(currentLocation, places)
            currentLocation = the_place[0]
            ## add currentLocation to route list
            route.append(currentLocation)
            ## delete currentLocation from places
            places.remove(currentLocation)
            overallDistance += the_place[1]
        ## return route & overallDistance
        return (route, overallDistance)

        
sleigh = Sleigh()        
    
listData = sleigh.fileLoader("gifts.csv")
giftsListData = sleigh.createCoordsList("gifts.csv")
 
routePlanner = sleigh.shortestRoute(giftsListData)
print "Shortest route is: ", routePlanner[1]

