

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

our_plays_result_dict = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win" 
}

play_value_dict = {
    "Rock": 2,
    "Paper": 0,
    "Scissors": 1        
}

play_value_dict_reverse = {
    2: "Rock",
    0: "Paper",
    1: "Scissors"
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
    
    # Get Our Play in Format 'Lose' 'Win' 'Draw'
    our_play_result = plays[1]
    our_play_result = our_plays_result_dict[our_play_result]
    
    # Transform into a Int corresponding to his strength 
    oponnent_value_play = play_value_dict[oponnent_play]
    
    
    
    

    if our_play_result == "Draw":
        #current_play => The Draw we should play
        current_play = play_value_dict_reverse[oponnent_value_play]
        current_round += win_value_dict[current_play]
        current_round += 3
    elif our_play_result == "Win":
        current_round += 6
        
        if (oponnent_value_play == 2) :
            current_play= 0
        else:
            current_play = oponnent_value_play + 1    
        
        current_play = play_value_dict_reverse[current_play]
        current_round += win_value_dict[current_play]
        
    elif (our_play_result == "Lose"):
        if (oponnent_value_play == 0) :
            current_play= 2
        else:
            current_play = oponnent_value_play - 1    
        
        current_play = play_value_dict_reverse[current_play]
        current_round += win_value_dict[current_play]   
      
        
                      
    total += current_round
    
    
    
print(total)    
    

    