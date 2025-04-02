def carFleet(target, position, speed):

    x = len(position)
    result = {}

    for i in range(x):
        fleet = (target-position[i])//speed[i]
        if fleet in result:
            result[fleet] += 1
        else:
            result[fleet] = 1

    print(result)
    return len(result)

target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]
 

print(carFleet(target , position , speed))