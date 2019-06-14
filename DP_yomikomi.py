import numpy as np

Tem_file_name = "./city011/city011_"
Tar_file_name = "./city021/city021_"

def read_file(file_name):
    #array[file][frame][dimention] read file
    list=[]
    for number in range(1,101):
        file_number='%03d' % number
        file_name_number=file_name+file_number+".txt"
        array=(np.loadtxt(file_name_number, skiprows=3, unpack=True)).T
        list.append(array)
        
    return list

def Local_distance(Temp,Targ):
    rootmae=0.0
    Tem_frame,Tem_dime = Temp.shape
    Tar_frame,Tar_dime = Targ.shape

    d=np.empty((Tem_frame,Tar_frame))
    print("tem_gyou=",Tem_frame)
    print("tem_retsu=",Tem_dime)
    print("tar_gyou=",Tar_frame)
    print("tar_retsu=",Tar_dime)
    for i in range(Tem_frame):

        for j in range(Tar_frame):
            rootmae=0.0
            for k in range(Tem_dime):
                rootmae+=((Temp[i][k]-Targ[j][k])**2)
            d[i][j]=np.sqrt(rootmae)
    return d

def DP_matching(d):
    #boundary condition
    gyou,retsu=d.shape
    for i in range(retsu):
        if(i>0):
            d[0][i]=d[0][i-1]+d[0][i]
    for j in range(gyou):
        if(j>0):
            d[j][0]=d[j-1][0]+d[j][0]
    #DP
    for j in range(1,gyou):
            
            for i in range(1,retsu):

                d[j][i]=min([d[j][i-1]+d[j][i],d[j-1][i-1]+(d[j][i])*2,d[j-1][i]+d[j][i]])
    word_distance=(d[gyou-1][retsu-1])/(gyou+retsu)
    return d,word_distance

def accuracy(Temp,Targ):
    for Temp100 in range(100):
        for Targ100 in range(100):
            d=Local_distance(Temp[Temp100],Targ[Targ100])
            d,wd=DP_matching(d)




def main():
    Temp = read_file(Tem_file_name)
    Targ = read_file(Tar_file_name)
    #for file in range (100):
    d=Local_distance(Temp[1],Targ[1])
    d,wd=DP_matching(d)
    i,j=d.shape
    print(d.shape)
    print(wd)

if __name__ == '__main__':
    main() 

