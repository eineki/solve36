moves = ( (), 
   (4, 15, 19), 
   (5, 16, 20), 
   (6, 13, 17, 21), 
   (1, 14, 18, 22), 
   (2, 15, 23), 
   (3, 16, 24), 
   (10, 21, 25), 
   (11, 22, 26), 
   (12, 19, 23, 27), 
   (7, 20, 24, 28), 
   (8, 21, 29), 
   (9, 22, 30), 
   (3, 16, 27, 31), 
   (4, 17, 28, 32), 
   (1, 5, 18, 25, 29, 33), 
   (2, 6, 13, 26, 30, 34), 
   (3, 14, 27, 35), 
   (4, 15, 28, 36), 
   (1, 9, 22, 33), 
   (2, 10, 23, 34), 
   (3, 7, 11, 24, 31, 35), 
   (4, 8, 12, 19, 32, 36), 
   (5, 9, 20, 33), 
   (6, 10, 21, 34), 
   (7, 15, 28), 
   (8, 16, 29), 
   (9, 13, 17, 30), 
   (10, 14, 18, 25), 
   (11, 15, 26), 
   (12, 16, 27), 
   (13, 21, 34), 
   (14, 22, 35), 
   (15, 19, 23, 36), 
   (16, 20, 24, 31), 
   (17, 21, 32), 
   (18, 22, 33)
)
 
def move_list(index):
    return [ i for i in moves[index] if i not in game]

def next_move(game):
    legal = move_list( game[-1] )
    if legal: 
        return legal[0]
    return None


def change_move(game):
    wrong_move = game.pop() # take back a move
    legal = move_list( game[-1] )
    legal = legal[legal.index(wrong_move)+1:]
    if legal: 
        return legal[0]
    return None

if __name__ == "__main__":
    for i in range (1,37):
        game = [ i ]    
        while len(game)<36:
            move = next_move( game )
            while not move:
                move = change_move(game)
            if move:
                game.append( move )
        print( game[0], game )
