
import heapq


h = []

def maxUnits(num, boxes, unitSize, unitsPerBox, truckSize):
    h = []
    
    # create maxheap 
    for i in range(len(boxes)):
        units_per_box = unitsPerBox[i]
        heapq.heappush(h, (-units_per_box, boxes[i]))
    
    print(h)
    res = 0   
    while truckSize and h:
        max_units, max_boxes = heapq.heappop(h)
        max_boxes = min(truckSize, max_boxes )
        truckSize -= max_boxes
        res += max_boxes * ( max_units * -1)
    return res
            
# test cases
print(maxUnits(3, [1,2,3], 3, [3,2,1], 3))
print(maxUnits(3, [2,5,3], 3, [3,2,1], 50))
        








"""
num = 3  # number of products
boxes = [1,2,3]    # a litof integers representing the nubme of avilable boxes for products
unitsize = 3 #represents units per box
unitsPerBox = [3, 2, 1] #
trucksize =3        # an integer respresenting the number of boxes the truck can carry
#return the integer that rerprents the max amount of units can carried by the truck
"""

