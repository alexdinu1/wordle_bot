with open('valid-wordle-words.txt', 'r') as f:
    words = [line.strip() for line in f]

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

start = "naieo"

'''
def prob(sample):
    zero = []

    for word in words:
        if sample[0] not in word and sample[1] not in word and sample[2] not in word and sample[3] not in word and sample[4] not in word:
            zero.append(word)
    
    return len(zero)/len(words)

prob_list = {}

for word in words:
    prob_list[word] = prob(word)
    
lowest = min(prob_list, key=prob_list.get)

'''

def play():
    word = "naieo"
    print(word)
    
    result = None
    
    while result != "ggggg":
        result = input("please input the result (b for gray, y for yellow, g for green)\n")
        
        pairs = []
        glist = []
        
        filtered_words = words[:]  # Create a copy of the list to avoid modifying it directly
        for n, (i, j) in enumerate(zip(result, word)):
            pairs.append((i,j,n))
        
        for pair in pairs:
            if pair[0] == "g":
                for w in words:
                    if w[n] == pair[1]:
                        print(w)
                        words.remove(w)
            
           
        word = words[0]
        print("this is the word!!!! ", word)
        words.remove(word)
    
        print(glist)
    return word
        
play()
