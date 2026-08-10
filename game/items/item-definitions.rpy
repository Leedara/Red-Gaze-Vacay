##############################################################################
# InvItem class

init -2 python:
    class InvItem(store.object):
        def __init__(self, name, image, value, info, id, cost=[]): #if you add any properties, list them up here, too!
            self.name = name #item name (as seen by the player)
            self.image = image #item art
            self.value = int(value) #market price
            self.info = info #item description
            self.id = id #string to be used as a codename
        #!! IMPORTANT !! don't change the order of anything above this line!
            ## INSERT REQUIRED PROPERTIES HERE ##
            self.cost = cost #list of ingredients, only necessary for craftable items
            ## INSERT OPTIONAL PROPERTIES HERE ##

    ## INVITEM FUNCTIONS

        # add item to the list of seen items
        def see(self):
            if self.id not in seen_items:
                seen_items.append(self.id)

        # add crafting recipe to the list of seen recipes
        def see_recipe(self):
            if self.id not in seen_recipes:
                seen_recipes.append(self.id)

        # see the item and add it to your inventory
        def pickup(self, amount=1):
            self.see()
            while amount>0:
                inv.append(self.id)
                amount -= 1

        # discard the item from your inventory
        def toss(self, amount):
            while amount>0:
                inv.remove(self.id)
                amount -= 1

        # exchange gold for an item
        def buy(self, amount):
            global gold

            self.see()

            gold -= self.value*amount
            while amount>0:
                inv.append(self.id)
                amount -=1

        # exchange an item for gold
        def sell(self, amount):
            global gold

            gold += int(self.value*amount/2)
            self.toss(amount)

        # craft an item
        def make(self, amount):

            self.see()

            while amount>0:
                for i in self.cost:
                    inv.remove(i)
                inv.append(self.id)
                made_recipes.append(self.id)
                amount -=1

        #for shop screen--checks that you can afford to buy 1 of any item
        def check_price(self):
            if self.value <= gold:
                return True
            return False

##############################################################################
# more functions! (not part of InvItem)

    # turns the item tuple into the item object
    def set_item(self):

        for i in itemlist:
            if self==i[4]: #checks the id--this is why you can't change the order!!
                return i

    #inventory sorting
    def sortbyname(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.name

    def sortbyprice(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.value

    # for crafting-screens.rpy--checks that you are able to craft at least 1 of the item
    def check_ingredients(craftitem):

        check = 0
        for i in craftitem.cost:
            if inv.count(i) > 0:
                check += 1

        if check == len(craftitem.cost):
            return True

        return False

    # used to check if you have battle items in battle-screens.rpy--but you can make other lists to check for too!
    def check_inv_for(itemtype):
        for i in itemtype:
            if inv.count(i) > 0:
                return True

##############################################################################
# ITEM DEFINITIONS

# INGREDIENTS
define item_water = (_("{color=#f00}Haste Gel{/color}"), "item water", 2,
    _("A light, blue substance. Makes one run faster.{vspace=1} {vspace=1}Being two of the founding members of Mercenary Division 9, Lady Chrona and Heartsplitter have forged a tight bond over the years."), "item_water")

define item_knife = (_("{color=#f00}Tiny Knife{/color}"), "knife", 2,
    _("{size=-2}A simple knife. The blade is too small and dull to fight with.{vspace=1} {vspace=1}Fashioned after the butter knives of Mercenary Division 20. Their Captain used to say that regardless of good or evil, everyone needs to eat.{/size}"), "item_knife")

define item_wheat = (_("{color=#f00}Yulian Wheat{/color}"), "wheat", 2,
    _("{size=-5}Plant-based medicine developed by Yulia the Prodigy. Cures burns. {vspace=1} {vspace=1}Revered for her groundbreaking discoveries in Biology, there is not a soul in the world who haven't heard the name Yulia the Prodigy.{/size}"), "item_wheat")

define item_obsidian = (_("{color=#f00}Voidstone{/color}"), "obsidian", 5,
    _("An ore of unknown origin. Emits an ominous aura under light.{vspace=1} {vspace=1}Looted from the defeated Famous Hero Tiger. Could an otherworldly item like this be how Yulia's brother fell ill?"), "item_obsidian")

define item_paper = (_("{size=-6}{color=#f00}Cloth of the Venerable{/color}{/size}"), "cloth", 400,
    _("{size=-7}Kevrish cloth of Dolor the Venerable. Utterly valuable.{vspace=1} {vspace=1}Somehow, Dolor carried five of his dying comrades through Ord Desert alone. He collapsed ten metres from the city walls.{vspace=1}{vspace=1}It was hidden away deep within Fulham Manor until not long ago.{/size}"), "item_paper")

define item_beet = (_("{color=#f00}Kevrish Silk{/color}"), "dolor", 40,
    _("{size=-6}A piece of soft yet conductive silk. Valuable.{vspace=1} {vspace=1}Some claim that the faraway city of Kevra is overflowing with enchanted fabrics, but surely this is little more than hearsay. Was hidden away deep within Fulham Manor until not long ago.{/size}"), "item_beet")

define item_stone = (_("{color=#f00}Nernas Fragment{/color}"), "frag",20,
    _("{size=-6}Shard of the second strongest Mercenary Nernas' greataxe. Passively increases damage.{vspace=1} {vspace=1}As Nernas weapon clashed with the staff of Famous Hero Calm Leaf, both weapons shattered and rained down upon Mer City.{/size}"), "item_stone")

define item_large = (_("{size=-7}{color=#f00}Large Nernas Fragment{/color}{/size}"), "large",40,
    _("{size=-11}Large shard of the second strongest Mercenary Nernas' axe. Passively increases damage by a lot.{vspace=1} {vspace=1}Riddled with dozens of big pieces of his own greataxe, Nernas tried to take down his foe by detonating his own body in a cataclysmic explosion that eclipsed even the sun. The violent event destabilized the very atmosphere, resulting in heavy storms and rain for several days.{/size}"), "item_large")

define item_herb = (_("{color=#f00}Yulian Wings{/color}"), "herb",5,
    _("Plant-based medicine developed by Yulia the Prodigy. Cures poison.{vspace=1} {vspace=1}When not even Yulia's skills in Biology could cure her brother, she discarded her herbs in favor of more... Questionable methods."), "item_herb")

define item_heart = (_("{color=#f00}Yulian Heart{/color}"), "heart",5,
    _("{size=-6}Plant-based medicine developed by Yulia the Prodigy. Cures slow and makes ones skin become poisonous.{/size}{vspace=1} {vspace=1}{size=-8}Steely Dan and Yulia often have heated debates late into the night. Perhaps they are more than just allies.{/size}"), "item_heart")

# CRAFTABLE
define item_sugar = (_("{color=#f00}Steely Sugar{/color}"), "item sugar", 5,
    _("A protein-rich powder. Reacts with fire, turning Burn into Black Burn.{vspace=1} {vspace=1}Steely Dan's products and gyms were commonplace long before he became a Famous Hero."), "item_sugar",
    ["item_beet", "item_water"])

define item_sucker = (_("{size=-6}{color=#f00}Memento: Chopsticks{/color}{/size}"), "chopsticks", 10,
    _("The chopsticks of Tiny Swallow, Red Gaze's childhood friend.{vspace=1} {vspace=1}Mercenary Division 20 were among the first to be annihilated by the Heroes. Their culinary love is greatly missed in Mer City."), "item_sucker",
    ["item_sugar", "item_paper"])

define item_chain = (_("{color=#f00}Steely Mia's Belt{/color}"), "chain", 10,
    _("{size=-7}A steel chain belt. Worn by the instructors of Steely Gyms.{vspace=1} {vspace=1}Ever since her childhood, Mia greatly looked up to Steely Dan and worked hard to attain great muscles like him. And last year, she was proudly accepted as the first female instructor of Steely Gyms.{/size}"), "item_chain",
    ["item_sugar", "item_chain"])

define item_ring1 = (_("{color=#f00}Saint Aria's Ring{/color}"), "ring1", 1000000,
    _("{size=-6}A wedding ring embedded with a pearl whiter than snow. Insanely valuable.{vspace=1} {vspace=1}One of the Five Sacred Rings. For millennia, Saint Aria has guarded the tomb of her husband Fredrick the Demon Slayer with the extended life and celestial powers of her sainthood. Surely, she would have been a grand challenge in her prime.{/size}"), "item_ring1",
    ["item_sugar", "item_ring1"])

define item_ring2 = (_("Fredrick's Ring"), "ring2", 1000000,
    _("A green wedding ring. A treasure of unfathomable value.{vspace=1} {vspace=1}Belonged to Fredrick, leader of the Demon Slayers. Legend has it, that even the Seven Demon Princes feared Fredrick and his greatsword."), "item_ring2",
    ["item_sugar", "item_ring2"])

define item_sword = (_("Demon Slayer Sword"), "sword", 499999999999,
    _("A broken greatsword. Could never be measured in mere gold.{vspace=1} {vspace=1}Belonged to Fredrick, leader of the Demon Slayers. Said to have broken in his fight against Lucifer, which ended The First War."), "item_sword",
    ["item_sugar", "item_sword"])

define item_roses = (_("{color=#f00}{size=-6}Stone of Roses{/color}"), "roses", 2,
    _("{size=-6}A stone that grants a skill which summons thorns that can heal from Poison.{vspace=1} {vspace=1}Items with these enchanted symbols are said to come from the ancient civilization of a cold, northern land.{/size}"), "item_roses")

define item_untouchable = (_("{color=#f00}Stone of the Untouchable. Pairs well with Stone of Lightning.{/color}"), "untouchable", 2,
    _("A stone that grants a massive increase to Parry damage.{vspace=1} {vspace=1}Items with these enchanted symbols are said to come from the ancient civilization of a cold, northern land. "), "item_untouchable")

define item_fire = (_("{color=#f00}Stone of Fire{/color}"), "fire", 2,
    _("A stone that grants the burning skill Nernas Flameshot.{vspace=1} {vspace=1}Items with these enchanted symbols are said to come from the ancient civilization of a cold, northern land."), "item_fire")

define item_ice = (_("{color=#f00}Stone of Ice{/color}"), "ice", 2,
    _("{size=-6}A stone that grants access to a chilling skill that can Freeze the target.{vspace=1} {vspace=1}Items with these enchanted symbols are said to come from the ancient civilization of a cold, northern land.{/size}"), "item_ice")

define item_lightningg = (_("{color=#f00}Stone of Lightning{/color}"), "lightningg", 2,
    _("{size=-6}A stone that makes your Kick-skill build up Charge instead of dealing damage. At certain stacks of Charge, new skills can be used.{vspace=1} {vspace=1}Items with these enchanted symbols are said to come from the ancient civilization of a cold, northern land.{/size}"), "item_lightningg")

define item_luck = (_("{color=#f00}{size=-6}Stone of Luck{/color}"), "luck", 2,
    _("{size=-6}A stone that grants a skill which weakens Brutal Hits, but makes them more common. Pairs well with Stone of Ice.{vspace=1} {vspace=1}Items with these enchanted symbols are said to come from the ancient civilization of a cold, northern land.{/size}"), "item_luck")

define item_sisyphus = (_("{color=#f00}Stone of Sisyphus{/color}"), "sisyphus", 2,
    _("{size=-6}Just an abnormally heavy stone. Will grant no benefits to its carrier.{vspace=1} {vspace=1}Items with these enchanted symbols are said to come from the ancient civilization of a cold, northern land. However, this is just an ordinary rock.{/size}"), "item_sisyphus")

define item_end = (_("{color=#f00}Stone of the End{/color}"), "end", 2,
    _("A stone that grants a powerful skill at death's door.{vspace=1} {vspace=1}Items with these enchanted symbols are said to come from the ancient civilization of a cold, northern land."), "item_end")

##############################################################################
# ITEM LISTS

# ALL ITEMS (every single one!!)
define itemlist = [
    item_water,
    item_paper,
    item_beet,
    item_sugar,
    item_sucker,
    item_stone,
    item_herb,
    item_heart,
    item_wheat,
    item_obsidian,
    item_chain,
    item_ring1,
    item_ring2,
    item_sword,
    item_large,
    item_knife,
    item_roses,
    item_fire,
    item_ice,
    item_lightningg,
    item_luck,
    item_sisyphus,
    item_end,
    item_untouchable
    ]

# all items that can be crafted
define allrecipes = [
    "item_sugar",
    "item_sucker"
    ]

# all items that can be used in battle
define battle_items = [
    "item_sucker"
    ]

## INSERT NEW RECIPE LISTS HERE ##

# for recipes screen
define recipelists = [ allrecipes, battle_items ]
define recipelist_names = [ _("All"), _("Battle") ]
