def operand(base,op):
    """
    validates if a number is really containing only numbers in the given base
    raises ValueError if a digit in then number is greater or equal to the base
    """
    for d in op:
        if int(d) >= int(base) :
            raise ValueError("The number contains digits which do not exist in the given base ")
    return op
        
def convert_to(op):
    """
    fills a list with the digits of the number in the base 10, using the ascii table
    if the code is not between the code of 0 and 9 appends with the digit,otherwise computes the corresponding
    values to the digit from the greater basis than 10
    returns a list of digits in base 10
    """
    operand=[]
    for digit in op:
        if ord(digit) in range(48,57) :
            operand.append(int(digit))
        else :
            operand.append(ord(digit)-87)     
    return operand  

def convert_from(op):
    """
    convers the list of digits into a number
    if the base is greater than 10, the greater digits will be computed correspondingly
    """
    operand=[]
    l=["a","b","c","d","e","f"]
    for digit in op:
        if digit in range(10,16):
            operand.append(l[digit-10])     
        else:
            operand.append(digit) 
    return operand  

def number(base):
    """
    raises valueerror if the inrtoduces string contains literals
    """
    for el in base:
        if ord(el) not in range(48,58):
            raise ValueError("Base can not contain literals")
            
def right_base(base):
    """
    raises valueerror if the the number is less than 2 or greater than 16
    """
    if int(base) not in range(2,17):
        raise ValueError("Base has to be a number between 2 and 16")
    
def validate_base():
    """
    verifies if the base is introduces correctly using number and right_base functions
    asks for a base until the introduced data is right
    """
    ok=False
    while ok==False:   
     try:
        base=raw_input("Give base:").strip()
        number(base)
        right_base(base)
        ok=True
        return base
     except ValueError,msg:
        print msg

def validate_dest():
    ok=False
    while ok==False:   
     try:
        base=raw_input("Give the dest base:").strip()
        number(base)
        right_base(base)
        ok=True
        return base
     except ValueError,msg:
        print msg

def validate_inter():
    ok=False
    while ok==False:   
     try:
        base=raw_input("Give the intermediate base:").strip()
        number(base)
        right_base(base)
        ok=True
        return base
     except ValueError,msg:
        print msg
            
def valid_op(base):
    """
    verifies if a number is introduces correctly using convert_to and operand functions
    asks for an operand until the introduced data is right
    """
    ok=False
    while ok==False:          
            try:
                op=raw_input("Give the operand:").strip()
                op=convert_to(op)
                op=operand(base,op)
                ok=True
                return op
            except ValueError,msg:
                print msg

def power_of2(base):
    """
    check if a base fullfils the pre condition of rapid conversion: base must be 2,4,,8 or 16
    """
    if int(base)<>2 and int(base)<>4 and int(base)<>8 and int(base)<>16:
        raise ValueError("Using this method source and destination base should be a power of 2")
                    
def valid_rapid():
    """
    verifies if a fullfils the conditions of rapid conversion
    base has to be a number and a power of 2
    """
    ok=False
    while ok==False:   
     try:
        base=raw_input("Give base:").strip()
        number(base)
        power_of2(base)
        ok=True
        return base
     except ValueError,msg:
        print msg

    
 