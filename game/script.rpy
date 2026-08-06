define rg = Character("Red Gaze")
define sg = Character("Smiling Golem")
define lc = Character("Lady Chrona")
define bar = Character("Shady Bartender")
define bard = Character("Shady Bartender disguised")
define n = Character("Narrator")
define no = False
define yes = False
define back = False
define ring = False
define start3 = False
define start4 = False
define start5 = False
define start6 = False
define start7 = False
define end = False
define lucky = False
define flame = False
define ice = False
define thorns = False
define electro = False
define sis = False
define untouchable = False

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
    $ InvItem(*item_sugar).pickup(15)
    $ InvItem(*item_heart).pickup(10)
    $ InvItem(*item_wheat).pickup(1)
    $ InvItem(*item_herb).pickup(1)
    $ InvItem(*item_water).pickup(1)
    $ InvItem(*item_sucker).pickup(1)
    $ InvItem(*item_beet).pickup(1)
    $ InvItem(*item_paper).pickup(1)
    $ InvItem(*item_stone).pickup(1)
    $ InvItem(*item_large).pickup(1)
    $ InvItem(*item_obsidian).pickup(1)
    $ InvItem(*item_chain).pickup(1)

    "NOTE! This is a spinoff-game to the main game I am working on, Red Gaze: Advent"

    n "This world is set in a future where Mercenaries are the main military force. However, a faction of self-proclaimed Heroes have recently appeared, determined to kill all Mercenaries."

    n "One such Mercenary is Lyra Sanchez, aka Red Gaze. Despite the ongoing conflict, Red Gaze's unit has been graced with a trip to the beaches near Ord Desert."

    n "She has been granted a vacation northwest of Mer City, along with her fellow Mercenaries Smiling Golem and Lady Chrona. There is just one problem - she forgot to bring a swimsuit!"

    scene be ach
    with dissolve 

    play music "Beach Vibes.opus"

    show lyra2

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

    show lyra2

    menu:
        "A knife could come in handy, I suppose.": 
            $ Slaying_the_princess.grant()        
            jump choice0_yes
        "Ha ha, funny. No, you can keep both your knife and your humor.":
            $ Not_slaying_the_princess.grant()
            jump choice0_no
        "Inventory":
            jump inventory
        "Check map":
            rg "Where are we now again? Let's see."            
            jump map2

label map2:
    show map
    rg "Oh right, got it."
    jump start2

label inventory:
    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump start2

label choice0_yes:

    n "Red Gaze accepts the knife, and heads over to the bar"

    $ InvItem(*item_knife).pickup(1)

    $ yes = True

    jump choice0_done

label choice0_no:

    n "Red Gaze rejects the knife, and heads over to the bar"

    $ no = True

    jump choice0_done

label choice0_done:

    rg "Hold on, what is that sparkling in the water?."

    rg "Ohh, small stones with foreign letters, they are said to bring various fortunes."

    rg "Guh, they are quite heavy for their size though! I will only be able to carry one."

    menu:
        "Take the Stone of Fire":
         jump fire
        "Take the Stone of Ice":
         jump ice
        "Take the Stone of Lightning":
         jump electro

label fire:
    $ Mineralogist.progress(1)        
    $ flame = True
    $ InvItem(*item_fire).pickup(1)
    n "Red Gaze found Stone of Fire!"
    jump rune

label ice:
    $ Mineralogist.progress(1)         
    $ ice = True
    $ InvItem(*item_ice).pickup(1)
    n "Red Gaze found Stone of Ice!"
    jump rune

label electro:
    $ Mineralogist.progress(1)         
    $ electro = True
    $ InvItem(*item_lightningg).pickup(1)
    n "Red Gaze found Stone of Lightning!"
    jump rune

label rune:

    rg "Maybe reading the Item Description in the Inventory will reveal more about the stone. I bet they're short and interesti-"

    n "Red Gaze, please let the player play however they want."

    rg "Alright, alright, I'm just saying."

    rg "Okay, now I really need that drink."

    n "Red Gaze heads over to the bar"

    bar "What are you buying, stranger?"

label start3:
    scene be ach

    show lyra2

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
        "Check map":
            rg "Where are we now again? Let's see."            
            jump map1

label map1:
    show map
    rg "Oh right, got it."
    jump start3

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

    show lyra2

    show ruins:
      xalign 0.9
      yalign 0.5

    rg "Haah, haah. It's way too hot to run in this outfit."

    rg "Wait a moment, there is something in the sand. A cross-shaped badge, that is the symbol of the Heroes."

    rg "I could head back to the others - but maybe HE is here."

    rg "If only I had... No, focus on the robber, Lyra."

label start4:

    scene oa sis
    with dissolve

    play music "Desert Vibes.opus"

    show lyra2

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
            $ I_am_only_human_after_all.grant() 
            jump choice2_baack

        "What are those arches in the distance?":
         jump choice2_ruins

        "Inventory":
         jump invento

        "Check map":
            rg "Where are we now again? Let's see."            
            jump map3

label map3:
    show map2
    rg "Oh right, got it."
    jump start4

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

    n "Red Gaze explores the ruins and finds an oyster."

    show oyster:
      xalign 0.5
      yalign 0.65

    rg "An oyster, out here?"

if yes:

    rg "The knife should do the trick. Yes, it worked!"

    $ InvItem(*item_ring1).pickup(1)
    $ ring = True
    hide oyster

    show ooyster:
      xalign 0.5
      yalign 0.65

    show ring1:
      xalign 0.5
      yalign 0.65

    rg "Wow, what a beautiful ring! Not sure who put it in there, but it was totally worth the detour."

    rg "And the bartender didn't even cover his tracks, nice!"

    jump choice2_cave

if no:

    rg "Hnnggh! No use, it won't open. I should just move on."

    rg "At least the bartender didn't cover his tracks."

    jump choice2_cave

label choice2_cave:

    scene ca ves
    with dissolve

    stop music fadeout 10

    play music "Cave Vibes.opus"

    show lyra2

    show algae:
      xalign 0.8
      yalign 0.88

    show starr:
      xalign 0.98
      yalign 0.85

    show birb:
      xalign 0.33
      yalign 0.58

    rg "Whoa it's so cool in here."    

    bar "A dead end?"

    rg "Give it up, you bastard."

    bar "You are the only one who will give up - give up your life, that is!"

    rg "Man, what a comeback. Either way, you are going down."

label test_menu2:

    scene ca ves
    with dissolve

    stop music fadeout 10

    play music "Cave Vibes.opus"

    show lyra2

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

        "Check map":
            rg "Where are we now again? Let's see."            
            jump map5
        "Guide: Combat Mechanics":
            jump status

label status:
    rg "I already know most of these. But practice makes perfect, I guess."

    rg "Parry - click the assigned button on the screen in time.{vspace=1}Charge - builds up stacks on yourself, enabling certain skills."

    rg "Burn - deals Fire damage over time.{vspace=1}Poison - deals normal damage over time.{vspace=1}Toxic Blaze - deals high Fire and normal damage once. Consumes Burn and Poison." 

    rg "Blue Burn - a stronger version of Burn.{vspace=1}Frozen - takes more damage from Blunt and Ice-based sources.{vspace=1}{vspace=1}Stunned - skips the next turn."

    jump test_menu2

label map5:
    show map3
    rg "Oh right, got it."
    jump test_menu2

label invent:
    
    $ start5 = True    

    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump test_menu2

label victory:

    scene ca ves
    with dissolve

    stop music fadeout 10

    play music "Cave Vibes.opus"

    show lyra2

    if lohp:
        show lyra lohp
        $ Tis_just_a_flesh_wound.grant()

    show algae:
      xalign 0.8
      yalign 0.88

    show starr:
      xalign 0.98
      yalign 0.85

    show birb:
      xalign 0.33
      yalign 0.58

    bar "Ungh, so strong. You don't like capybaras?"

    rg "Huh, no that's not what I- Damn you Smiling Golem, you said that was a cool line."

    n "Everyone likes capybaras."

    rg "You know you're not supposed to interact with us, right?"

    rg "Finally, my wallet. Just be grateful Lady Chrona is still tanning back at the beach."

    bar "D-d-did you say Lady Chrona, the seventh strongest Mercenary??"

    rg "Sure did. Now get out of here."

    bar "Wait, so you are not going to kill me?"

    rg "Mercenaries only kill when they are working, we are not monsters killing for fun. But of course the Heroes wouldn't tell you that."

    bar "No, they never said that."

    bar "She was here."

    rg "What?"

    bar "Wink was here, in person. I have watched her streams for years, and she said that if I took out a Mercenary, I could ditch my boring office job to come and work for her."

    rg "The pop star and Famous Hero, Wink. I see."

    rg "Thanks. And just so you know, killing someone for the first time is... Not that easy. See you."

    scene be ach

    show lyra2

    play music "Beach Vibes.opus"

    show crab at right

    show island:
      xalign 0.25
      yalign 0.6

    lc "You're 13 minutes and 7 seconds late."

    sg "Red Gaze, where have you been all day?"

    rg "I ran into one of the Heroes."

    sg "The Heroes again. Was Simon there?"

    rg "No. He was not."

    rg "If only I had stopped him back then, maybe we wouldn't be at war with the Heroe-"

    sg "No, stop it. We've told you not to blame yourself for the past."

    rg "Y-yeah, I know. Thanks."

    scene da rk

    show lyra2

    if lohp:
        show lyra lohp

    stop music fadeout 10

    n "A few hours later, Lyra arrives back home. Her mom is not back yet. "

    n "She finally takes off her uniform, curls up into a ball on her bed... And cries."

    rg "*sob* I'm sorry, everyone. I should have stopped him..."

    n "..."

    n "To be continued"

    n "Ending A unlocked"
    $ No_rest_for_the_weary.grant()

    n "Thank you for playing."

    "Special thanks to Brian Bartram, Jennifer Svedberg-Yen and Ali Nouraei for inspiring me to get into game development!!"

    "CREDITS{vspace=1}Writing and programming - leedara (me, discord)"

    "CREDITS{vspace=1}Intro to the Game (Main Menu theme) - zuupo (discord){vspace=1}Beach Vibes (Beach theme) - zuupo (discord){vspace=1}Desert Vibes (Desert theme) - zuupo (discord){vspace=1}Cave Vibes (Cave theme) - zuupo (discord){vspace=1}Red Gaze Battle! (Battle song) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Red Gaze Battle! (Battle theme) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Beach scene - free-game-assets.itch.io{vspace=1}Desert village scene - free-game-assets.itch.io{vspace=1}Cave scene - free-game-assets.itch.io{vspace=1}Lyra Red Gaze Sanchez sprite - emily_rose234 (discord)"

    "CREDITS{vspace=1}Steel Sugar - NomnomNami (nomnomnami.com){vspace=1}Haste Gel - NomnomNami (nomnomnami.com){vspace=1}Memento: Chopsticks - freegamesprites.com{vspace=1}"

    "CREDITS{vspace=1}Kevrish Cloth - freegamesprites.com{vspace=1}Cloth of the Venerable - freegameassets.com{vspace=1}Nernas Fragment - freegamesprites.com"

    "CREDITS{vspace=1}Yulian Wings - freegamesprites.com{vspace=1}Yulian Heart - freegamesprites.com{vspace=1}Yulian Wheat - freegamesprites.com"

    "CREDITS{vspace=1}Crab - Haiyoooo (discord){vspace=1}Shark - Haiyoooo (discord){vspace=1}Island - Haiyoooo (discord)"

    "CREDITS{vspace=1}Oyster - Haiyoooo (discord){vspace=1}Oyster open - Haiyoooo (discord){vspace=1}Ring1 - freegamesprites.com{vspace=1}Seagull - Haiyoooo (discord)"

    "CREDITS{vspace=1}Seastar - Haiyoooo (discord){vspace=1}Pink corals in cave - Haiyoooo (discord){vspace=1}Red Gaze pixel combat sprites - leedara (discord){vspace=1}Shady Bartender combat sprites - leedara (discord)"

    "CREDITS{vspace=1}Voidstone - freegamesprites.com{vspace=1}Steely Chain - freegamesprites.com{vspace=1}Marked Stones - freegamesprites.com{vspace=1}I downloaded the image and drew the rune-symbols myself."

    "CREDITS{vspace=1}Aria's Ring - clockworkraven.itch.io{vspace=1}Fredrick's Ring - clockworkraven.itch.io{vspace=1}Demon Slayer Sword - clockworkraven.itch.io"

    "CREDITS{vspace=1}Dark apartment - noranekogames.itch.io"

    "CREDITS{vspace=1}Skill animations - arimia.itch.io{vspace=1}Achievement system - feniksdev.itch.io"

    "CREDITS{vspace=1}Skill sound effects - pixabay.com{vspace=1}Kick sound effect - pixabay.com"

    "CREDITS{vspace=1}Door kicked sound effect - pixabay.com{vspace=1}Explosion sound effect - pixabay.com"

    "CREDITS{vspace=1}SYRUP LITE RPG FRAMEWORK (combat system) - NomnomNami{vspace=1}The combat sprites were made by me by using the character Syrup from this combat system as a template."


    #

    return    

label choice2_back:

    $ menu_flag = False

    rg "You know what? I am on vacation, I am not dealing with this today."

    n "After a short yet hot day, Red Gaze heads back."

    scene be ach
    with dissolve 

    show lyra2

    play music "Beach Vibes.opus"

    show crab at right

    show island:
      xalign 0.25
      yalign 0.6

    sg "Red Gaze, where did you go off to?"

    rg "Uhh, too tired to talk."

    n "Red Gaze is too tired to deal with anything, and falls asleep under the shadow of a parasol."

    n "To be continued"

    n "Ending B unlocked"
    $ Vacay_for_Red_Gaze.grant()

    n "Thank you for playing!"

    "Special thanks to Brian Bartram, Jennifer Svedberg-Yen and Ali Nouraei for inspiring me to get into game development!!"

    "CREDITS{vspace=1}Writing and programming - leedara (me, discord)"

    "CREDITS{vspace=1}Intro to the Game (Main Menu theme) - zuupo (discord){vspace=1}Beach Vibes (Beach theme) - zuupo (discord){vspace=1}Desert Vibes (Desert theme) - zuupo (discord){vspace=1}Cave Vibes (Cave theme) - zuupo (discord){vspace=1}Red Gaze Battle! (Battle song) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Red Gaze Battle! (Battle theme) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Beach scene - free-game-assets.itch.io{vspace=1}Desert village scene - free-game-assets.itch.io{vspace=1}Cave scene - free-game-assets.itch.io{vspace=1}Lyra Red Gaze Sanchez sprite - emily_rose234 (discord)"

    "CREDITS{vspace=1}Steel Sugar - NomnomNami (nomnomnami.com){vspace=1}Haste Gel - NomnomNami (nomnomnami.com){vspace=1}Memento: Chopsticks - freegamesprites.com{vspace=1}"

    "CREDITS{vspace=1}Kevrish Cloth - freegamesprites.com{vspace=1}Cloth of the Venerable - freegameassets.com{vspace=1}Nernas Fragment - freegamesprites.com"

    "CREDITS{vspace=1}Yulian Wings - freegamesprites.com{vspace=1}Yulian Heart - freegamesprites.com{vspace=1}Yulian Wheat - freegamesprites.com"

    "CREDITS{vspace=1}Crab - Haiyoooo (discord){vspace=1}Shark - Haiyoooo (discord){vspace=1}Island - Haiyoooo (discord)"

    "CREDITS{vspace=1}Oyster - Haiyoooo (discord){vspace=1}Oyster open - Haiyoooo (discord){vspace=1}Ring1 - freegamesprites.com{vspace=1}Seagull - Haiyoooo (discord)"

    "CREDITS{vspace=1}Seastar - Haiyoooo (discord){vspace=1}Pink corals in cave - Haiyoooo (discord){vspace=1}Red Gaze pixel combat sprites - leedara (discord){vspace=1}Shady Bartender combat sprites - leedara (discord)"

    "CREDITS{vspace=1}Voidstone - freegamesprites.com{vspace=1}Steely Chain - freegamesprites.com{vspace=1}Marked Stones - freegamesprites.com{vspace=1}I downloaded the image and drew the rune-symbols myself."

    "CREDITS{vspace=1}Aria's Ring - clockworkraven.itch.io{vspace=1}Fredrick's Ring - clockworkraven.itch.io{vspace=1}Demon Slayer Sword - clockworkraven.itch.io"

    "CREDITS{vspace=1}Dark apartment - noranekogames.itch.io"

    "CREDITS{vspace=1}Skill animations - arimia.itch.io{vspace=1}Achievement system - feniksdev.itch.io"

    "CREDITS{vspace=1}Skill sound effects - pixabay.com{vspace=1}Kick sound effect - pixabay.com"

    "CREDITS{vspace=1}Door kicked sound effect - pixabay.com{vspace=1}Explosion sound effect - pixabay.com"

    "CREDITS{vspace=1}SYRUP LITE RPG FRAMEWORK (combat system) - NomnomNami{vspace=1}The combat sprites were made by me by using the character Syrup from this combat system as a template."

    #

    return

label choice2_done:

label start6:
    
    scene oa sis
    with dissolve

    play music "Desert Vibes.opus"

    show lyra2

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

        "Check map":
            rg "Where are we now again? Let's see."            
            jump map6

label map6:
    show map2
    rg "Oh right, got it."
    jump start2

label inven:

    $ start6 = True    

    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump start6

label choice3_trust:

    play sound "door.mp3"

    rg "The door is locked. And I am hearing a ticking sound. A bomb?!"

    bard "Mwahaha, your end will please the Heroes greatly, Mercenary!" 

    rg "Let's get out of here. Haa-yah!!"

    play sound "kick.mp3"

    n "Red Gaze dropkicks the door apart right before the bomb goes off."

    play sound "explosion.mp3"

    jump choice3_done

label choice3_call:

    bard "Nani? My glorious trap has failed! I must escape."

    jump choice3_done

label choice3_done:

    rg "Not this ti- Wait, what's that? Something is glowing inside the blown-up building."

    rg "Ohh, more of those marked stones from before."

    rg "These are lighter, but I will still only be able to bring one."

    menu:
        "Take the Stone of Luck":
         jump lucky
        "Take the Stone of Roses":
         jump thorns
        "Take the Stone of the Untouchable":
         jump untouchable
        "Take the Stone of Sisyphus":
         jump sis
        "Take the Stone of the End":
         jump end

label lucky:
    $ Mineralogist.progress(1) 
    $ lucky = True
    $ InvItem(*item_luck).pickup(1)
    n "Red Gaze found Stone of Luck!"
    jump runes

label untouchable:
    $ Mineralogist.progress(1) 
    $ untouchable = True
    $ InvItem(*item_untouchable).pickup(1)
    n "Red Gaze found Stone of the Untouchable!"
    jump runes

label thorns:
    $ Mineralogist.progress(1) 
    $ thorns = True
    $ InvItem(*item_roses).pickup(1)
    n "Red Gaze found Stone of Roses!"
    jump runes

label sis:
    $ Mineralogist.progress(1) 
    $ sis = True
    $ InvItem(*item_sisyphus).pickup(1)
    n "Red Gaze found Stone of Sisyphus!"
    rg "I have a bad feeling about this one..."
    jump runes

label end:
    $ Mineralogist.progress(1) 
    $ end = True
    $ InvItem(*item_end).pickup(1)
    n "Red Gaze found Stone of the End!"
    rg "Whoa, this one feels special."
    jump runes

label runes:

    rg "Right, now hurry after that shady bartender. Good thing he didn't erase his tracks."

    scene ca ves
    with dissolve

    show lyra2

    stop music fadeout 10

    play music "Cave Vibes.opus"

    rg "Whoa it's so cool in here."

    bar "A dead end?"

    rg "Give it up, you bastard."

    bar "You are the only one who will give up - give up your life, that is!"

    rg "Man, what a comeback. Either way, you are going down."

label test_menu3:

    scene ca ves
    with dissolve

    stop music fadeout 10

    play music "Cave Vibes.opus"

    show lyra2

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
         jump inv
        
        "Check map":
            rg "Where are we now again? Let's see."            
            jump map0

        "Guide: Combat Mechanics":
            jump status0

label status0:
    rg "Oh yeah, I almost forgot I still have one of these. Let's see."

    rg "Parry - click the assigned button on the screen in time.{vspace=1}Charge - builds up stacks on yourself, enabling certain skills."

    rg "Burn - deals Fire damage over time.{vspace=1}Poison - deals normal damage over time.{vspace=1}Toxic Blaze - deals high Fire and normal damage once. Consumes Burn and Poison." 

    rg "Blue Burn - a stronger version of Burn.{vspace=1}Frozen - takes more damage from Blunt and Ice-based sources.{vspace=1}{vspace=1}Stunned - skips the next turn."

    jump test_menu3

label map0:
    show map3
    rg "Right, got it."
    jump test_menu3

label inv:
    
    $ start7 = True    

    scene bl acc
    with dissolve
    call screen inventory(inv) with Dissolve(.2)
    
    jump test_menu3

label victory2:


    scene ca ves
    with dissolve

    stop music fadeout 10

    play music "Cave Vibes.opus"

    show lyra2

    if lohp:
        show lyra lohp
        $ Tis_just_a_flesh_wound.grant()

    show algae:
      xalign 0.8
      yalign 0.88

    show starr:
      xalign 0.98
      yalign 0.85

    show birb:
      xalign 0.33
      yalign 0.58

    bar "Ungh, so strong. You don't like capybaras?"

    rg "Huh, no that's not what I- Damn you Smiling Golem, you said that was a cool line."

    n "Everyone likes capybaras."

    rg "You know you're not supposed to interact with us, right?"

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

    show lyra2

    if lohp:
        show lyra lohp

    play music "Beach Vibes.opus"

    show crab at right

    show island:
      xalign 0.25
      yalign 0.6

    lc "You're 9 minutes and 22 seconds late."

    sg "Red Gaze, where have you been all day?"

if ring:

    rg "It's a long story, but first check out this ring!"

    sg "That's amazing! The rest of Mercenary Division 9 is gonna love this."

    rg " And I ran into one of the Heroes."

    sg "The Heroes again. Was Simon there?"

    rg "No. He was not."

    rg "If only I had stopped him back then, maybe we wouldn't be at war with the Heroe-"

    sg "No, stop. We've told you not to blame yourself for the past."

    rg "Y-yeah, I know. Thanks."

    n "To be continued"

    n "Ending C unlocked"
    $ Red_Saint.grant()

    n "Thank you for playing!"

    "Special thanks to Brian Bartram, Jennifer Svedberg-Yen and Ali Nouraei for inspiring me to get into game development!!"

    "CREDITS{vspace=1}Writing and programming - leedara (me, discord)"

    "CREDITS{vspace=1}Intro to the Game (Main Menu theme) - zuupo (discord){vspace=1}Beach Vibes (Beach theme) - zuupo (discord){vspace=1}Desert Vibes (Desert theme) - zuupo (discord){vspace=1}Cave Vibes (Cave theme) - zuupo (discord){vspace=1}Red Gaze Battle! (Battle song) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Red Gaze Battle! (Battle theme) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Beach scene - free-game-assets.itch.io{vspace=1}Desert village scene - free-game-assets.itch.io{vspace=1}Cave scene - free-game-assets.itch.io{vspace=1}Lyra Red Gaze Sanchez sprite - emily_rose234 (discord)"

    "CREDITS{vspace=1}Steel Sugar - NomnomNami (nomnomnami.com){vspace=1}Haste Gel - NomnomNami (nomnomnami.com){vspace=1}Memento: Chopsticks - freegamesprites.com{vspace=1}"

    "CREDITS{vspace=1}Kevrish Cloth - freegamesprites.com{vspace=1}Cloth of the Venerable - freegameassets.com{vspace=1}Nernas Fragment - freegamesprites.com"

    "CREDITS{vspace=1}Yulian Wings - freegamesprites.com{vspace=1}Yulian Heart - freegamesprites.com{vspace=1}Yulian Wheat - freegamesprites.com"

    "CREDITS{vspace=1}Crab - Haiyoooo (discord){vspace=1}Shark - Haiyoooo (discord){vspace=1}Island - Haiyoooo (discord)"

    "CREDITS{vspace=1}Oyster - Haiyoooo (discord){vspace=1}Oyster open - Haiyoooo (discord){vspace=1}Ring1 - freegamesprites.com{vspace=1}Seagull - Haiyoooo (discord)"

    "CREDITS{vspace=1}Seastar - Haiyoooo (discord){vspace=1}Pink corals in cave - Haiyoooo (discord){vspace=1}Red Gaze pixel combat sprites - leedara (discord){vspace=1}Shady Bartender combat sprites - leedara (discord)"

    "CREDITS{vspace=1}Voidstone - freegamesprites.com{vspace=1}Steely Chain - freegamesprites.com{vspace=1}Marked Stones - freegamesprites.com{vspace=1}I downloaded the image and drew the rune-symbols myself."

    "CREDITS{vspace=1}Aria's Ring - clockworkraven.itch.io{vspace=1}Fredrick's Ring - clockworkraven.itch.io{vspace=1}Demon Slayer Sword - clockworkraven.itch.io"

    "CREDITS{vspace=1}Dark apartment - noranekogames.itch.io"

    "CREDITS{vspace=1}Skill animations - arimia.itch.io{vspace=1}Achievement system - feniksdev.itch.io"

    "CREDITS{vspace=1}Skill sound effects - pixabay.com{vspace=1}Kick sound effect - pixabay.com"

    "CREDITS{vspace=1}Door kicked sound effect - pixabay.com{vspace=1}Explosion sound effect - pixabay.com"

    "CREDITS{vspace=1}SYRUP LITE RPG FRAMEWORK (combat system) - NomnomNami{vspace=1}The combat sprites were made by me by using the character Syrup from this combat system as a template."


else:

    rg "I ran into one of the Heroes."

    sg "The Heroes again. Was Simon there?"

    rg "No. He was not."

    rg "If only I had stopped him back then, maybe we wouldn't be at war with the Heroe-"

    sg "No, stop. We've told you not to blame yourself for the past."

    sg "Y-yeah, I know. Thanks."

    scene da rk

    show lyra2

    if lohp:
        show lyra lohp

    stop music fadeout 10

    n "A few hours later, Lyra arrives back home. Her mom is not back yet. "

    n "She finally takes off her uniform, curls up into a ball on her bed... And cries."

    rg "*sob* I'm sorry, everyone. I should have stopped him..."

    n "..."

    n "To be continued"

    n "Ending A unlocked"
    $ No_rest_for_the_weary.grant()

    n "Thank you for playing."

    "Special thanks to Brian Bartram, Jennifer Svedberg-Yen and Ali Nouraei for inspiring me to get into game development!!"

    "CREDITS{vspace=1}Writing and programming - leedara (me, discord)"

    "CREDITS{vspace=1}Intro to the Game (Main Menu theme) - zuupo (discord){vspace=1}Beach Vibes (Beach theme) - zuupo (discord){vspace=1}Desert Vibes (Desert theme) - zuupo (discord){vspace=1}Cave Vibes (Cave theme) - zuupo (discord){vspace=1}Red Gaze Battle! (Battle song) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Red Gaze Battle! (Battle theme) - zuupo (discord){vspace=1}"

    "CREDITS{vspace=1}Beach scene - free-game-assets.itch.io{vspace=1}Desert village scene - free-game-assets.itch.io{vspace=1}Cave scene - free-game-assets.itch.io{vspace=1}Lyra Red Gaze Sanchez sprite - emily_rose234 (discord)"

    "CREDITS{vspace=1}Steel Sugar - NomnomNami (nomnomnami.com){vspace=1}Haste Gel - NomnomNami (nomnomnami.com){vspace=1}Memento: Chopsticks - freegamesprites.com{vspace=1}"

    "CREDITS{vspace=1}Kevrish Cloth - freegamesprites.com{vspace=1}Cloth of the Venerable - freegameassets.com{vspace=1}Nernas Fragment - freegamesprites.com"

    "CREDITS{vspace=1}Yulian Wings - freegamesprites.com{vspace=1}Yulian Heart - freegamesprites.com{vspace=1}Yulian Wheat - freegamesprites.com"

    "CREDITS{vspace=1}Crab - Haiyoooo (discord){vspace=1}Shark - Haiyoooo (discord){vspace=1}Island - Haiyoooo (discord)"

    "CREDITS{vspace=1}Oyster - Haiyoooo (discord){vspace=1}Oyster open - Haiyoooo (discord){vspace=1}Ring1 - freegamesprites.com{vspace=1}Seagull - Haiyoooo (discord)"

    "CREDITS{vspace=1}Seastar - Haiyoooo (discord){vspace=1}Pink corals in cave - Haiyoooo (discord){vspace=1}Red Gaze pixel combat sprites - leedara (discord){vspace=1}Shady Bartender combat sprites - leedara (discord)"

    "CREDITS{vspace=1}Voidstone - freegamesprites.com{vspace=1}Steely Chain - freegamesprites.com{vspace=1}Marked Stones - freegamesprites.com{vspace=1}I downloaded the image and drew the rune-symbols myself."

    "CREDITS{vspace=1}Aria's Ring - clockworkraven.itch.io{vspace=1}Fredrick's Ring - clockworkraven.itch.io{vspace=1}Demon Slayer Sword - clockworkraven.itch.io"

    "CREDITS{vspace=1}Dark apartment - noranekogames.itch.io"

    "CREDITS{vspace=1}Skill animations - arimia.itch.io{vspace=1}Achievement system - feniksdev.itch.io"

    "CREDITS{vspace=1}Skill sound effects - pixabay.com{vspace=1}Kick sound effect - pixabay.com"

    "CREDITS{vspace=1}Door kicked sound effect - pixabay.com{vspace=1}Explosion sound effect - pixabay.com"

    "CREDITS{vspace=1}SYRUP LITE RPG FRAMEWORK (combat system) - NomnomNami{vspace=1}The combat sprites were made by me by using the character Syrup from this combat system as a template."

    jump victory_done

label victory_done:

    #

    return
