init offset = -1

## IMPORTANT! ## IF YOU USE THE ITEM SCRIPTS you can take these lines out

## hello there

# defined in item-screens.rpy
transform zoomx(x):
    zoom x
    nearest True
# defined in item-definitions.rpy
define battle_items = []
define secret = False
python:
    def check_inv_for(itemtype):
        for i in itemtype:
            if inv.count(i) > 0:
                return True

## THAT'S ALL! ## had to do this so it'd still work for people only using the battles...

##############################################################################
## battle menu

screen battle_menu():

    # this flag decides whether to show the main battle menu, or items menu
    default showbattlemenu = True

    tag menu
    style_prefix "battle"

    hbox:
        xalign .5
        yalign .9
        spacing 40

        if showbattlemenu:
            textbutton _("{color=#0080c0}Kick{/color}"):
                action Jump("battle_attack")
                tooltip _("{color=#fff}Do like the honey badgers and go for the balls! Deals low Blunt damage.")

            if not charge > 9 and charge > 4:
                textbutton _("{color=#f00}Hollow Thunder{/color}"):
                    action Jump("battle_thunder")
                    tooltip _("{color=#fff}Unleash that built-up Charge! Deals high damage.")

            if charge > 9:
                textbutton _("{color=#f00}Keraunos{/color}"):
                    action Jump("battle_keraunos")
                    tooltip _("{color=#fff}End this.")


            if not charge > 9 and charge > 4 and poison:
                textbutton _("{color=f00}{size=-6}Reverse Serpent Flash{/color}"):
                    action Jump("battle_serpent")
                    tooltip _("{color=#fff}Unleash that built-up Charge! Deals high damage.")

            if thorns:
                textbutton _("{color=#0080c0}Emerald Samsara{/color}"):
                    action Jump("battle_rose")
                    tooltip _("{color=#fff}Rend your foe with sharp vines! Deals medium damage. Can heal when striking a Poisoned target.")

            if ice:
                textbutton _("{color=#0080c0}Impaling Tears{/color}"):
                    action Jump("battle_frost")
                    tooltip _("{color=#fff}Summon a rain of icicles! Deals medium damage. High chance to apply Freeze.")

            if flame:
                textbutton _("{color=#0080c0}Nernas Flareshot{/color}"):
                    action Jump("battle_fire")
                    tooltip _("{color=#fff}A lesser version of Nernas Sunshot! Deals medium damage. Applies Burn.{/color}")

            textbutton _("{color=#0080c0}Muramasa: Red Hunt{/color}"):
                action Jump("battle_red")
                tooltip _("{color=#fff}Slice six times rapidly! Deals medium damage.{/color}")

            if lucky:
                textbutton _("{color=#0080c0}Muramasa: Fracturing Red Hunt{/color}"):
                    action Jump("battle_redluck")
                    tooltip _("{color=#fff}Slice six times rapidly! Deals medium damage. High chance for a Brutal Blow.{/color}")

            if lohp and end: 
                textbutton _("{color=#f00}{size=-6}Muramasa: Oblivion Hunt{/size}{/color}"):
                    action Jump("battle_redd")
                    tooltip _("{color=#f00}Call your hardened blood to your blade, and exterminate your foe! Deals extreme damage.{/color}")

            textbutton _("{color=#0080c0}Steely Resolve{/color}"):
                action Jump("battle_defend")
                tooltip _("{color=#fff}Focus your mind and muscles! Halves incoming damage.{/color}")

            if frozen: 
                textbutton _("{color=#f00}Steely Slam{/color}"):
                    action Jump("battle_slam")
                    tooltip _("{color=#fff}Shatter your Frozen opponent!{/color}")                           

            if frozen and lucky: 
                textbutton _("{color=#f00}Herakles Impact{/color}"):
                    action Jump("battle_impact")
                    tooltip _("{color=#fff}Crush your Frozen victim to pieces!{/color}")  

            if check_inv_for(battle_items):
                textbutton _("{color=#0080c0}Items{/color}"):
                    action SetScreenVariable("showbattlemenu", False)
                    tooltip _("{color=#fff}Use some of your tools!{/color}") 

        else:
            #ITEM MENU
            if "item_sugar" in inv:
                textbutton _("{color=#0080c0}{size=-8}Steely Sugar (throw){/size}{/color}"):
                    action Jump("battle_sugar")
                    tooltip _("{color=#fff}It's just some sugar.{/color}")
                # add new items here
                # only room for 4 at a time with this setup

            if "item_heart" in inv:
                textbutton _("{color=#0080c0}{size=-8}Yulian Heart (eat){/size}{/color}"):
                    action Jump("battle_poison")
                    tooltip _("{color=#fff}It's a herb that cures Slow...{/color}")

            textbutton _("{color=#0080c0}Cancel{/color}"):
                action SetScreenVariable("showbattlemenu", True)
                tooltip _("{color=#fff}Close the item menu.{/color}")

    hbox:
        xalign .05
        yalign .35
        spacing 40

        if showbattlemenu:
                $ secret = True            
                textbutton _("???"):
                    action Jump("battle_secret")

    $ tooltip = GetTooltip()

    if tooltip:
        text "[tooltip!t]" xalign .2 yalign .99

default turn = 0
default atkbuff = 0
default defbuff = 0

default downer = 0
screen QTEdown(rangeD, missed_event):
    on "show" action SetVariable("downer", rangeD)
    frame:
        xalign 0.5
        yalign 0.0
        hbox:
            timer 0.1 action If(0 < downer, true = SetVariable("downer", downer - 0.1), false = [Hide("timerDown"), Jump(missed_event)]) repeat True

            bar:
                value AnimatedValue(value=downer, range=rangeD, delay= 0.5)
                xalign 0.0
                yalign 0.0
                xmaximum 200

##############################################################################
## battle overlay

screen battleoverlay():
    zorder 99

    label _("BATTLE!") style "battle_label" align (.5,.05)

    if not burn and not poison and not frozen:
        label _("Turn: [turn]{vspace=1}Charge: [charge]") xalign .75 yalign .1 style "battleinfo_label"

    if burn and not sugar:
        label _("Turn: [turn]{vspace=1}Charge: [charge]{vspace=1}Burn(Hero): [burn]") xalign .75 yalign .1 style "battleinfo_label"

    if burn and sugar:
        label _("Turn: [turn]{vspace=1}Charge: [charge]{vspace=1}Black Burn(Hero): [bburn]") xalign .75 yalign .1 style "battleinfo_label"

    if poison:
        label _("Turn: [turn]{vspace=1}Charge: [charge]{vspace=1}Poison(Hero): [poison]") xalign .75 yalign .1 style "battleinfo_label"

    if frozen:
        label _("Turn: [turn]{vspace=1}Charge: [charge]{vspace=1}Frozen(Hero): [frozen]") xalign .75 yalign .1 style "battleinfo_label"

    # HP bars
    bar value playerHP range playerMAXHP style "battle_bar" at battle_party1
    bar value enemyHP range enemy.MAXHP style "battle_bar" at battle_enemy1

    frame:
        style_group "battleinfo"
        xalign .025
        vbox:
            hbox:
                xfill True
                label _("Lyra Red Gaze Sanchez")
                text _("Lv [playerLV]") style "battleHP_text" xalign 1.0

            if not playerHP < playerMAXHP/3:
                text _("HP: [playerHP] / [playerMAXHP]") style "battleHP_text"
            else:
                text _("HP: [playerHP] / [playerMAXHP]") style "battleLOWHP_text"

            frame:
                style "battleinfo_stat_frame"
                has vbox
                if atkbuff:
                    text "ATK: [playerATK] {color=#ff7c9b}+ [atkbuff]{/color}"
                else:
                    text "ATK: [playerATK]"
                if defbuff:
                    text "DEF: [playerDEF] {color=#ff7c9b}+ [defbuff]{/color}"
                else:
                    text "DEF: [playerDEF]"
                text "LUC: [playerLUC]"

    frame:
        style_group "battleinfo"
        xalign .975
        vbox:
            label "[enemy.name!t]"
            hbox:
                if enemy.boss:
                    add "bosscrown" yalign .5
                text _("HP: [enemyHP] / [enemy.MAXHP]") style "battleHP_text"
            frame:
                style "battleinfo_stat_frame"
                has vbox
                text "ATK: [enemy.ATK]"
                text "DEF: [enemy.DEF]"
                text "LUC: [enemy.LUC]"

            null height 8
            text "[enemy.info!t]"
                                                                                                                                                                                                                                                                                                
style battle_label_text:
    size 60
    color "#FFF"
    outlines [(6,"#A51F63",1,1)]

image hp full:
    "gui/bar/left.png"
    nearest True
image hp empty:
    "gui/bar/right.png"
    nearest True
style battle_bar:
    left_bar "hp full"
    right_bar "hp empty"
    xsize 120
    ysize 10
    yoffset 90

style battleinfo_frame:
    xsize 250
    ysize 320
    yalign .42
    padding (16,16)
style battleinfo_vbox:
    spacing 6
style battleinfo_stat_frame:
    background "#ffe0ed"
    xfill True
    padding (10,6)

style battleinfo_label_text:
    color "#FFF"
    outlines [(2,"#525252",0,0),(3,"#525252",1,1)]

style battleinfo_text:
    color "#333"

style battleHP_text:
    color "#FFF"
    outlines [(2,"#5d5d5d",0,0)]
style battleLOWHP_text is battleHP_text:
    outlines [(2,"#bd2c47",0,0)]

style battle_button:
    background "[prefix_]battle"
    xysize (200,100)
    size_group "battle"
style battle_button_text:
    xalign .5
    idle_color gui.text_color
    size gui.label_text_size


##############################################################################
## show damage/crit/heal/miss

## DAMAGE NUMBERS
default damage = 0

screen showdamage(target):
    zorder 100
    style_prefix "damage"

    if target=="player":
        text "[damage]" at battle_party1, playerdamage_appear
    else:
        text "[damage]" at battle_enemy1, damage_appear

    timer .1 action Hide('showdamage')

style damage_text:
    bold True
    color "#FFF"
    outlines [(2,"#000",0,0)]

transform damage_appear:
    on show:
        alpha 1 yoffset -10 xoffset 0
        easeout .05 yoffset -20
    on hide:
        easeout .5 alpha 0 yoffset 100 xoffset 10
transform playerdamage_appear:
    on show:
        alpha 1 yoffset -10 xoffset 0
        easeout .05 yoffset -20
    on hide:
        easeout .5 alpha 0 yoffset 100 xoffset -10

screen showcrit():
    zorder 100
    style_prefix "damage"

    text "[damage]" color "#ff3939" size 36 at battle_enemy1, damage_appear

    timer .1 action Hide('showcrit')

screen showheal():
    zorder 100
    style_prefix "damage"

    # on "show" action Play("sound", audio.heal)

    text "[damage]" color "#53ff55" at battle_party1, heal_appear

    timer .1 action Hide('showheal')

transform heal_appear:
    on show:
        alpha 0 yoffset -10 xoffset 15
        easeout .1 alpha 1
    on hide:
        easeout .6 alpha 0 yoffset -60

screen showmiss():
    zorder 100
    style_prefix "damage"

    text _("MISS") at battle_enemy1, miss_appear

    timer .1 action Hide('showmiss')

transform miss_appear:
    on show:
        alpha 0 yoffset -10
        easeout .1 alpha 1
    on hide:
        easeout .6 alpha 0 yoffset 50
