import numpy as np
#import pdb
Tem_file_name = "./city022/city022_"
Tar_file_name = "./city021/city021_"

#array[file][frame][dimention] read file
def read_file(file_name):

    list=[]

    for number in range(1,101):

        file_number='%03d' % number
        file_name_number=file_name+file_number+".txt"
        array=(np.loadtxt(file_name_number, skiprows=3, unpack=True)).T
        list.append(array)
        
    return list

#局所距離を求める
def Local_distance(Temp,Targ):

    #テンプレートとターゲットの最大フレームと次元を保存
    Tem_frame,Tem_dime = Temp.shape
    Tar_frame,Tar_dime = Targ.shape

    #局所距離を入れる配列を初期化
    d=np.empty((Tem_frame,Tar_frame))

    #計算パート
    for i in range(Tem_frame):

        for j in range(Tar_frame):
            rootmae=0.0
            for k in range(Tem_dime):
                rootmae+=((Temp[i][k]-Targ[j][k])**2)
            d[i][j]=np.sqrt(rootmae)
    return d

#局所距離の配列を読み込みDPマッチングする
def DP_matching(d):

    #boundary condition
    #読み込んだ局所距離の行数列数
    gyou,retsu=d.shape

    #境界条件を求める
    for i in range(retsu):
        if(i>0):
            d[0][i]=d[0][i-1]+d[0][i]

    for j in range(gyou):
        if(j>0):
            d[j][0]=d[j-1][0]+d[j][0]
    #DPマッチング
    for j in range(1,gyou):
            for i in range(1,retsu):
                #dに上書きしているがgの行列
                d[j][i]=min([d[j][i-1]+d[j][i],d[j-1][i-1]+(d[j][i])*2,d[j-1][i]+d[j][i]])
    #pdb.set_trace()
    #単語間距離の計算
    word_distance=(d[gyou-1][retsu-1])/(gyou+retsu)

    #return DPマッチング後の行列と単語間距離
    return d,word_distance

#100*100の単語間距離と正解率の出力
def accuracy(Temp,Targ):

    #正解率の初期化
    accuracy=0

    #100*100の単語間距離
    for Temp100 in range(100):

        #bwdはその時最小の値、最小の値を更新する、初期化はてきとうにでかい数
        bwd=1000

        for Targ100 in range(100):

            #局所距離の関数
            d=Local_distance(Temp[Temp100],Targ[Targ100])

            #DPの関数
            g,wd=DP_matching(d)

            #if 今回の単語間距離＜今までで一番小さい単語間距離
            if wd<bwd:

                #一番小さい単語間距離の更新
                handan_num=Targ100
                bwd=wd

        #正解判断
        if handan_num==Temp100:
            accuracy+=1
        else:
            print(Temp100+1,"番、不正解",handan_num+1,"と誤認")

    #正解率を出力
    print("\n","accuracy=",accuracy)
def pinpointTem(TempNumber,Temp,Targ):
    bwd=1000
    for Targ100 in range(100):
        d=Local_distance(Temp[TempNumber],Targ[Targ100])
        g,wd=DP_matching(d)
        if wd<bwd:
            bwd=wd
            handan=Targ100
    print(handan,bwd)

def main():
    Temp = read_file(Tem_file_name)
    Targ = read_file(Tar_file_name)
    print("Template file name = ",Tem_file_name)
    print("Target file name = ",Tar_file_name)
    accuracy(Temp,Targ)

if __name__ == '__main__':
    main() 

