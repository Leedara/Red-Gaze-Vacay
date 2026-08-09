##############################################################################
## BATTLE SYSTEM!!!!!!
# don't allow mid-battle saves, it might mess things up...

# battle text is a special character
define bt = Character(None, window_background="gui/textbox.png") #you can replace the textbox image, font, whatever else
# add these in if you want: #what_font="", what_size=, what_color=""

# player stat values are set by a list so it can check the corresponding stat to what level you are
define HPvalues = [0, 30,34,42,48,50, 54,58,62,260]
define ATKvalues = [0, 5,6,8,9,12, 15,19,23,27,32]
define DEFvalues = [0, 3,4,5,7,9, 12,14,17,20,23]
define LUCvalues = [0, 1,2,4,6,7, 9,10,12,13,15]
define burn = False
define sugar = False
define guard = False
define e1 = False
define e2 = False
define lohp = False
define poison = False
define parry = False
define frozen = False
define two = False
define four = False
define bburn = False

default battling = False

default playerLV = 1
default playerMAXHP = HPvalues[9]
default playerHP = HPvalues[9]
default playerATK = ATKvalues[5]
default playerDEF = DEFvalues[5]
default playerLUC = LUCvalues[1]
default playerEXP = 0

        # calculate exp to next level
# exp needed to reach level 2. this formula is from disgaea, apparently!
# http://howtomakeanrpg.com/a/how-to-make-an-rpg-levels.html
default nextEXP = round( 0.04 * (1 ** 3) + 0.8 * (1 ** 2) + 2 * 1 )

# enemy defaults
default enemyHP = 1
default seen_enemies = []

# which background the battle is fought against. the caller sets this.
default battle_bg = "ca ves"
##############################################################################
## ENTERING A BATTLE
#
# CALL this, don't jump to it -- the battle returns to whatever comes next:
#
#     $ enemy = m_crab
#     $ battle_bg = "be ach"
#     call pre_battle
#     # ...the story picks up again right here once the fight is over
#
label pre_battle:

    scene expression battle_bg # fullscreen background
    show stage bg # frame the characters stand inside (feel free to remove)

    play music "Red Gaze Battle!.opus"

    # show the enemy's sprite. this uses the "enemy" tag, which is why every
    # "show enemy hit" / "show enemy down" below keeps working no matter which
    # enemy is on screen -- Ren'Py holds on to the enemy's own attribute.
    $ renpy.show(enemy.sprite + " idle", at_list=[battle_enemy1, zoomx(3)])

label battle_start:

    #SETUP TIME
    python:
        _game_menu_screen = None
        _history = False
        quick_menu = False

        battling = True
        turn = 0
        charge = 0
        battle_events = [] # tracks one-time conditional lines

        atkbuff = 0
        defbuff = 0
        CRIT = False

        # Set to false here so things like burning and poisoning does not persist between battles.
        burn = False
        sugar = False
        heart = False
        guard = False
        e1 = False
        e2 = False
        lohp = False
        poison = False
        parry = False
        frozen = False
        two = False
        four = False

        # start every battle (and every retry after a defeat) at full health
        playerHP = playerMAXHP


        enemy.see_enemy()
        enemyHP = enemy.MAXHP

    show player syrup idle at battle_party1, zoomx(3) behind enemy

    n "[enemy.name!t] picks a fight!!"

    show screen battleoverlay

label battle_turn:
    # start of player turn
    $ turn += 1
    $ guard = False
    show enemy idle at battle_enemy1, zoomx(3)
    show player syrup idle at battle_party1, zoomx(3) behind enemy
    play music "Red Gaze Battle!.opus"
    if parry:
        play music "Red Gaze Battle!.opus"
        hide player syrup parry
        show player syrup idle at battle_party1, zoomx(3) behind enemy
        show enemy idle at battle_enemy1, zoomx(3)
    if untouchable:
        play music "Red Gaze Battle!.opus"
        hide blightt
        show player syrup idle at battle_party1, zoomx(3) behind enemy
        show enemy idle at battle_enemy1, zoomx(3)
    
    if lohp:
        show player idlez
    if burn:
        show enemy goop idle burn
    if burn and sugar:
        show enemy goop idle bburn
    if not lohp and not charge > 9 and charge > 4:
        show player syrup electro
        play sound "electroo.mp3"
    if not lohp and charge > 9:
        show player syrup kerauno
        play sound "keraunoo.mp3"
    call screen battle_menu

label battle_secret:

        $ InvItem(*item_stone).pickup(1)
        n "Found a Nernas Shard!"
        $ Shard_hunter.grant()
        rg "Dude, we are in the middle of a fight."
        n "Stop complaining, or I'll use another protagonist for the main game."

label battle_attack:
    # damage calculation
    $ damage = playerATK + atkbuff - enemy.DEF*2
    n "Red Gaze kicks!"
    show player syrup attack
    play sound "kick.mp3"

    if frozen:
        $ damage = playerATK*2.5 + atkbuff - enemy.DEF*2
        n "Red Gaze breaks the Frozen foe!"
        $ frozen = False
        show player syrup attack
        play sound "kick.mp3"

    if electro:
        $ charge += 1
        $ damage = playerATK*0
        jump battle_enemy_turn

    if lohp:
        show player syrup attackz

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.5)

    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

    if charge==7:
        n "Nice! But you can stop now."

    if charge==8:
        n "That is literally not how you stop."

    if charge==9:
        n "I realize now that you are ignoring me. Real mature."
        rg "Let them play the way they want to!"
        n "Don't you have a skill to use?"
        rg "Pft-"

label battle_thunder:

    $ damage = playerATK*5.5 + atkbuff - enemy.DEF*2
    show player syrup lightning 
    play sound "hollow.mp3"
    jump battle_damage

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.5)

    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_serpent:
    $ poison = False
    $ damage = playerATK*7.5 + atkbuff - enemy.DEF*2
    show player syrup lightning 
    play sound "hollow.mp3"
    jump battle_damage

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.5)

    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_keraunos:

    $ Lyra_Thorsdottir.grant()
    $ charge -= 10
    $ damage = playerATK*8 + atkbuff - enemy.DEF*2
    show player keraunos
    play sound "kerau.mp3"
    jump battle_damage

label battle_frost:
    show player syrup hail
    # damage calculation
    $ damage = playerATK*3 + atkbuff - enemy.DEF*2
    n "Red Gaze attacks!"
    play sound "ice.mp3"

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll > 2:
        $ frozen = True
        $ damage = int(damage*2.1)
        n "Target is Frozen!"    

    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:
        jump battle_miss

label battle_rose:
show player syrup vines
$ damage = playerATK*3 + atkbuff - enemy.DEF*2
rg "Be torn to shreds."

# roll for crits/misses
$ d6roll = renpy.random.randint(1, 6)

# 1 in 6 chance of critical hit
if d6roll==3:
    $ CRIT = True
    $ damage = int(damage*1.4)
    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

if poison:
    show player syrup vines
    play sound "whip.mp3"
    $ damage = int(playerMAXHP/10)
    $ playerHP += damage
    show screen showheal
    if playerHP > playerMAXHP:
        $ playerHP = playerMAXHP

    show player syrup vines
    $ damage = playerATK*3 + atkbuff - enemy.DEF*2
    rg "Be torn to shreds."

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.4)
        jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_fire:
    # damage calculation
    $ damage = playerATK*2.5 + atkbuff - enemy.DEF*2
    $ burn = True
    $ burn_turns = 3
    n "Red Gaze attacks!"
    show player syrup fire
    play sound "flame.mp3"
    if lohp:
        show player syrup firez

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==1:
        $ CRIT = True
        $ damage = int(damage*1.5)

    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_red:
    # damage calculation
    $ damage = playerATK*4 + atkbuff - enemy.DEF*2
    rg "Rip, Muramasa."
    show player syrup red
    play sound "red.mp3"

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.4)

    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_redluck:
    # damage calculation
    $ damage = playerATK*4 + atkbuff - enemy.DEF*2
    rg "Rip, Muramasa."
    show player syrup red
    play sound "red.mp3"

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll < 5:
        $ CRIT = True
        $ damage = int(damage*1.2)
        
        jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_redd:
    $ Last_Resort.grant()    
    # damage calculation
    $ damage = playerATK*9.5 + atkbuff - enemy.DEF*2
    rg "This is the end."
    show player syrup redd
    play sound "red.mp3"
    play sound "sword.mp3"
    play sound "red.mp3"

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.1)

    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_defend:
    $ guard = True
    show player guard
    n "Red Gaze is guarding!"
    jump battle_enemy_turn
    if lohp:
        show player guardz

label battle_slam:
    show player syrup slam
    $ damage = playerATK*3.5 + atkbuff - enemy.DEF*2
    n "Red Gaze is shattering her foe! High Brutal Hit damage."
    $ frozen = False
    jump battle_enemy_turn
    if lohp:
        show player guardz

    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*2.3)

    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_impact:
    show player syrup slam
    $ damage = playerATK*4 + atkbuff - enemy.DEF*2
    n "Red Gaze crushes her victim to pieces! High Brutal Hit damage and chance."
    $ frozen = False
    jump battle_enemy_turn
    if lohp:
        show player guardz

    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if not d6roll==3:
        $ CRIT = True
        $ damage = int(damage*2.3)

    jump battle_damage

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_sugar:
    $ sugar = True
    $ inv.remove("item_sugar")
    show player guard
    n "Red Gaze, uh... Throws some sugar at her foe, I guess."
    jump battle_enemy_turn
    if lohp:
        show player guardz

label battle_poison:
    $ poison = True
    $ poison_turns = 3
    $ inv.remove("item_heart")
    show player guard
    n "Red Gaze decides to be a vegan."
    rg "Oh, put a sock in it."
    rg "Blegh, I don't remember it being this sour."
    rg "Take this!" with hpunch
    n "Enemy is Poisoned!"
    jump battle_enemy_turn
    if lohp:
        show player guardz

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

label battle_miss:
    show screen showmiss
    show enemy dodge
    n "But it missed!"
    jump battle_attack_result

label battle_damage:

    # can't deal negative damage
    if damage < 0:
        $ damage = 0
    $ enemyHP -= damage
    # enemy can't have negative hp
    if enemyHP < 0:
        jump battle_won

    if CRIT:
        show screen showcrit with vpunch and hpunch
        play sound "crit.mp3"
    else:
        show screen showdamage("enemy")

    show enemy hit
    if CRIT:
        n "A BRUTAL BLOW!!" with vpunch and hpunch
        play sound "crit.mp3"
    else:
        rg "TAKE THAT!"
    $ CRIT= False

label battle_attack_result:

    if enemyHP <= 0:
        jump battle_won

    if playerHP <= 0:
        jump pre_battle

        show player idle
        show enemy idle

    jump battle_enemy_turn

##############################################################################
## ENEMY TURN

label battle_enemy_turn:

    if burn and not sugar:
        show enemy goop idle burn
        "Hero Burns!"
        # can't deal negative damage
        $ damage = playerATK
        if damage < 0:
            $ damage = 0
        $ enemyHP -= damage
        # enemy can't have negative hp
        $ burn_turns -= 1

        # Remove burn when it expires
        if burn_turns <= 0:
            $ burn = False
            "The burn wears off."
        if enemyHP < 0:
            jump battle_won

        # Remove burn when it expires
        if burn_turns <= 0:
            $ burn = False
            "The burn wears off."
        if enemyHP < 0:
            jump battle_won

    if burn and sugar:
        show enemy goop idle bburn  
        $ bburn = True  
        n "The flames react with the sugar, transforming into Black Burn!"
        # can't deal negative damage
        $ damage = playerATK*0.5
        if damage < 0:
            $ damage = 0
        $ enemyHP -= damage
        # enemy can't have negative hp
        if enemyHP < 0:
            jump battle_won

    if poison:
        $ poison = True
        "Hero is hurt by Poison!"
        # can't deal negative damage
        $ damage = playerATK*1.5
        if damage < 0:
            $ damage = 0
        $ enemyHP -= damage
        # enemy can't have negative hp
        $ poison_turns -= 1

        # Remove burn when it expires
        if poison_turns <= 0:
            $ Poison = False
            "The Poison wears off."
        if enemyHP < 0:
            jump battle_won

    if poison and burn:
        "The flames boil the poison, turning into Toxic Blaze!"
        # can't deal negative damage
        $ burn = False
        $ poison = False
        $ Nonmetal_alchemist.grant()
        $ damage = playerATK*3.5
        if damage < 0:
            $ damage = 0
        $ enemyHP -= damage
        # enemy can't have negative hp
        if enemyHP < 0:
            jump battle_won

    $ d12roll = renpy.random.randint(1, 12)

    if d12roll < 6:
        jump battle_enemy_damage

    if d12roll > 6:
        jump battle_enemy_damage2

    else:
        jump battle_enemy_damage3

label battle_enemy_damage:

    n "[enemy.name!t] unleashes his true power!!"

    play sound "kick.mp3"

    $ e1 = True

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump enemy_miss

    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.5)

    $ damage = (enemy.ATK*4 - playerDEF*2 - defbuff)

    if guard: #halve damage
        $ damage = int(damage/2)

    if damage <= 0: #can't do negative damage
    #always take at least 1 damage unless you guard
        if guard:
            $ damage = 15
        else:
            $ damage = 30

    # now apply to syrup...
    $ playerHP -= damage
    if guard:
        $ damage = 15
    else:
        $ damage = 30

    if playerHP<=0:
        $ playerHP = 0

    show screen showdamage("player")

    if guard and playerHP > 0:
        show player guardhit
    if lohp and guard and playerHP > 0:
        show player guardhitz
    if lohp and playerHP > 0:
        show player hitz 
    else:
        show player hit

    # different text for different damage results
    if guard and playerHP > 0:
        if damage>0:
            rg "That's not gonna be enough!"
        else:
            n "PERFECT BLOCK!"
    else:
        rg "OOF!"

        jump battle_enemy_turn_end

label battle_enemy_turn_end:
    
    show player idle
    show enemy idle
# you lose when your HP runs out
    if playerHP <= 0:
        jump battle_lost
# if you hit 25% health, warn the player
    if playerHP <= playerMAXHP/3:
        if "lowHP" not in battle_events:
            jump battle_lowhp

    jump battle_turn

label battle_shock:
    show player syrup electro
    jump battle_turn

label battle_keraun:
    show player syrup kerauno
    jump battle_turn

label battle_lowhp:
    rg "Ugh, not bad...!"
    $ lohp = True
    $ battle_events.append("lowHP")
    jump battle_turn

label battle_lost:
    hide screen battleoverlay

    show player down
    n "DEFEAT..."
    jump pre_battle

label battle_won:
    hide screen battleoverlay
    rg "Sayonara capybara!"
    if lohp:
        rg "Ah, gotta fix my hair."

    show player win
    show enemy down

    stop music fadeout 1

    n "[enemy.name!t] STOPPED!"

    # if not playerLV==10: # level cap
    #     $ playerEXP += enemy.EXP
    #     n "Red Gaze gains [enemy.EXP] experience points!"
    #     if playerEXP >= int(nextEXP):
    #         call levelup

    jump battle_end

label battle_enemy_damage2:

$ d6roll = renpy.random.randint(1, 6)

if d6roll < 4:
    $ two = True

    show screen QTEdown(2, "missedit3") #seconds to fail, label to jump on fail
    menu:
        "My, what lovely feet!"
        "PARRY IT!!":
            hide screen QTEdown
            jump choice3

else:
    $ four = True

    show screen QTEdown(4, "missedit3") #seconds to fail, label to jump on fail
    menu:
        "My, what lovely feet!"
        "PARRY IT!!":
            hide screen QTEdown
            jump choice3

label missedit3:
    hide screen QTEdown

    "You failed to parry!"

    $ playerHP -= 40

    play sound "kick.mp3"

    show player hit

    if playerHP <= 0:
        jump battle_lost

    if playerHP <= playerMAXHP/3:
        if "lowHP" not in battle_events:
            show player idlez
            jump battle_lowhp2

    jump battle_turn  

label choice3: 
    show player syrup parry
    $ damage = playerATK
    $ d6roll = renpy.random.randint(1, 6)

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.5)

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump battle_miss

    $ enemyHP -= damage
    # enemy can't have negative hp
    if enemyHP < 0:
        jump battle_won2
    play sound "slooo.mp3" volume 2.0
    queue sound "parry3.mp3" volume 1.5
    n "Devastating!!"
    jump battle_turn

    if untouchable:
        $ damage = playerATK*5

        $ d6roll = renpy.random.randint(1, 6)

        # 1 in 6 chance of critical hit
        if d6roll==3:
            $ CRIT = True
            $ damage = int(damage*1.5)

        $ d10roll = renpy.random.randint(1, 10)

        if d10roll==1:

         jump battle_miss

    if untouchable and charge > 4:       
        show blightt:
          xalign .65
          yalign .5


        $ damage = playerATK*6.5
        $ charge -= 5

        $ d6roll = renpy.random.randint(1, 6)

        # 1 in 6 chance of critical hit
        if d6roll==3:
            $ CRIT = True
            $ damage = int(damage*1.5)

        $ d10roll = renpy.random.randint(1, 10)

        if d10roll==1:

         jump battle_miss

label battle_lowhp2:
    rg "Ugh, not bad...!"
    $ battle_events.append("lowHP")
    show player idlez
    jump battle_turn

label battle_lost2:
    hide screen battleoverlay

    show player down
    n "DEFEAT..."
    jump pre_battle

label battle_won2:
    hide screen battleoverlay
    rg "Sayonara capybara!"
    if lohp:
        rg "Ah, gotta fix my hair."

        show player win
        show enemy down

    stop music fadeout 1

    n "[enemy.name!t] STOPPED!"

    # if not playerLV==10: # level cap
    #     $ playerEXP += enemy.EXP
    #     n "Red Gaze gains [enemy.EXP] experience points!"
    #     if playerEXP >= int(nextEXP):
    #         call levelup

    jump battle_end

label battle_enemy_damage3:

    n "Red Gaze is Stunned!"

    play sound "kick.mp3"

    $ d10roll = renpy.random.randint(1, 10)

    if d10roll==1:

     jump enemy_miss

    $ d6roll = renpy.random.randint(1, 4)

    # 1 in 6 chance of critical hit
    if d6roll==1:
        $ CRIT = True
        $ damage = int(damage*2.5)

    $ damage = (enemy.ATK - playerDEF*4 - defbuff)

    if guard: #halve damage
        $ damage = int(damage/2)

    if damage <= 0: #can't do negative damage
    #always take at least 1 damage unless you guard
        if guard:
            $ damage = 10
        else:
            $ damage = 20

    # now apply to syrup...
    $ playerHP -= damage
    if guard:    
        $ damage = 10
    else:
        $ damage = 20

    if playerHP<=0:
        $ playerHP = 0

    show screen showdamage("player")

    if guard and playerHP > 0:
        show player guardhit
    if lohp and guard and playerHP > 0:
        show player guardhitz
    if lohp and playerHP > 0:
        show player hitz 
    else:
        show player hit

    # different text for different damage results
    if guard and playerHP > 0:
        if damage>0:
            rg "That's not gonna be enough!"
        else:
            n "PERFECT BLOCK!"
    else:
        rg "OOF!"

    jump battle_enemy_turn_end3

label enemy_miss:
    n "But it missed!"
    jump battle_turn

label battle_enemy_turn_end3:
    show player idle
    show enemy idle
# you lose when your HP runs out
    if playerHP <= 0:
        jump battle_lost
# if you hit 25% health, warn the player
    if playerHP <= playerMAXHP/3:
        if "lowHP" not in battle_events:
            show player idlez
            jump battle_lowhp3

    jump battle_enemy_turn

label battle_lowhp3:
    rg "Ugh, not bad...!"
    $ battle_events.append("lowHP")
    $ lohp = True                                                                                                                                                                                                                                                                                                
    jump battle_enemy_turn


label battle_lost3:
    hide screen battleoverlay

    show player down
    n "DEFEAT..."
    jump pre_battle

label battle_won3:
    hide screen battleoverlay
    rg "Sayonara capybara!"
    if lohp:
        rg "Ah, gotta fix my hair."

    show player win
    show enemy idle

    stop music fadeout 1

    n "[enemy.name!t] STOPPED!"

    # gain exp and possibly level up
      # if not playerLV==10: # level cap
    #     $ playerEXP += enemy.EXP
    #     n "Red Gaze gains [enemy.EXP] experience points!"
    #     if playerEXP >= int(nextEXP):
    #         call levelup

    jump battle_end

##############################################################################
## OUTCOME

label levelup:

    if playerEXP >= int(nextEXP) and not playerLV==10:
        $ playerLV += 1
        # calculate amount of xp needed at your current level
        $ nextEXP = round( 0.04 * (playerLV ** 3) + 0.8 * (playerLV ** 2) + 2 * playerLV)
        #loop here in case you get enough xp to level twice
        jump levelup

    n "Red Gaze is now level [playerLV]!"
    # increase stats
    $ playerMAXHP = HPvalues[playerLV]
    $ playerATK = ATKvalues[playerLV]
    $ playerDEF = DEFvalues[playerLV]
    $ playerLUC = LUCvalues[playerLV]

    return

label battle_drops:

    $ newitem = InvItem(*set_item(enemy.drop))
    show screen reward(newitem.image)
    $ newitem.pickup()

    n "The [enemy.name!t] left behind a \n{color=#007dff}[newitem.name!t]{/color}!"

    hide screen reward

label battle_end:
    # put the game back the way it was before the battle started
    python:
        _game_menu_screen = "save"
        _history = True
        quick_menu = True

        battling = False

    # hand control back to whatever did "call pre_battle"
    return