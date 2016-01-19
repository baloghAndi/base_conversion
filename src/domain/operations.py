
def equalize(op1,op2):
    """
    equalizez the size of the two lists by inserting zeros in the front
    pre:op1 op2 must be lists
    returns the two list
    """
    nr_op1=len(op1)
    nr_op2=len(op2)
    if nr_op1 > nr_op2 :
        for i in range(0,nr_op1-nr_op2):
            op2.insert(i,0)
    if nr_op2 > nr_op1 :
        for i in range(0,nr_op2-nr_op1):
            op1.insert(i,0)
    return op1,op2
            
def add(base,op1,op2):
    """
    performs the addition of two numbers in the given base
    pre:op1 op2 must be lists
    performs the operation digit by digit holdin in the variable carry the carry number
    returns a list of digits
    """
    rez=[]
    carry=0
    equalize(op1,op2)
    nr_op1=len(op1)
    nr_op2=len(op2)
    while ( nr_op1> 0) or (nr_op2> 0):
        nr=op1[nr_op1-1] + op2[nr_op2-1] + carry
        carry=0
        if nr >= base:
            rez.append((nr % base))
            carry=nr/ base
        else:
            rez.append(nr)
        nr_op1= nr_op1-1
        nr_op2= nr_op2-1
        if ( nr_op1 ==0) and ( nr_op2==0) and (carry<>0):
            rez.append(carry)
    rez.reverse()
    return rez

def test_add():

    assert(add(4,[2,3],[1]))==[3,0]
    assert(add(2,[1,1],[1]))==[1,0,0]
    assert(add(8,[1,2,3,4],[0]))==[1,2,3,4]
    assert(add(5,[3,4,2,4],[3,4,2,3,2]))==[4,3,2,1,1]
    assert(add(4,[1,2,3],[3,2]))==[2,2,1]
    assert(add(2,[1],[1]))==[1,0]
    assert(add(16,[9],[6]))==[15]
test_add()

def sub(base,op1,op2):
    """
    performs the subtraction of two numbers in the given base
    pre:op1 op2 must be lists, op1>=op2
    performs the operation digit by digit subtracting from the previous digits at the moment
    returns a list of digits
    """
    base=int(base)
    rez=[]
    equalize(op1,op2)
    nr_op1=len(op1)
    nr_op2=len(op2)
    while ( nr_op1> 0) or (nr_op2> 0):
        if op1[ nr_op1-1]>= op2[ nr_op2-1]:
            rez.append(op1[ nr_op1-1]-op2[ nr_op2-1])
        else:
            back=1
            ok=False
            while ok<>True:
                if op1[nr_op1-1-back]==0:
                    op1[nr_op1-1-back]=base-1
                else:
                    op1[nr_op1-1-back]=op1[nr_op1-1-back]-1
                    ok=True
                back=back+1
            rez.append(base+op1[ nr_op1-1]-op2[ nr_op2-1])
        nr_op1= nr_op1-1
        nr_op2= nr_op2-1  
    rez.reverse()
    return rez

def test_sub():
    assert(sub(8,[1,2,3,4],[0]))==[1,2,3,4]
    assert(sub(3,[1,1,2],[2,1]))==[0,2,1]
    assert(sub(5,[3,4,2,3,2],[3,4,2,4]))==[3,0,3,0,3]
    assert(sub(3,[1,0,0],[2]))==[0,2,1]
    assert(sub(10,[1,0,0],[9]))==[0,9,1]
    assert(sub(16,[10,9,1],[9]))==[10,8,8]
test_sub()


def mul_1digit(base,op1,op2):
    """
    multiplies a number with one digit in a given base
    pre: op2 must be lists, len(op2) must be 1
    performs the operation digit by digit
    returns a list of digits
    """
    base=int(base)
    rez=[]
    carry=0
    nr_op1=len(op1)
    if len(op2)<>1:
        raise ValueError("Can only multiply with one digit")
    while nr_op1>0:
        nr=op1[nr_op1-1] * op2[0] + carry
        carry=0
        if  nr>= base:# and ((nr/base)*10 + nr % base )>=base:
            if nr%base<base:
                rez.append(nr)
            else:
                rez.append((nr % base))
            carry=nr/base
        else:
            rez.append(nr)
        nr_op1= nr_op1-1
        if ( nr_op1 ==0) and (carry<>0):
            rez.append(carry)
    rez.reverse()
    return rez

def test_mul_1():
    print mul_1digit(10,[9],[2])
    assert (mul_1digit(10,[9],[2]))==[1,8]
test_mul_1()

def mul(base,op1,op2):
    """
    multiplies two numbers in a given base,using the add and the mul_1digit functions
    pre:op2 must be lists
    returns a list of digits
    """
    base=int(base)
    nr_op2=len(op2)
    if nr_op2 ==1 :
        return  mul_1digit(base,op1,op2)
    else:    
        h=1
        final=[]
        times=0
        while nr_op2 > 0:
            digit=[op2[nr_op2-1]]
            rez=mul_1digit(base,op1,digit)
            for t in range(0,times):
                rez.append(0)
            times=times+1
            if nr_op2<>len(op2):
                final=(add(base,rez,final)) 
            else:
                final=rez
            nr_op2=nr_op2-1
        return final    

def test_mul():
    assert(mul(5,[2,3,4],[1]))==[2,3,4]
    assert(mul(3,[1,2,2,1],[0]))==[0,0,0,0]
    assert(mul(3,[1,2,1],[2]))==[1,0,1,2]
    assert(mul(7,[1,4,5],[3,1]))==[5,1,5,5]
    assert(mul(2,[1,0],[1,0]))==[1,0,0]
    assert(mul(10,[1,9],[1,0]))==[1,9,0]
    #assert(mul(16,[1,9,9],[10,9]))==[1,0,15,0,1]
#test_mul()


def div(base,op1,op2):
    """
    divides  a number with one digit in a given base
    pre: op1,op2 must be lists, len(op2) must be 1, op2 can not be 0
    performs the operation digit by digit, carry memorizes the remainder
    returns a list of digits, and the remainder
    """
    base=int(base)
    if len(op2)<>1 or op2[0]==0:
        raise ValueError("Can only divide with one digit")
    rez=[]
    nr_op1=0
    carry=0
    if len(op1)==1:
        return [[op1[0]/op2[0]], op1[0]%op2[0]]
    while nr_op1 < len(op1)-1:
        if nr_op1==0:
            rez.append(op1[0] / op2[0])
            carry=op1[0] % op2[0]
        if nr_op1==len(op1)-1:
            rez.append((carry*base+op1[nr_op1]) / op2[0])
        else:
            rez.append((carry*base+op1[nr_op1+1]) / op2[0])
            carry=(carry*base+op1[nr_op1+1]) % op2[0]
        nr_op1=nr_op1+1
    return [rez,carry]            
        
def test_div():
    assert div(14,[10],[2])==[[5], 0]
    assert(div(10,[1,2,6],[1]))==[[1,2,6],0]
    assert (div(7,[3,2,4,6],[5]))==[[0,4,5,1],1]
    assert(div(5,[3,4,2,1],[1]))==[[3,4,2,1], 0]
    assert(div(2,[2,2],[2]))==[[1, 1], 0]
    assert(div(5,[3,3],[3]))==[[1, 1], 0]
    assert(div(9,[8,6,1],[5]))==[[1,6,5],3]

#test_div()

def raise_power(base,op,power):
    """
    Raises a number to a givem power in  given base,using successiv multiplication
    pre: op must be a list
    returns a list containing the digits from the result
    """
    base=int(base)
    rez=op
    if power==0:
        rez=[1]
    else:
        for times in range(1,power):
            rez=mul(base,rez,op)
    return rez

def test_power():
    assert(raise_power(3,[2],3))==[2,2]
    assert(raise_power(6,[1,2],3))==[2,2,1,2]
    assert(raise_power(4,[1,2,3],0))==[1]
    assert(raise_power(7,[1,5,6],1))==[1,5,6]
    assert(raise_power(2,[1,0],2))==[1,0,0]
    assert(raise_power(3,[2],0))==[1]
#test_power()
        