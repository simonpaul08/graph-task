# 1.You have two jugs, a 4-gallon and a 3-gallon. Neither of the jugs has markings on them. There is a pump that can be used to fill the jugs with water. How can you get exactly two gallons of water in the 4 gallon jug? 
# 2. Generalise the problem above so that the parameters to your solution include the sizes of each jug and the final amount of water to be left in the larger jug.

# ---- Solution ----

#  First we will fill the 4 litre jug completely with water. Then optimal approach would be to empty water from 4-litre jug into 3-litre (leaving 1L water in 4L jug and 3L completely full). Hence we got 1L water.

#  Now, Empty water from 3L. Pour the water from 4L jug into 3L jug Now 4L container is completely empty and 1L water in present in 3L litre jug.

# Fill the 4L jug with water completely again. On transferring water from 4L jug to 3L jug, we will get 2L water in 4L jug which was our required quantity. 

# ---- Code ----



from collections import deque
 
 
def BFS(a, b, target):
 
    m = {}
    isSolvable = False
    path = []
 
   
    q = deque()
 
    q.append((0, 0))
 
    while (len(q) > 0):
        u = q.popleft() # already visited
        if ((u[0], u[1]) in m):
            continue
        if ((u[0] > a or u[1] > b or
             u[0] < 0 or u[1] < 0)):
            continue
 
        # Filling the vector for constructing
        # the solution path
        path.append([u[0], u[1]])
 
        # Marking current state as visited
        m[(u[0], u[1])] = 1
 
        # If we reach solution state, put ans=1
        if (u[0] == target or u[1] == target):
            isSolvable = True
 
            if (u[0] == target):
                if (u[1] != 0):
 
                    # Fill final state
                    path.append([u[0], 0])
            else:
                if (u[0] != 0):
 
                    # Fill final state
                    path.append([0, u[1]])
 
            # Print the solution path
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",",
                      path[i][1], ")")
            break
 
        # If we have not reached final state
        # then, start developing intermediate
        # states to reach solution state
        q.append([u[0], b])  # Fill Jug2
        q.append([a, u[1]])  # Fill Jug1
 
        for ap in range(max(a, b) + 1):
 
            # Pour amount ap from Jug2 to Jug1
            c = u[0] + ap
            d = u[1] - ap
 
            # Check if this state is possible or not
            if (c == a or (d == 0 and d >= 0)):
                q.append([c, d])
 
            # Pour amount ap from Jug 1 to Jug2
            c = u[0] - ap
            d = u[1] + ap
 
            # Check if this state is possible or not
            if ((c == 0 and c >= 0) or d == b):
                q.append([c, d])
 
        # Empty Jug2
        q.append([a, 0])
 
        # Empty Jug1
        q.append([0, b])
 
    # No, solution exists if ans=0
    if (not isSolvable):
        print("No solution")
 
 
 
Jug1, Jug2, target = 4, 3, 2
print("Path from initial state "
          "to solution state ::")
 
BFS(Jug1, Jug2, target)