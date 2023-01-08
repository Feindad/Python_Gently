###EX9-PG Chess Square Color

def getChessSquareColor(column,row):
    if row >= 9 or column >= 9:
        return ('')
    if row == 0 or column == 0:
        return ('')
   #column is odd and row is even or if column is even and row is odd
    if column % 2 == 1 and row % 2 == 0 or column % 2 == 0 and row % 2 == 1:
        return('black')
    else:
        return('white')

assert getChessSquareColor(1, 1) == 'white'

assert getChessSquareColor(2, 1) == 'black'

assert getChessSquareColor(1, 2) == 'black'

assert getChessSquareColor(8, 8) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''
