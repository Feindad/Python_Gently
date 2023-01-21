### Python Gently Ex 22 Rock, Paper, Scissors
def rpsWinner(player1,player2):
    hands = []
    hands.append(player1)
    hands.append(player2)

    if player1 == player2:
        return "tie"
    if "paper" in hands and "rock" in hands:
        if "rock"== player2:
            return "player one"
        else:
            return "player two"
    if "scissors" in hands and "rock" in hands:
        if "rock" == player2:
            return "player two"
        else:
            return "player one"
    if "scissors" in hands and "paper" in hands:
        if "paper" == player2:
            return "player one"
        else:
            return "player two"

assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'
