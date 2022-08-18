class String:
    def __init__(self):
        self.uppercase =0
        self.lowercase =0
        self.vowels =0
        self.consonants =0
        self.spaces =0
        self.string = ""
    def getstr(self):
        self.string = str(input("Enter a String : "))
    def countUpper(self):
        for ch in self.string:
            if(ch.isupper()):
                self.uppercase += 1
    def countLower(self):
        for ch in self.string:
            if(ch.islower()):
                self.lowercase += 1
    def countVowels(self):
        vow=( 'a','e','i','o','u' )
        a=self.string
        a.lower()
        for ch in a :
            if (ch in vow ):
                self.vowels += 1
    def countConsonants(self):
        vow=( 'a','e','i','o','u' )
        a=self.string
        a.lower()
        for ch in a :
            if (ch not in vow and ch.isalpha()):
                self.consonants += 1
    def countSpace(self):
        for ch in self.string :
            if (ch==" "):
                self.spaces +=1
    def execute(self):
        self.countUpper()
        self.countLower()
        self.countVowels()
        self.countConsonants()
        self.countSpace()
    def display(self):
        print("\nThe Given String Contains ,\n")
        print("\t* %d Upper case Letters \n"%self.uppercase)
        print("\t* %d Lower case Letters \n"%self.lowercase)
        print("\t* %d Vowels \n"%self.vowels)
        print("\t* %d Consonants \n"%self.consonants)
        print("\t* %d Spaces\n"%self.spaces)
S=String()
S.getstr()
S.execute()
S.display()