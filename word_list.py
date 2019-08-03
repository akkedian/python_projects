import random
import itertools
print("fill the following leave empty if no infprmation")

    
def rand():
    nm=[str(x) for x in input("enter the TARGETS name: \n").split()]
    pn=[str(x) for x in input("enter the target parent's name: \n").split()]
    sn=[str(x) for x in input("enter the spouse's name: \n").split()]
    pe=[str(x) for x in input("enter the pets name: \n").split()]
    mo=[int(x) for x in input("enter the phone no. in format <xxxx x x xxxx>: \n").split()]
    do=[int(x) for x in input("enter the date of birth in fprmat <dd mm yyy>: \n").split()]
    a=input("do you want any other specific words:\n Y es \n N o\n")
    if (a=='y') or(a=='Y'):
        rando=[str(x) for x in input("enter the words seprated by a space:\n").split()]
    else:
        rando=("")
        
        

    #al=itertools.chain(nm,pn,sn,pe,mo,do,rando)
    #list(al)
    al=nm+pn+sn+pe+mo+do+rando
    #print(*al,sep="\n")
    print(str(al))


rand()
'''    z=len(al)
    the_list=[""]
    for x in range(0,z+1):
        for sub in itertools.combinations(al,x):
            the_list.append(sub)
    #print("printing the list:"+str(the_list))
    return the_list


def main():
    
    wr=open('list.txt','w')
    j=str(rand())
    #st=''.join(j)
    #print(st)
    wr.write(j)
    wr.close()
if __name__=='__main__':
    main()


'''
