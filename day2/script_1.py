

file_input = open("input_1.txt", "r")
opponent_plays_dict = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors" 
}

our_plays_dict = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors" 
}

play_value_dict = {
    "Rock": 2,
    "Paper": 0,
    "Scissors": 1        
}

win_value_dict = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3 
}



total = 0
current_round = 0    
    
for line in file_input:
    current_round = 0
    plays = line[0:3].split(" ")
    test = []
    
    # Get the Oponnent's PLay in Format 'Rock' 'Paper' 'Scissors'
    oponnent_play =  plays[0]
    oponnent_play = opponent_plays_dict[oponnent_play]
    
    # Get Our Play in Format 'Rock' 'Paper' 'Scissors'
    our_play = plays[1]
    our_play = our_plays_dict[our_play]
    
    # Transform into a Int corresponding to his strength 
    oponnent_value_play = play_value_dict[oponnent_play]
    our_value_play = play_value_dict[our_play]
   
    
    # Add the Shape selected Value
    current_round += win_value_dict[our_play]

    # Condition to Verify who win
    diff = our_value_play - oponnent_value_play
    
    
    if (diff == -2):
        current_round += 6   
    elif (diff == 2):
        current_round += 0             
    elif (diff > 0):
        current_round += 6
    elif (diff == 0):
        current_round += 3
            
    total += current_round
    
    
    
print(total)    
    

    