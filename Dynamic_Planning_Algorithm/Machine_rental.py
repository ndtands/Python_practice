import pandas as pd
import numpy as np
# Start time 
A=[1,4,6,3,13]
B=[2,5,9,12,14]
C=[2,7,2,20,5]
rent = pd.DataFrame({"Start":[1,4,6,3,13], "Stop":[2,5,9,12,14], "Cost":[2,7,2,20,5]})
rent = rent.sort_values(by=['Stop'], ascending=True)
start= rent[['Start']].to_numpy()
stop= rent[['Stop']].to_numpy()
cost= rent[['Cost']].to_numpy()
def Machine_rental(Start,Stop,Cost):
    L=Cost
    n= len(Cost)
    for i in range(0,n):
        for j in range(0,i):
            if(Stop[j]<=Start[i] and L[i]<L[j]+Cost[i]):
                L[i]= L[j]+C[i]
    maximum = 0
    for i in range(n):
        maximum = max(maximum, L[i]) 
    return maximum
print(Machine_rental(start,stop,cost))