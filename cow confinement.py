class Cow(object):
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def print(self):
        print('x:', self.x, 'y:', self.y)

    def isReachable(self, flower):
        if self.x <= flower.x and self.y <= flower.y:
            isReachable = True
        else:
            isReachable = False
        return isReachable

class Flower(object):
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def print(self):
        print('x:', self.x, 'y:', self.y)

class Fence(object):
    def __init__(self, coordinates):
        self.x1 = coordinates[0]
        self.y1 = coordinates[1]
        self.x2 = coordinates[2]
        self.y2 = coordinates[3]
        self.x3 = self.x1
        self.y3 = self.y2
        self.x4 = self.x2
        self.y4 = self.y1

    def print(self):
        print('x1:', self.x1, 'y1:', self.y1, 'x2:', self.x1, 'y2:', self.y1)

class Field(object):
    def __init__(self, cows, flowers, fences):
        self.cows = cows
        self.flowers = flowers
        self.fences = fences
        self.n = len(self.cows)
        self.m = len(self.flowers)
        self.f = len(self.fences)

    def isInside(self, obj, fence):
        isInside = False
        if (obj.x >= fence.x1 and obj.y >= fence.y1) and (obj.x <= fence.x2 and obj.y <= fence.y2):
            isInside = True
        return isInside

    def isReachable(self, cow, flower):
        isReachable = False
        if cow.x <= flower.x and cow.y <= flower.y:
            isReachable = True
            i = 0
            while i < self.f:
                fence = self.fences[i]
                isInsideCow = self.isInside(cow, fence)
                isInsideFence = self.isInside(flower, fence)
                if isInsideCow == True and isInsideFence == False:
                    isReachable = False
                    break
                elif isInsideCow == False and isInsideFence == True:
                    isReachable = False
                    break
                elif (cow.x >= fence.x1 and flower.x <= fence.x2) and (cow.y < fence.y1 and flower.y > fence.y2):
                    isReachable = False
                    break
                elif (cow.x < fence.x1 and flower.x > fence.x2) and (cow.y >= fence.y1 and flower.y <= fence.y2):
                    isReachable = False
                    break
                else:
                    pass
                i += 1
        return isReachable

    
##cow1 = Cow([5, 6])
##cow2 = Cow(12, 9)
##flower1 = Flower([7, 4])
##flower2 = Flower([7, 8])
##flower3 = Flower([7, 12])
##fence1 = Fence([2, 2, 3, 4])
##fence2 = Fence([6, 11, 8, 13])


import time
start = time.time()

##numberOfElements = [0, 0, 0]
fences, flowers, cows = [], [], []
i = 0
with open('testdata.txt', 'r') as file:
    while 1:
        line = file.readline()
        if line == '':
            break
        line = line.strip('\n')
        line = line.split(' ')
        coordinates = [int(coord) for coord in line]
        if len(line) == 1:
##            numberOfElements[i] = int(line[0])
            if i == 0:
                mode = 'fences'
            elif i == 1:
                mode = 'flowers'
            elif i == 2:
                mode = 'cows'
            i += 1
        else:
            if mode == 'fences':
                fence = Fence(coordinates)
                fences.append(fence)
            elif mode == 'flowers':
                flower = Flower(coordinates)
                flowers.append(flower)
            elif mode == 'cows':
                cow = Cow(coordinates)
                cows.append(cow)



field = Field(cows, flowers, fences)
reachables = dict.fromkeys(cows, 0)
for cow in field.cows:
    for flower in field.flowers:
        if field.isReachable(cow, flower) == True:
            reachables[cow] += 1
##            print('---------')
##            cow.print()
##            flower.print()

##print(reachables)
for key, value in reachables.items():
    print(value)

end = time.time()
print(end - start)
