class Rules:
    def __init__(self,response):
        self.response = response
    def Match(self, sentence, pattern):
        pattern = pattern.split()
        sentence = sentence.split()
        sentence.append("f")
        print(sentence)
        patternindex = 0
        stringindex = 0
        x = False
        y = False
        lastword = "f"
        starstring = []
        while (x == False):
            if (sentence[stringindex] == lastword and patternindex == len(pattern)):
                return True
            if (pattern[patternindex] == sentence[stringindex]):
                patternindex += 1
                stringindex += 1
            if (pattern[patternindex] == '*'):
                while(y == False):
                    print(pattern[patternindex])
                    print(pattern[patternindex + 1])
                    if (pattern[patternindex + 1] == sentence[stringindex]):
                        patternindex += 1
                        y = True
                        break
                    if (pattern[patternindex + 1] != sentence[stringindex]): #If the two strings aren't equal i.e. the * string hasn't been interupeted
                        starstring.append(sentence[stringindex])     #then add the word to the star string and move onto the next
                        stringindex += 1
            if(stringindex > len(sentence) and len(starstring) < 1):
                print("not equal")
                return False
            if (pattern[patternindex] != sentence[stringindex]): #if the two strings aren't equal, then it adds one to the
                stringindex += 1
        print(self.response + starstring)
rule_list = ["I am * f", "I love * f"]
for item in rule_list:
    userinput = raw_input()
    ut = Rules("Why are You").Match(userinput, item)
    print(ut)
