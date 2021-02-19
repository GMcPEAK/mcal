def view(args): 
    # get the file name/path 
    arg1 = args.view[0] 
    print(arg1)

def main():
    print("Hello world!")
    # create parser object 
    parser = argparse.ArgumentParser(description = "A text file manager!") 
  
    # defining arguments for parser object 
    parser.add_argument("-v", "--view", type = str, nargs = 1, 
                        metavar = "arg1", default = None, 
                        help = "Displays the next week of your calendar.") 
  
    # parse the arguments from standard input 
    args = parser.parse_args() 
      
    # calling functions depending on type of argument 
    if args.view != None: 
        view(args) 

if __name__ == "__main__": 
    # calling the main function 
    main() 