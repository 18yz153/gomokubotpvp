class addchessexception(Exception):
    def __init__(self):
      self.i=1



class game():
  def __init__(self):
    self.board = [None]*15
    for i in range(len(self.board)):
      self.board[i]=["+ "]*15
    
  def addchess(self,chess,pos):
    x=int(pos[0])-1
    y=int(pos[1])-1
    if self.board[x][y]=="+ ":
      self.board[x][y]=chess
    else:
      raise addchessexception()

  def iscontiune(self):
    for i in range(len(self.board)):
        for j in range(len(self.board[i])):
            if self.board[i][j]!='+ ':
                if j<=11:
                    if self.board[i][j]==self.board[i][j+1]==self.board[i][j+2]==self.board[i][j+3]==self.board[i][j+4]:
                        return False
                if i<=11:
                    if self.board[i][j]==self.board[i+1][j]==self.board[i+2][j]==self.board[i+3][j]==self.board[i+4][j]:
                        return False
                if i<=11 and j<=11:
                    if self.board[i][j]==self.board[i][j+1]==self.board[i][j+2]==self.board[i][j+3]==self.board[i][j+4]:
                        return False
                if i>=4 and j<=11:
                    if self.board[i][j]==self.board[i][j+1]==self.board[i][j+2]==self.board[i][j+3]==self.board[i][j+4]:
                        return False
    return True


  
  def __str__(self):
    boardimg = '\n'.join(''.join(map(str,i)) for i in self.board)
    return boardimg


