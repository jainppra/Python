
# Pass the total string 
a = [0]*10

def displayboard(a):
    
    print(" {} | {} | {} ".format(a[6],a[7],a[8]))
    print(" __|___|__ ")
    print(" {} | {} | {} ".format(a[3],a[4],a[5]))
    print(" __|___|__ ")
    print(" {} | {} | {} ".format(a[0],a[1],a[2]))
    
def posentry(user,location):
    a[location]==user
    

    
def choosing_player():
    p1=''
    p2=''
    while p1!='X' or p1!='0':
        p1=input("Player1 chooose X or 0")
        if p1=='X':
            p2=='0'
            return (p1,'0')
        elif p1=='0':
            p2=='X'
            return(p1,'X')

         
        

player1,player2 = choosing_player()
print('player 1 is '+ player1)
print('player 2 is '+ player2)
print('Player 1 will play first \n\n\n')
for i in range(4):
    p = input('Enter the position where you want to play')
    a[p-1]=player1

