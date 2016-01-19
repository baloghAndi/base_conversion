from domain.operations import *
from validate import *
from domain.conversions import *

def main_menu():
    print """  
               operation - perform operations             Balogh Andrea
               conversion - perform conversions            group 911
               exit - exit the program
           """
    cmd=raw_input("Choose operation or conversion: ").strip()
    return cmd
    
def result(rez):
    s=""
    for digit in rez:
        s+=str(digit)
    #s=int(s)
    return s

def op_menu():
    print """                                        
                                                          Balogh Andrea
                                                            group 911
              add - addition of two numbers in a given base
              sub - substraction of two numbers in a given base                    
              mul - multiplication
              div - division
              back - back to main menu
         """
    cmd=raw_input("Give a command: ").strip()
    return cmd


def operations():
    """
    user interface for operations menu
    """
    cmd=op_menu()
    while cmd<>"back":
        if cmd=="add":
            base=validate_base()
            operand1=valid_op(base)
            operand2=valid_op(base)
            print result(convert_from(add(int(base),operand1,operand2)))
        elif cmd=="sub":
            base=validate_base()
            operand1=valid_op(base)
            operand2=valid_op(base)
            print result(convert_from(sub(int(base),operand1,operand2)))
        elif cmd=="mul":
            try:
                base=validate_base()
                operand1=valid_op(base)
                operand2=valid_op(base)
                rez=mul(int(base),operand1,operand2)
            except ValueError,msg:
                print msg
                operations()
            print result(convert_from(rez))
        elif cmd=="div":
            try:
                base=validate_base()
                operand1=valid_op(base)
                operand2=valid_op(base)
                rez=div(base,operand1,operand2)[0]
            except ValueError,msg:
                print msg
                operations()
            print result(convert_from(rez))
        elif cmd=="back":
            ui()
        else:
            print "No such command"
            operations()
        cmd=op_menu()

def conv_menu():
    print """                 
                                                     Balogh Andrea
                                                        group 911
              subst - converts a number whith substitution method                 
              successiv - converts a number whith successiv divisoon method
              rapid - converts a number whith rapid conversion method
              inter - converts a number whith intermediare base method
              back - back to main menu
    """
    cmd=raw_input("Give a command: ").strip()
    return cmd

def conversions():
    """
    user interface for conversions
    """
    cmd=conv_menu()
    while cmd<>"back":
        if cmd=="subst":
            base=validate_base()
            dest=validate_dest()
            number=valid_op(base)
            try:
                rez=substitution(int(base),int(dest),number)
            except ValueError,msg:
                print msg
                conversions()
        elif cmd=="successiv":
            base=validate_base()
            dest=validate_dest()
            number=valid_op(base)
            try:
                rez=successiv(int(base),int(dest),number)
            except ValueError,msg:
                print msg
                conversions()
        elif cmd=="inter":
            base=validate_base()
            dest=validate_dest()
            inter=validate_inter()
            number=valid_op(base)
            try:
                rez=intermediate(int(base),int(inter),int(dest),number)
            except ValueError,msg:
                print msg
                conversions()
        elif cmd=="rapid":
            base=valid_rapid()
            dest=validate_dest()
            number=valid_op(base)
            try:
                rez=rapid(int(base),int(dest),number)
            except ValueError,msg:
                print msg
                conversions()
        elif cmd=="back":
            ui()
        else:
            print "No such command"
            conversions()
        print result(convert_from(rez))
        cmd=conv_menu()
def ui():
    cmd=main_menu()
    while cmd<> "exit":      
        if cmd=="operation":
            operations()
        elif cmd=="conversion":
            conversions()
        else:
            print "No such command"
        cmd=main_menu()