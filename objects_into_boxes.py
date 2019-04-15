#Yiyang Zhao
#Objects_into_Boxes


def main():
    print ("This program helps you solve distribution problems. ")
    intro()

       
def intro():
    pos_set = {"yes","YES","Yes","Yes.","yes.","YES.","y","Y"}
    neg_set = {"no","NO","No","No.","no.","NO.","n","N"}

    while True:
        try:
            nobj = int(input ("Please input the number of objects. "))
            break
        except ValueError:
            error1()
    while True:
        obj = input("Are the objects distinct? ")
        if obj in pos_set or obj in neg_set:
             break
        elif obj == 'quit':
            quit(intro())
        else:
            error2()
    while True:
        try: 
            nbox = int(input ("Please input the number of boxes. "))
            break
        except ValueError:
            error1()
    while True:
        box = input("Are the boxes distinct? ")
        if box in pos_set or box in neg_set:
            break
        elif box == 'quit':
            quit(intro())
        else:
            error2()
    
    if nobj == 0 or nbox == 0:
        print("There are 0 ways. ")
    else:
        if obj in pos_set and box in pos_set:
            print ("Distributing", nobj, "distinct objects into" ,nbox, "distinct boxes. ")
            d_o_d_b(nobj,nbox)
        elif obj in pos_set and box in neg_set:
            print("Distributing", nobj, "distinct objects into" ,nbox, "identical boxes. ")
            d_o_i_b(nobj,nbox)
        elif obj in neg_set and box in pos_set:
            print("Distributing", nobj, "identical objects into" ,nbox, "distinct boxes. ")
            i_o_d_b(nobj,nbox)
        elif obj in neg_set and box in neg_set:
            print("Distributing", nobj, "identical objects into" ,nbox, "identical boxes. ")
            i_o_i_b(nobj,nbox)


    
def d_o_d_b(nobj,nbox):
    while True:
        res = restrict() 
        if res == '1': 
            ways = nbox**nobj
            result(ways)
        elif res == '2':
            if nobj < nbox:
                ways = 0
                result(ways)
            if nobj == nbox: #n!
                ways = fac(nbox)
                result(ways)
            if nobj > nbox: #(Stirling2)(n!) or P.I.E.
                w1 = stirling(nobj,nbox)
                w2 = fac(nbox)
                ways = w1*w2
                result(ways)   
        elif res == '3':
            dk()
            back()
            return d_o_d_b(nobj, nbox)
        elif res == 'quit':
            quit(intro())
        else:
            uhoh()
            return d_o_d_b(nobj, nbox)
        back()



def d_o_i_b(nobj,nbox):
    while True:
        res = restrict()
        if res == '1': #S(n,1)+S(n,2)+S(n,3)+...+S(n,k)
            ways = 0
            for i in range (nbox):
                ways += stirling(nobj,i+1)
            result(ways)
        elif res == '2':#S(n,k)
            ways = stirling(nobj,nbox)
            result(ways)
        elif res == '3':
            dk()
            back()
            return d_o_i_b(nobj, nbox)
        elif res == 'quit':
            quit(intro())        
        else:
            uhoh()
            return d_o_i_b(nobj, nbox)
        back()
        
def i_o_d_b(nobj,nbox): #Bijection and adding partitions
    while True:
        res = restrict() 
        if res == '1': #(n+r-1, r-1) or (n+r-1,n) #(n,r)=(n!)/((r!)*(n-r)!)
            w1 = fac(nobj+nbox-1)
            w2 = fac(nbox-1)
            w3 = fac(nobj)
            ways  = w1/(w2*w3)
            result(ways)
        elif res == '2': #(n-r+r-1, r-1)=(n-1,r-1)
            w1 = fac(nobj-1)
            w2 = fac(nbox-1)
            w3 = fac(nobj-nbox)
            ways  = w1/(w2*w3)
            result(ways)       
        elif res == '3':
            dk()
            back()
            return i_o_d_b(nobj, nbox)            
        elif res == 'quit':
            quit(intro())
        else:
            uhoh()
            return i_o_d_b(nobj, nbox)
        back()

        
def i_o_i_b(nobj,nbox): #Counting #Method of Exhausion
    while True:
        res = restrict() 
        if res == '1': 
            ways = count(nobj,0,nbox)
            result(ways)
        elif res == '2':
            ways = count(nobj,1,nbox)
            result(ways)
        elif res == '3':
            try:
                x = int(input("At least x objects in each box. Pleas input x. ")) 
                ways = count(nobj,x,nbox)
                result(ways)
            except ValueError:
                dk()
                back()
                return i_o_i_b(nobj, nbox)
        elif res == 'quit':
            quit(intro())            
        else:
            uhoh()
            return i_o_i_b(nobj, nbox)  
        back()


def error1():
    print("Oops! That was not a valid number. Try again...")

def error2():
    print("Oops! Please answer yes or no.")
    
def restrict():
    return str(input("Any restriction? \n1.No \n2.No empty boxes \n3.Other \n"))

def stirling(a,b): #S(n,k) = S(n-1,k-1)+kS(n-1,k)
    if a <= 0 or b <= 0:
        return 0
    elif b == 1:
        return 1
    elif b == 2:
        return 2**(a-1)-1
    elif a == b:
        return 1
    else:
        return stirling(a-1,b-1)+b*(stirling(a-1,b))

def fac(x):
    w = 1
    for i in range (x):
        w = w*(i+1)
    return w
    
def count(a,pre,b):
    if a < pre:
        return 0
    if b == 1:
        return 1
    result = 0
    for i in range(pre,a+1):
        result += count(a-i,i,b-1)
    return result

def result(x):
    if int(x) == 1:
        print("There is only 1 way.")        
    else: 
        print("There are %.d ways. " %x)

def dk():
    print ("Sorry >< I don't know how to do. Can you teach me?")

def uhoh():
    print("Uh-oh!")
    
def back():
    while True:
        ret = str(input("Enter '-' to return to re-input restriction. \nEnter '#' to return to the main menu. \nQuit if otherwise. "))
        if ret == '#':
            quit(intro())
        elif ret == '-':
            break
        else:
            print ("Hope I have helped you :)")
            quit()
        break


    
main()

