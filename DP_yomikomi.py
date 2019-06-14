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
                


def main():
    Temp = read_file(Tem_file_name)
    Targ = read_file(Tar_file_name)
    print(Targ[2][0][1])
    #for file in range (100):
    d=Local_distance(Temp[1],Targ[1])
    print(d.shape)
    print(d)

if __name__ == '__main__':
    main() 

