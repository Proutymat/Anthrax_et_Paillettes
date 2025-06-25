# fonctions custom
init python:
    def type_sound(event, interact=True, cps=35, **kwargs):
        speed = int((0.1/cps)*1000)/1000
        silence = "<silence " + str(speed) + ">"
    
        if not interact:
            return

        if event == "show" :
            for i in range(100):
                print(silence)
                renpy.sound.queue(renpy.random.choice(type_sounds))
                renpy.sound.queue(silence)

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def pausedialogue():
        if renpy.music.is_playing('sound'):
            renpy.pause((20-renpy.music.get_pos('sound')),hard=True)


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

#Assets personnages
image mother:
    "images/Personnages/mother.png"
    zoom 0.35

image delaunay_neutre:
    "images/Personnages/delaunay_neutre.png"
    zoom 0.35

image leandre_neutre:
    "images/Personnages/leandre_neutre.png"
    zoom 0.35

image gatsby_neutre:
    "images/Personnages/gatsby_neutre.png"
    zoom 0.35

image aimee_neutre:
    "images/Personnages/aimee_neutre.png"
    zoom 0.35

image peacock_neutre:
    "images/Personnages/peacock_neutre.png"
    zoom 0.35

image imani_neutre:
    "images/Personnages/imani_neutre.png"
    zoom 0.35

#Assets backgrounds
image devanture = "Backgrounds/devanture.png"

image auditorium = "Backgrounds/auditorium.png"

image bar = "Backgrounds/bar.png"

image loges = "Backgrounds/loges.png"

image rideau = "Backgrounds/rideau.png"

image balcon = "Backgrounds/balcon.png"

image CG_gatsby = "images/CGs/gatsby.jpg"

image background_cg = "images/Backgrounds/background_cg.png"

# Liste des sfx
define type_sounds = ['audio/SFX/TextMix-001.ogg','audio/SFX/TextMix-002.ogg','audio/SFX/TextMix-003.ogg','audio/SFX/TextMix-004.ogg','audio/SFX/TextMix-005.ogg','audio/SFX/TextMix-006.ogg','audio/SFX/TextMix-007.ogg','audio/SFX/TextMix-008.ogg','audio/SFX/TextMix-009.ogg','audio/SFX/TextMix-010.ogg']
define A_type_sounds = ['audio/SFX/AP_TA-001.ogg','audio/SFX/AP_TA-002.ogg','audio/SFX/AP_TA-003.ogg','audio/SFX/AP_TA-004.ogg']
define D_type_sounds = ['audio/SFX/AP_T1-001.ogg','audio/SFX/AP_T1-002.ogg','audio/SFX/AP_T1-003.ogg','audio/SFX/AP_T1-004.ogg']
define M_type_sounds = ['audio/SFX/AP_T2-001.ogg','audio/SFX/AP_T2-002.ogg','audio/SFX/AP_T2-003.ogg','audio/SFX/AP_T2-004.ogg']
define G_type_sounds = ['audio/SFX/AP_T3-001.ogg','audio/SFX/AP_T3-002.ogg','audio/SFX/AP_T3-003.ogg','audio/SFX/AP_T3-004.ogg'] 
define P_type_sounds = ['audio/SFX/AP_T4-001.ogg','audio/SFX/AP_T4-002.ogg','audio/SFX/AP_T4-003.ogg','audio/SFX/AP_T4-004.ogg']
define type_silent = ['<silence 1.0>']

define ui_choice_click = ['audio/SFX/AP_UI_Click-001.ogg','audio/SFX/AP_UI_Click-002.ogg','audio/SFX/AP_UI_Click-003.ogg','audio/SFX/AP_UI_Click-004.ogg','audio/SFX/AP_UI_Click-005.ogg','audio/SFX/AP_UI_Click-006.ogg']

# Liste des ambiances
define audio.AmbAndrogameDay = "audio/Amb/Amb_Cabaret_V4.ogg"
define audio.AmbLoges = "audio/Amb/Amb_LogesDay_V6.ogg"
define audio.AmbRue = "audio/Amb/Amb_Rue_V2.ogg"
define audio.AmbLogesNight = "audio/Amb/Amb_LogesNight_V3.ogg"
define audio.AmbDelShow = "audio/Amb/AP_Amb_ShowDel_V1.ogg"
define audio.BarDay = "audio/Amb/Amb_BarDay_V4.ogg"
define audio.BarEnd = "audio/Amb/Amb_BarEnd_V2.ogg"

# Liste des musiques
define audio.CabaretEntrance = "audio/Music/ON_CabaretEntrance_V1.ogg"
define audio.CabaretIntro = "audio/Music/ON_CabaretIntro_V1_.ogg"
define audio.CabaretLightVerse = "audio/Music/ON_CabaretLightVerse_V1.ogg"
define audio.CabaretLightChorus = "audio/Music/ON_CabaretLightChorus_V1.ogg"
define audio.CabaretLightSolo = "audio/Music/ON_CabaretLightSolo_V1.ogg"
define audio.BadEndSt1 = "audio/Music/AP_Stinger1_V1.ogg"
define audio.BadEndSt2 = "audio/Music/AP_Stinger2_V1.ogg"
define audio.BadEndSt3 = "audio/Music/AP_Stinger3_V1.ogg"
define audio.BadEndSt4 = "audio/Music/AP_Stinger4_V1.ogg"
define audio.BadEnd = "audio/Music/AP_LogesTruc_V1.ogg"
define audio.BackstageLoop = "audio/Music/AP_LogesTruc_V1.ogg"
define audio.BackstageDrumLoop = "audio/Music/ON_BackStageLoop_V1.ogg"
define audio.BarMusic = "audio/Music/AP_BarFull.ogg"
define audio.BarMusicPartB = "audio/Music/AP_BarPartieB.ogg"
define audio.BalconIntro = "audio/Music/AP_Balcon_Intro.ogg"
define audio.BalconCoupletIntro = "audio/Music/AP_Balcon_IntroCouplet.ogg"
define audio.BalconCouplet = "audio/Music/AP_Balcon_Couplet.ogg"
define audio.BalconRefrain = "audio/Music/AP_Balcon_Refrain.ogg"
define audio.BalconEnd = "audio/Music/AP_Balcon_End.ogg"
define audio.LogesIntro = "audio/Music/AP_Loges_Intro.ogg"
define audio.LogesRefrain = "audio/Music/AP_Loges_Refrain.ogg"
define audio.ShowDelaunay = "audio/Music/AP_ShowDelaunay_V2.ogg"
define audio.ShowGatsby = "audio/Music/AP_ShowGatsby_V1.ogg"
define audio.ShowPeacock = "audio/Music/AP_ShowPeacock_V1.ogg"

# Déclarez les personnages utilisés dans le jeu.
define mother = Character('Mother', color="#b51963", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=30, callback=type_sound, cb_cps=30, cb_boopfile=M_type_sounds)
define anthrax = Character('Anthräx', color="#9370db", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=35, callback=type_sound, cb_cps=35, cb_boopfile=A_type_sounds)
define delaunay = Character('Delaunay', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define gatsby = Character('Gatsby', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=G_type_sounds)
define peacock = Character('Peacock', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=P_type_sounds)  
define leandre = Character('Léandre', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define aimee = Character('Aimé.e', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=G_type_sounds)
define imani = Character('Imani', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=P_type_sounds)
define inconnu = Character('???', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50)
define delinconnu = Character('Del?', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define player = Character('[player_name]', color="9370db", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define staff = Character('Staff', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50)
define text = Character(color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)


label gatsby_start:
$ persistent.bg_parallax = True
$ quick_menu = True
default indice_gat = 0
scene black with fade
show loges
show aimee_neutre at gat_center with dissolve
play ambiance AmbLoges volume 0.5 fadein 2.0
stop music fadeout 0.1

#GAT.1
show aimee_laugh at gat_center with dissolve

$ current_textbox = "gatsby"

aimee "Let's go ! On va former un duo d'enfer, je te le dis !"
$ current_textbox = "anthrax"

anthrax "Aha ! J'adore cette énergie. Par quoi voudrais-tu commencer ?"
$ current_textbox = "gatsby"

show aimee_neutre at gat_center
hide aimee_laugh
aimee "Hm... On pourrait se présenter mutuellement, histoire d'apprendre à se connaître, et voir ensuite où ça nous mène ?"
$ current_textbox = "anthrax"

anthrax "C'est une excellente idée."
$ current_textbox = "gatsby"

$ quick_menu = False
show aimee_neutre at gat_right with dissolve
   
menu:
    aimee "Ça te dit qu'on se pose au bar ? C'est plus intime et Barman est un vrai génie dans tout ce qui est cocktail, alcoolisé ou non."
    "Ça me tente bien.":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Je te suis !":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Ça, je ne dis pas non !":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass

$ quick_menu = True

#TRANSITION RIDEAU VERS BAR
#GAT.2
hide aimee_neutre with dissolve
hide loges with dissolve
scene black with fade

play music BarMusicPartB volume 0.5

$ current_textbox = "description" 
text "Nous sommes arrivé.e.s dans l'auditorium et nous sommes approché.e.s du comptoir derrière lequel brillaient un mur de bouteilles aux couleurs uniques."
text "Nous avions depuis le bar une vue imprenable sur la scène, légèrement en contrebas."
text "Les tablées y étaient déjà dressées et se regroupaient autour du big band et de l'estrade secondaire au centre de la pièce."
text "L'immense lustre duquel pendaient des larmes de verre reflétait les spots de lumière à la manière d'une boule à facettes sur le papier peint texturé."
text "Aimée s'assit sur l'une des chaises hautes de bois verni et commanda un Bloody Mary au barman."

show bar 
play ambiance BarDay volume 0.7 fadein 0.5


$ current_textbox = "gatsby"

$ quick_menu = False
show aimee_laugh at gat_right with dissolve
   
menu:
    aimee "Est-ce que tu sais déjà quoi commander ?"
    "Un Pornstar Martini.":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Un Negroni Sbagliato, avec une pointe de prosecco.":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Une citronnade bien fraîche.":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass


$ quick_menu = True
queue music BarMusic volume 0.5
queue music BarMusicPartB volume 0.5

show aimee_neutre at gat_right
hide aimee_laugh

aimee "Alors ! Raconte-moi tout ! D'où est-ce que tu viens ? Qu'est-ce que tu fais ici ? Comment est-ce que tu nous as connu.e.s ?"
$ current_textbox = "anthrax"

anthrax "Oh... Euh... Ça fait beaucoup de questions à la fois..."
$ current_textbox = "gatsby"
show aimee_nosmile at gat_right
hide aimee_neutre

aimee "Pas faux. Commence par le drag alors. Qu'est-ce qui t'as lancé.e ?"
$ current_textbox = "anthrax"

anthrax "Je n'habite pas très loin, donc je passais souvent devant L'Androgame et vous observais de loin."
anthrax "C'est un peu impressionnant. Je me demande si j'ai ma place, je ne m'attendais pas à être retenu.e après l'audition..."

$ current_textbox = "gatsby"

$ quick_menu = False
show aimee_neutre at gat_right
show joy at joy_right
play vfxR VFXJoy
   
menu:
    
    aimee "Bien sûr que tu as ta place ! Mother a l'œil pour repérer les talents."

    "Ça fait longtemps que tu as intégré la troupe?":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Depuis combien de temps est-ce que tu es là?":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Ça doit faire des années que tu es là, non ?":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass


$ quick_menu = True

queue music BarMusic volume 0.5
queue music BarMusicPartB volume 0.5

$ current_textbox = "gatsby"
show aimee_nosmile at gat_right
hide aimee_neutre
aimee "Peut-être... Cinq ans ? Quatre ? Léandre était là déjà avant moi, mais je n'ai pas tardé après lui."
show aimee_neutre at gat_right
hide aimee_nosmile
aimee "Et Imani...? Eh bien, elle bossait déjà là avant en tant que technicienne son. C'est plus récent son lancement dans le drag. Deux ans, il me semble ?"
$ current_textbox = "anthrax"

anthrax "Ah oui, donc ça fait un moment que vous vous connaissez."
$ current_textbox = "gatsby"

show aimee_laugh at gat_right
hide aimee_neutre
aimee "Oui. Ils font même partie de mon cercle d'ami.e.s le plus proche. Mais je ne vais pas leur dire en face sinon ils vont prendre la grosse tête..."
show joy at joy_right
aimee "Et je m'imagine déjà les vannes de Delaunay, quand Léandre sort son alter-ego. Tu verras, c'est assez marrant."
hide joy
$ current_textbox = "anthrax"



$ quick_menu = False
show aimee_neutre at gat_right
hide aimee_laugh
   
menu:
    anthrax "En tout cas, ça promet pour la suite !"
    "Et toi? Qu'est-ce qui t'as lancé dans le drag ?":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Qu'est-ce qui t'as améné.e à L'Androgame?":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Et pourquoi le drag?":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass

$ quick_menu = True

$ current_textbox = "gatsby"
show aimee_nosmile at gat_right
hide aimee_neutre
aimee "Ma quête de genre principalement... Enfin je pense. J'étais dans une phase où je me redécouvrais entièrement."
aimee "Je sortais d'un burn-out, je savais que j'avais plein de choses enfouies à régler... Et j'ai décidé de commencer par ça."
show aimee_neutre at gat_right
hide aimee_nosmile
aimee "Le reste a suivi."


#Choix GAT.2
label choix_gat2:
    $ quick_menu = False
    
    show aimee_neutre at gat_right
    with fade

    menu: 
        "Tu faisais du cirque du coup?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call gat_2_1 from _call_gat_2_1 
        "J'ignorais que tu avais fait un burn-out...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call gat_2_2 from _call_gat_2_2 
        "Donc tu as commencé par le drag pour... Te relever?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call gat_2_3 from _call_gat_2_3 
          

#GAT.2.1
#+1
label gat_2_1:
    $ quick_menu = True
    $ indice_gat += 1
    
    show aimee_neutre at gat_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Tu faisais du cirque du coup ? Est-ce que tu peux m'en raconter davantage ?"
    $ current_textbox = "gatsby"

    show aimee_laugh at gat_center
    hide aimee_neutre
    aimee "Eh bien... J'ai commencé très jeune, avec de la gymnastique."
    aimee "Mes parents ont découvert assez vite que j'étais hyperlaxe, c'était donc un avantage dans ce type de discipline."
    show aimee_neutre at gat_center
    hide aimee_laugh
    aimee "Et j'étais plutôt bon.ne en plus. Mais je commençais à m'ennuyer et j'avais envie de changement."
    aimee "Et avec l'âge, je me suis de plus en plus intéressé.e à d'autres formes d'art, un peu plus physiques mais plus challengeantes !"
    
    $ quick_menu = False
    #show gatsby_neutre at gat_right
    show aimee_laugh at gat_right
    hide aimee_neutre
   
    menu:
        aimee "Et qui dit challenge, dit fun."

        "Énergique à ce que je vois!":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Du genre à aimer les défis, j'aime!":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ça te correspond bien. Tu as l'air d'être du genre...explosif ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "gatsby"

    show joy at joy_right
    aimee "Ha ha ! Merci. Oui, j'ai toujours été assez turbulent.e !"
    hide joy
    show aimee_neutre at gat_right
    hide aimee_laugh
    aimee "Donc fallait y aller pour m'épuiser !"
    $ current_textbox = "anthrax"

    anthrax "Et qu'est-ce que tu sais faire du coup ?"
    $ current_textbox = "gatsby"

    aimee "Pendant quelques années, j'étais contorsionniste."
    aimee "Puis je me suis intéressé.e aux hauteurs."
    $ current_textbox = "anthrax"

    anthrax "Aux hauteurs ?"
    $ current_textbox = "gatsby"

    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "Oui ! Toutes les disciplines qui avaient un rapport de près ou de loin au vide."
    aimee "Équilibrisme, acrobatie aérienne, voltige, trapèze, cerceaux volants..."
    show aimee_neutre at gat_right
    hide aimee_laugh
    $ current_textbox = "anthrax"

    anthrax "Et tu n'as jamais eu le vertige ? J'ai le tournis rien que de m'imaginer ça."
    $ current_textbox = "gatsby"

    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "Jamais ! Au contraire, la partie la plus drôle, c'était la chute."
    show aimee_neutre at gat_right
    hide aimee_laugh
    aimee "Après, il y avait toujours un filet ou des matelas pour nous rattraper, donc les dangers étaient minimes pour peu qu'on apprenne à bien tomber."


    $ quick_menu = False
    show aimee_laugh at gat_right
    hide aimee_neutre
   
    menu:
        aimee "Et rien de mieux dans la vie que d'apprendre à se relever après un échec !"
        "Mais tu as arrêté en rejoignant la troupe, non ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Tu continues sur ton temps libre?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Et tu en fais toujours?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True


    show aimee_neutre at gat_right
    hide aimee_laugh

    anthrax "Et tu en fais toujours ?"
    $ current_textbox = "gatsby"

    
    aimee "Hm... Disons que je reprends doucement."
    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "J'ai beau avoir un corps d'Adonis, il n'a plus les mêmes capacités qu'avant."
    show aimee_neutre at gat_right
    hide aimee_laugh
    aimee "Mais ça ne m'empêche pas d'improviser, puisque je n'ai pas non plus tout perdu."
    show joy at joy_right
    aimee "Après tout, j'y ai consacré la majorité de ma vie. Ce n'est pas une mauvaise passe qui va envoyer en l'air tous mes efforts."
    hide joy
    aimee "Recommencer ne me fait pas peur. Et si je peux compiler avec la personne que je suis devenu.e, ce serait un triomphe !"

    jump gat_3
    call gat_3 from _call_gat_3 

#GAT.2.2
#-1
label gat_2_2:
    $ quick_menu = True
    $ indice_gat -= 1
    
    show aimee_neutre at gat_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "J'ignorais que tu avais fait un burn-out. C'était quel genre d'environnement de travail pour que ça en arrive là ?"
    $ current_textbox = "gatsby"

    show aimee_nosmile at gat_center
    hide aimee_neutre
    aimee "Ça n'en a peut-être pas l'air comme ça, mais j'étais acrobate dans une troupe de cirque..."
    aimee "On était constamment en déplacement à l'étranger pour des tournées, et disons que l'ambiance aux répétitions et en spectacles n'était pas au beau fixe."
    show aimee_irritated at gat_right
    hide aimee_nosmile
    aimee "Pendant un long moment, c'était le genre de chose que je ne pouvais pas voir en peinture ou entendre parler."
   
   
    $ quick_menu = False
    show aimee_neutre at gat_right
    hide aimee_irritated
   
    menu:
        aimee "Alors que j'en étais réellement passionné.e..."

        "Quel enfer... De quoi abandonner...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Tu as arrêté?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Merde... Et du coup, ça a dû te dégoûter complètement..":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True


    anthrax "Merde... Et du coup, ça a dû te dégoûter complètement..."
    $ current_textbox = "gatsby"

    aimee "Pendant un temps, oui."
    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "Mais plus à présent. C'est même redevenu ma spécialité au sein de l'Androgame."
    show aimee_neutre at gat_right
    hide aimee_laugh
    aimee "La majorité de mes numéros sont acrobatiques."
    aimee "Dis-toi que Mother a même fait des modifications dans la structure de la scène, pour l'accommoder à mes besoins techniques."
    $ current_textbox = "anthrax"

    anthrax "Ça a dû être assez coûteux."
    $ current_textbox = "gatsby"

    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "Rien qu'une avance sur le salaire ne puisse régler !"
    show aimee_neutre at gat_right
    hide aimee_laugh
    aimee "Non, je plaisante. Je n'ai pas eu à contribuer aux frais. C'est juste bien tombé puisque des rénovations étaient déjà prévues."
    aimee "Mother est une vraie businesswoman. Je ne sais pas quels contacts elle cache dans son décolleté..."
    

    $ quick_menu = False
    show aimee_laugh at gat_right
    hide aimee_neutre
   
    menu:
        aimee "Mais si tu as besoin de n'importe quoi, je suis sûr.e qu'elle a quelqu'un pour te dépanner."
        "Dans quoi est-ce que tu te spécialises alors ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Qu'est-ce que tu as repris comme discipline du coup ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Et du coup, qu'est-ce que tu fais exactement comme acrobatisme?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    show aimee_pensive at gat_right
    hide aimee_neutre
    anthrax "Et du coup, qu'est-ce que tu fais exactement comme acrobatisme ?"
    $ current_textbox = "gatsby"

    show aimee_neutre at gat_right
    hide aimee_pensive
    aimee "As-tu réellement envie que je te spoile ? Je peux te laisser la surprise pour le prochain show~"
    $ current_textbox = "anthrax"

    anthrax "Juste un indice alors ?"
    $ current_textbox = "gatsby"

    aimee "Un indice ? Très bien."
    show aimee_laugh at gat_right
    hide aimee_neutre
    show joy at joy_right
    aimee "Il y a de quoi te faire tourner la tête...~"
    hide joy

    call gat_3 from _call_gat_3_1 

#GAT.2.3
#+0
label gat_2_3:
    $ quick_menu = True

    show aimee_neutre at gat_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Donc tu as commencé par le drag pour... Te relever ? Ce n'est peut-être pas la première chose à laquelle on pense quand on commence sa \"healing journey\"."
    $ current_textbox = "gatsby"

    show aimee_laugh at gat_center
    hide aimee_neutre
    aimee "Oh, ne t'en fais pas que j'allais déjà chez le psy ! Je ne l'ai d'ailleurs jamais quitté.e..."
    show aimee_neutre at gat_center
    hide aimee_laugh
    aimee "Non, j'étais déjà à un stade suffisamment avancé de réflexion pour me lancer dans l'exploration tout de même."
    aimee "J'avais les clefs en main, mais je ne savais pas quelle porte ouvrir. Ou bien même où est-ce qu'elle était cette foutue porte."
    aimee "Alors que je suis plutôt du genre à les enfoncer..."
    show aimee_laugh at gat_center
    hide aimee_neutre
    aimee "Et tout ça pour réaliser que ce n'était pas une porte mais une trappe vers le grenier où j'avais entassé pas mal de vieux démons en espérant les y oublier..."
    


    $ quick_menu = False
    show aimee_laugh at gat_right with dissolve
    show joy at joy_right
    play vfxR VFXJoy

    show aimee_pensive at gat_right
    hide aimee_laugh at gat_right
   
    menu:
        aimee "Enfin bref, pas mal de métaphores pour dire une seule chose : \"Maintenant, ça va mieux\"."
        "Une sacrée progression alors... Et un peu de déni ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ça a l'air d'avoir été fastidieux. Comment t'es tu lancé.e ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Par quoi est-ce que tu as commencé le drag ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "gatsby"
    show aimee_neutre at gat_right
    hide aimee_pensive
    aimee "Eh bien... Au tout départ, c'était avec des sorties costumées, comme Halloween ou Mardi Gras."
    aimee "On avait aussi ces petites soirées à thème avec mes ami.e.s où l'on venait déguisé.e.s, et j'utilisais ces occasions à fond..."
    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "Puisque c'était les seuls moments où je sentais que je pouvais m'amuser avec les frontières du genre et repousser quelques limites."
    show aimee_neutre at gat_right
    hide aimee_laugh
    aimee "Puis j'ai de plus en plus assumé, avec du jeu de rôle notamment."
    aimee "Et j'ai découvert une association queer qui proposait des ateliers drag. Donc, je me suis inscrit.e."
   
    $ current_textbox = "anthrax"

    anthrax "Sur un coup de tête ? Comme ça ?"
    $ current_textbox = "gatsby"


    $ quick_menu = False
    #show gatsby_neutre at gat_right
    show aimee_neutre at gat_right
    hide aimee_neutre
    show joy at joy_right
    play vfxR VFXJoy
    show aimee_laugh at gat_right
   
    menu:
        aimee "Après tout, c'est un peu comme toi lorsque tu t'es présenté.e à l'audition. Parfois, il faut juste se lancer."
        "Tu me montreras des photos? Je suis curieux.se.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Qu'est-ce qui t'as inspiré.e pour créer ton personnage?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est vrai... Et à quoi ressemblait ton drag au début?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass

    $ quick_menu = True

    $ current_textbox = "gatsby"

    show joy at joy_right
    aimee "Je suis content.e que tu demandes !"
    hide joy
    show aimee_neutre at gat_right
    hide aimee_laugh
    aimee "Au départ, c'était plutôt du drag clown et du drag creature... Ça ne ressemblait pas à grand-chose, mais c'était le but."
    aimee "Je m'inspirais principalement d'œuvres d'art et j'essayais de les reproduire sur mon corps avec une pointe de body horror."
    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "C'était assez fun. Dommage que ça ne colle pas trop avec le style de l'Androgame..."
    $ current_textbox = "anthrax"
    show aimee_neutre at gat_right
    hide aimee_laugh
    anthrax "Et tu es toujours dans cette association ?"
    $ current_textbox = "gatsby"
    
    show sadness at sadness_right
    play vfxR VFXSadness
    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "Oui ! Mais malheureusement, on n'y fait plus trop de spectacles. Chacun.e a sa vie et d'autres priorités, et le drag est passé au second plan." 
    show aimee_neutre at gat_right
    hide aimee_laugh
    aimee "Mais peut-être que ça reprendra un jour, qui sait ?"
    call gat_3 from _call_gat_3_2 

#TRANSITION RIDEAU & GRADIENT A AJOUTER + quelques mois blabla (vers auditorium)
#GAT.3
label gat_3:

    $ persistent.bg_parallax = False
    hide aimee_laugh with dissolve
    stop music fadeout 0.5
    stop ambiance fadeout 1.0
    show curtain_close with dissolve
    play vfxC SFXCurtainClose
    pause 1.5
    hide bar
    show curtain_open 
    play vfxC SFXCurtainOpen

    show gradient
    play music LongEllipse volume 0.7
    show text "{size=60}{color=#FFFFFF}Quelques mois passèrent...{/color}{/size}" at truecenter

    pause 6

    hide text with dissolve
    hide gradient with fade
    stop music fadeout 1.5

    pause 2

    $ persistent.bg_parallax = True

    $ current_textbox = "description"
    text "Cela faisait plusieurs minutes que je cherchais Aimé.e, avec qui j'étais supposé.e répéter une partie de mon numéro, que l'on construisait ensemble."
    text "Après avoir fait trois fois le tour du bâtiment, je finis par retourner sur les planches de la scène, pensif.ve."
    text "Et en toute honnêteté, un peu inquiet.e."
    text "Puis je l'aperçus, dominant un carnet sur lequel iel tapotait la mine de son crayon, posé sur l'un des mange-debouts. "
    text "Je le.a rejoignis rapidement."

    play music BalconIntro noloop
    show auditorium

    $ current_textbox = "anthrax"

    $ quick_menu = False
    

    play vfxR VFXSadness
    show aimee_irritated at gat_right with dissolve
    show sadness at sadness_right
   
    menu:
        "Hey... Je me demandais où tu étais passé.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Aimé.e ! Ça fait un moment que je te cherche !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Alors c'était là où tu te cachais !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "gatsby"

    hide sadness
    show aimee_pensive at gat_right
    hide aimee_irritated
    aimee "Oh, pardon... Je ne pensais pas que tu me cherchais."

    $ current_textbox = "anthrax"
    anthrax "Euh... Nous étions censé.e.s nous retrouver pour nous entraîner..."

    $ current_textbox = "gatsby"
    show aimee_nosmile at gat_right
    hide aimee_pensive
    aimee "Meeeeeerde ! J'ai complètement zappé ! Je suis désolé.e !"

    $ current_textbox = "anthrax"
    anthrax "Ce n'est pas grave, c'est le genre de chose qui arrive. Qu'est-ce que tu fais... ?"

    $ current_textbox = "gatsby"
    show aimee_neutre at gat_right
    hide aimee_nosmile
    aimee "Ça ? J'essaye de tenir un journal."

    $ current_textbox = "anthrax"
    anthrax "Un journal ?"

    $ current_textbox = "gatsby"
    aimee "Oui, pour mettre à plat ma progression, mes hauts et mes bas... Histoire de garder une trace du chemin parcouru et de ce que j'ai accompli."

    $ current_textbox = "anthrax"
    anthrax "Oh ! Un journal intime quoi !"

    $ current_textbox = "gatsby"
    show aimee_irritated at gat_right
    hide aimee_neutre
    aimee "Ça fait tout de suite moins sérieux dit comme ça... Mais oui, un journal intime."
    queue music BalconIntro noloop

    $ current_textbox = "description"

    $ quick_menu = False
    show aimee_neutre at gat_right
    show sadness at sadness_right
    play vfxR VFXSadness
   
    show aimee_nosmile at gat_right
    hide aimee_irritated
    show overlay

    menu:
        text "Soudainement l'air un peu ailleurs, Aimée se mordit l'intérieur de la joue, sans reprendre la parole. Ellui étant si bavard.e, c'était plutôt surprenant de sa part..."
        "Allô la Terre, Aimé.e ? Ici [player_name]...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ta tête ne me dit rien qui vaille... Qu'est-ce qu'il y a ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Tout va bien?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    hide overlay
    $ current_textbox = "gatsby"

    show aimee_pensive at gat_right
    hide aimee_nosmile
    aimee "Hm..."
    aimee "Peut-être qu'en parler m'aidera à mieux trouver les mots pour l'écrire..."

    $ current_textbox = "anthrax"
    anthrax "Oh... ?"

    queue music BalconCoupletIntro
    queue music BalconCouplet
    $ current_textbox = "gatsby"
    show aimee_nosmile at gat_right
    hide aimee_pensive
    aimee "Tu vois quand je t'ai parlé de mon burn-out ? Ça a eu des conséquences bien plus dévastatrices sur ma santé mentale qu'une \"simple\" dépression..."
    aimee "Avec la pression au sein de mon ancienne troupe, j'ai développé des troubles du comportement alimentaire."
    show aimee_pensive at gat_right
    hide aimee_nosmile
    aimee "Boulimie, anorexie, un mix des deux, puis un soupçon de mérycisme... Enfin bref."
    aimee "Rien de bien joyeux, mais j'aimerais réussir à le noter dans mon carnet pour..."
    show aimee_nosmile at gat_right
    hide aimee_pensive
    aimee "Je ne sais pas... Enfin tourner la page ?"


#Choix GAT.3
label choix_gat3:
    $ quick_menu = False

    show aimee_neutre at gat_right
    hide aimee_nosmile 
    with fade

    menu: 
        "Est-ce que ça va mieux maintenant ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call gat_3_1 from _call_gat_3_1_1
            queue music BalconRefrain
        "Wow... Quand je te vois maintenant... Je ne pensais pas...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call gat_3_2 from _call_gat_3_2_1
            queue music BalconRefrain
        "Tu as dû prendre pas mal de temps pour t'en remettre, non?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            queue music BalconRefrain
            call gat_3_3 from _call_gat_3_3 

#GAT.3.1
#+0
label gat_3_1:
    $ quick_menu = True

    show aimee_neutre at gat_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Est-ce que ça va mieux maintenant que tu as quitté cet environnement ?"
    $ current_textbox = "gatsby"

    show aimee_laugh at gat_center
    hide aimee_neutre
    aimee "Oui ! Énormément même !"
    show aimee_neutre at gat_center
    hide aimee_laugh
    aimee "Ça n'a pas encore complètement disparu, mais c'est sur une excellente voie !"
    aimee "Je n'ai jamais été aussi bien dans ma peau, mon apparence et ma confiance."
    $ current_textbox = "anthrax"

    anthrax "Ça me rassure un peu... Ça ne rigole pas les TCA."
    $ current_textbox = "gatsby"

    show aimee_laugh at gat_center
    hide aimee_neutre
    aimee "Ce n'est pas moi qui vais te dire le contraire !"

    $ quick_menu = False
    show aimee_neutre at gat_right with dissolve
    hide aimee_laugh
   
    menu:
        aimee "Remonter la pente est ce qui a été le plus compliqué, mais maintenant que c'est passé, je suis inarrêtable."
        "Ça fait plaisir de te voir d'attaque, mais pourquoi c'est arrivé ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Comment est-ce que tu es tombé dedans ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Mais qu'est-ce qui t'as causé de sombrer en premier lieu ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True


    $ current_textbox = "gatsby"

    show aimee_nosmile at gat_right
    hide aimee_neutre
    aimee "Je pense que c'était sincèrement la pression qu'on me mettait. C'est même indéniable..."
    show aimee_irritated at gat_right
    hide aimee_nosmile
    aimee "Quelqu'un était constamment sur mon dos pour surveiller mon poids, mon déficit calorique, combien de litres d'eau je buvais par jour, quels compléments alimentaires..."
    aimee "Je n'ai pas toujours eu le corps que j'ai aujourd'hui, c'était un régime très strict."
    show aimee_pensive at gat_right
    hide aimee_irritated
    aimee "Ça a d'ailleurs commencé par de l'anorexie. Je pense qu'avec le recul, j'avais terriblement besoin de contrôle."
    show aimee_nosmile at gat_right
    hide aimee_pensive
    aimee "Et le peu que je pouvais grapiller se trouvait là..."
    $ current_textbox = "anthrax"

    anthrax "Ça devait être abominable."
    $ current_textbox = "gatsby"

    show aimee_neutre at gat_right
    hide aimee_nosmile
    aimee "Hm... Peut-être, mais j'ai survécu."
    aimee "Surtout qu'à cette époque, j'étais particulièrement mal dans mes baskets, et je n'avais pas encore réalisé que je me posais des questions sur mon genre."
    show aimee_pensive at gat_right
    hide aimee_neutre
    aimee "C'était vraiment un pêle-mêle de sentiments néfastes, sans un pour rattraper l'autre."
    aimee "Et j'ai beau avoir fini par quitter la troupe, j'étais tellement matrixé.e que les TCA ne se sont pas arrêtés là."
    show aimee_nosmile at gat_right
    hide aimee_pensive
    aimee "Maintenant, j'avais une sorte de vide à combler, et j'ai fait de l'hyperphagie."

    $ quick_menu = False
   
    menu:
        aimee "Bref..."
        "Le cabaret a dû avoir une sacrée influence sur ta guérison...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est ce lieu qui t'as sauvé.e ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est l'Androgame qui t'as aidé à t'en sortir ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass

    $ quick_menu = True

    $ current_textbox = "gatsby"

    aimee "L'Androgame ? Non."
    show aimee_neutre at gat_right
    hide aimee_nosmile
    aimee "Mais ma psy et le drag, par contre, oui !"
    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "J'ai trouvé une communauté, et un espace pour me redécouvrir, qui m'acceptait pour quiconque je devenais."
    show joy at joy_right
    play vfxR VFXJoy
    aimee "Franchement, c'était salvateur. Et j'ai pu commencer à aborder plus ouvertement les épreuves que je traversais."
    hide joy
    show aimee_neutre at gat_right
    hide aimee_laugh
    aimee "Jusqu'à ultimement les surmonter."
    aimee "C'est après seulement que j'ai découvert l'Androgame !"

    call gat_4 from _call_gat_4 

#GAT.3.2

label gat_3_2:
    $ indice_gat += 1
    $ quick_menu = True
    
    show aimee_neutre at gat_center
    with fade

    anthrax "Wow... Quand je te vois maintenant... Je ne pensais pas..."
    $ current_textbox = "gatsby"

    show aimee_pensive at gat_center
    hide aimee_neutre
    aimee "\"Tu ne pensais pas\" quoi ?"
    $ current_textbox = "anthrax"

    anthrax "Eh bien... Ça ne te ressemble pas. Enfin, pas au toi d’aujourd’hui."
    show aimee_nosmile at gat_center
    hide aimee_pensive
    anthrax "Je te vois comme cette personne bien dans son corps, hyper confiante..."
    anthrax "J’ai juste un peu de mal à réaliser que tu n’as pas été... épargné.e ?"
    $ current_textbox = "gatsby"

    show aimee_irritated at gat_center
    hide aimee_nosmile
    aimee "Hm... Je pourrais me vexer, mais je crois voir où tu veux en venir."
    show aimee_nosmile at gat_center
    hide aimee_irritated
    aimee "Je ne pense pas que mes TCA viennent de là, il y a plein d’autres raisons que de vouloir correspondre à un standard de beauté pour que ça se déclenche."
    aimee "Ça a commencé avec moi parce que j’avais besoin de contrôle dans ma vie, et que c’était là où je le trouvais."
    show aimee_pensive at gat_center
    hide aimee_nosmile
    aimee "Enfin... C’est ce que je préférais me raconter plutôt..."
    $ current_textbox = "anthrax"
    hide aimee_pensive
    

    $ quick_menu = False
    show aimee_nosmile at gat_right with dissolve
   
    menu:
        anthrax "Désolé.e, je ne voulais pas te blesser. J’ai été maladroit.e dans mes mots."
        "Est-ce que tu peux... développer ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est-à-dire ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Qu'est-ce que tu sous-entends par là?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "gatsby"

    show aimee_pensive at gat_right
    hide aimee_nosmile
    aimee "Eh bien..."
    show sadness at sadness_right
    play vfxR VFXSadness
    aimee "Putain, c’est pas simple d’en parler..."
    hide sadness
    show aimee_nosmile at gat_right
    hide aimee_pensive
    aimee "En fait, quand tu entres dans une crise... Que ce soit à te pencher au-dessus d’une cuvette et enfoncer tes doigts dans la gorge ou avaler tout ce qui tombe sous ta main..."
    aimee "Tu n’es pas toi-même. Enfin, plutôt... Tu n’as pas le contrôle sur ce que tu fais à cet instant..."
    aimee "C’est comme si tu étais possédé.e."
    show aimee_irritated at gat_right
    hide aimee_nosmile
    aimee "Mais le pire dans tout ça, c’est que tu te sens étrangement satisfait.e après... Et c’est là où est le danger."
    aimee "Parce que ça te fait sentir bien, tu commences à croire que c’est normal, et que c’est même une solution."

    $ quick_menu = False
    show aimee_nosmile at gat_right
    hide aimee_irritated
   
    menu:
        aimee "Et ensuite, tu ne te sors plus de ce cercle vicieux. Ou du moins, très difficilement..."
        "C'est tant mieux si tu n'as plus rien maintenant.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ça n'a pas dû être simple de tourner la page...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Mais maintenant, tu en as encore...?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass

    $ quick_menu = True

    $ current_textbox = "gatsby"

    show aimee_pensive at gat_right
    hide aimee_nosmile
    aimee "Hm... Ce n’est pas aussi simple que ça. J’en ai encore les stigmates, pour être honnête."
    show aimee_neutre at gat_right
    hide aimee_pensive
    aimee "Justement, je me sens bien dans mes baskets, et j’aime le reflet que je vois dans le miroir..."
    aimee "Puisque c’est la version de moi la plus heureuse que j’ai eue dans ma vie."
    aimee "Sauf peut-être quand j’étais enfant, mais je n’en ai plus tellement de souvenirs..."
    show aimee_nosmile at gat_right
    hide aimee_neutre
    aimee "Tout le monde ne penserait pas que c’est le cas parce que dans leur tête, être gros.se équivaut à devoir automatiquement se sentir misérable."
    show aimee_pensive at gat_right
    hide aimee_nosmile
    aimee "Mais j’étais bien plus misérable quand j’avais la peau sur les os et que mon patron me disait que je devais encore surveiller mon poids pour pouvoir faire de la contorsion."
    show aimee_neutre at gat_right
    hide aimee_pensive
    aimee "C’est toute une histoire..."
    $ current_textbox = "anthrax"

    anthrax "Et pas l’une des plus joyeuses..."
    $ current_textbox = "gatsby"

    aimee "Ça c’est clair..."
    show aimee_laugh at gat_right
    hide aimee_neutre
    aimee "Mais je suis là aujourd'hui, j'en demande pas plus !"

    hide aimee_laugh with dissolve
    call gat_4 from _call_gat_4_1 

#GAT.3.3
label gat_3_3:
    $ quick_menu = True
    $ indice_gat -= 1
    
    show aimee_neutre at gat_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Tu as dû prendre pas mal de temps pour t'en remettre, non ?"
    $ current_textbox = "gatsby"

    show aimee_laugh at gat_center
    hide aimee_neutre
    aimee "Oh ça ! Et encore, je suis loin d'en avoir fini !"
    show aimee_pensive at gat_center
    hide aimee_laugh
    aimee "Bon, au moins je ne me prive plus de nourriture, ni me fais vomir, ni vide les placards au moindre mental breakdown."
    show aimee_neutre at gat_center
    hide aimee_pensive
    aimee "Juste parfois, je me reprends à y penser. Sans l'envisager hein ! C'est déjà du progrès."
    $ current_textbox = "anthrax"

    

    $ quick_menu = False
    show aimee_neutre at gat_right with dissolve
   
    menu:
        aimee "Tant que je ne rechute pas, c'est le principal."
        "C'est un risque seulement ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Mais tu as surmonté tout ça, ça devrait aller...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est quelque chose qui t'inquiète? De rechuter ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass

    $ quick_menu = True

    $ current_textbox = "gatsby"

    show aimee_pensive at gat_right
    hide aimee_neutre
    aimee "Oui, et non... J'ai suffisamment dépassé tout ça et me suis construit une force mentale telle que je ne me laisserais pas retomber."
    show aimee_nosmile at gat_right
    hide aimee_pensive
    aimee "Et d'un autre côté, c'est toujours une peur un peu irrationnelle qui ne me quitte jamais."
    show sadness at sadness_right
    aimee "Surtout que sur le chemin de la convalescence, j'ai eu beaucoup de hauts et de bas."
    hide sadness
    show aimee_irritated at gat_right
    hide aimee_nosmile
    aimee "Des périodes qui allaient vraiment très bien, et d'autres où je me sentais comme la dernière des merdes."
    show aimee_nosmile at gat_right
    hide aimee_irritated
    aimee "Chacune durait plus ou moins longtemps. Des mois même !"
    aimee "Et mon corps qui subissait tout ça au passage."

    anthrax "Ça a fini par se stabiliser du coup ?"
    $ current_textbox = "gatsby"

    show aimee_neutre at gat_right
    hide aimee_nosmile
    aimee "Visualise ça comme un yo-yo. Sans mauvais jeu de mot."
    aimee "Au début, il descend et remonte très fort, jusqu'à perdre en vélocité. Et ensuite, il rebondit de moins en moins haut et de moins en moins bas."
    $ current_textbox = "anthrax"

    anthrax "Bon, un yo-yo finit quand même par se stopper tout en bas..."
    $ current_textbox = "gatsby"

    show aimee_irritated at gat_right
    hide aimee_neutre
    aimee "Imagine qu'il n'y a pas de gravité dans ce cas. Ah mais du coup, le yo-yo ne tomberait pas en premier lieu..."
    aimee "Bon, oublie cette métaphore foireuse !"
    show aimee_nosmile at gat_right
    hide aimee_irritated
    aimee "Ce qui compte, c'est qu'au fil du temps, avec la volonté de guérir qui va avec parce qu'on n'a rien sans rien, les pics sont moins intenses."
    aimee "Jusqu'à disparaître."

    $ current_textbox = "anthrax"

    $ quick_menu = False
    show aimee_neutre at gat_right
    hide aimee_nosmile
   
    menu:
        aimee "Et que les TCA disparaissent, c'est ça qu'on veut."
        "Tu penses que c'est derrière toi tout ça?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Qu'est-ce qu'il faudrait pour te destabiliser à nouveau?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Et où est-ce que tu en es à présent? Si ce n'est pas encore ça....":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "gatsby"

    show aimee_nosmile at gat_right
    hide aimee_neutre
    aimee "Eh bien... Disons que le yo-yo oscille. Mais il faudrait vraiment un gros coup de vent ou une catastrophe naturelle pour qu'il se remette à bouger vraiment."
    aimee "Je n'ai pas parcouru tout ce chemin pour me laisser tomber au moindre inconvénient..."
    $ current_textbox = "anthrax"

    anthrax "Bon, tant mieux alors !"

    call gat_4 from _call_gat_4_2 

#TRANSITION RIDEAU & GRADIENT VERS LOGES + "LE JOUR DU SPECTACLE"
#GAT.4
label gat_4:

    stop music fadeout 0.5
    $ persistent.bg_parallax = False
    hide aimee_nosmile with dissolve
    hide aimee_neutre with dissolve
    show curtain_close  with dissolve
    pause 1.5
    hide auditorium 
    show curtain_open 

    show gradient with dissolve
    show text "{size=60}{color=#FFFFFF}Le jour du spectacle...{/color}{/size}" at truecenter

    pause 6

    hide text with dissolve
    hide gradient with fade

    stop music fadeout 0.5
    stop ambiance fadeout 0.5
    play music LogesIntro volume 0.5
    
    hide aimee_neutre

    $ persistent.bg_parallax = True
    $ current_textbox = "description"
    text "Le calme illusoire de la loge contrastait drastiquement avec le bourdonnement du staff passé la porte."
    text "Les discussions étaient légères et l'entraide entre les artistes pour régler les petits aléas techniques était doux à voir."
    text "Malgré tout, chacun.e se préparait avec diligence, en jetant nerveusement un coup d'œil à l'heure qui tournait plusieurs fois dans la même minute."
    text "Assis.e sur une chaise face à l'un des miroirs, Aimé décoiffait son mohawk à l'aide d'une large brosse avant d'appliquer un conditionner."
    text "Pendant que son teint était en train de se fixer, iel tressa les sections, puis enfila un collant pour tout bien plaquer contre son crâne..."
    text "Puis mit la perruque qui l'attendait sur son mannequin... En quelques coups de peigne et de gel, des vagues décorèrent son front..."
    text "Et quelques perles adoucissaient son regard tandis que ses paupières se berçaient d'écume."
    $ current_textbox = "gatsby"

    $ current_textbox = "anthrax"

    $ quick_menu = False
    show loges
    play ambiance AmbLoges fadein 0.5
    queue music LogesRefrain
    show gatsby_pensive at gat_right with dissolve
   
    menu:
        gatsby "[player_name], est-ce que tu pourrais me rendre un service ?"
        "Bien sûr, de quoi as-tu besoin ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Sans soucis ! Dis-moi.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Certainement! Quoi donc...?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "gatsby"

    show gatsby_nosmile at gat_right
    hide gatsby_pensive
    gatsby "Est-ce que ce serait possible de me passer les pièces de mon costume pendant que je me change ? Le paravent est ridiculement petit..."

    $ current_textbox = "description"
    #show overlay
    text "Aimé.e gardait son air confiant malgré son maquillage aux traits de Pierrot. Cependant, je décelais quelques incertitudes dans son regard. Peut-être de l'appréhension."


    $ quick_menu = False
    show gatsby_neutre at gat_right
   
    menu:
        text "Avait-iel peur de me demander une telle chose ? Cela semblait délicat pour iel de me demander cela. Mais qu'iel me fasse confiance ainsi me fit anormalement plaisir."
        
        "Qu'est-ce que tu veux que je t'apporte ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Où est-ce que tu as rangé tes affaires ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Je te trouve ça où...?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True


    text "Iel me pointa une chaise et disparu avec son regard espiègle derrière la toile de la cabine improvisée."
    text "Je pris le costume et passa mes doigts sur le tulle léger, les strass, testant l'élasticité du tissu avec précaution."
    show gatsby_pensive at gat_right
    hide gatsby_neutre
    text "Aimé.e me tendit ensuite son haut en dehors de son vestiaire et je compris à l'oreille que Gatsby quittait son binder pour taper sa poitrine."
    text "Après tout, son tour était très physique et lui demandait une liberté de mouvements, qui clashaient peut-être avec sa dysphorie de genre..."
    #hide overlay
    $ current_textbox = "gatsby"

    show gatsby_neutre at gat_right
    hide gatsby_pensive
    gatsby "Merci... J'aurais besoin du harnais de sécurité s'il te plaît."

#Choix GAT.4
label choix_gat4:
    $ quick_menu = False
    $ current_textbox = "description"

    show gatsby_neutre at gat_right

    menu: 
        text "Je lui tendis en réfléchissant à quoi dire pour meubler le silence."
        "Ce n'est pas trop compliqué de performer ? ":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call gat_4_1 from _call_gat_4_1_1 
        "Je te trouve courageux.se. Tout ce que tu réussis à accomplir...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call gat_4_2 from _call_gat_4_2_1 
        "J'étais persuadé.e que tu ne toucherais plus aux arts acrobatiques.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call gat_4_3 from _call_gat_4_3 

#GAT.4.1
#+1
label gat_4_1:
    $ quick_menu = True
    $ indice_gat += 1
    
    hide gatsby_nosmile
    show gatsby_neutre at gat_center with fade
    $ current_textbox = "anthrax"

    anthrax "Ce n'est pas trop compliqué de performer ? Je veux dire... Le rapport au corps, tout ça... ?"
    $ current_textbox = "gatsby"


    gatsby "Mon corps, c'est un peu mon meilleur ennemi."
    gatsby "Dans le sens où c'est avec lui que je suis capable de faire ce que je fais, et je sais que je suis doué.e."
    show gatsby_nosmile at gat_right
    hide gatsby_neutre
    gatsby "Et d'un autre côté, j'ai toujours une dysphorie de genre assez fluctuante..."
    $ current_textbox = "anthrax"

    $ quick_menu = False
    show gatsby_neutre at gat_right with dissolve
    hide gatsby_nosmile
   
    menu:
        gatsby "Donc je ne sais pas si je vais être au top de ma forme ou non, avant un show."
        "J'imagine ça comme un sentiment très... viscéral ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ça sonne comme terriblement handicapant...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "À ce point ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "gatsby"

    show gatsby_laugh at gat_right
    gatsby "Parfois oui, j'adore mon corps, mes formes, sa force... "
    hide gatsby_laugh
    show gatsby_nosmile at gat_right
    gatsby "Et il suffit d'un instant pour avoir l'impression que ma peau n'est pas la mienne, que quelque chose est à vif en dessous, que ça grouille."
    hide gatsby_neutre
    show gatsby_pensive at gat_right
    hide gatsby_nosmile
    gatsby "C'est très spécial à décrire..."
    $ current_textbox = "delaunay"

    show delaunay_nosmile at del_left with dissolve
    delaunay "Hm... Je comprends exactement ce que tu veux dire..."
    $ current_textbox = "peacock"

    hide gatsby_pensive
    show peacock_neutre at pea_right with dissolve
    peacock "C'est peut-être pour ça que le drag est notre plus grand atout finalement, on peut se permettre d'explorer."
    $ current_textbox = "gatsby"

    hide delaunay_nosmile
    show gatsby_laugh at gat_left with dissolve
    gatsby "Plus qu'explorer, je dirais même se réconcilier. La majeure partie du temps, je me sens super bien dans ma peau."
    hide gatsby_laugh
    gatsby "Devoir accomplir des prouesses physiques, se dévoiler, ne pas avoir droit à l'erreur et être obligé.e de rester concentré.e..."
    gatsby "Quand juste parfois le mood n'est pas là, c'est bien plus embarrassant que ce qu'on croirait."
    show gatsby_pensive at gat_left
    hide gatsby_neutre
    gatsby "Même moi, j'ai sous-estimé l'impact que ça aurait sur ma performance au début. Ça va que je réussis maintenant à gérer."
    $ current_textbox = "anthrax"
    
    anthrax "Ça t'est déjà arrivé pendant que tu étais sur scène ?"
    $ current_textbox = "gatsby"

    show gatsby_nosmile at gat_left
    hide gatsby_pensive
    gatsby "Si on parle de crise de dysphorie, non. Et j'ai bien de la chance. C'est plus une sensation de malaise qu'autre chose."
    $ current_textbox = "peacock"

    $ quick_menu = False
   
    show peacock_nosmile at pea_right
    hide gatsby_nosmile

    menu:
        peacock "C'est déjà arrivé une fois à Léandre cependant, au début."
         
        "Vraiment ?!":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Je n'y crois pas !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Oh non...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "delaunay"

    show delaunay_shy at del_left with dissolve
    delaunay "Oui, mais c'était un cas exceptionnel. "
    delaunay "Et j'avais d'autres facteurs dans ma vie personnelle qui ont fait que je n'ai plus réussi à assumer mon numéro en plein milieu."

    hide peacock_neutre with dissolve
    hide peacock_nosmile with dissolve
    $ current_textbox = "gatsby"

    show gatsby_neutre at gat_right with dissolve
    gatsby "Mais au final, ça s'est bien fini et le public était très compréhensif..."
    gatsby "Et on se soutient suffisamment dans la troupe pour savoir exprimer nos besoins et nos difficultés."
    $ current_textbox = "peacock"

    hide delaunay_shy with dissolve
    show peacock_laugh at pea_left with dissolve
    peacock "Et se rassurer."

    stop music fadeout 0.1
    $ current_textbox = "mother"

    hide gatsby_neutre with dissolve
    hide peacock_laugh with dissolve
    staff "Ok les filles ! Showtime dans dix minutes !"
    $ current_textbox = "gatsby"

    show joy at joy_center
    play vfxC VFXJoy
    show gatsby_laugh at gat_center with dissolve
    gatsby "Allez ! On doit mettre les bouchées doubles si on veut être à l'heure, girlies ! Chop-chop !"
    hide joy

    stop ambiance fadeout 1.0
    call gat_5 from _call_gat_5 

#GAT.4.2
#-1
label gat_4_2:
    $ quick_menu = True
    $ indice_gat -= 1
    
    hide gatsby_nosmile
    show gatsby_neutre at gat_center with fade
    $ current_textbox = "anthrax"

    anthrax "Je te trouve courageux.e... Tout ce que tu réussis à accomplir sans que ça ait vraiment l'air de t'affecter."
    $ current_textbox = "gatsby"

    show gatsby_irritated at gat_center
    hide gatsby_neutre
    gatsby "Ce n'est pas du courage ça. Ça s'appelle juste vivre... Tu dis ça parce que tu n'es pas dans mes baskets."
    $ current_textbox = "anthrax"

    anthrax "Pourquoi tu dis ça ? Ce n'est pas comme si j'essayais pas ou que j'étais complètement ignorant.e."
    $ current_textbox = "gatsby"

    show gatsby_pensive at gat_center
    hide gatsby_irritated
    gatsby "Non ! Pas dans ce sens-là ! Dans le sens où on a tous.te.s nos limites de compréhension. "
    show gatsby_nosmile at gat_center
    hide gatsby_pensive
    gatsby "Tu n'es pas dans ma tête, ni dans mon corps. Alors la définition de courage est celle qui te vient en premier."
    $ current_textbox = "anthrax"


    $ quick_menu = False
    show gatsby_nosmile at gat_right with dissolve
   
    menu:
        gatsby "Je déteste ce mot, pour me définir en tout cas."
        "Je ne pensais pas que tu le prendrais mal.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ce n'est pas comme si je t'avais insulté.e...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Pourquoi donc? Ce n'est pas péjoratif.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True


    $ current_textbox = "gatsby"

    show gatsby_irritated at gat_right
    hide gatsby_nosmile
    gatsby "Non, en effet. Mais ça sous-entend un peu que mon existence est une corvée. "
    show angry at angry_right
    play vfxR VFXAnger
    gatsby "Ce n'est pas le cas du tout. En fait, j'ai l'impression d'être pris.e en pitié, et je ne supporte pas ça."
    hide angry
    $ current_textbox = "anthrax"

    show gatsby_nosmile at gat_right
    hide gatsby_irritated
    anthrax "Pardon, ce n'est pas ce que je souhaitais dire."
    $ current_textbox = "gatsby"

    show gatsby_neutre at gat_right
    hide gatsby_nosmile
    gatsby "Je sais. Et j'ai aussi été maladroit.e dans ma réaction. Désolé.e."
    show gatsby_pensive at gat_right
    hide gatsby_neutre
    gatsby "J'ai conscience d'être une personne grosse, noire et non-binaire. Très clairement, je cumule."
    show gatsby_neutre at gat_right
    hide gatsby_pensive
    gatsby "Mais ce n'est pas une raison pour s'apitoyer, au contraire."
    show gatsby_laugh at gat_right
    hide gatsby_neutre
    gatsby "Mon bonheur, c'est ma plus belle arme de résistance face à une société peu accueillante. "
    gatsby "Et c'est quelque chose que je ne compte pas lui abandonner de sitôt."
    $ current_textbox = "anthrax"

    $ current_textbox = "gatsby"


    $ quick_menu = False
    show gatsby_neutre at gat_right
    hide gatsby_laugh
   
    menu:

        gatsby "J'ai trop travaillé pour arriver là où j'en suis aujourd'hui. De l'effort, de la résilience, de la joie, mais pas du courage."
        "Je n'aurais pas du résumer avec ce terme alors...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Je saisis la nuance, je pense. C'était trop... réducteur.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'était un raccourci trop simple, si je comprends bien.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass




    $ quick_menu = True

    show gatsby_laugh at gat_right
    hide gatsby_neutre
    gatsby "Je n'aurais pas dit mieux !"
    $ current_textbox = "peacock"

    show peacock_sassy at pea_left with dissolve
    peacock "Mais t'aurais pu lui répondre plus gentiment. Maintenant [player_name] a l'air tout.e embarrassé.e."
    $ current_textbox = "delaunay"

    hide gatsby_laugh with dissolve
    show delaunay_nosmile at del_right with dissolve
    delaunay "C'était peut-être maladroit, mais ça ne partait pas d'un mauvais fond. Tu es encore parti.e au quart de tour By-By."
    $ current_textbox = "gatsby"

    hide peacock_sassy with dissolve
    hide delaunay_nosmile with dissolve
    show gatsby_pensive at gat_center with dissolve
    gatsby "C'est vrai, my bad. Je ferai plus gaffe."
    $ current_textbox = "anthrax"

    anthrax "Ce n'est pas grave, ça m'a plus surpris.e qu'autre chose. Mais au final, ça m'a donné plus de perspective, et j'apprécie l'honnêteté."

    stop music fadeout 0.1
    $ current_textbox = "mother"

    hide gatsby_pensive with dissolve

    staff "Ok les filles ! Showtime dans dix minutes !"
    $ current_textbox = "gatsby"

    show joy at joy_center
    play vfxC VFXJoy
    show gatsby_laugh at gat_center with dissolve
    gatsby "Allez ! On doit mettre les bouchées doubles si on veut être à l'heure girlies ! Chop-chop !"
    hide joy
    
    stop ambiance fadeout 2.0
    call gat_5 from _call_gat_5_1 

   
#GAT.4.3
#+0
label gat_4_3:
    $ quick_menu = True

    hide gatsby_nosmile
    show gatsby_neutre at gat_center with fade
    $ current_textbox = "anthrax"

    anthrax "J'étais persuadé.e qu'avec tout ce que tu m'as mentionné avant, tu ne toucherais plus jamais aux arts acrobatiques."
    $ current_textbox = "gatsby"

    show gatsby_pensive at gat_center
    hide gatsby_neutre
    gatsby "Eh bien... En soi, je comprends que tu puisses penser cela. Moi aussi j'étais persuadé.e que je ne reprendrais pas."
    gatsby "Mais petit à petit, l'envie de m'y remettre a prit le pas sur mes réticences."
    show gatsby_neutre at gat_center
    hide gatsby_pensive
    gatsby "Et au final, j'ai réalisé que ce n'était pas contre les soies aériennes que j'étais fâché.e..."
    gatsby "Mais tout ce qu'elles avaient représenté de toxique dans mon ancien environnement de travail."
    show gatsby_nosmile at gat_center
    hide gatsby_neutre
    gatsby "C'était plus facile d'amalgamer quelque chose que j'adore avec les horreurs que l'on m'a fait subir dans cette industrie..."
    
    $ current_textbox = "anthrax"


    $ quick_menu = False
    show gatsby_nosmile at gat_right with dissolve
   
    menu:
        gatsby "Plutôt que de déconstruire et dissocier des années d'abus."
        "Personne ne peux te blâmer, de ce que tu m'as raconté.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est compréhensible, tu te protégeais...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "J'en reviens pas que ces salauds continuent de bosser !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "gatsby"

    show gatsby_pensive at gat_right
    hide gatsby_nosmile
    gatsby "Bah... Ce n'était pas juste la pression de bien performer au spectacle. "
    show gatsby_irritated at gat_right
    hide gatsby_pensive
    gatsby "C'était de la pure misogynie, un racisme ambiant, des standards de beauté inatteignables, une absence de contrôle sur ma manière de penser..."
    show sadness at sadness_right
    play vfxR VFXSadness
    gatsby "J'étais vraiment conditionné.e."
    hide sadness
    show gatsby_irritated at gat_right
    hide gatsby_pensive
    gatsby "Après, c'est aussi surtout parce que je suis tombé.e sur une troupe particulièrement toxique."
    show gatsby_neutre at gat_right
    hide gatsby_irritated
    gatsby "J'ai de nombreux.euses ami.e.s qui l'ont quittée et qui travaillent maintenant dans un climat plus sain, avec de l'entraide et de l'empathie. J'en ai d'excellents échos."
    show gatsby_laugh at gat_right
    hide gatsby_neutre
    gatsby "Et de toute manière, j'ai entendu dire que l'entreprise pour laquelle on bossait a fait faillite."
    show gatsby_neutre at gat_right
    hide gatsby_laugh
    gatsby "Donc j'ai vraiment l'esprit en paix à présent."
    $ current_textbox = "delaunay"

    show delaunay_nosmile at del_left with dissolve
    delaunay "Je me demande surtout comment tu as fait pour ne pas partir avant..."
    $ current_textbox = "gatsby"

    show gatsby_irritated at gat_right
    hide gatsby_neutre
    gatsby "Pour les mêmes raisons que toi. J'avais mes circonstances, je ne questionne pas les tiennes pour autant..."
    $ current_textbox = "delaunay"

    
    $ quick_menu = False
    hide gatsby_irritated
    hide delaunay_nosmile with dissolve
    show delaunay_shy at del_right with dissolve
   
    menu:
        delaunay "Touché."
        "Calmez-vous... Ça ne sert à rien de s'énerver.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Aïe, aïe, aïe !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Eh beh, c'est tendu dans la salle. ~":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass

    hide delaunay_neutre with dissolve
    show peacock_sassy at pea_left with dissolve
    $ quick_menu = True
    $ current_textbox = "peacock"
    peacock "Stop vous deux. C'est pas simple de briser un pattern malsain auquel on est habitué.e.s."
    peacock "Vous êtes le plus à même de le comprendre ici. L'un.e comme l'autre."
    $ current_textbox = "gatsby"

    show gatsby_irritated at gat_right with dissolve
    gatsby "Tu dis ça, mais ton industrie n'est pas non plus très haute placée sur l'échelle des bisounours..."
    $ current_textbox = "peacock"

    show peacock_nosmile at pea_left
    hide peacock_sassy
    peacock "C'est vrai, c'est surtout de la chance. Et du bouche à oreille. J'ai l'avantage de bosser beaucoup avec des petits contrats. "
    peacock "Ça aide à ne pas rester enfermé.e avec la même équipe et de pouvoir tourner."
    show gatsby_neutre at gat_right
    hide gatsby_irritated
    show peacock_neutre at pea_left
    hide peacock_nosmile
    peacock "Ou alors de trouver justement les personnes avec qui j'apprécie bosser et pouvoir les recontacter."
    $ current_textbox = "gatsby"

    hide peacock_neutre with dissolve
    show delaunay_flirty at del_left with dissolve
    delaunay "Roh ~ C'est pour ça que tu es restée ici ? Je suis touché."

    show gatsby_laugh at gat_right
    hide gatsby_neutre
    gatsby "Enfin bref ! Morale de l'histoire : bien s'entourer, et faire du drag. Parce qu'au moins, on s'entoure de gens qui nous comprennent."

    stop music fadeout 0.1
    $ current_textbox = "mother"

    hide delaunay_neutre with dissolve
    hide gatsby_neutre with dissolve
    staff "Ok les filles ! Showtime dans dix minutes !"
    $ current_textbox = "gatsby"

    show joy at joy_center
    play vfxC VFXJoy
    show gatsby_laugh at gat_center with dissolve
    gatsby "Allez ! On doit mettre les bouchées doubles si on veut être à l'heure, girlies ! Chop-chop !"
    hide joy

    stop ambiance fadeout 2.0
    call gat_5 from _call_gat_5_2 


# AJOUTER LA TRANSITION RIDEAU DE SES MORTS LA J'EN PEUX PLUS LIBEREZ NOUS
#GAT.5
label gat_5:
    hide gatsby_neutre with dissolve
    show curtain_close with dissolve
    play vfxC SFXCurtainClose
    pause 1.5
    hide loges
    show curtain_open with dissolve
    play vfxC SFXCurtainClose

    scene black with dissolve
    play music ShowGatsby noloop

    $ current_textbox = "description"

    text "Le band commença le morceau suivant alors que la scène était encore vide de toute activité..."
    text "Si bien que les spectateur.ice.s en venaient à se demander si quelque chose clochait."
    text "Un projecteur se braqua sur deux longues soies qui venaient d'être lâchées. "
    show auditorium
    text "Tout en douceur, accompagné.e par les accords du piano, Gatsby avançait sur les planches."
    show gatsby_pensive at gat_center with dissolve
    text "Après une courte parade, iel retira sa redingote et se hissa le long des deux voilages à la force de ses bras et de ses jambes..."
    text " Sécurisant son ascension en se créant un harnais en quelques tours de draps."
    hide gatsby_pensive with dissolve
    show gatsby_neutre at gat_left with dissolve
    text "Surplombant l'atrium de quelques mètres de hauteurs, iel démarra son numéro de soies aériennes avec grâce."
    text "Tourbillonnant, usant de sa flexibilité pour réaliser des postures impressionnantes, Gatsby captivait le regard."
    text "Et le souffle retenu de chaque membre de l'audience faisait planer une tension éthérée et palpable."
    hide gatsby_neutre with dissolve
    show gatsby_nosmile at gat_right with dissolve
    text "Les deux nœuds au bout de chaque cheville et plante le.a tenait suspendu.e en grand écart, qui lui demandaient un effort d'équilibre surhumain."
    text "Soudainement, iel tomba."
    hide gatsby_nosmile
    text "Virevoltant, sa chute se stoppa si près du sol qu'un cri de surprise fusa depuis le comptoir du bar."
    show gatsby_laugh at gat_center with dissolve
    text "Mais le risque était calculé, et son sourire fier tandis qu'iel se redressait en disait long sur le contrôle que Gatsby avait sur la situation."
    show flirt at flirt_center
    text "Quelques minutes plus tard et notre acrobate revinait sur la terre ferme, saluant avec humilité son public ému."
    hide flirt

    stop music fadeout 2.0

    $ persistent.bg_parallax = False
    hide gatsby_neutre with dissolve
    show curtain_close with dissolve
    play vfxC SFXCurtainClose
    pause 1.5
    hide auditorium
    show curtain_open with dissolve
    play vfxC SFXCurtainOpen

call gat_6 from _call_gat_6_1


#GAT.6
label gat_6:
    $ persistent.bg_parallax = True
    show loges
    show gatsby_neutre at gat_center with dissolve

    $ current_textbox = "gatsby"

    show gatsby_laugh at gat_center

    gatsby "Franchement, je ne me laisserais jamais de cette réaction!"
    gatsby "Tu as vu leur tête quand je suis tombé.e?"

    hide gatsby_neutre
 
    $ quick_menu = False

    scene background_cg
    show CG_gatsby at CG_center with fade

    $ current_textbox = "description"

    pause 1.0
    "Nouvelle illustration débloquée"
    hide CG_gatsby with dissolve
    hide background_cg with fade
    $ persistent.gatsby_unlocked = True  


    $ quick_menu = False
    $ current_textbox = "gatsby"
    show gatsby_laugh at gat_right with dissolve
   
    menu:
        gatsby "Mémorable! J'ai cru que le premier rang allait faire un arrêt cardiaque!"

        "Pas que le premier rang! Un peu plus, et moi aussi !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "La grâce et la force que ça demande, sans te faire broncher !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Le public était complètement hypnotisé !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass

    $ quick_menu = True

    show gatsby_pensive at gat_right
    hide gatsby_laugh
    show flirt at flirt_right
    play vfxR VFXFlirt
    gatsby "Roh, arrête! Tu vas me faire rougir, va!"
    hide flirt
    show gatsby_laugh at gat_right
    hide gatsby_pensive
    gatsby "Tu sais que ça marche trop bien avec moi en plus!"
    gatsby "Plus qu'à me montrer maintenant ce dont TOI tu es capable!"

    $ current_textbox = "anthrax"

    show gatsby_neutre at gat_right
    hide gatsby_laugh
    anthrax "C'est en cours! Patience, patience! Moi aussi, j'ai envie de te garder la surprise~"

label indice_gat:
    if indice_gat >= 0:
        jump gat_6_good
    else:
        jump gat_6_bad
    
    show gatsby_neutre at gat_right
    with fade
    gatsby "Ça te tente que l'on sorte un peu après? Se promener en ville, grignoter un truc, quelque chose du style..."
 
    menu: 
        text "Accepter le date ?"
        "Oui":
            call gat_6_good from _call_gat_6_good 
        "Non":
            call gat_6_bad from _call_gat_6_bad

#GAT.6.GOOD
label gat_6_good:
    $ quick_menu = False
    $ current_textbox = "gatsby"
    
    play ambiance AmbLoges volume 0.4
    with fade
    gatsby "Ça te tente que l'on sorte un peu après? Se promener en ville, grignoter un truc, quelque chose du style..."
    
    $ current_textbox = "description"
    menu: 
        text "Accepter le date ?"
        "Oui":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Non":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call gat_6_good_bad from _call_gat_6_good_bad 


    $ quick_menu = True
    show gatsby_laugh at gat_center with dissolve
    show loges with dissolve
    hide flirt

    $ current_textbox = "gatsby"
    show flirt at flirt_right
    play vfxC VFXFlirt
    gatsby "Nickel! Je fais vite! Attends-moi devant l'entrée quand tu aura aussi fini!"
    hide flirt

    
    show curtain_close with dissolve
    play vfxC SFXCurtainClose
    hide gatsby_neutre with dissolve
    hide gatsby_laugh with dissolve
    hide bar
    scene black
    hide loges with dissolve
    scene black
    pause 1.5
    show curtain_open with dissolve
    play vfxC SFXCurtainOpen
    with fade
 
    scene black with dissolve
    play music BadEnd volume 0.8 noloop

    $ current_textbox = "description"
    text "Le temps que Gatsby et les autres artistes terminent de se démaquiller et de se rhabiller en civil, je passai le balai sur les planches de la scène..."
    text "Laissant mon esprit vagabonder au jour où moi-même je les foulerais."
    text "À l'extérieur, quelques clients étaient restés sur le pavé pour continuer leurs discussions et attendre la sortie de la royauté de L'Androgame."
 
    show devanture
    show aimee_laugh at gat_center with dissolve

    
    $ current_textbox = "gatsby"
    show joy at joy_center
    play vfxC VFXJoy
    aimee "Promis, j'ai fais aussi vite que possible! Quelle horreur de retirer la colle après avoir sué toute la soirée!"
    hide joy

    $ current_textbox = "anthrax"
    anthrax "Merci pour l'invitation... Qu'est-ce que les autres ont prévu de faire?"

    $ current_textbox = "gatsby"
    show aimee_neutre at gat_center
    hide aimee_laugh
    aimee "Je pense qu'ils vont trinquer un coup et puis rentrer... C'était une très bonne soirée, mais diablement épuisante!"
    show aimee_laugh at gat_center
    hide aimee_neutre
    aimee "Mais j'ai encore la niaque pour un date avec toi! Si tu te poses la question."
    show aimee_pensive at gat_center
    hide aimee_laugh
    aimee "Enfin, si tu es toujours ok..."


    $ current_textbox = "anthrax"
    anthrax "Je n'attendais que ça Aimé.e!"
    anthrax "Alors dis-moi! Où est-ce que tu m'emmènes ce soir?"

    $ current_textbox = "gatsby"
    show flirt at flirt_center
    play vfxC VFXFlirt
    show aimee_laugh at gat_center
    hide aimee_pensive
    aimee "Aha! Mystère, mystère... Mais te connaissant, tu devrais bien kiffer!"


    hide flirt
    call final_gatsby from _call_final_gatsby 

#GAT.6.BAD
#COPYPASTE DE LA RUN DEL A MODIFIER
label gat_6_bad:
    $ quick_menu = True
    
    hide auditorium
    show loges
    show gatsby_neutre at gat_right with dissolve
    
    $ current_textbox = "gatsby"
    $ quick_menu = False

    menu:
        gatsby "On va aller boire un verre avec les autres une fois que les derniers clients auront quitté la salle. Tu te joins à nous ?"
    
        "Oui, bien sûr! Je termine ça et j'arrive!":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Si vous insistez!":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Proposé si gentiment, comment refuser?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass

    $ quick_menu = True
    
    jump gat_6_good_bad
    

label gat_6_good_bad:
    #Transition Rideau
    hide gatsby_neutre with dissolve
    show curtain_close with dissolve
    play vfxC SFXCurtainClose
    pause 1.5
    hide bar
    hide loges
    scene black
    show curtain_open with dissolve
    play vfxC SFXCurtainOpen
    with fade

    show bar with fade
    play music BadEnd volume 0.8 noloop
   
    $ current_textbox = "description"
  
    text "Tous.te.s étaient réuni.e.s face au comptoir, se faisant servir par notre merveilleux \"Dobarman\"."
    show imani_neutre at pea_left with dissolve
    text "Imani avait entre ses doigts un mocktail de sa création..."
    show leandre_neutre at del_right with dissolve
    text "Léandre retrouvait peu à peu sa timidité, laissant Delaunay s'effacer."
    show aimee_neutre at gat_center with dissolve
    text "Partageant son verre avec Aimé.e pour qu'iel goûte, riant aux éclats en détaillant quelques anecdotes de leurs expériences."
    text "Le tout appuyé.e par l'approbation et les précisions de Mother."
    
    hide imani_neutre
    hide leandre_neutre
    hide aimee_neutre
    show aimee_laugh at gat_right with dissolve

    $ current_textbox = "gatsby"
    aimee "Nan mais je te jure ! La manière dont sa perruque a volé au milieu de la pièce !"

    $ current_textbox = "delaunay"
    show leandre_laugh at del_left with dissolve
    leandre "Et surtout sa tête, en s'en rendant compte... !"

    $ current_textbox = "peacock"
    hide aimee_laugh

    show imani_laugh at pea_right with dissolve
    imani "J'aurais rêvé être là cette soirée, et non derrière les machines !"

    $ current_textbox = "mother"
    hide leandre_laugh
    show mother_laugh at mother_left with dissolve

    show joy at joy_left
    play vfxL VFXJoy
    mother "Je suis sûre que je peux te retrouver une vidéo d'excellente qualité, vu comment elle a tourné sur les plateformes."
    hide joy
    
    hide imani_laugh

    hide mother_laugh

    show imani_neutre at pea_left with dissolve
    show leandre_neutre at del_right with dissolve
    show aimee_neutre at gat_center with dissolve


    $ current_textbox = "description"

    text "Les écoutant avec une certaine envie, ayant hâte de pouvoir raconter à mon tour mes aventures."
    text "Je les observais un à une, ancrant cette image dans ma mémoire, essayant d'y graver le moindre détail."
    hide imani_neutre with dissolve
    hide leandre_neutre with dissolve
    show aimee_laugh at gat_center
    text "Je m'en voulais peut-être un peu de ne pas avoir demandé à Aimé.e d'être sorti.e avec moi ce soir."
    text "Mais quelque chose me dit que c'était peut-être un peu trop tôt..."
    show flirt at flirt_center
    play vfxC VFXFlirt
    text "Et j'aurais loupé cet instant précieux, sachant pertinemment que je passerais le reste de la soirée bien entouré.e !"
    hide flirt

    call final_gatsby from _call_final_gatsby_1 

    

label final_gatsby:
    $ current_textbox = "description"
    hide aimee_neutre with dissolve
    hide aimee_laugh with dissolve
    hide devanture with fade
    hide bar with fade
    
    $ quick_menu = False
    stop music fadeout 1.0
    pause 1.0
    scene black with fade

    $ renpy.full_restart()

