##############################################################################
## BATTLE SYSTEM!!!!!!
# don't allow mid-battle saves, it might mess things up...

# battle text is a special character
define bt = Character(None, window_background="gui/textbox.png") #you can replace the textbox image, font, whatever else
# add these in if you want: #what_font="", what_size=, what_color=""

# player stat values are set by a list so it can check the corresponding stat to what level you are
define HPvalues = [0, 30,34,42,48,50, 54,58,62,68]
define ATKvalues = [0, 5,6,8,9,12, 15,19,23,27,32]
define DEFvalues = [0, 3,4,5,7,9, 12,14,17,20,23]
define LUCvalues = [0, 1,2,4,6,7, 9,10,12,13,15]
define burn = False
define sugar = False
define heart = False
define guard = False
define e1 = False
define e2 = False

label pre_battle:

    ## put this block at the beginning of your start label
    python:
        # disable rollback during battle
        battling = False
        renpy.suspend_rollback(battling)

        # battle stats
        playerLV = 1
        playerMAXHP = HPvalues[9]
        playerHP = HPvalues[9]
        playerATK = ATKvalues[5]
        playerDEF = DEFvalues[5]
        playerLUC = LUCvalues[1]
        playerEXP = 0

        # calculate exp to next level
        nextEXP = round( 0.04 * (playerLV ** 3) + 0.8 * (playerLV ** 2) + 2 * playerLV)
        # this formula is from disgaea, apparently!
        # http://howtomakeanrpg.com/a/how-to-make-an-rpg-levels.html

        # enemy defaults
        enemyHP = 1
        seen_enemies = []
    #

    # put the rest of this in script.rpy wherever you want the enter a battle

    scene ca ves # fullscreen background
    show stage bg # frame the characters stand inside (feel free to remove)

    play music "Red Gaze Battle!.opus"

    # set the enemy to fight
    $ enemy = m_goop

    # and show their sprite!
    show enemy goop idle at battle_enemy1, zoomx(3)

label battle_start:

    #SETUP TIME
    python:
        _game_menu_screen = None
        _history = False
        quick_menu = False

        battling = True
        turn = 0
        battle_events = [] # tracks one-time conditional lines

        atkbuff = 0
        defbuff = 0
        CRIT = False
        consecutive_miss = 0

        enemy.see_enemy()
        enemyHP = enemy.MAXHP

    show player syrup idle at battle_party1, zoomx(3) behind enemy

    bt "[enemy.name!t] picks a fight!!"

    show screen battleoverlay
label battle_turn:
    # start of player turn
    $ turn += 1
    $ guard = False

    call screen battle_menu

label battle_attack:
    # damage calculation
    $ damage = playerATK*2 + atkbuff - enemy.DEF*2
    bt "Red Gaze kicks!"
    show player attack

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # no chance of miss if enemy has lower luck
    if enemy.LUC>playerLUC:
        if d6roll < 4 and consecutive_miss < 2: # never miss 3 times in a row
            jump battle_miss

    # reaching this line means you didn't miss, so reset the counter
    $ consecutive_miss = 0

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.5)

    jump battle_damage

label battle_attackk:
    # damage calculation
    $ damage = playerATK*3 + atkbuff - enemy.DEF*2
    $ burn = True
    bt "Red Gaze attacks!"
    show player attackk

    # roll for crits/misses
    $ d6roll = renpy.random.randint(1, 6)

    # no chance of miss if enemy has lower luck
    if enemy.LUC>playerLUC:
        if d6roll < 4 and consecutive_miss < 2: # never miss 3 times in a row
            jump battle_miss

    # reaching this line means you didn't miss, so reset the counter
    $ consecutive_miss = 0

    # 1 in 6 chance of critical hit
    if d6roll==3:
        $ CRIT = True
        $ damage = int(damage*1.5)

    jump battle_damage

label battle_miss:
    show screen showmiss
    show enemy dodge
    bt "[enemy.name!t] dodged it!"
    $ consecutive_miss += 1
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
        show screen showcrit
    else:
        show screen showdamage("enemy")

    show enemy hit
    if CRIT:
        bt "NICE HIT!!" with vpunch
    else:
        rg "TAKE THAT!"
    $ CRIT= False

label battle_attack_result:

    if enemyHP <= 0:
        jump battle_won

    show player idle
    show enemy idle

    jump battle_enemy_turn

label battle_defend:
    $ guard = True
    show player guard
    bt "Red Gaze is guarding!"
    jump battle_enemy_turn

label battle_sugar:
    $ sugar = True
    show player guard
    bt "Red Gaze, uh... Throws some sugar at her foe, I guess."
    jump battle_enemy_turn

label battle_heart:
    $ heart = True
    show player guard
    bt "Red Gaze decides to be a vegan."
    rg "Oh, put a sock in it."
    rg "Blegh, I don't remember it being this sour!"
    jump battle_enemy_turn

##############################################################################
## ENEMY TURN

label battle_enemy_turn:

    if burn:
        "Hero minion burns!"
        # can't deal negative damage
        $ damage = playerATK
        if damage < 0:
            $ damage = 0
        $ enemyHP -= damage
        # enemy can't have negative hp
        if enemyHP < 0:
            jump battle_won

    if burn and sugar:
        "Hero minion burns badly!"
        # can't deal negative damage
        $ damage = playerATK*2
        if damage < 0:
            $ damage = 0
        $ enemyHP -= damage
        # enemy can't have negative hp
        if enemyHP < 0:
            jump battle_won

    if guard and heart:
        "Hero minion is hurt by poison!"
        # can't deal negative damage
        $ damage = playerATK
        if damage < 0:
            $ damage = 0
        $ enemyHP -= damage
        # enemy can't have negative hp
        if enemyHP < 0:
            jump battle_won

    show enemy attack

    $ d12roll = renpy.random.randint(1, 12)

    if d12roll < 6:
        jump battle_enemy_damage

    if d12roll > 6:
        jump battle_enemy_damage2

    else:
        jump battle_enemy_damage3

label battle_enemy_damage:

    bt "[enemy.name!t] unleashes his true power!!"

    $ e1 = True

    $ damage = (enemy.ATK*4 - playerDEF*2 - defbuff)

    if guard: #halve damage
        $ damage = int(damage/2)

    if guard and heart:
         $ damage = int(damage/3)

    if damage <= 0: #can't do negative damage
    #always take at least 1 damage unless you guard
        if guard:
            $ damage = 4
        if guard and heart:
            $ damage = 5
        else:
            $ damage = 6

    # now apply to syrup...
    $ playerHP -= damage
    if guard and heart:
        $ damage = 5

    if playerHP<=0:
        $ playerHP = 0

    show screen showdamage("player")

    if guard and playerHP > 0:
        show player guardhit
    else:
        show player hit

    # different text for different damage results
    if guard and playerHP > 0:
        if damage>0:
            rg "That's not gonna be enough!"
        else:
            bt "PERFECT BLOCK!"
    else:
        rg "OOF!"

label battle_enemy_turn_end:
    show player idle
    show enemy idle
# you lose when your HP runs out
    if playerHP <= 0:
        jump battle_lost
# if you hit 25% health, warn the player
    if playerHP <= playerMAXHP/4:
        if "lowHP" not in battle_events:
            jump battle_lowhp

    jump battle_turn

label battle_lowhp:
    rg "Ugh, not bad...!"
    $ battle_events.append("lowHP")
    jump battle_turn


label battle_lost:
    hide screen battleoverlay

    show player down
    bt "DEFEAT..."
    jump pre_battle

label battle_won:
    hide screen battleoverlay

    show player win
    show enemy down

    stop music fadeout 1

    bt "HERO STOPPED!"
    jump victory

    # gain exp and possibly level up
    if not playerLV==10: # level cap
        $ playerEXP += enemy.EXP
        bt "Red Gaze gains [enemy.EXP] experience points!"
        if playerEXP >= int(nextEXP):
            call levelup

    jump battle_done

label battle_enemy_damage2:

    bt "[enemy.name!t] attacks!"

    $ e2 = True

    $ damage = (enemy.ATK*6 - playerDEF*2 - defbuff)

    if guard: #halve damage
        $ damage = int(damage/2)

    if guard and heart:
         $ damage = int(damage/3)

    if damage <= 0: #can't do negative damage
    #always take at least 1 damage unless you guard
        if guard:
            $ damage = 8
        if guard and heart:
            $ damage = 8
        else:
            $ damage = 8

    # now apply to syrup...
    $ playerHP -= damage
    if guard and heart:
        $ damage = 8

    if playerHP<=0:
        $ playerHP = 0

    show screen showdamage("player")

    if guard and playerHP > 0:
        show player guardhit
    else:
        show player hit

    # different text for different damage results
    if guard and playerHP > 0:
        if damage>0:
            rg "That's not gonna be enough!"
        else:
            bt "PERFECT BLOCK!"
    else:
        rg "OOF!"

    jump battle_turn

label battle_enemy_turn_end2:
    show player idle
    show enemy idle
# you lose when your HP runs out
    if playerHP <= 0:
        jump battle_lost
# if you hit 25% health, warn the player
    if playerHP <= playerMAXHP/4:
        if "lowHP" not in battle_events:
            jump battle_lowhp

    jump battle_turn

label battle_lowhp2:
    rg "Ugh, not bad...!"
    $ battle_events.append("lowHP")
    jump battle_turn


label battle_lost2:
    hide screen battleoverlay

    show player down
    bt "DEFEAT..."
    jump pre_battle

label battle_won2:
    hide screen battleoverlay

    show player win
    show enemy down

    stop music fadeout 1

    bt "HERO STOPPED!"
    jump victory

    # gain exp and possibly level up
    if not playerLV==10: # level cap
        $ playerEXP += enemy.EXP
        bt "Red Gaze gains [enemy.EXP] experience points!"
        if playerEXP >= int(nextEXP):
            call levelup

    jump battle_done

label battle_enemy_damage3:

    bt "Red Gaze is Stunned!"

    $ damage = (enemy.ATK - playerDEF*4 - defbuff)

    if guard: #halve damage
        $ damage = int(damage/2)

    if guard and heart:
         $ damage = int(damage/3)

    if damage <= 0: #can't do negative damage
    #always take at least 1 damage unless you guard
        if guard:
            $ damage = 2
        if guard and heart:
            $ damage = 1
        else:
            $ damage = 3

    # now apply to syrup...
    $ playerHP -= damage
    if guard and heart:
        $ damage = 5

    if playerHP<=0:
        $ playerHP = 0

    show screen showdamage("player")

    if guard and playerHP > 0:
        show player guardhit
    else:
        show player hit

    # different text for different damage results
    if guard and playerHP > 0:
        if damage>0:
            rg "That's not gonna be enough!"
        else:
            bt "PERFECT BLOCK!"
    else:
        rg "OOF!"

    jump battle_enemy_turn

label battle_enemy_turn_end3:
    show player idle
    show enemy idle
# you lose when your HP runs out
    if playerHP <= 0:
        jump battle_lost
# if you hit 25% health, warn the player
    if playerHP <= playerMAXHP/4:
        if "lowHP" not in battle_events:
            jump battle_lowhp

    jump battle_enemy_turn

label battle_lowhp3:
    rg "Ugh, not bad...!"
    $ battle_events.append("lowHP")
    jump battle_turn


label battle_lost3:
    hide screen battleoverlay

    show player down
    bt "DEFEAT..."
    jump pre_battle

label battle_won3:
    hide screen battleoverlay

    show player win
    show enemy down

    stop music fadeout 1

    bt "HERO STOPPED!"
    jump victory

    # gain exp and possibly level up
    if not playerLV==10: # level cap
        $ playerEXP += enemy.EXP
        bt "Red Gaze gains [enemy.EXP] experience points!"
        if playerEXP >= int(nextEXP):
            call levelup

    jump battle_done

##############################################################################
## OUTCOME

label levelup:

    if playerEXP >= int(nextEXP) and not playerLV==10:
        $ playerLV += 1
        # calculate amount of xp needed at your current level
        $ nextEXP = round( 0.04 * (playerLV ** 3) + 0.8 * (playerLV ** 2) + 2 * playerLV)
        #loop here in case you get enough xp to level twice
        jump levelup

    bt "Red Gaze is now level [playerLV]!"
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

    bt "The [enemy.name!t] left behind a \n{color=#007dff}[newitem.name!t]{/color}!"

    hide screen reward