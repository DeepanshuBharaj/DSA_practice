#return max amount of water container can save
#height=[1,8,6,2,5,4,8,3,2]

# Approach 1 : brute force approach        time-complexity=O(n^2)
def bforce(height:list[int]):
    # initialize max_water named variable as 0 
    max_water = 0 

    best_pair=(0,0)
    best_width = 0 
    
    # **use nested loop to find out every possible container
    for i in range(0,len(height)):
        for j in range(i+1,len(height)):
            # find out width and min height to find area
            width = j-i
            min_height = min(height[i],height[j])

            # calculate area
            area= width*min_height

            # assign indexes to the container with max_water
            if area > max_water:
                max_water = area
                best_pair = (i, j)
                best_width = width
            
    return max_water , best_pair , best_width


height = [1,8,6,2,5,4,8,3,2]
result = bforce(height)
print(result)  # (49, (1, 8))


# Approach 2 : using two pointers (optimal approach)       time-complexity=O(n)
def twoptr(height:list[int])->int:
    left=0
    right=len(height)-1
    max_area=0
    # container = width * ht

    while left<right:
        width=right-left
        ht=min(height[left],height[right])

        current_area=width*ht
        max_area = max(max_area,current_area)

        #  ***imp*** moving the min. one
        if height[left] < height[right]:             
            left +=1

        else :
            right -=1

    return max_area        

height=[1,8,6,2,5,4,8,3,2]
result=twoptr(height)
print(result)