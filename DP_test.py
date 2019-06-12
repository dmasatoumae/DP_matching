import numpy as np

vec1 = np.array([[1,2,2,2,1,3],[1,3,1,3,2,2],[3,2,2,1,3,2],[1,1,3,1,3,3],[2,3,1,1,2,2]])
print("input_array = ",'\n',vec1)
gyou,retsu=vec1.shape
print("gyou_size=",gyou)
print("retsu_size=",retsu)
#境界条件
for i in range(retsu):
    if(i>0):
        vec1[0][i]=vec1[0][i-1]+vec1[0][i]
for j in range(gyou):
    if(j>0):
        vec1[j][0]=vec1[j-1][0]+vec1[j][0]
#DP
for j in range(1,gyou):
    
    for i in range(1,retsu):

        vec1[j][i]=min([vec1[j][i-1]+vec1[j][i],vec1[j-1][i-1]+(vec1[j][i])*2,vec1[j-1][i]+vec1[j][i]])
print(vec1)
