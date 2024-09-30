with open('valid-wordle-words.txt', 'r') as f:
    words = [line.strip() for line in f]

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

start = "naieo"

def prob(sample):
    zero = []

    for word in words:
        if sample[0] not in word and sample[1] not in word and sample[2] not in word and sample[3] not in word and sample[4] not in word:
            zero.append(word)
    
    return len(zero)/len(words)

def next_word():
    prob_list = {}

    for word in words:
        prob_list[word] = prob(word)
        
    lowest = min(prob_list, key=prob_list.get)
    
    return lowest



def play():
    word = "naieo"  # Replace with the guessed word for each round
    print(word)
    
    result = None
    
    while result != "ggggg":
        result = input("please input the result (b for gray, y for yellow, g for green)\n")
        
        # Keep track of letter counts for handling multiple occurrences
        correct_positions = {}  # Tracks 'g' positions
        yellow_positions = {}  # Tracks 'y' positions
        
        # First pass to handle green ('g') and yellow ('y') letters
        for i in range(len(result)):
            if result[i] == 'g':
                correct_positions[word[i]] = correct_positions.get(word[i], 0) + 1
            elif result[i] == 'y':
                yellow_positions[word[i]] = yellow_positions.get(word[i], 0) + 1
        
        for k in words[:]:  # Use a copy of the list to avoid modifying it while iterating
            remove_word = False  # Flag to track if the word should be removed
            
            for i in range(len(result)):
                if result[i] == "g":
                    if k[i] != word[i]:
                        remove_word = True
                
                elif result[i] == "y":
                    # Check that the letter exists but not in the same position
                    if k[i] == word[i]:
                        remove_word = True
                    if word[i] not in k:
                        remove_word = True
                
                elif result[i] == "b":
                    # Count the occurrences of the gray letter in the current word (guess)
                    if word[i] in correct_positions:
                        # If 'g' or 'y' was already marked for this letter, handle carefully
                        if k.count(word[i]) > correct_positions[word[i]] + yellow_positions.get(word[i], 0):
                            remove_word = True
                    else:
                        # If no 'g' or 'y', then the gray letter shouldn't appear in the word
                        if word[i] in k:
                            remove_word = True
            
            # Remove the word if flagged
            if remove_word:
                try:
                    words.remove(k)
                except ValueError:
                    continue
        
        if words:
            word = next_word()
            print("try this word!!!! ", word)
        else:
            print("No words left to guess.")
            break
    
    if result == "ggggg":
        print("You guessed the word!!!!")

    return word

play()
