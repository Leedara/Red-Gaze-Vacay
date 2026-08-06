##############################################################################
# Enemy class

init -2 python:
    class Enemy(store.object):
        def __init__(self, name, id, info, MAXHP, ATK, DEF, LUC, RES, EXP=0, G=0, drop=None, boss=False):
            self.name=name #enemy name as seen by the player
            self.id=id #string to be used as a codename
            self.info=info #enemy description

            #STATS
            self.MAXHP=MAXHP #base HP value
            self.ATK=ATK #physical attack points
            self.DEF=DEF #physical defense points
            self.LUC=LUC #factors into crit and dodge rate
            self.RES=RES #magic effectiveness multiplier

            #REWARDS (default to 0 or None)
            self.EXP=EXP #how much exp you get for defeating them
            self.G=G #gold earned by defeating them
            self.drop=drop #item to drop

            #extra
            self.boss=boss #if True, you can't run away

        # adds enemy to list of seen enemies
        def see_enemy(self):
            if self.id not in seen_enemies:
                seen_enemies.append(self.id)

# define your own enemies here!
define m_goop = Enemy(_("Hero minion"), "m_goop",
    info=_("Weak to most stuff."),
    MAXHP=200, ATK=4, DEF=7, LUC=0, RES=.5,
    EXP=3, G=2, drop="item_water")

##############################################################################
# Battle transforms
transform battle_party1:
    xalign .4
    yalign .52
transform battle_enemy1:
    xalign .6
    yalign .52

image battle bg = Solid("#c6ffa3")
image stage bg = Frame("gui/frame.png",4,4, xysize=(700,400), yoffset=-1960)

##############################################################################
# Sprite animations

##PLAYER SPRITES

image player syrup idle:
    "player syrup idle1"
    pause .2
    "player syrup idle2"
    pause .2
    "player syrup idle1"
    pause .2
    "player syrup idle3"
    pause .2
    repeat

image player syrup idlez:
    "player syrup idlez1"
    pause .4
    "player syrup idlez2"
    pause .4
    "player syrup idlez1"
    pause .4
    "player syrup idlez3"
    pause .4
    repeat

image player syrup electro:
    "player syrup idle1 electro"
    pause .1
    "player syrup idle2 electro"
    pause .1
    "player syrup idle3 electro"
    pause .1
    repeat

image player syrup kerauno:
    "player syrup idle1 kerauno"
    pause .1
    "player syrup idle2 kerauno"
    pause .1
    "player syrup idle3 kerauno"
    pause .1
    repeat

image player syrup attack:
    "player syrup attack1"
    pause .2
    "player syrup attack2"
    pause .2
    "player syrup attack3"

image player syrup attackz:
    "player syrup attackz1"
    pause .4
    "player syrup attackz2"
    pause .4
    "player syrup attackz3"

image player syrup fire:
    "player syrup fire1"
    pause .2
    "player syrup fire2"
    pause .2
    "player syrup fire3"
    pause .2
    "player syrup fire4"

if lohp:

    image player syrup firez:
        "player syrup firez1"
        pause .4
        "player syrup firez2"
        pause .4
        "player syrup firez3"
        pause .4
        "player syrup firez4"

image player syrup red:
    "slice"
    pause .4
    "slice2"
    pause .4
    "slice3"
    pause .4
    "blacc"

image player syrup redd:
    "slice"
    pause .4
    "slice2"
    pause .4
    "slice3"
    pause .3
    "slice2"
    pause .3
    "slice3"
    pause .2
    "slice2"
    pause .2
    "slice3"
    "slice3"
    pause .1
    "slice2"
    pause .1
    "slice3"
    pause .5
    "blacc"

image player syrup slam:
    "player syrup guard2"
    xoffset 0
    linear .06 xoffset +20
    easein .2 xoffset 0

image player syrup parry:
    "white"
    pause .05
    "slice"
    pause .2
    "blacc"

image blightt:
    "white"
    pause .05
    "blight"
    pause .4
    "blacc"

image player syrup hit:
    "player syrup hit1"
    pause .1
    "player syrup hit2"
    pause .06
    "player syrup hit1"
    pause .06
    "player syrup hit2"

image player syrup hitz:
    "player syrup hit1"
    pause .1
    "player syrup hitz2"
    pause .06
    "player syrup hit1"
    pause .06
    "player syrup hitz2"

image player syrup lightning:
    "electro"
    pause .5
    "electro2"
    pause .5
    "blacc"
    pause .5
    "electro3"

image player syrup keraunos:
    "blacc"
    pause .3
    "kerauno" with vpunch
    pause .3
    "kerauno2" with vpunch
    pause .3
    "kerauno3" with vpunch

image player syrup vines:
    "vines"
    pause .5
    "vines2"
    pause .5
    "vines3"
    pause .5
    "vines4"

image player syrup hail:
    "hail3"
    pause .5
    "hail2"
    pause .5
    "hail"
    pause .5
    "hail2"
    pause .5
    "hail"

image player syrup guard:
    "player syrup guard1"
    pause .1
    "player syrup guard2"
image player syrup guardhit:
        "player syrup guard3"
        pause .1
        "player syrup guard2"

image player syrup guardz:
    "player syrup guardz1"
    pause .1
    "player syrup guardz2"

image player syrup guardhitz:
    "player syrup guardz3"
    pause .1
    "player syrup guardz2"

image player syrup down:
    "player syrup down1"
    xoffset 10

    parallel:
        xoffset 0
        easein .8 xoffset -150
    parallel:
        alpha 1.0
        pause .4
        linear .4 alpha 0

image player syrup win:
        "player syrup win1"
        pause .1
        block:
            "player syrup win2"
            pause .3
            "player syrup win3"
            pause .3
            repeat

##ENEMY SPRITES
image enemy goop idle:
    "enemy goop idle1"
    pause .12
    "enemy goop idle2"
    pause .1
    "enemy goop idle3"
    pause .12
    "enemy goop idle4"
    pause .15
    repeat
image enemy goop move:
    "enemy goop idle"
image enemy goop attack:
    "enemy goop idle"
    xoffset 0
    linear .06 xoffset -20
    easein .2 xoffset 0
image enemy goop dodge:
    "enemy goop idle"
    xoffset 0
    linear .06 xoffset 20
    easein .2 xoffset 0
image enemy goop hit:
    "enemy goop hit1"
    pause .1
    "enemy goop hit2"
    pause .06
    "enemy goop hit1"
    pause .06
    "enemy goop hit2"
image enemy goop down:
    "enemy goop down1"
