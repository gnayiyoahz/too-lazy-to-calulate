def findcp():
    
    print ('This program is to find the cross product of 2 vectors in the form of (a,b,c). ')
    v = eval(input('Please input the first vector. '))
    u = eval(input('Please input the second vector. '))

    cp = []
    cp.extend( (v[1]*u[2]-v[2]*u[1],-v[0]*u[2]+v[2]*u[0],v[0]*u[1]-v[1]*u[0]) )
    print (tuple(cp))

findcp ()
