"""
File: keyboarding.py
By Mathieu Steele

This program teaches keyboarding accuracy by encouraging the
user to type words as they fall from the top of the screen.
"""
from abc import ABC
import arcade
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

INITIAL_WORD_SPEED = 1.5
INITIAL_WORD_COUNT = 10

FALLING_WORD_COLOR = arcade.color.WHITE

# This was from a list of the top 1000 most commonly used words in English
WORD_LIST = ["the","of","to","and","a","in","is","it","you","that","he","was",
"for","on","are","with","as","I","his","they","be","at","one","have","this",
"from","or","had","by","not","word","but","what","some","we","can","out","other",
"were","all","there","when","up","use","your","how","said","an","each","she","which",
"do","their","time","if","will","way","about","many","then","them","write","would",
"like","so","these","her","long","make","thing","see","him","two","has","look","more",
"day","could","go","come","did","number","sound","no","most","people","my","over",
"know","water","than","call","first","who","may","down","side","been","now","find",
"any","new","work","part","take","get","place","made","live","where","after","back",
"little","only","round","man","year","came","show","every","good","me","give","our",
"under","name","very","through","just","form","sentence","great","think","say","help",
"low","line","differ","turn","cause","much","mean","before","move","right","boy","old",
"too","same","tell","does","set","three","want","air","well","also","play","small","end",
"put","home","read","hand","port","large","spell","add","even","land","here","must","big",
"high","such","follow","act","why","ask","men","change","went","light","kind","off","need",
"house","picture","try","us","again","animal","point","mother","world","near","build","self",
"earth","father","head","stand","own","page","should","country","found","answer","school",
"grow","study","still","learn","plant","cover","food","sun","four","between","state","keep",
"eye","never","last","let","thought","city","tree","cross","farm","hard","start","might",
"story","saw","far","sea","draw","left","late","run","while","press","close","night",
"real","life","few","north","open","seem","together","next","white","children","begin","got",
"walk","example","ease","paper","group","always","music","those","both","mark","often","letter",
"until","mile","river","car","feet","care","second","book","carry","took","science","eat","room",
"friend","began","idea","fish","mountain","stop","once","base","hear","horse","cut","sure","watch",
"color","face","wood","main","enough","plain","girl","usual","young","ready","above","ever","red",
"list","though","feel","talk","bird","soon","body","dog","family","direct","pose","leave","song",
"measure","door","product","black","short","numeral","class","wind","question","happen","complete",
"ship","area","half","rock","order","fire","south","problem","piece","told","knew","pass","since",
"top","whole","king","space","heard","best","hour","better","true","during","hundred","five",
"remember","step","early","hold","west","ground","interest","reach","fast","verb","sing",
"listen","six","table","travel","less","morning","ten","simple","several","vowel","toward",
"war","lay","against","pattern","slow","center","love","person","money","serve","appear",
"road","map","rain","rule","govern","pull","cold","notice","voice","unit","power","town",
"fine","certain","fly","fall","lead","cry","dark","machine","note","wait","plan","figure",
"star","box","noun","field","rest","correct","able","pound","done","beauty","drive","stood",
"contain","front","teach","week","final","gave","green","oh","quick","develop","ocean","warm",
"free","minute","strong","special","mind","behind","clear","tail","produce","fact","street","inch",
"multiply","nothing","course","stay","wheel","full","force","blue","object","decide","surface","deep",
"moon","island","foot","system","busy","test","record","boat","common","gold","possible","plane",
"stead","dry","wonder","laugh","thousand","ago","ran","check","game","shape","equate","hot","miss",
"brought","heat","snow","tire","bring","yes","distant","fill","east","paint","language","among",
"grand","ball","yet","wave","drop","heart","am","present","heavy","dance","engine","position",
"arm","wide","sail","material","size","vary","settle","speak","weight","general","ice","matter",
"circle","pair","include","divide","syllable","felt","perhaps","pick","sudden","count","square",
"reason","length","represent","art","subject","region","energy","hunt","probable","bed","brother",
"egg","ride","cell","believe","fraction","forest","sit","race","window","store","summer","train",
"sleep","prove","lone","leg","exercise","wall","catch","mount","wish","sky","board","joy","winter",
"sat","written","wild","instrument","kept","glass","grass","cow","job","edge","sign","visit","past",
"soft","fun","bright","gas","weather","month","million","bear","finish","happy","hope","flower",
"clothe","strange","gone","jump","baby","eight","village","meet","root","buy","raise","solve","metal",
"whether","push","seven","paragraph","third","shall","held","hair","describe","cook","floor","either",
"result","burn","hill","safe","cat","century","consider","type","law","bit","coast","copy","phrase",
"silent","tall","sand","soil","roll","temperature","finger","industry","value","fight","lie","beat",
"excite","natural","view","sense","ear","else","quite","broke","case","middle","kill","son","lake",
"moment","scale","loud","spring","observe","child","straight","consonant","nation","dictionary","milk",
"speed","method","organ","pay","age","section","dress","cloud","surprise","quiet","stone","tiny","climb",
"cool","design","poor","lot","experiment","bottom","key","iron","single","stick","flat","twenty","skin",
"smile","crease","hole","trade","melody","trip","office","receive","row","mouth","exact","symbol","die",
"least","trouble","shout","except","wrote","seed","tone","join","suggest","clean","break","lady","yard",
"rise","bad","blow","oil","blood","touch","grew","cent","mix","team","wire","cost","lost","brown","wear",
"garden","equal","sent","choose","fell","fit","flow","fair","bank","collect","save","control","decimal",
"gentle","woman","captain","practice","separate","difficult","doctor","please","protect","noon","whose",
"locate","ring","character","insect","caught","period","indicate","radio","spoke","atom","human","history",
"effect","electric","expect","crop","modern","element","hit","student","corner","party","supply","bone",
"rail","imagine","provide","agree","thus","capital","chair","danger","fruit","rich","thick",
"soldier","process","operate","guess","necessary","sharp","wing","create","neighbor","wash","bat",
"rather","crowd","corn","compare","poem","string","bell","depend","meat","rub","tube","famous",
"dollar","stream","fear","sight","thin","triangle","planet","hurry","chief","colony","clock",
"mine","tie","enter","major","fresh","search","send","yellow","gun","allow","print","dead","spot",
"desert","suit","current","lift","rose","continue","block","chart","hat","sell","success","company",
"subtract","event","particular","deal","swim","term","opposite","wife","shoe","shoulder","spread",
"arrange","camp","invent","cotton","born","determine","quart","nine","truck","noise","level","chance",
"gather","shop","stretch","throw","shine","property","column","molecule","select","wrong","gray",
"repeat","require","broad","prepare","salt","nose","plural","anger","claim","continent","oxygen",
"sugar","death","pretty","skill","women","season","solution","magnet","silver","thank","branch",
"match","suffix","especially","fig","afraid","huge","sister","steel","discuss","forward","similar",
"guide","experience","score","apple","bought","led","pitch","coat","mass","card","band","rope",
"slip","win","dream","evening","condition","feed","tool","total","basic","smell","valley","nor",
"double","seat","arrive","master","track","parent","shore","division","sheet","substance",
"favor","connect","post","spend","chord","fat","glad","original","share","station","dad",
"bread","charge","proper","bar","offer","segment","slave","duck","instant","market","degree",
"populate","chick","dear","enemy","reply","drink","occur","support","speech","nature","range",
"steam","motion","path","liquid","log","meant","quotient","teeth","shell","neck",
]

class Point:
    """
    This represents a point on the board
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def advance(self, velocity):
        """
        Move the point forward in it's trajectory
        """

        self.x += velocity.dx
        self.y += velocity.dy

        # wrap around the screen
        if self.y < 0:
            self.y += SCREEN_HEIGHT * 1.25
        

class Velocity:
    """
    This represents a velocity
    """
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class FlyingObject(ABC):
    """
    Represents a movable object
    """
    def __init__(self, x=0, y=0, velocity=Velocity(0,0), text=""):
        self._center = Point(x, y)
        self._velocity = velocity
        self._text = text
        
    def advance(self):
        """
        Move the object forward in the direction it is going
        """
        self.center.advance(self.velocity)
    
    def draw(self):
        """
        Render the object to the screen
        Adjusts size of image to match the object's radius in pixels.
        """
        arcade.draw_text(self._text, self.center.x, self.center.y, FALLING_WORD_COLOR, font_size=20)
    
    def get_center(self):
        """
        Get the center
        """
        return self._center
    
    def set_center(self, center):
        """
        Set the center
        """
        self._center = center
    
    def get_velocity(self):
        """
        Get the velocity
        """
        return self._velocity
    
    def set_velocity(self, velocity):
        """
        Set the velocity
        """
        self._velocity = velocity
    
    center = property(get_center, set_center)
    velocity = property(get_velocity, set_velocity)

    
def get_suggested_velocity_from_word_length(word_length):
    """
    Calculate the suggested velocity based on the length of the word
    """

    # Shorter words will move faster
    if word_length <= 3:
        return Velocity(0, -INITIAL_WORD_SPEED  * 1.5)
    elif word_length <= 5:
        return Velocity(0, -INITIAL_WORD_SPEED)
    elif word_length <= 7:
        return Velocity(0, -INITIAL_WORD_SPEED * .80)
    elif word_length <= 9:
        return Velocity(0, -INITIAL_WORD_SPEED * .70)
    else:
        return Velocity(0, -INITIAL_WORD_SPEED * .60)

class Word(FlyingObject):
    """
    Represents a word that will be used in the game
    """
    def __init__(self, text):
        # randomize the position of the word
        super().__init__(
            random.randint(0, SCREEN_WIDTH-100),
            random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT*2),
            get_suggested_velocity_from_word_length(len(text)),
            text
            )


class Game(arcade.Window):

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.words = []

        # The user's starting score should be zero.
        self.score = 0

        # We configure this setting at the top of this file. It represents how many words to show on the screen at once.
        self.add_words(INITIAL_WORD_COUNT)

        self.entered_keys = ""

    def add_words(self, number):
        """
        add one or more words to the list
        :param number: number of words to add
        """
        while number > 0:
            # add a random word to the list of words
            self.words.append(Word(random.choice(WORD_LIST)))
            number -= 1
    
    def remove_words(self, number):
        """
        remove one or more words from the list
        :param number: number of words to remove
        """
        while number > 0:
            self.words.pop()
            number -= 1

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        for word in self.words:
            # Each word knows how to draw itself and where it should be placed
            word.draw()
        
        # show the current text entry from the user
        arcade.draw_text(self.entered_keys, 20, 20, arcade.color.BRIGHT_GREEN, 16, width=600, align="left", anchor_x="left", anchor_y="center")
        # show the score
        arcade.draw_text("score: " + str(self.score), SCREEN_WIDTH-150, 20, arcade.color.BRIGHT_GREEN, 16, width=600, align="left", anchor_x="left", anchor_y="center")
        
        

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        for word in self.words:
            # We are only looking for exact matches
            if word._text.lower() == self.entered_keys:
                # remove the word from the list after it was entered correctly
                self.words.remove(word)

                # Award a higher score for longer words
                self.score += len(word._text)**3

                # Reset the list of entered keys after a word match has taken place
                self.entered_keys = ""

                # Add a new word to replace the one that just got removed
                self.add_words(1)
            else:
                word.advance()


    def on_key_press(self, key: int, modifiers: int):
        """
        detects which key was pressed by the player.
        List of keys here: https://api.arcade.academy/en/latest/arcade.key.html
        """

        if key == 97:
            self.entered_keys += "a"
        elif key == 98:
            self.entered_keys += "b"
        elif key == 99:
            self.entered_keys += "c"
        elif key == 100:
            self.entered_keys += "d"
        elif key == 101:
            self.entered_keys += "e"
        elif key == 102:
            self.entered_keys += "f"
        elif key == 103:
            self.entered_keys += "g"
        elif key == 104:
            self.entered_keys += "h"
        elif key == 105:
            self.entered_keys += "i"
        elif key == 106:
            self.entered_keys += "j"
        elif key == 107:
            self.entered_keys += "k"
        elif key == 108:
            self.entered_keys += "l"
        elif key == 109:
            self.entered_keys += "m"
        elif key == 110:
            self.entered_keys += "n"
        elif key == 111:
            self.entered_keys += "o"
        elif key == 112:
            self.entered_keys += "p"
        elif key == 113:
            self.entered_keys += "q"
        elif key == 114:
            self.entered_keys += "r"
        elif key == 115:
            self.entered_keys += "s"
        elif key == 116:
            self.entered_keys += "t"
        elif key == 117:
            self.entered_keys += "u"
        elif key == 118:
            self.entered_keys += "v"
        elif key == 119:
            self.entered_keys += "w"
        elif key == 120:
            self.entered_keys += "x"
        elif key == 121:
            self.entered_keys += "y"
        elif key == 122:
            self.entered_keys += "z"
        elif key == 65288:
            self.entered_keys = self.entered_keys[:-1]
            self.score -= 1
        elif key == 65363:
            self.add_words(1)
        elif key == 65361:
            self.remove_words(1)


        

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()