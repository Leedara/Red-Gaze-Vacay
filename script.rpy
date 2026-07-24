define rg = Character("Red Gaze")
define sg = Character("Smiling Golem")
define lc = Character("Lady Chrona")
define bar = Character("Shady Bartender")
define bard = Character("Shady Bartender disguised")
define no = False
define yes = False
define back = False
define start3 = False
define start4 = False
define start5 = False
define start6 = False
define start7 = False

label start:
    
    stop music fadeout 10
   
    python:
        gold = 100 #starting amount
        inv = []
        seen_items = []

        # crafting
        known_recipes = []
        seen_recipes = []
        made_recipes = []
        newitem = ""

        # shop inventory
        market = []

        # quests
        new_quests = []
        active_quests = []
        completed_quests = []

    ## CRAFT/SHOP SETUP
    $ known_recipes = ["item_sugar", "item_sucker"]
    $ market = [ "item_water", "item_paper", "item_beet" ]

    ## INVENTORY SETUP
    $ InvItem(*item_sugar).pickup(1)
    $ InvItem(*item_water).pickup(1)
    $ InvItem(*item_sucker).pickup(1)
    $ InvItem(*item_beet).pickup(1)
    $ InvItem(*item_paper).pickup(1)
    $ InvItem(*item_stone).pickup(1)
    $ InvItem(*item_large).pickup(1)
    $ InvItem(*item_herb).pickup(1)
    $ InvItem(*item_heart).pickup(1)
    $ InvItem(*item_wheat).pickup(1)
    $ InvItem(*item_obsidian).pickup(1)
    $ InvItem(*item_chain).pickup(1)

    "(This world is set in a future where Mercenaries are the main military force. However, a faction of self-proclaimed Heroes have recently appeared, determined to kill all Mercenaries.)"

    "(One such Mercenary is Lyra Sanchez, aka Red Gaze. Despite the ongoing conflict, Red Gaze's unit has been graced with a trip to the beaches near Ord Desert.)"

    "(She has been granted a vacation southwest of Mer City, along with her fellow Mercenaries Smiling Golem and Lady Chrona. There is just one problem - she forgot to bring a swimsuit!)"

    scene be ach
    with dissolve 

    play music "Beach Vibes.opus"

    show lyra

    show crab at right

    show shark:
      xalign 0.9
      yalign 0.6

    show island:
      xalign 0.25
      yalign 0.6

    rg "..."

    sg "Is that a shark over there? Lunch is on me, gir-"

    rg "Gaah, I am burning up!"

    lc "We reminded you to bring a swimsuit last month."

    rg "I know, but... Last month was like a hundred years ago, I can't remember stuff like that."

    sg "I have a knife if you want to get some coconut water!"

label start2:
    scene be ach

    show lyra

    menu:
        "A knife wouldn't hurt, I suppose.":         
            jump choice0_yes
        "Ha ha, funny. No, you can keep both your knife and your humor.":
            jump choice0_no
        "Inventory":
            jump inventory

label inventory:
    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump start2

label choice0_yes:

    "(Red Gaze accepts the knife)"

    $ InvItem(*item_knife).pickup(1)

    $ yes = True

    jump choice0_done

label choice0_no:

    "(Red Gaze declines the knife)"

    $ no = True

    jump choice0_done

label choice0_done:

    rg "Uhh, so hot. Screw this, I am having a drink."

    "(Red Gaze heads over to the bar)"

    bar "What are you buying, stranger?"

label start3:
    scene be ach

    show lyra

    menu:
        "Just some still water. (€7, sounds reasonable)":
            jump choice1_water
        "I'll take a soda. (€10, seems legit)":
            jump choice1_soda
        "One beer, please. (€15, I see nothing wrong with that)":
            jump choice1_beer
        "WHAT ARE THESE UNHOLY PRICES, YOU THIEF?!":
            jump choice1_thief
        "Inventory":
         jump inventor

label inventor:
    
    $ start3 = True    

    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump start3

label choice1_water:

    bar "Heh, my pleasure."

    rg "Aahh, that hit the spot. Time to head back."

    jump choice1_done

label choice1_soda:

    bar "Heh, on it."

    rg "Aahh, that hit the spot. Time to head back."

    jump choice1_done

label choice1_beer:

    bar "Heh, coming right up."

    rg "Aahh, that hit the spot. Time to head back."

    jump choice1_done

label choice1_thief:

    bar "U-uhm, excuse me??"

    rg "Who the hell charges €15 for a single beer?? I'm out of here!"

    jump choice1_done

label choice1_done:

    rg "Hm? Wait, what, where is my- I swear I didn't forget my wallet too."

    bar "Heh heh, pleasure doing business with you!"

    rg "Get back here, you slimy bastard!!"
    
    scene oa sis
    with dissolve

    play music "Desert Vibes.opus"

    show lyra

    show ruins:
      xalign 0.9
      yalign 0.5

    rg "Haah, haah. It's way too hot to run in this outfit."

    rg "Wait a moment, there is something in the sand. A cross-shaped badge, that is the symbol of the Heroes."

    rg "I could head back to the others, but... Maybe HE is here."

label start4:

    scene oa sis
    with dissolve

    play music "Desert Vibes.opus"

    show lyra

    show ruins:
      xalign 0.9
      yalign 0.5

    menu: 

        "I will investigate that village.":
         jump choice2_village

        "No time to waste, I am going straight ahead.":
         jump choice2_cave

        "It's too dangerous, let's just go back." if back:
         jump choice2_back

        "Maybe I should return to the beach." if not back:
         jump choice2_baack

        "What are those arches in the distance?":
         jump choice2_ruins

        "Inventory":
         jump invento

label invento:
    
    $ start4 = True    

    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump start4

label choice2_baack:

    $ menu_flag = True
    $ back = True

    rg "But it could be a good chance to improve my skills. Hmm..."

    jump start4

label choice2_village:

    rg "Excuse me sir, have you seen a shady bartender around here?"

    bard "Heh, yeah, stranger. They went in here."

    jump choice2_done

label choice2_ruins:

    "(Red Gaze explores the ruins and finds an oyster.)"

    show oyster:
      xalign 0.5
      yalign 0.65

    rg "An oyster, out here?"

if yes:

    rg "The knife should do the trick. Yes, it worked!"

    $ InvItem(*item_ring1).pickup(1)

    hide oyster

    show ooyster:
      xalign 0.5
      yalign 0.65

    show ring1:
      xalign 0.5
      yalign 0.65

    rg "Wow, what a beautiful ring! Not sure who put it in there, but it was totally worth the detour."

    rg "And I still have some of Lady Chrona's Haste Gel left, nice!"

    jump choice2_cave

if no:

    rg "Hnnggh! No use, it won't open. I should just move on."

    rg "At least I still have some of Lady Chrona's Haste Gel left."

    jump choice2_cave

label choice2_cave:

    scene ca ves
    with dissolve

    stop music fadeout 10

    play music "Cave Vibes.opus"

    show lyra

    show algae:
      xalign 0.8
      yalign 0.88

    show starr:
      xalign 0.98
      yalign 0.85

    show birb:
      xalign 0.33
      yalign 0.58

    rg "Whoa it's a lot less hot in here."    

    bar "A dead end? Curses!"

    rg "Give it up, you bastard."

    bar "Hmm, but it seems like Lady Luck has blessed me. For you have dropped your weapon. Mwahaha!"

    rg "Dropped? Yeah, I dropped it back with the others, who brings a weapon to buy a drink?"

    rg "And if you think I am harmless without my blade - your are in for a rude awakening."

label test_menu2:

    scene ca ves
    with dissolve

    stop music fadeout 10

    play music "Cave Vibes.opus"

    show lyra

    show algae:
      xalign 0.8
      yalign 0.88

    show starr:
      xalign 0.98
      yalign 0.85

    show birb:
      xalign 0.33
      yalign 0.58

    menu:
        "Ready - fight!":
            jump pre_battle

        "Inventory":
         jump invent

label invent:
    
    $ start5 = True    

    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump test_menu2

    play music "Cave Vibes.opus"

    bar "Ungh, so strong."

    rg "Finally, my wallet. Just be grateful Lady Chrona is still tanning back at the beach."

    bar "D-d-did you say Lady Chrona, the seventh strongest Mercenary??"

    rg "Sure did. Now get out of here."

    bar "Wait, so you are not going to kill me?"

    rg "Huh? Mercenaries only kill when they are working, we are not monsters killing for fun. But of course the Heroes wouldn't tell you that."

    bar "No, they never said that."

    bar "She was here."

    rg "What?"

    bar "Wink was here, in person. I have watched her streams for years, and she said that if I took out a Mercenary, I could ditch my boring office job to come and work for her."

    rg "The pop star and Famous Hero, Wink. I see."

    rg "Thanks. And just so you know, killing someone for the first time is... Not that easy. See you."

    scene be ach

    show lyra

    play music "Beach Vibes.opus"

    show crab at right

    show island:
      xalign 0.25
      yalign 0.6

    lc "You're 13 minutes and 7 seconds late."

    sg "Red Gaze, where have you been all day?"

    rg "I ran into a minion of the Heroes."

    sg "The Heroes again. Was Simon there?"

    rg "No. He was not."

    rg "If only I had stopped him back then, maybe we wouldn't be at war with the Heroe-"

    sg "No, stop it. We've told you not to blame yourself for the past."

    rg "Y-yeah, I know. Thanks."

    "Thank you for playing!"

    "CREDITS{vspace=1}Intro to the Game (Main Menu theme) - zuupo (discord){vspace=1}Beach Vibes (Beach theme) - zuupo (discord){vspace=1}Desert Vibes (Desert theme) - zuupo (discord){vspace=1}Cave Vibes (Cave theme) - zuupo (discord){vspace=1}Red Gaze Battle! (Battle song) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Red Gaze Battle! (Battle theme) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Beach scene - free-game-assets.itch.io{vspace=1}Desert village scene - free-game-assets.itch.io{vspace=1}Cave scene - free-game-assets.itch.io{vspace=1}"

    "CREDITS{vspace=1}Steel Sugar - NomnomNami (nomnomnami.com){vspace=1}Haste Gel - NomnomNami (nomnomnami.com){vspace=1}Memento: Chopsticks - freegamesprites.com{vspace=1}"

    "CREDITS{vspace=1}Yulian Wings - freegamesprites.com{vspace=1}Yulian Heart - freegamesprites.com{vspace=1}Yulian Wheat - freegamesprites.com"

    "CREDITS{vspace=1}Kevrish Cloth - freegamesprites.com{vspace=1}Cloth of the Venerable - freegameassets.com{vspace=1}Nernas Fragment - freegamesprites.com"

    "CREDITS{vspace=1}Lyra Red Gaze Sanchez - emily_rose234 (discord){vspace=1}Crab - Haiyoooo (discord){vspace=1}Shark - Haiyoooo (discord){vspace=1}Island - Haiyoooo (discord)"

    "CREDITS{vspace=1}Oyster - Haiyoooo (discord){vspace=1}Oyster open - Haiyoooo (discord){vspace=1}Ring1 - freegamesprites.com{vspace=1}Seagull - Haiyoooo (discord)"

    "CREDITS{vspace=1}Seastar - Haiyoooo (discord){vspace=1}Pink corals in cave - Haiyoooo (discord){vspace=1}Red Gaze pixel combat sprites - leedara (discord){vspace=1}Shady Bartender combat sprites - leedara (discord)"

    "CREDITS{vspace=1}Voidstone - freegamesprites.com{vspace=1}Steely Chain - freegamesprites.com"

    "CREDITS{vspace=1}Aria's Ring - clockworkraven.itch.io{vspace=1}Fredrick's Ring - clockworkraven.itch.io{vspace=1}Demon Slayer Sword - clockworkraven.itch.io"

    "CREDITS{vspace=1}SYRUP LITE RPG FRAMEWORK (combat system) - NomnomNami{vspace=1}The combat sprites were made by using the character Syrup from this combat system as a template."

    #

    return    

label choice2_back:

    $ menu_flag = False

    rg "You know what? I am on vacation, I am not dealing with this today."

    $ InvItem(*item_stone).pickup(1)

    rg "Wait a sec, isn't that... A Nernas Fragment? Those storms sure made you fly far away."

    "(After a short yet hot day, Red Gaze heads back.)"

    scene be ach
    with dissolve 

    show lyra 

    play music "Beach Vibes.opus"

    show crab at right

    show island:
      xalign 0.25
      yalign 0.6

    sg "Red Gaze, where did you go off to?"

    rg "Uhh, too tired to talk."

    "(Red Gaze is too tired to deal with anything, and falls asleep under the shadow of a parasol.)"

    "Ending C unlocked"

    "Thank you for playing!"

    "CREDITS{vspace=1}Intro to the Game (Main Menu theme) - zuupo (discord){vspace=1}Beach Vibes (Beach theme) - zuupo (discord){vspace=1}Desert Vibes (Desert theme) - zuupo (discord){vspace=1}Cave Vibes (Cave theme) - zuupo (discord){vspace=1}Red Gaze Battle! (Battle song) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Red Gaze Battle! (Battle theme) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Beach scene - free-game-assets.itch.io{vspace=1}Desert village scene - free-game-assets.itch.io{vspace=1}Cave scene - free-game-assets.itch.io{vspace=1}"

    "CREDITS{vspace=1}Steel Sugar - NomnomNami (nomnomnami.com){vspace=1}Haste Gel - NomnomNami (nomnomnami.com){vspace=1}Memento: Chopsticks - freegamesprites.com{vspace=1}"

    "CREDITS{vspace=1}Nernas Fragment - freegamesprites.com{vspace=1}Yulian Wings - freegamesprites.com{vspace=1}Yulian Heart - freegamesprites.com{vspace=1}Yulian Wheat - freegamesprites.com"

    "CREDITS{vspace=1}Kevrish Cloth - freegamesprites.com{vspace=1}Cloth of the Venerable - freegameassets.com{vspace=1}Nernas Fragment - freegamesprites.com"

    "CREDITS{vspace=1}Lyra Red Gaze Sanchez - emily_rose234 (discord){vspace=1}Crab - Haiyoooo (discord){vspace=1}Shark - Haiyoooo (discord){vspace=1}Island - Haiyoooo (discord)"

    "CREDITS{vspace=1}Oyster - Haiyoooo (discord){vspace=1}Oyster open - Haiyoooo (discord){vspace=1}Ring1 - freegamesprites.com{vspace=1}Seagull - Haiyoooo (discord)"

    "CREDITS{vspace=1}Seastar - Haiyoooo (discord){vspace=1}Pink corals in cave - Haiyoooo (discord){vspace=1}Red Gaze pixel combat sprites - leedara (discord){vspace=1}Shady Bartender combat sprites - leedara (discord)"

    "CREDITS{vspace=1}Voidstone - freegamesprites.com{vspace=1}Steely Chain - freegamesprites.com"

    "CREDITS{vspace=1}Aria's Ring - clockworkraven.itch.io{vspace=1}Fredrick's Ring - clockworkraven.itch.io{vspace=1}Demon Slayer Sword - clockworkraven.itch.io"

    "CREDITS{vspace=1}SYRUP LITE RPG FRAMEWORK (combat system) - NomnomNami{vspace=1}The combat sprites were made by using the character Syrup from this combat system as a template."

    #

    return

label choice2_done:

label start6:
    
    scene oa sis
    with dissolve

    play music "Desert Vibes.opus"

    show lyra

    show ruins:
      xalign 0.9
      yalign 0.5

    menu:

        "Thank you, kind sir! (...really? you literally know he is the bad guy. oh well, it's your call, buddy.)":
         jump choice3_trust

        "I'm not falling for your tricks again!":
         jump choice3_call

        "Inventory":
         jump inven

label inven:

    $ start6 = True    

    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump start6

label choice3_trust:

    "BAM"

    rg "The door is locked. And I am hearing a ticking sound. A bomb?!"

    bard "Mwahaha, your end will please the Heroes greatly, Mercenary!" 

    rg "Let's get out of here. Haa-yah!! (Red Gaze dropkicks the door apart right before the bomb goes off.)"

    "KABOOM"

    jump choice3_done

label choice3_call:

    bard "Nani? Impossible, how could she see through my flawless disguise?"

    rg "Dude, you literally just added a fake moustache."

    jump choice3_done

label choice3_done:

    bard "My glorious trap has failed! I must escape."

    rg "Oh no, not this time! Good thing I still got some of Lady Chrona's Haste Gel."

    scene ca ves
    with dissolve

    show lyra

    stop music fadeout 10

    play music "Cave Vibes.opus"

    rg "Whoa it's a lot less hot in here."

    bard "A dead end? Curses!"

    rg "Give it up, you bastard."

    bard "Hmm, but it seems like Lady Luck has blessed me. For you have dropped your weapon. Mwahaha!"

    rg "Dropped? Yeah, I dropped it back with the others, who brings a weapon to buy a drink?"

    rg "And if you think I am harmless without my blade - your are in for a rude awakening."

label test_menu:
    menu:
        "Ready - fight!":
            jump pre_battle

        "Inventory":
         jump inve

label inve:
    
    $ start7 = True   

    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump test_menu

label victory:

    scene ca ves
    with dissolve

    show lyra

    show algae:
      xalign 0.8
      yalign 0.88

    show starr:
      xalign 0.98
      yalign 0.85

    show birb:
      xalign 0.33
      yalign 0.58

    play music "Cave Vibes.opus"

    bard "Ungh, so strong."

    rg "My dear wallet. Just be grateful Lady Chrona is still tanning back at the beach."

    bard "D-d-did you say Lady Chrona, one of the ten Elite Mercenaries??"

    rg "Sure did. Now get out of here."

    bard "Wait, but... You are not going to kill me?"

    rg "Huh? Mercenaries only kill when they are working, we are not monsters killing for fun. But of course the Heroes wouldn't tell you that."

    bar "No, they never said that."

    bar "She was here."

    rg "What?"

    bar "Wink was here, in person. I have watched her streams for years, and she said that if I took out a Mercenary, I could ditch my boring office job to come and work for her."

    rg "The pop star and Famous Hero, Wink. I see."

    rg "Thanks. And just so you know, killing someone for the first time is... Not that easy. See you."

    scene be ach

    show lyra

    play music "Beach Vibes.opus"

    show crab at right

    show island:
      xalign 0.25
      yalign 0.6

    lc "You're 9 minutes and 22 seconds late."

    sg "Red Gaze, where have you been all day?"

if yes:

    rg "It's a long story, but first check out this ring!"

    sg "That's amazing! The rest of Mercenary Division 9 is gonna love this."

    rg " And I ran into a minion of the Heroes."

    sg "The Heroes again. Was Simon there?"

    rg "No. He was not."

    rg "If only I had stopped him back then, maybe we wouldn't be at war with the Heroe-"

    sg "No, stop. We've told you not to blame yourself for the past."

    rg "Y-yeah, I know. Thanks."

    "Ending D unlocked"

    "Thank you for playing!"

    "CREDITS{vspace=1}Intro to the Game (Main Menu theme) - zuupo (discord){vspace=1}Beach Vibes (Beach theme) - zuupo (discord){vspace=1}Desert Vibes (Desert theme) - zuupo (discord){vspace=1}Cave Vibes (Cave theme) - zuupo (discord){vspace=1}Red Gaze Battle! (Battle song) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Red Gaze Battle! (Battle theme) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Beach scene - free-game-assets.itch.io{vspace=1}Desert village scene - free-game-assets.itch.io{vspace=1}Cave scene - free-game-assets.itch.io{vspace=1}Lyra Red Gaze Sanchez sprite - emily_rose234 (discord)"

    "CREDITS{vspace=1}Steel Sugar - NomnomNami (nomnomnami.com){vspace=1}Haste Gel - NomnomNami (nomnomnami.com){vspace=1}Memento: Chopsticks - freegamesprites.com{vspace=1}"

    "CREDITS{vspace=1}{vspace=1}Yulian Wheat - freegamesprites.com{vspace=1}Yulian Wings - freegamesprites.com{vspace=1}Yulian Heart - freegamesprites.com"

    "CREDITS{vspace=1}Kevrish Cloth - freegamesprites.com{vspace=1}Cloth of the Venerable - freegameassets.com{vspace=1}Nernas Fragment - freegamesprites.com"

    "CREDITS{vspace=1}Crab - Haiyoooo (discord){vspace=1}Shark - Haiyoooo (discord){vspace=1}Island - Haiyoooo (discord)"

    "CREDITS{vspace=1}Oyster - Haiyoooo (discord){vspace=1}Oyster open - Haiyoooo (discord){vspace=1}Ring1 - freegamesprites.com{vspace=1}Seagull - Haiyoooo (discord)"

    "CREDITS{vspace=1}Seastar - Haiyoooo (discord){vspace=1}Pink corals in cave - Haiyoooo (discord){vspace=1}Red Gaze pixel combat sprites - leedara (discord){vspace=1}Shady Bartender combat sprites - leedara (discord)"

    "CREDITS{vspace=1}Voidstone - freegamesprites.com{vspace=1}Steely Chain - freegamesprites.com"

    "CREDITS{vspace=1}Aria's Ring - clockworkraven.itch.io{vspace=1}Fredrick's Ring - clockworkraven.itch.io{vspace=1}Demon Slayer Sword - clockworkraven.itch.io"

    "CREDITS{vspace=1}SYRUP LITE RPG FRAMEWORK (combat system) - NomnomNami{vspace=1}The combat sprites were made by using the character Syrup from this combat system as a template."

else:

    rg "I ran into a minion of the Heroes."

    sg "The Heroes again. Was Simon there?"

    rg "No. He was not."

    rg "If only I had stopped him back then, maybe we wouldn't be at war with the Heroe-"

    sg "No, stop. We've told you not to blame yourself for the past."

    sg "Y-yeah, I know. Thanks."

    "Ending A unlocked"

    "Thank you for playing!"

    "CREDITS{vspace=1}Intro to the Game (Main Menu theme) - zuupo (discord){vspace=1}Beach Vibes (Beach theme) - zuupo (discord){vspace=1}Desert Vibes (Desert theme) - zuupo (discord){vspace=1}Cave Vibes (Cave theme) - zuupo (discord){vspace=1}Red Gaze Battle! (Battle song) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Red Gaze Battle! (Battle theme) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Beach scene - free-game-assets.itch.io{vspace=1}Desert village scene - free-game-assets.itch.io{vspace=1}Cave scene - free-game-assets.itch.io{vspace=1}Lyra Red Gaze Sanchez sprite - emily_rose234 (discord)"

    "CREDITS{vspace=1}Steel Sugar - NomnomNami (nomnomnami.com){vspace=1}Haste Gel - NomnomNami (nomnomnami.com){vspace=1}Memento: Chopsticks - freegamesprites.com{vspace=1}"

    "CREDITS{vspace=1}Kevrish Cloth - freegamesprites.com{vspace=1}Cloth of the Venerable - freegameassets.com{vspace=1}Nernas Fragment - freegamesprites.com"

    "CREDITS{vspace=1}Yulian Wings - freegamesprites.com{vspace=1}Yulian Heart - freegamesprites.com{vspace=1}Yulian Wheat - freegamesprites.com"

    "CREDITS{vspace=1}Crab - Haiyoooo (discord){vspace=1}Shark - Haiyoooo (discord){vspace=1}Island - Haiyoooo (discord)"

    "CREDITS{vspace=1}Oyster - Haiyoooo (discord){vspace=1}Oyster open - Haiyoooo (discord){vspace=1}Ring1 - freegamesprites.com{vspace=1}Seagull - Haiyoooo (discord)"

    "CREDITS{vspace=1}Seastar - Haiyoooo (discord){vspace=1}Pink corals in cave - Haiyoooo (discord){vspace=1}Red Gaze pixel combat sprites - leedara (discord){vspace=1}Shady Bartender combat sprites - leedara (discord)"

    "CREDITS{vspace=1}Voidstone - freegamesprites.com{vspace=1}Steely Chain - freegamesprites.com"

    "CREDITS{vspace=1}Aria's Ring - clockworkraven.itch.io{vspace=1}Fredrick's Ring - clockworkraven.itch.io{vspace=1}Demon Slayer Sword - clockworkraven.itch.io"

    "CREDITS{vspace=1}SYRUP LITE RPG FRAMEWORK (combat system) - NomnomNami{vspace=1}The combat sprites were made by using the character Syrup from this combat system as a template."

    jump victory_done

label victory_done:

    #

    return
