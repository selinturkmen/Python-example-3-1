
def is_magic(X):


    N= len(list(X))
    
    number = 0
    for element in X:
        for i in element:
         number += 1
    if N**2 != number:
        return print("False")
    
    else:
        a=X[0][0]
        b=X[0][1] 
        c=X[0][2]
        s=X[1][0]
        d=X[1][1] 
        f=X[1][2]
        n=X[2][0]
        m=X[2][1] 
        v=X[2][2]
        print(a,b,c)
        print(s,d,f)
        print(n,m,v)
        t= N*(((N**2)+1)/2)
        print("The sum of a row/column/diagonal:")
        return t
 

def main():
   
    print(is_magic([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print(is_magic([[4, 9, 7], [3, 5], [8, 1, 6]]))
    

    
################################################################ 

if __name__ == '__main__':
    main()
