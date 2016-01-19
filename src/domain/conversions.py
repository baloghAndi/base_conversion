from operations import *
def substitution(source,dest,number):
    """
    Converts a number using substitution method
    Works with lists of digits, returns the list of digits converted
    pre condition: source base must be smaller than destination base
    """
    if source>=dest:
        raise ValueError("Using this methos source base must be smaller than destination base")
    rez=[]
    p=0
    final=[]
    x=0
    nr=len(number)
    while nr>0:
        base=raise_power(dest,[source],p)
        rez.append(mul(dest,base,[number[nr-1]]))
        nr=nr-1
        p=p+1
    for el in rez:
        final=add(dest,el,final)
    return final

def test_substitution():
    assert(substitution(2,3,[1,1,0]))==[2,0]
    assert(substitution(3,7,[2,1,0,1]))==[1,2,1]
    assert(substitution(7,9,[2,3,4,5]))==[1,1,6,2]   
test_substitution()

def create_number(number):
    """
    Gets a list of digits
    Returns the number built by the digits
    """
    num=0
    nr=[]
    h=10
    for digit in number:
        if digit<10:
            nr.append(digit)
        else:
            for d in str(digit):
                nr.append(int(d))
    for digit in nr:
        if digit == 0:
            num=num*10
        else:
            num=num*10+digit
    return num


def successiv(source,dest,number):
    """
    Converst a number using successiv division
    pre: source base must be smaller than destination base
    divides each digit using the div fnction from operation module
    returns a list containing the converted digits in the right order
    """
    if source<=dest:
        raise ValueError("Using this methos source base must be greater than destination base")
    rez=[]
    ok=False
    quotient=number
    while ok==False:
        rez.append(div(source,number,[dest])[1])
        number=div(source,number,[dest])[0]
        nr=create_number(number)
        if nr==0:
            ok=True
    rez.reverse()
    return rez

def test_successiv():
        assert (successiv(9,5,[8,6,1]))==[1,0,3,0,3]
        assert(successiv(7,3,[3,4,5,6]))==[1,2,0,1,2,2,0]
        assert(successiv(14,4,[10]))==[2,2]
test_successiv()


def intermediate(source,inter,dest,number):
    """
    Converts a number using an intermediate base
    uses the previous converesions, so there is no restriction which base should be the greater one
    returns a list containing the converted digits in the right order
    """
    if source>inter:
        nr=successiv(source,inter,number)
        if inter>dest:
            number=successiv(inter,dest,nr)
        else:
            number=substitution(inter,dest,nr)
    else:
        nr=substitution(source,inter,number)
        if inter>dest:
            number=successiv(inter,dest,nr)
        else:
            number=substitution(inter,dest,nr)
    return number

def test_intermediate():
    assert(intermediate(9,10,5,[8,6,1]))==[1,0,3,0,3]
    assert(intermediate(3,4,7,[2,1,0,1]))==[1,2,1]
           
test_intermediate()
        
def rapid_from2(source,dest,number):
    """
    Converst a number using rapid conversion
    pre:source base must be 2, dest base must be a power of 2
    each group of digits from base to is converted into dest base and added to the list
    returns a a list containing the converted digits in the right order
    """
    #if create_number(raise_power(10,[source],2))<>dest and create_number(raise_power(10,[source],3))<>dest and create_number(raise_power(10,[source],4))<>dest :
    if source<>2: 
        raise ValueError("Destination base not a power of source base")
    elif create_number(raise_power(10,[source],2))==dest:
        power=2
    elif create_number(raise_power(10,[source],3))==dest:
        power=3
    elif create_number(raise_power(10,[source],4))==dest:
        power=4
    while len(number) % power<>0:
        number.insert(0,0)
    i=0
    j=power
    final=[]
    while j<=len(number):
        sequence=number[i:j]
        p=power-1
        rez=0
        for digit in sequence:
            if digit==0:
                p=p-1
            if digit==1:
                plus=create_number(raise_power(10,[2],p))
                rez=rez+plus
                p=p-1
        final.append(rez)

        i=j
        j=j+power
    return final
def test_rapid_from2():
    assert(rapid_from2(2,4,[1,0,1]))==[1,1]
    assert(rapid_from2(2, 8,[1,0,0,1,1]))==[2,3]
    assert(rapid_from2(2,16,[1,1,0,1,1,0,0,1,1]))==[1,11,3]
    assert(rapid_from2(2,4,[1,1,0,1,1,1,1,0,0,0,0,1,0,0]))==[3,1,3,2,0,1,0]
test_rapid_from2()


def rapid_to2(source,dest,number):
    """
    Converst a number using rapid conversion
    pre:dest base must be 2, sourca base must be a power of 2
    each digit is converted into a group of binary digits,according to the power destination
    returns a a list containing the converted digits in the right order
    """
    #if raise_power(10,[dest],2)<>[source] and raise_power(10,[dest],3)<>[source] and create_number(raise_power(10,[dest],4))<>source:
    if dest<>2: 
        raise ValueError("Not destination base not a power of source base")
    elif raise_power(10,[dest],2)==[source]:
        power=2
    elif raise_power(10,[dest],3)==[source]:
        power=3
    elif create_number(raise_power(10,[dest],4))==source:
        power=4
    nr=0
    rez=[]
    for digit in number:
        seq=[]
        p=power-1
        while len(seq)<power:
            if digit >= create_number(raise_power(10,[dest],p)):
                give=1
                digit=digit-create_number(raise_power(10,[dest],p))
            else:
                give=0
            p=p-1
            seq.append(give)
        for s in seq:
            rez.append(s)
        #final=create_number(rez)
    return rez

def test_rapid_to2():
    assert rapid_to2(4,2,[1,2,3])==[0,1,1,0,1,1]
    assert rapid_to2(8,2,[5,7,6,3])==[1,0,1,1,1,1,1,1,0,0,1,1]
    assert rapid_to2(16,2,[11,12,13,14,15,10])==[1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0]
        
test_rapid_to2()

def rapid(source,dest,number):
    """
    Converst a number using the previous functions: rapid_to2 and rapid_from2 
    pre:dest and source base must be 2,4,8 or 16
    returns a a list containing the converted digits in the right order
    """
    num=[]
    if source==2:
            rez=rapid_from2(source,dest,number)
    elif dest==2:
            rez=rapid_to2(source,dest,number)
    else:
            nr=rapid_to2(source,2,number)
            rez=rapid_from2(2,dest,nr)
    return rez

def test_rapid():
    assert(rapid(4,2,[3,2,2,1]))==[1,1,1,0,1,0,0,1]
    assert(rapid(2, 8,[1,0,0,1,1]))==[2,3]
    assert(rapid(2,4,[1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0]))==[3,1,3,2,0,1,0]
    assert(rapid(16,4,[3,7,8,4,9]))==[0,3,1,3,2,0,1,0]
    assert(rapid(8,16,[4,6,7,3,2]))==[4,13,13,10]
    
test_rapid()            

            
        
        
    
        
        
        
        