class flashcard:
    def __init__(self,world,meaning):
        self.word = world
        self.meaning = meaning
    def __str__(self):

        #we will return a string
        return self.word+' ( '+self.meaning+')'
    
flash = []
print("welcome to flashcard application")

#the folllowing loopwill be repeated until
#user stops to add the flashcard
while(True):
    word = input("enter the name you want to add in your flash card")

    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 , if you want to add another flashcard otherwise enter 1 : "))

    if (option):
        break