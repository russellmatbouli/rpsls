```
players = <input> as integer
player_names = <input> as string array
best_of = <input> as integer || 5

game => 2 players
match => 2 players, num game wins
overall_winner => match.wins, game.game

for each player:
  player.choice = <input>
log player moves
determine winning play
  increment game wins
if all players have played each other,
display results table
```

```
match_wins = {}
game_wins = {}

legal_input = [ rock, paper, scissors, lizard, spock ]

rules_english = [
  Scissors cuts Paper
  Paper covers Rock
  Rock crushes Lizard
  Lizard poisons Spock
  Spock smashes Scissors
  Scissors decapitates Lizard
  Lizard eats Paper
  Paper disproves Spock
  Spock vaporizes Rock
  Rock crushes Scissors
]

winning_plays = {
  rock => [ scissors, lizard ],
  paper => [ rock, spock ],
  scissors => [ paper, lizard ],
  lizard => [ spock, paper ],
  spock => [ scissors, rock ],
}

outcomes = [ win, lose, draw ]

determine winner ()
  return draw if player1.choice == player2.choice
  return win if winning_plays[player1.choice][player2.choice]
  return lose

```

User: Name
Scoreboard: User, Game tot, Match tot
Rules:
