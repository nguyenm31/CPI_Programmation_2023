import random
import math


CHARACTERS = ["Achilles", "Adonis", "Adriana", "Aegeon", "Aemilia", "Agamemnon", "Agrippa", "Ajax", "Alonso", "Andromache","Angelo", "Antiochus", "Antonio", "Arthur", "Autolycus", "Balthazar", "Banquo", "Beatrice", "Benedick", "Benvolio", "Bianca","Brabantio", "Brutus", "Capulet", "Cassandra", "Cassius", "Christopher Sly", "Cicero", "Claudio", "Claudius", "Cleopatra","Cordelia", "Cornelius", "Cressida", "Cymberline", "Demetrius", "Desdemona", "Dionyza", "Doctor Caius", "Dogberry", "Don John","Don Pedro", "Donalbain", "Dorcas", "Duncan", "Egeus", "Emilia", "Escalus", "Falstaff", "Fenton", "Ferdinand", "Ford", "Fortinbras","Francisca", "Friar John", "Friar Laurence", "Gertrude", "Goneril", "Hamlet", "Hecate", "Hector", "Helen", "Helena", "Hermia","Hermonie", "Hippolyta", "Horatio", "Imogen", "Isabella", "John of Gaunt", "John of Lancaster", "Julia", "Juliet", "Julius Caesar","King Henry", "King John", "King Lear", "King Richard", "Lady Capulet", "Lady Macbeth", "Lady Macduff", "Lady Montague", "Lennox","Leonato", "Luciana", "Lucio", "Lychorida", "Lysander", "Macbeth", "Macduff", "Malcolm", "Mariana", "Mark Antony", "Mercutio","Miranda", "Mistress Ford", "Mistress Overdone", "Mistress Page", "Montague", "Mopsa", "Oberon", "Octavia", "Octavius Caesar","Olivia", "Ophelia", "Orlando", "Orsino", "Othello", "Page", "Pantino", "Paris", "Pericles", "Pinch", "Polonius", "Pompeius","Portia", "Priam", "Prince Henry", "Prospero", "Proteus", "Publius", "Puck", "Queen Elinor", "Regan", "Robin", "Romeo", "Rosalind","Sebastian", "Shallow", "Shylock", "Slender", "Solinus", "Stephano", "Thaisa", "The Abbot of Westminster", "The Apothecary","The Archbishop of Canterbury", "The Duke of Milan", "The Duke of Venice", "The Ghost", "Theseus", "Thurio", "Timon", "Titania","Titus", "Troilus", "Tybalt", "Ulysses", "Valentine", "Venus", "Vincentio", "Viola"]
NEGATIVE_ADJECTIVE = ["bad","cowardly","cursed","damned","dirty","disgusting", "distasteful","dusty","evil","fat-kidneyed","fat","fatherless","foul","hairy","half-witted", "horrible","horrid","infected","lying","miserable","misused","oozing","rotten","rotten","smelly","snotty","sorry", "stinking","stuffed","stupid","vile","villainous","worried"]
NEGATIVE_NOUNS = ["Hell","Microsoft","bastard","beggar","blister","codpiece","coward","curse","death","devil","draught","famine","flirt-gill","goat","hate","hog","hound","leech","lie","pig","plague","starvation","toad","war","wolf"]
NEUTRAL_ADJECTIVES = ["big","black","blue","bluest","bottomless","furry","green","hard","huge","large","little","normal","old","purple","red","rural","small","tiny","white","yellow"]
NEUTRAL_NOUNS = ["animal","aunt","brother","cat","chihuahua","cousin","cow","daughter","door","face","father","fellow","granddaughter","grandfather","grandmother","grandson","hair","hamster","horse","lamp","lantern","mistletoe","moon","morning","mother","nephew","niece","nose","purse","road","roman","sister","sky","son","squirrel","stone wall","thing","town","tree","uncle","wind"]
POSITIVE_ADJECTIVES = ["amazing","beautiful","blossoming","bold","brave","charming","clearest","cunning","cute","delicious","embroidered","fair","fine","gentle","golden","good","handsome","happy","healthy","honest","lovely","loving","mighty","noble","peaceful","pretty","prompt","proud","reddest","rich","smooth","sunny","sweet","sweetest","trustworthy","warm"]
POSITIVE_NOUN = ["Heaven","King","Lord","angel","flower","happiness","joy","plum","summer's day","hero","rose","kingdom","pony"]
ROMAIN_NUMBER = ["I", "II", "III", "IV", "V", "VI", "VI"]
SCENE_ADJ = ["The praising of ", "The insulting of ", "'s conversarion"]


# Get two numbers
in_1 = input("Enter your first number: ")
in_2 = input("Enter your second number: ")

try:
    int_1 = int(in_1)
    int_2 = int(in_2)

    print("You entered:", int_1)
    print("You entered:", int_2)

except ValueError:
    print("Invalid input. Please enter a valid integer.")
    
    
def create_sequence(x,y):
    sequence = [x,y]

    for i in range(5):
        next_term = 2 * (sequence[i+1]-sequence[i])
        sequence.append(next_term)
    return sequence
    

# Generate 5 numbers and the caracter that plays in the script
suites = create_sequence(int_1,int_2)
characters_in  = random.sample(CHARACTERS, 5)

# Generate Title
title = "Script Generated by Two Numbers. \n\n"


# Persent Caracters
present_caracters = ""
for num in range(0,5) :
    adjectif = ""
    if (suites[num] < 0):
        adjectif = random.sample(NEUTRAL_ADJECTIVES, 1)
    elif (suites[num] > 0):
        adjectif = random.sample(POSITIVE_ADJECTIVES, 1)
    else :
        adjectif = random.sample(NEUTRAL_ADJECTIVES, 1)

    present_caracters += characters_in[num] + " is a " + adjectif[0] + " person. \n"


act = "\nACT I: The people talk together \n"


# Get Scene
def generate(num, adj, noun):

    text = "You "
    sqrt_number = math.sqrt(abs(num))
    nAdjectives = int(sqrt_number)
    rest = int(num - (nAdjectives*nAdjectives))

    for i in range(nAdjectives):
        text += random.sample(adj, 1)[0] + " "    #mettre le random     
    text += random.sample(noun, 1)[0] + "!"

    next_line = ""
    for i in range(rest):
            next_line = " You are as " + random.sample(adj, 1)[0] + " as the sum of " #random adj
            next_line += "hero " + "and thyself!" #add random noun
    result = text + next_line
    return result



scene = ""
for num in range(0,5) :
    # Scene ...
    scene += "\nScene "+ ROMAIN_NUMBER[num] + ": "
    speaker = random.sample([char for char in characters_in if char != characters_in[num]], 1)[0]
    listener = characters_in[num]
    
    if (suites[num] < 0):
        scene += SCENE_ADJ[1] + listener
    elif (suites[num] > 0):
        scene += SCENE_ADJ[0] + listener
    else :
        scene += listener + " and " + speaker + SCENE_ADJ[2] + "\n"
        
    # [Enter speaker and listener]
    scene += "\n[Enter " + speaker +" and " + listener+"]\n"
    
    #ALGO
    dialog = ""
    if (suites[num] < 0):
        dialog = generate(suites[num], NEGATIVE_ADJECTIVE, NEGATIVE_NOUNS)    
    elif (suites[num] > 0):
       dialog = generate(suites[num], POSITIVE_ADJECTIVES, POSITIVE_NOUN)    
    else :
       dialog = generate(suites[num], NEGATIVE_ADJECTIVE, NEUTRAL_ADJECTIVES)    
    
    scene += "\n" + dialog + " Open your heart.\n"
    # [Exit  speaker and listener]
    scene += "\n[Exit " + speaker +" and " + listener+"]\n"


script_content = title + present_caracters + act + scene + "\n[Exeunt]"

# Open the file in write mode and write the script content
with open("script.spl", "w") as file:
    file.write(script_content)


