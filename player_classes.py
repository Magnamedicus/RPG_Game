
import math
import random

class Player():
    def __init__(self, name, age, birthplace, allignment, demeaner, origin,
                 trade, health_points, health_capacity, strength, endurance,
                 intelligence, wisdom, agility, dexterity, charisma, perception,armor_rating):

        #basic info
        self.name = name
        self.age = age
        self.birthplace = birthplace
        self. allignment = allignment
        self.demeaner = demeaner
        self.origin = origin
        self.trade = trade
        self.level = 1

        #action switches
        walk_left = 0
        walk_right = 0
        run_left = 0
        run_right = 0
        walk_up = 0
        walk_down = 0
        attack_fists = 0
        attack_sword = 0
        attack_bow = 0
        attack_axe = 0
        attack_club = 0
        attack_knife = 0
        attack_staff = 0
        attack_magic_f = 0
        attack_magic_i = 0
        attack_magic_l = 0


        #Character Skill Modifiers



        #Character stats
        self.health_points = health_points
        self.health_capacity = health_capacity
        self.strength = strength
        self.endurance = endurance
        self.intelligence = intelligence
        self.agility = agility
        self.dexterity = dexterity
        self.charisma = charisma
        self.wisdom = wisdom
        self.perception = perception

        #greetings
        self.greetings_lst_warm = ["Well met friend", "Hello", "Pleased to meet you", "Salutations", "Good day to you",
                              "Well be with you", "Blessings to thee"]

        self.greetings_lst_guarded = ["Mind yourself", "Keep your distance", "We've little to say to each other"]

        self.greetings_lst_hostile = ["Be warned", "Fuck off", "You might die today", "Back away cockroach", "Your face offends me"]

    def introduce_self_warm(self):
        random_greeting = random.randint(0,len(self.greetings_lst_warm)-1)
        greeting = self.greetings_lst_warm[random_greeting]
        return f"{greeting}, my name is {self.name} of {self.birthplace}. I am a {self.trade} by trade."

    def introduce_self_guarded(self):
        random_greeting = random.randint(0,len(self.greetings_lst_guarded)-1)
        greeting = self.greetings_lst_guarded[random_greeting]
        return f"{greeting}........my name is {self.name}. The rest is none of your business."

    def introduce_self_hostile(self):
        random_greeting = random.randint(0,len(self.greetings_lst_hostile)-1)
        greeting = self.greetings_lst_hostile[random_greeting]
        return f"{greeting}. My name is {self.name} and I have no tolerance for your kind."

    def explain_allignment(self,allignment):

        if allignment == "Lawful Good":
            return ("'I fight for the good of the realm and its people. I've sworn to uphold the law and defend those "
                    "who cannot defend themselves. On my honor, I oppose all evil and wield my powers for that which is pure and good.'")

        elif allignment == "Neutral Good":
            return ("'Truly, there is good in this world, and I seek to preserve it. Though surely the world is more complex than simply 'good' and 'evil'. The tree that does not bend may one day break. "
                    "The law may guide us, but must we not all draw our own conclusions about right and wrong? I pray I find the wisdom to know the difference when it counts.'")

        elif allignment == "Chaotic Good":
            return ("'There's a lot of good to be done in this world...........no reason why I can't also get paid in the process. There's no greater wealth than freedom, "
                    "but a little bit of coin here and there never hurt either. I hate a bully, and I don't abide the cruel and sadistic types. For me though, I'm really just here for the wild ride.'")

        elif allignment == "Lawful Neutral":
            return ("'I have a code, as should we all. The world isn't about right and wrong, it's about tradition and order and discipline. Without that, we have nothing. "
                    "Without rules we are but beasts in the wilderness. I do things by the book, even if I don't always agree with every chapter.'")

        elif allignment == "True Neutral":
            return ("'Right and wrong, good and evil.........illusions, all of it.The only thing that's ever been real is power. This world was here long before me and it will remain long after I'm gone. I don't waste my time trying to change things I can't control. "
                    "I do fair work for fair pay......and you most definitely better pay me if you know what's good for you.'")

        elif allignment == "Chaotic Neutral":
            return ("'I go where I want, I do what I want, and I care about exactly one person's opinion.....mine. You won't catch me praying to some religion or worrying about made up nonsense like morality. We come into this life alone, "
                    "and we leave it alone. I don't apologize for what happens inbetween and I didn't ask for anyone's sympathy.'")

        elif allignment == "Lawful Evil":
            return ("'I will impose order upon this broken world...by any means necessary. Freedom is an illusion. We all serve a master. I will bring all who oppose me to heel and be that master."
                    " Only pain and fear can truly purify this world of its weakness. A new tomorrow will be forged, in blood and fire if it must.'")

        elif allignment == "Neutral Evil":
            return ("'The world is unfortunately a place of predators and prey, puppets and puppeteers. This is simply the order of things and the nature of life. Must not all life be built upon death? Is every mouth not a slaughter house? "
                    "Is every stomach not a graveyard? If I must be something in this world, I'll always choose to be the axe rather than the tree.'")

        elif allignment == "Chaotic Evil":
            return ("'Should I burn down your house with your family inside? Or wait until they're all gone so they can come home to the rubble? "
                    "What's maximum fun? I'm here for the laughs, it's not my fault your horribe death is so funny.'")


class Mage(Player):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade,health_points,
                 health_capacity, strength, endurance,intelligence,wisdom, agility, dexterity, charisma, perception, armor_rating, mana_points, mana_capacity):
        super().__init__(name,age,birthplace, allignment, demeaner, origin, trade, health_points, health_capacity, strength, endurance,
                 intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

        self.mana_points = mana_points
        self.mana_capacity = mana_capacity
        self.player_class = "Mage"

    def __repr__(self):
        return "The central mage class"

    def mage_declaration(self):

        return (f"'I am a mage, a student of the deeper mysteries. I wield the twisting arcane forces of nature and beyond. I can restore life or blast it away in ice and fire.'")


    def arcane_blast(self,target):
        damage = 12 - (0.1*target.endurance) - (0.1*target.agility)
        target.health_points -= damage


class Knight(Player):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade,health_points,
                 health_capacity, strength, endurance,intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating):
        super().__init__(name,age,birthplace, allignment, demeaner, origin, trade, health_points, health_capacity, strength, endurance,
                 intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

        self.weapon_damage = 1
        self.blood_rage = 0
        self.player_class = "Knight"

    def __repr__(self):
        return "central knight class"

    def knight_declaration(self):
        return ("'I am a wielder of the shield and blade. My noble art is ancient and deadly."
                "The rigor of my training is matched only by the greatness of my house. "
                "All those who oppose me will fall before my sword'")

    def swing_weapon(self,target):
        damage = (self.strength * self.weapon_damage) - (target.endurance * 0.1) - (target.agility * 0.1)
        target.health_points -= damage


class Brute(Player):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade,health_points,
                 health_capacity, strength, endurance,intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating):
        super().__init__(name,age,birthplace, allignment, demeaner, origin, trade, health_points, health_capacity, strength, endurance,
                 intelligence, wisdom, agility, dexterity, charisma, perception,armor_rating)

        self.player_class = "Brute"

    def brute_declaration(self):
        return "'I learned to fight on the streets and in the pits, not in some castle. Fuck with me at your peril. If you try to take what's mine, I'll happily take your miserable life.'"




class Rogue(Player):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade, health_points,
                 health_capacity, strength, endurance, intelligence, wisdom, agility, dexterity, charisma, perception,
                 armor_rating):
        super().__init__(name, age, birthplace, allignment, demeaner, origin, trade, health_points, health_capacity,
                         strength, endurance,
                         intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

        self.player_class = "Rogue"

    def rogue_declaration(self):
        return "'The night and shadows are my oldest friends. Silence is my native language. You fear the darkness. You should. I will stalk you and snatch your life away.......unseen and unknown.'"


class Hospitaller(Knight):
        def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade,health_points,
                 health_capacity, strength, endurance,intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating):
            super().__init__(name,age,birthplace, allignment, demeaner, origin, trade, health_points, health_capacity, strength, endurance,
                     intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

        def explain_subclass(self):
            return ("The hospitallers of Thripsia are a small but ancient order, trained in the art of restoring and preserving life, "
                    "as well as taking it. Traditionally, hospitaller knights have served as medics and battlefield "
                    "surgeons in the northern provincial armies. In The Shattering's wake, their order was one of the first to "
                    "enter the plague lands as missionaries to the sick and dying. In addition to their medic skills, hospitallers call on magic "
                    "from The Inner-Light to both heal and protect. This class has increased natural resistance to The Hungry-Rot"
                    " and can linger unprotected in the plague lands longer than most.")


        def quote(self):
            return "'With bandage, sword, and the light, I will protect all those who would heal this shattered world.'"


class Executioner(Knight):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade, health_points,
                 health_capacity, strength, endurance, intelligence, wisdom, agility, dexterity, charisma, perception,
                 armor_rating):
        super().__init__(name, age, birthplace, allignment, demeaner, origin, trade, health_points, health_capacity,
                         strength, endurance,
                         intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

    def explain_subclass(self):
        return ("The 'Executioners' were once highborn lords of Korgoth sent to oversee Tyrus the III's "
                "extermination camps along the border of the plague lands. For 15 years they tortured "
                "and slaughtered the refugees of Sylmafi until their souls were left twisted and hollow. Long term exposure to the "
                "Hungry Rot have left most of these knights horribly disfigured as well. After The Dying of The Light, and the sundering of "
                "the camps, only a handful of executioners remain. With King Tyrus dead and gone, they wander the abysall kingdoms, using blade "
                "and blood magic to assert their will. This sub-class is completey immune to the Hungry Rot and can roam the plague lands freely")

    def quote(self):
        return "'With screams and horror, all will know the loving purity of my blade.'"



class Bulwark(Knight):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade, health_points,
                 health_capacity, strength, endurance, intelligence, wisdom, agility, dexterity, charisma, perception,
                 armor_rating):
        super().__init__(name, age, birthplace, allignment, demeaner, origin, trade, health_points, health_capacity,
                         strength, endurance,
                         intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)



    def explain_subclass(self):
        return ("Bulwarks are knights that have spent their lives in a specific kind of training usually reserved "
                "for the biggest and strongest of warriors. They favor thick heavy armor, nearly impenetrable to ranged attacks. Bulwarks "
                "are also infamous for weilding absurdly large shields and weapons, too heavy for most fighters to lift let alone swing. "
                "Their brutal training has given them extraordinary stamina and endurance. It is said that a bulwark knight can fight for "
                "days without rest in even the most ferocious of battles. When locking shields as a unit, their power has been compared to "
                "battling a mountain or an avalanche. In the early days of Darius Callan's first invasion, an outnumbered force of bulwark knights "
                "held the line for nearly a week before reinforcements could arrive. This subclass has access to unique weapons and armor, "
                "unusable by other disciplines.")

    def quote(self):
        return ("'Enemies break upon my shield like waves upon a rocky shore. They "
                "split like firewood under the weight of my axe.' ")



class Champion(Knight):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade, health_points,
                 health_capacity, strength, endurance, intelligence, wisdom, agility, dexterity, charisma, perception,
                 armor_rating):
        super().__init__(name, age, birthplace, allignment, demeaner, origin, trade, health_points, health_capacity,
                         strength, endurance,
                         intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

    def explain_subclass(self):
        return ("By far the most common form of knight found in the Northern Provinces. Historically, "
                "Champions are usually the first or second born sons of noble families, trained to represent their "
                "house in tournment and battle. Although typically male, in the Shattering's aftermath, many daughters have likewise "
                "chosen the path of the sword. This subclass is easily the most well-rounded of all the knights, versatile and well trained on "
                "all fronts. In addition to their abilities with sword and shield and mace, this subclass recieves a bonus to riding skill and "
                "can ride on horse back longer and faster than all others.  ")

    def quote(self):
        return "'Being born into a noble house.....family, honor, oaths, training. It all just comes with the territory.'"



class BloodMage(Mage):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade, health_points,
                 health_capacity, strength, endurance, intelligence, wisdom, agility, dexterity, charisma, perception,
                 armor_rating):
        super().__init__(name, age, birthplace, allignment, demeaner, origin, trade, health_points, health_capacity,
                         strength, endurance,
                         intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

    def explain_subclass(self):
        return ("One of the most feared and reviled groups in the northern provinces, if not the entire world, blood mages are a force "
                "of terror and depravity. Typically having backgrounds in other forms of magic, blood mages are individuals that at "
                "some point became enamered with teachings from the ancient, long dead sorcerer, Quae-Tetra-Viriditas. The now forbidden text "
                "he authored, The 'Kuzima Maisha', nearly destroyed the world and provoked a war so terrible its said to have ripped a hole in the sky. "
                "Modern day bloodmages are those who've taken up Viriditas' studies for one purpose, to summon and control demons. "
                ""
                "Their magic is focused on weakening and consuming the life-force of others, as well as imbuing themselves with demonic abilities. This class requires "
                "the use of human sacrifice to temporarily raise powerful demons from The Burning Void. Considering their reputation, blood mages often "
                "take pains to conceal their identity, and are practiced liars. This class recieves a bonus to all deception skills. Still, it is common "
                "for people to report feeling intense waves of sudden dread when a blood mage is close.  ")



    def quote(self):
        return "'Give me your flesh, and I'll show you the most beautiful nightmares.'"


class ShadowMage(Mage):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade, health_points,
                 health_capacity, strength, endurance, intelligence, wisdom, agility, dexterity, charisma, perception,
                 armor_rating):
        super().__init__(name, age, birthplace, allignment, demeaner, origin, trade, health_points, health_capacity,
                         strength, endurance,
                         intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

    def quote(self):
        return "'All that we see. All that we are.....but a dream within a dream.'"

    def explain_subclass(self):
        return ("The children of nocturnea, otherwise known as Shadow Mages, are an enigmatic and secretive group of magic "
                "users. The exact nature of their power is still poorly understood. They are, at their core, acolytes of Salacea "
                "Miribilis: the night goddess. These mages have made a perilous pilgrimage to the remote Eastern desert known as The Shadow Lands, and "
                "returned as something not entirely human. They exist mostly in our world, while also existing partially.....somewhere else. "
                "Shadow Mages have been known to pass through walls like ghosts, as well as render themselves invisible. Some even claim these "
                "mages have the power to shapeshift into any human being who's life they've taken. This subclass has the highest stealth rating in the game. ")



class LifeSpring(Mage):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade, health_points,
                 health_capacity, strength, endurance, intelligence, wisdom, agility, dexterity, charisma, perception,
                 armor_rating):
        super().__init__(name, age, birthplace, allignment, demeaner, origin, trade, health_points, health_capacity,
                         strength, endurance,
                         intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

    def quote(self):
        return "'May you live and be well, for where there is life there is potential.'"

    def explain_subclass(self):
        return ("Life Spring mages are dedicated servants of The Inner Light and can summon powerful entities for both healing and protection. "
                "Their order's history long pre-dates the Sylmafi Empire and has represented the people's main source of hope and healing "
                "across generations. Their soothing presence has been felt at nearly every catalysm in recorded history, including being the very first "
                "northerners to enter the plague lands. Their monasteries remain in the wake of The Shattering and can often be found in places "
                "one might not expect. Life Springs are completely immune to The Hungry Rot as well as all other disease and negative status effects. "
                "They also possess the ability to bless others with resistance, allowing them temporary access to the plague lands. Due to this subclass' "
                "revered history, charmisa is boosted in the presence of good and neutral allignments, while degraded in the presence of evil ones.  ")



class ElementalMage(Mage):
    def __init__(self, name, age, birthplace, allignment, demeaner, origin, trade, health_points,
                 health_capacity, strength, endurance, intelligence, wisdom, agility, dexterity, charisma, perception,
                 armor_rating):
        super().__init__(name, age, birthplace, allignment, demeaner, origin, trade, health_points, health_capacity,
                         strength, endurance,
                         intelligence, wisdom, agility, dexterity, charisma, perception, armor_rating)

    def quote(self):
        return "'You couldn't fathom the natural forces I contend with'"

    def explain_subclass(self):
        return ("Easily the most common practioner of magic in The Abyssal Kingdoms, elementals harness the destructive forces "
                "of nature. Elemental mages typically specialize in one specific form of destructive magic, though it's not unheard of "
                "for some to pursue a more generalist vocation. At its height, the Sylmafi Empire trained entire battalions of fire mages, "
                "terrifying and devastating their enemies. This class deals the greatest offensive damage and can negotiate obstacles "
                "otherwise impassable to others. For instance, elementals may burn away fallen trees or freeze a lake to cross to the other side.")
