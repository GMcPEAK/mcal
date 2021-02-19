import error as e
import numpy as np
import os 
import sys



def view(): 
    size = os.get_terminal_size()
    for i in range(size.columns):
        print("_", end="") 
    
def check_input():
    if(len(sys.argv) > 1):
        valid = True
        bad_args = []
        for a in range(1, len(sys.argv)):
            if (sys.argv[a] != "v" and
                sys.argv[a] != "view" and
                sys.argv[a] != "g" and
                sys.argv[a] != "get"):
                valid = False
                bad_args.append(a)
        if not(valid):
            if (len(bad_args) > 2):
                arg_list_str = ""
                for i in range(len(bad_args)-2):
                    arg_list_str = arg_list_str+str(bad_args[i])+", "
                arg_list_str = arg_list_str+str(bad_args[len(bad_args)-2])+" and "+str(bad_args[len(bad_args)-1])
                e.throw("Arguments "+arg_list_str+" not recognized.")
            elif (len(bad_args) > 1):
                arg_list_str = str(bad_args[0])+" & "+str(bad_args[1])
                e.throw("Arguments "+arg_list_str+" not recognized.")
            else:
                e.throw("Argument "+bad_args[0]+" not recognized.")

    else:
        e.throw("No arguments passed")

def main():
    check_input()

if __name__ == "__main__": 
    # calling the main function 
    main() 