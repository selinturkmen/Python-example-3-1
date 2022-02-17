
def is_magic(X):
    """
    Write your code inside this function.
    """

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
    """
    You can test your is_magic function via the function calls below.
    You can add more tests if you want to, but you do not have to. 
    You will not be graded on what is inside your main() function, but
    make sure that it does not cause a syntax error.
    """
   
    print(is_magic([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print(is_magic([[4, 9, 7], [3, 5], [8, 1, 6]]))
    

    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()