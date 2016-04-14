import unittest

from sleigh import *
from haversine import distance

fileName = "gifts.csv"

northPole = (90, 0)
southPole = (-90, 0)

class TestSleigh(unittest.TestCase):
    
    def setUp(self):
        self.sleigh = Sleigh()
        
        listData = sleigh.fileLoader(fileName)
        giftsListData = sleigh.createCoordsList(fileName)

    ## test fileLoader function
    def test_fileLoader(self):
        self.assertFalse(0, self.sleigh.fileLoader(fileName))
    
    ## test CountNumberOfLines function
    def test_CountNumberOfLines(self):
        self.assertEquals(100000, self.sleigh.CountNumberOfLines(fileName))
    
    ## test createCoordsList function
    def test_createCoordsList(self):
        self.assertEquals(100000, len(self.sleigh.createCoordsList(fileName)))
    
    ## test shortestRoute function
    def test_shortestRoute(self):
        self.assertFalse([], self.sleigh.shortestRoute(giftsListData))
    
    ## test shortestPath function
    def test_shortestPath(self):
        self.assertFalse(0, self.sleigh.shortestPath)
    
    ## test routePlanner function
    def test_routePlanner(self):
        self.assertFalse([], self.sleigh.shortestRoute(giftsListData))
        
    ## test haversine distance function
    def test_routePlanner(self):
        self.assertAlmostEqual(20015.086796, distance(northPole, southPole))
    
              
if __name__ == '__main__':
    unittest.main()