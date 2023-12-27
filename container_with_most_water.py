

def container(heights):
    maximum=0
    for i in range(len(heights)-1):
        width1 = heights.index(heights[i]) + 1
        height1=heights[i]
        for j in range(i+1,len(heights)):
            width2=heights.index(heights[j]) + 1
            height2 = heights[i]
            area=(width2-width1)*(height2-height1)
            if area > maximum:
                maximum = area
                print(maximum)
    return maximum


print(container([1,8,6,5,4,3,7]))

