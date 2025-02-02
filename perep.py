f = open('perepis.txt', 'r')
k=0
chislo1=int(input())
chislo2=int(input())
for i in f:
    a=i.split()
    data=a[3].split('.')
    if int(data[2])<1978:
        print(int(data[2]), a[0])
        k+=1
print(k)



f.close()