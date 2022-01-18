#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input("Enter a number:"))
        
def KnightTour(n):
    solution = [[-1 for i in range(n)]for i in range(n)]
    solution[0][0] = 0
    x_update = [2,1,-1,-2,-2,-1,1,2]
    y_update = [1,2,2,1,-1,-2,-2,-1]
    pos = 1
    if(not ktsolution(n,solution,pos,x_update,y_update,0,0)):
        print("No solution")
    else:
        printsolution(n,solution)
        
def ktsolution(n,solution,pos,x_update,y_update,x,y):
    if (pos == n ** 2):
        return True
    
    for i in range(8):
        curr_x = x + x_update[i]
        curr_y = y + y_update[i]
        if issafe(curr_x,curr_y,solution):
            solution[curr_x][curr_y] = pos
            if(ktsolution(n,solution,pos+1,x_update,y_update,curr_x,curr_y)):
                return True
            
            solution[curr_x][curr_y] = -1
    return False

def printsolution(n,solution):
    for i in range(n):
        for j in range(n):
            print(solution[i][j], end=' ')
        print()
    return False

def issafe(x,y,solution):
    if x>=0 and y>=0 and x<n and y<n and solution[x][y] == -1:
        return True
    else:
        return False
    
if __name__ == "__main__":
    KnightTour(n)


# In[ ]:





# In[ ]:




