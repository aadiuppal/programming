def search_word(word,game):
    m = len(game)
    n = len(game[0])
    return search(word,0,game,m,n)

def search(word,w,game,m,n):
    for i in range(m):
        for j in range(n):
            if game[i][j] == word[w]:
                qu = [[i,j]]
                while qu:
                    t_m,t_n = qu[0]
                    qu = qu[1:]
                    if word[w] != game[t_m][t_n]:
                        continue
                    if w == len(word)-1:
                        return True
                    w +=1
                    qu += valid_moves(t_m,t_n,game)
    return False
def valid_moves(i,j,game):
    moves = [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]
    move = []
    m= len(game)
    n =len(game[0])
    for p,q in moves:
        if p<0 or p>=m or q<0 or q>=n:
            continue
        move.append([p,q])
    return move

word1 = "asd"
word2 = "qbw"
game = [['a','d','a'],['b','q','s'],['d','s','d']]
print search_word(word1,game)
print search_word(word2,game)
