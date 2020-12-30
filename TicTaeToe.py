board = ["1" , "2" ,"3" , "4", "5", "6", "7", "8", "9"] # list
def structure_board():
    print("|"+ board[0]+"|"+board[1]+"|"+board[2]+"|");
    print("|"+ board[3]+"|"+board[4]+"|"+board[5]+"|");
    print("|"+ board[6]+"|"+board[7]+"|"+board[8]+"|");
def structure_position_1():
    structure_board()
    x = input("Which position firstplayer want to select: ");# In this case input is a string
    x= int(x);# This will convert the string into integer
    x=x-1;
    board[x]='X';
    print(structure_board());
    return 0;
def structure_position_2():
    structure_position_1();
    y = input("Which position Secondplayer want to select: ");
    y= int(y);# This will convert the string into integer
    y= y-1;
    board[y]='O';
    
    if ( board[0]==board[1] and board[1]==board[2]):
        t=board[1];
        if (t=="X"):
           print("First Player is win on position 0112")
        else:
            print("Second Player is win on position 0112")
    elif(board[3]==board[4] and board[4]==board[5]):
        t=board[3];
        if (t=="X"):
           print("First Player is win on position 3445")
        else:
           print("Second Player is win on position 3445")
    elif(board[6]==board[7] and board[7]==board[8]):
        t=board[6];
        if (t=="X"):
           print("First Player is win on position 0778")
        else:
           print("Second Player is win on position 0778")
       
    elif(board[0]==board[4] and board[4]==board[8]):
        t=board[0];
        if (t=="X"):
           print("First Player is win on position 0448")
        else:
            print("Second Player is win on position 0448")
    elif(board[2]==board[4] and board[4]==board[6]):
        t=board[2];
        if (t=="X"):
           print("First Player is win on position 2446")
        else:
           print("Second Player is win on position 0112")
    elif(board[0]==board[3] and board[3]==board[6]):
        t=board[3];
        if (t=="X"):
           print("First Player is win on position 0336")
        else:
           print("Second Player is win on position 0336")
    elif(board[1]==board[4] and board[4]==board[7]):
        t=board[4];
        if (t=="X"):
           print("First Player is win on position 1447")
        else:
           print("Second Player is win on position 1447")
    elif(board[2]==board[5] and board[5]==board[8]):
        t=board[5];
        if (t=="X"):
           print("First Player is win on position 2558")
        else:
           print("Second Player is win on position 2558")
 
    else:
      return structure_position_2();
      print(structure_board);

structure_position_2();





    



    

        


   
    
    
       





