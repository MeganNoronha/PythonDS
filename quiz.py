import random

# Define a function to separate the word from the 
# definition and return the tuple

def get_word_and_definition(rawstring):
    word, definition = rawstring.split(',', 1) #split on the first comma
    return word, definition

# Define a function to get a random word from the list and
# get the corresponding definition
def get_def_and_pop(word_list, word_dict):
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    definition = word_dict.get(word)
    return word, definition

# Read file into list
fh = open("Vocabulary_list.csv", "r") 
wd_list = fh.readlines()
#print(wd_list)

#Use a Set
wd_list.pop(0) #remove the first line
wd_set = set(wd_list) #remove any duplicates
fh = open("Vocabulary_set.csv", "w")
fh.writelines(wd_set)

#Make a dictionary with word as key and def as value
word_dict = dict()
for rawstring in wd_set:
    word, definition = get_word_and_definition(rawstring)
    word_dict[word] = definition
    #print(word)


# Create a simple quiz where the user must select the correct definition for a word

while True:
    wd_list = list(word_dict) #gives us a list of the key set of the dict
    choice_list = [] # to fill in all the choices
    for x in range(4):
        word,definition = get_def_and_pop(wd_list, word_dict)
        choice_list.append(definition)
    random.shuffle(choice_list) #So our correct def isnt always at the end
    print("")
    print(word)
    print("")
    print("---- Options ----")
    for idx, choice in enumerate(choice_list):
        print(idx + 1, choice)
    
    user_choice = int(input('Enter 1, 2, 3, or 4; 0 to exit'))
    if user_choice == 0:
        print("Thanks for playing!")
        exit(0)
    elif choice_list[user_choice - 1] == definition:
        print("YESS, Correct answer!")
    else:
        print("Sorry! Try again")