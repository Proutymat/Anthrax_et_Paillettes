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
                renpy.sound.queue(renpy.random.choice(type_silent))
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

image CG_peacock = "images/CGs/peacock.jpg"

image background_cg = "images/Backgrounds/background_cg.png"

# Liste des sfx
define type_sounds = ['audio/SFX/TextMix-001.ogg','audio/SFX/TextMix-002.ogg','audio/SFX/TextMix-003.ogg','audio/SFX/TextMix-004.ogg','audio/SFX/TextMix-005.ogg','audio/SFX/TextMix-006.ogg','audio/SFX/TextMix-007.ogg','audio/SFX/TextMix-008.ogg','audio/SFX/TextMix-009.ogg','audio/SFX/TextMix-010.ogg']
define A_type_sounds = ['audio/SFX/AP_TA-001.ogg','audio/SFX/AP_TA-002.ogg','audio/SFX/AP_TA-003.ogg','audio/SFX/AP_TA-004.ogg']
define D_type_sounds = ['audio/SFX/AP_T1-001.ogg','audio/SFX/AP_T1-002.ogg','audio/SFX/AP_T1-003.ogg','audio/SFX/AP_T1-004.ogg']
define M_type_sounds = ['audio/SFX/AP_T2-001.ogg','audio/SFX/AP_T2-002.ogg','audio/SFX/AP_T2-003.ogg','audio/SFX/AP_T2-004.ogg']
define G_type_sounds = ['audio/SFX/AP_T3-001.ogg','audio/SFX/AP_T3-002.ogg','audio/SFX/AP_T3-003.ogg','audio/SFX/AP_T3-004.ogg'] 
define P_type_sounds = ['audio/SFX/AP_T4-001.ogg','audio/SFX/AP_T4-002.ogg','audio/SFX/AP_T4-003.ogg','audio/SFX/AP_T4-004.ogg']
define type_silent = ['<silence 1.0>']

define ui_hover = ['audio/SFX/AP_UI_Hover-001.ogg','audio/SFX/AP_UI_Hover-002.ogg','audio/SFX/AP_UI_Hover-003.ogg','audio/SFX/AP_UI_Hover-004.ogg','audio/SFX/AP_UI_Hover-005.ogg','audio/SFX/AP_UI_Hover-006.ogg']
define ui_click = ['audio/SFX/AP_UI_Click-001.ogg','audio/SFX/AP_UI_Click-002.ogg','audio/SFX/AP_UI_Click-003.ogg','audio/SFX/AP_UI_Click-004.ogg','audio/SFX/AP_UI_Click-005.ogg','audio/SFX/AP_UI_Click-006.ogg']
define ui_back = ['audio/SFX/AP_UI_Back_V4-001.ogg','audio/SFX/AP_UI_Back_V4-002.ogg','audio/SFX/AP_UI_Back_V4-003.ogg','audio/SFX/AP_UI_Back_V4-004.ogg','audio/SFX/AP_UI_Back_V4-005.ogg','audio/SFX/AP_UI_Back_V4-006.ogg']
define ui_choice_click = ['audio/SFX/AP_UI_Click-001.ogg','audio/SFX/AP_UI_Click-002.ogg','audio/SFX/AP_UI_Click-003.ogg','audio/SFX/AP_UI_Click-004.ogg','audio/SFX/AP_UI_Click-005.ogg','audio/SFX/AP_UI_Click-006.ogg']

# Liste des ambiances
define audio.AmbAndrogameDay = "audio/Amb/Amb_CabaretDay_V3.ogg"
define audio.AmbLoges = "audio/Amb/Amb_LogesDay_V4.ogg"
define audio.AmbRue = "audio/Amb/Amb_Rue_V2.ogg"
define audio.AmbLogesNight = "audio/Amb/Amb_LogesNight_V3.ogg"
define audio.AmbDelShow = "audio/Amb/AP_Amb_ShowDel_V1.ogg"
define audio.BarDay = "audio/Amb/Amb_BarDay_V4.ogg"

# Liste des réactions de foule
define audio.CrowdDel1 = "audio/Amb/AP_Crowd_ShowDelSt1.ogg"
define audio.CrowdDel2 = "audio/Amb/AP_Crowd_ShowDelSt2.ogg"
define audio.CrowdDel3 = "audio/Amb/AP_Crowd_ShowDelSt3.ogg"
define audio.CrowdDel4 = "audio/Amb/AP_Crowd_ShowDelSt4.ogg"

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
define audio.BackstageDrumLoop = "audio/Music/ON_BackStageLoop_V1.ogg"
define audio.BarMusic = "audio/Music/AP_BarFull.ogg"
define audio.BarMusicPartB = "audio/Music/AP_BarPartieB.ogg"
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

label peacock_start:
$ persistent.bg_parallax = True
$ quick_menu = True
default indice_pea = 0
scene black with fade
show loges
show imani_neutre at pea_center with dissolve
stop music fadeout 0.1
show imani_laugh at pea_center with dissolve
hide imani_neutre


play ambiance AmbLoges fadein 0.5


#PEA.1
$ current_textbox = "peacock"

imani "Je suis flattée ~"

show imani_neutre at pea_center
hide imani_laugh
imani "Alors comme ça je t'ai fait une telle impression ?"
$ current_textbox = "anthrax"

anthrax "Il semblerait, j'adore ta vibe. Tu as un certain talent pour mettre les gens à l'aise."
$ current_textbox = "peacock"

show joy at joy_center
play vfxC VFXJoy
imani "Ah ça ! On me le dit souvent !"
hide joy
imani "Même si parfois j'ai l'impression de faire trop vieux jeu."
$ current_textbox = "anthrax"

anthrax "Vieux jeu ? J'aimerais bien croiser la personne qui a dit ça."
$ current_textbox = "peacock"

imani "Hm... Je pense que je peux définitivement blâmer mon reflet dans le miroir. "
imani "Pas que ce visage ne soit pas sublime, mais c'est un peu mon meilleur ennemi."
$ current_textbox = "anthrax"

anthrax "Comme dirait RuPaul, il ne faut pas écouter notre 'inner saboteur'."
$ current_textbox = "peacock"

show imani_sassy at pea_center
hide imani_neutre
imani "Word."
show imani_neutre at pea_center
hide imani_sassy

$ quick_menu = False
show imani_neutre at pea_right
   
menu:
    imani "Ça te dit de t'installer quelque part de plus cosy pour continuer à discuter ?"
    "Je te suis !":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "J'adorerais !":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Ça, je ne dis pas non !":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
          



$ quick_menu = True

#TRANSITION VERS LE BAR
#PEA.2
stop ambiance fadeout 2.0
play music BarMusicPartB volume 0.5

$ current_textbox = "description"

hide loges
hide imani_neutre with fade
scene black

text "Nous sommes arrivé.e.s dans l'auditorium et nous sommes approché.e.s du comptoir derrière lequel brillaient un mur de bouteilles aux couleurs uniques."
text "Nous avions depuis le bar une vue imprenable sur la scène, légèrement en contrebas."
text "Les tablées y étaient déjà dressées et se regroupaient autour du big band et de l'estrade secondaire au centre de la pièce."
text "L'immense lustre duquel pendaient des larmes de verre reflétait les spots de lumière à la manière d'une boule à facettes sur le papier peint texturé."
text "Imani s'assît sur l'une des chaises hautes de bois verni et commanda un Virgin Moscow Mule au barman."



$ quick_menu = False
show bar with fade
show imani_neutre at pea_right 
   
menu:
    imani "Est-ce que tu sais déjà quoi commander ?"
    "Un Pornstar Martini.":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Un Negroni Sbagliato, avec une pointe de prosecco.":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Un Expresso Martini !":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass


$ quick_menu = True

$ current_textbox = "peacock"

play ambiance BarDay fadein 0.5

imani "Tu verras, notre barman est un vrai génie en la matière. Il peut te concocter le meilleur mocktail de ta vie sans que tu t'y attendes."
show imani_laugh at pea_right
hide imani_neutre
imani "Et des cocktails aussi, bien sûr !"
show imani_neutre at pea_right
hide imani_laugh

$ current_textbox = "anthrax"
anthrax "Tu ne bois pas d’alcool ?"

$ current_textbox = "peacock"
show joy at joy_right
play vfxR VFXJoy
imani "Non ! Mais j’adore le concept. Mêler jus, sirops, eau gazeuse, et créer quelque chose d’un peu plus fancy qu’une limonade, je prends !"
hide joy

$ current_textbox = "anthrax"
show imani_laugh at pea_right
hide imani_neutre
anthrax "Je me sens bête de prendre un Martini du coup..."
show imani_neutre at pea_right
hide imani_laugh


$ current_textbox = "peacock"

imani "Oh non ! Ne t’en fais pas, tant que tu es raisonnable dans ta consommation, tout va bien !"
$ current_textbox = "description"

show overlay
text "Imani sourit et prit sa boisson entre ses doigts vernis, la portant à ses lèvres et sirotant en me fixant, comme pour me jauger."
hide overlay
$ current_textbox = "peacock"


$ current_textbox = "anthrax"

$ quick_menu = False
show imani_neutre at pea_right
   
menu:
    imani "Alors, dis-moi. C’est quoi ton drag ?"
    "Mon drag ?":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "Oh ? Comme ça, maintenant ?":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "M-Moi? Directement ? Sans préli' ?! ":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass


$ quick_menu = True


$ current_textbox = "peacock"
show imani_laugh at pea_right
hide imani_neutre
imani "Oui ! C’est pour ça que tu es là après tout !"
show imani_neutre at pea_right
hide imani_laugh
$ current_textbox = "anthrax"

anthrax "Oh. Eh bien... Je dirais que c’est plus du drag quing. Je ne me fixe pas à un genre précis, parfois pas même l’espèce humaine pour tout dire..."
anthrax "J’ai commencé dans le confort de mon appart, sur les réseaux sociaux. Je n’ai jamais mis les pieds dans une troupe. Ou même un cabaret."
anthrax "Mais le burlesque, c’est quelque chose qui m’a toujours attiré.e. C’est culturel, niche, voluptueux... À la fois décent et indécent."
anthrax "Ça me parle."

show joy at joy_right
play vfxR VFXJoy
imani "À moi aussi tu me parles ! Je comprends mieux ce que Mother a vu chez toi !"
hide joy
$ current_textbox = "anthrax"

anthrax "Ah bah merci..."

show imani_laugh at pea_right
hide imani_neutre
imani "Non, non ! C’était un compliment. Je sais que j’ai beaucoup de shade à revendre, mais là, c’était sincère."
show imani_neutre at pea_right
hide imani_laugh

#Choix PEA.2
label choix_pea2:
    $ quick_menu = False
    
    show imani_neutre at pea_right

    menu: 
        "Tu m'a l'air la plus engagée au sein de la troupe...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_2_1 from _call_pea_2_1 
        "Est-ce que tu peux m’en dire davantage sur ce que tu fais ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_2_2 from _call_pea_2_2 
        "Et toi ? Qu’est-ce qui t’as lancée dans le drag ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_2_3 from _call_pea_2_3 
          

#PEA.2.1

label pea_2_1:
    $ indice_pea += 1
    $ quick_menu = True
    
    show imani_neutre at pea_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Tu es la personne qui m'a l'air la plus engagée au sein de la troupe."
    $ current_textbox = "peacock"
    show imani_laugh at pea_center
    hide imani_neutre
    imani "Oh ! Ne dis pas ça aux autres, les oreilles vont chauffer !"
    show imani_neutre at pea_center
    hide imani_laugh
    imani "C’est vrai que Léandre a l’air plus discret mais n’en est pas moins activiste."
    imani "Et Aimée... Eh bien, je crois que tu as remarqué qu’iel avait plutôt grande gueule..."
    show joy at joy_center
    play vfxC VFXJoy
    imani "Même l’Androgame est un lieu très central dans la sphère queer de la ville. Toutes les Paillettes vont défiler aux prides et scandent des slogans."
    hide joy

    $ quick_menu = False
    show imani_neutre at pea_right with dissolve
   
    menu:
        imani "Et c’est un peu devenu une tradition même que l’on fasse un discours sur le char, après la minute de silence."

        "C'est vrai que je vous y avais vu.e.s quelques fois. ":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Je n'avais pas fait le rapprochement...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Oh! J'avais complêtement oublié !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True


    $ current_textbox = "peacock"
    show imani_nosmile at pea_right
    hide imani_neutre
    imani "Même en dehors du drag, je suis très politisée. Contre le racisme, l’islamophobie, et le trafic d’enfants avec l’adoption internationale."
    $ current_textbox = "anthrax"

    anthrax "L’adoption internationale ?"
    $ current_textbox = "peacock"

    imani "Oui, c’est assez méconnu. Mais c’est la dure réalité d’une grande partie des enfants adoptés de l’étranger."
    imani "Le déracinement, la méconnaissance de ses origines et la quête de soi qui vont avec."
    show imani_neutre at pea_right
    hide imani_nosmile
    $ current_textbox = "anthrax"

    anthrax "Je l’ignorais..."
    $ current_textbox = "peacock"

    show imani_laugh at pea_right
    hide imani_neutre
    imani "Ce n’est pas la première chose à laquelle on pense en me voyant après tout."



    $ quick_menu = False
    show imani_neutre at pea_right
   
    menu:
        imani "J’aurais très bien pu être un petit-fils d’immigrés, mais non ! Adopté par des parents français !"
        "Et comment est-ce que tu le vis? Si ce n'est pas indiscret...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ça n'a pas dû être simple... Ça s'est bien passé ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "On ne se l'imagine pas du tout en te voyant. Tu le vis bien ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True


    $ current_textbox = "peacock"
    show imani_neutre at pea_right
    hide imani_laugh
    imani "Hm... Plutôt bien. J’aime beaucoup ma famille adoptive, même si ça a posé de nombreux problèmes avec le temps."
    show joy at joy_right
    play vfxR VFXJoy
    imani "La discussion a toujours été très ouverte avec mes parents sur ce sujet-là, et ils ne sont pas responsables des travers de procédures qu’il y a eu."
    hide joy
    imani "C’est plutôt une incompréhension de leur part parfois, quand j’essaye de me rapprocher de mes origines."
    show imani_nosmile at pea_right
    hide imani_neutre
    imani "Je leur en ai un peu voulu lorsque j’étais adolescent, mais je sais maintenant que c’est parce que ça atteint simplement leurs limites éducationnelles."
    imani "C’est un peu vexant parfois, mais on fait avec. Et ça ne change rien à l’amour et au soutien qu’ils me donnent. Je m’estime donc très chanceux."
    show imani_laugh at pea_right
    hide imani_nosmile
    imani "Je me sers, pour le coup, beaucoup du drag pour explorer cette facette de ma personne."
    $ current_textbox = "anthrax"


    $ quick_menu = False
    show imani_neutre at pea_right
    hide imani_laugh

    menu:
        imani "Et remédier un peu au white-washing que j’ai intégré en grandissant."

        "C'est un sacré parcours en perspective. Pas trop la pression ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est beau comme message à porter, un peu lourd, non ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Tu as de sacrées épaules pour te lancer là dedans, bravo !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "peacock"

    show imani_laugh at pea_right
    hide imani_neutre
    imani "J'ai énormément la pression, oui ! Haha !"
    show imani_neutre at pea_right
    hide imani_laugh
    imani "Je me sens parfois toujours pas légitime, alors que je suis littéralement maghrébin."
    show imani_sassy at pea_right
    hide imani_neutre
    imani "Sérieusement, c’est quelle logique ?!"
    show imani_neutre at pea_right
    hide imani_sassy

    $ current_textbox = "anthrax"

    anthrax "J’avais tout de même raison quand je disais que tu avais l’air d’être la personne la plus militante..."

    call pea_3 from _call_pea_3_4 

#PEA.2.2

label pea_2_2:
    $ quick_menu = True
    
    show imani_neutre at pea_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Est-ce que tu peux m'en dire davantage sur ce que tu fais ? Mother a piqué ma curiosité, mais je brûle d'avoir plus de détails."
    $ current_textbox = "peacock"


    imani "Eh bien... Comme Mother l'a expliqué. Je me spécialise dans tout ce qui est \"vocal\"..."
    imani "Mais c'est plus de l'ordre de l'humour, de la lecture, du chant..."
    show flirt at flirt_center
    play vfxC VFXFlirt
    imani "Récemment, je m'intéresse plus à comment utiliser davantage mon corps dans mes numéros."
    hide flirt
    imani "Avec de la danse notamment."
    $ current_textbox = "anthrax"

    anthrax "Elle ne l'a pas précisé ça !"
    $ current_textbox = "peacock"

    show imani_laugh at pea_center
    hide imani_neutre
    imani "C'est suffisamment récent pour que tu en aies l'exclusivité."
    show imani_neutre at pea_center
    hide imani_laugh


    $ quick_menu = False
    show imani_neutre at pea_right with dissolve
   
    menu:

        imani "Je prends des cours en dehors du travail. Sauf que comme j'en ai beaucoup, de travail, ça a prit un certain temps avant de devenir décent."
        "Mytho ! Tu es super athlétique !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Tu m'as l'air pourtant... Bien en forme ~":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Je ne te crois pas.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass




    $ quick_menu = True

   
    $ current_textbox = "peacock"
    
    show imani_laugh at pea_right
    hide imani_neutre
    imani "Je suis né avec deux pieds gauches, je te jure !"
    show imani_emo at pea_right
    hide imani_laugh
    imani "C'est pas la faute de mes parents d'avoir essayé..."
    show imani_nosmile at pea_right
    hide imani_emo
    imani "Mais à défaut d'avoir appris à danser, ils m'ont introduit très jeune au monde du spectacle, en m'emmenant voir des comédies musicales, des concerts et des ballets."
    imani "C'est sûrement pour ça que je fais de la régie d'ailleurs..."
    show imani_nautre at pea_right
    hide imani_nosmile
    imani "Au moins, quand les procédures sont protocolaires, je n'ai pas à m'inquiéter de ma maladresse."
    $ current_textbox = "anthrax"

    anthrax "Tu ne m'as pas l'air si maladroit que ça... "
    anthrax "Encore moins si tu commences à inclure de la danse à un acte dans lequel tu chantes ou tu lipsync déjà."
    $ current_textbox = "peacock"

    show imani_laugh at pea_right
    hide imani_neutre
    imani "C'est gentil de dire ça... Tu me flattes."
    show imani_neutre at pea_right
    hide imani_laugh
    $ current_textbox = "anthrax"

    anthrax "Et sinon, c'est un genre de danse en particulier que tu apprends en ce moment ?"
    $ current_textbox = "peacock"

    show joy at joy_right
    play vfxR VFXJoy
    imani "En ce moment ? Eh bien, ce que je commence à intégrer à mon gig, c'est de la danse à éventails... "
    hide joy


    $ quick_menu = False
    show imani_neutre at pea_right
   
    menu:
        imani "Mais ultimement, j'aimerais bien y rajouter quelques éléments de shaabi."

        "Du shaabi ? C'est une danse oriental, non ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Les éventails ? Tu veux dire les éventails à plumes ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ça fait très cabaret en tout cas !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "peacock"
    show imani_laugh at pea_right
    hide imani_neutre
    imani "Eh bien, mon nom de scène est Peacock après tout. Ce serait bête de ne pas l'exploiter un minimum."
    imani "Et pour tout dire, c'est même ce qui a initialement inspiré le nom."
    show imani_emo at pea_right
    hide imani_laugh
    imani "Je n'avais juste pas encore les compétences pour prétendre être à la hauteur de mon titre !"
    show imani_laugh at pea_right
    hide imani_emo
    $ current_textbox = "anthrax"

    anthrax "Il me faudrait le voir pour le croire alors, mais ça ne saurait tarder !"

    call pea_3 from _call_pea_3 

#PEA.2.3
#-1
label pea_2_3:
    $ quick_menu = True
    $ indice_pea -= 1

    show imani_neutre at pea_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Et toi ? Qu'est-ce qui t'as lancée dans le drag ?"
    $ current_textbox = "peacock"

    imani "En fait, je bossais déjà à l'Androgame avant."
    imani "Je faisais partie du crew à la technique et en régie."
    imani "Plus particulièrement, tout ce qui était relatif aux enceintes, micros et tout autres appareils sonores."
    imani "Pour faire simple."
    $ current_textbox = "anthrax"

    anthrax "Ah oui ! Donc tu connais les coulisses du cabaret depuis un moment déjà ! Pas étonnant que tu aies l'air aussi expérimenté."
    $ current_textbox = "peacock"


    $ quick_menu = False
    show imani_neutre at pea_right
    show imani_laugh at pea_right
    hide imani_neutre
   
    menu:
        imani "En tant que technicien, peut-être, mais je suis encore assez débutant en drag. Ça fait seulement deux ans que j'ai officiellement commencé."
        "C'est déjà plus que moi...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ne te sous-estimes pas !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Deux ans ?! C'est énorme !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "peacock"

    show imani_neutre at pea_right
    hide imani_laugh
    imani "C'est pour cela que j'ai dit \"débutant\" et non \"novice\"."
    imani "Enfin bref, c'est Delaunay qui m'a costumé pour la première fois après une soirée arrosée pour fêter la fin d'un show."
    imani "Et j'y ai pris vraiment goût."
    show imani_laugh at pea_right
    hide imani_neutre
    imani "Comme mon contrat se terminait, je suis allé bosser ailleurs en régie, mais j'ai gardé contact avec les filles."
    show imani_neutre at pea_right
    hide imani_laugh
    $ current_textbox = "anthrax"

    anthrax "Et je suppose que tu as continué de ton côté avant de revenir, mais cette fois en intégrant la troupe ?"
    $ current_textbox = "peacock"

    show imani_laugh at pea_right
    hide imani_neutre
    imani "Très bien deviné !"
    show imani_emo at pea_right
    hide imani_laugh
    imani "Au départ, Mother n'était pas très encline, et j'ai mis un moment à faire mes preuves."
    show imani_neutre at pea_right
    hide imani_emo
    imani "Mais du coup, on a bidouillé une sorte de contrat pour que je file un coup de main en technique de temps en temps, tout en peaufinant mon drag."
    show joy at joy_right
    play vfxR VFXJoy
    imani "Et au final, ça s'est plutôt bien goupillé. J'avais une stabilité financière et un espace familier, dans lequel je pouvais progresser."
    hide joy

    $ quick_menu = False
    show imani_neutre at pea_right
   
    menu:
        imani "Puis un jour, j'ai eu le droit à mon premier show, et c'était magique."
        "Ah oui ? Comment c'était ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Raconte-moi !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Tu sais que j'ai besoin de détails maintenant !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "peacock"

    show imani_laugh at pea_right
    hide imani_neutre
    imani " C'était quelque chose !"
    show imani_emo at pea_right
    hide imani_laugh
    imani "J'étais tellement nerveuse que je suis allée vomir deux fois avant de monter sur scène !"
    show imani_laugh at pea_right
    hide imani_emo
    imani "Mais une fois dessus, c'était comme si je m'étais fait posséder par quelqu'un d'autre, Peacock avait complètement prit le contrôle sur ma personne."
    imani "C'était grisant !"
    show imani_neutre at pea_right
    hide imani_laugh
    imani "J'étais tellement habitué à être sur le derrière de la scène, à faire en sorte que tout se déroule bien, que je n'avais jamais envisagé autant aimer être sur le devant."

    anthrax "J'ai hâte que ce soit mon tour !"

    call pea_3 from _call_pea_3_1 


#AJOUTER TRANSITION RIDEAUX + QUELQUES MOIS
#PEA.3
label pea_3:
    
    $ persistent.bg_parallax = False
    hide imani_neutre with dissolve
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
    text "Cela faisait plusieurs minutes que je cherchais Imani, avec qui j'étais supposé.e répéter une partie de mon numéro, que l'on construisait ensemble."
    text "Après avoir fait trois fois le tour du bâtiment, je finis par retourner sur les planches de la scène, pensif.ve."
    text "Et en toute honnêteté, un peu inquiet.e."
    text "En relevant le regard vers le balcon, je le remarquai appuyé.e contre la balustrade, me faisant signe de le rejoindre, un verre de jus à moitié vide à la main avec lequel il jouait."

    play music BalconIntro noloop
    show auditorium with dissolve

    $ current_textbox = "anthrax"

    $ quick_menu = False
    show imani_neutre at pea_right
   
    menu:
        #gatsby ""
        "Hey... Je me demandais où tu étais passé.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Aimé.e! Ça fait un moment que je te cherche !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Alors c'était là où tu te cachais !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "peacock"
    queue music BalconCoupletIntro noloop
    queue music BalconCouplet
    show imani_laugh at pea_right
    hide imani_neutre
    imani "Moi aussi ! Ça fait une demie-heure que je te cherche ! On a dû faire que de se louper."
    show imani_neutre at pea_right
    hide imani_laugh
    imani "Bon, au final, je me suis pris à boire et j'ai arrêté de bouger pour que tu puisses me retrouver !"
    $ current_textbox = "anthrax"

    anthrax "J'aurais pu tourner encore longtemps, dis ! Pourquoi tu ne m'as pas appelé.e ?"
    $ current_textbox = "peacock"
    show imani_nosmile at pea_right
    hide imani_neutre
    imani "J'ai laissé mon téléphone dans les loges, j'avais la flemme d'aller le chercher."
    $ current_textbox = "anthrax"

    anthrax "Ah... Tu n'es pas possible."
    $ current_textbox = "peacock"

    show imani_laugh at pea_right
    hide imani_neutre
    show flirt at flirt_right
    play vfxR VFXFlirt
    imani "Roh, arrête~ C'est comme ça qu'on m'aime !"
    hide flirt
    $ current_textbox = "anthrax"
    show imani_neutre at pea_right
    hide imani_laugh
    anthrax "Oui, oui... Bien sûr. Qu'est-ce que tu bois ?"
    $ current_textbox = "peacock"


    imani "Un jus d'abricot. Classique et délicieux !"
    $ current_textbox = "description"

    #show overlay
    text "Il termina le fond de son verre d'une traite, avant de le poser sur l'une des tables qui n'avaient pas encore été dressées pour la soirée."

    $ quick_menu = False
    show imani_neutre at pea_right
   
    menu:
        text "Il termina le fond de son verre d'une traite, avant de le poser sur l'une des tables qui n'avaient pas encore été dressées pour la soirée."
        
        "Quand j'y repense, je ne t'ai jamais vu boire.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            queue music BalconRefrain
            pass
        "Tu aimes vraiment les softs. Haha !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            queue music BalconRefrain
            pass
        "Je ne t'ai vu tourner qu'à l'eau dernièrement, ça change !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            queue music BalconRefrain
            pass

    #hide overlay


    $ quick_menu = True

    $ current_textbox = "peacock"
    show imani_laugh at pea_right
    hide imani_neutre
    imani "Hm... Peut-être parce qu’il est 16h00 de l’après-midi et qu’il est un peu tôt à mon goût pour ça ?"
    $ current_textbox = "anthrax"
    show imani_nosmile at pea_right
    hide imani_laugh
    anthrax "Non ! Pas dans ce sens là, je n’ai pas envie de passer pour un.e ivrogne ! Je me faisais juste la réflexion..."
    $ current_textbox = "peacock"

    imani "Non, je ne bois pas. Je ne bois plus..."
    show angry at angry_right
    play vfxR VFXAnger
    imani "Parce que moi, je l’ai été... ivrogne. Et il n’y a pas un monde où je me laisserais retomber là dedans."
    hide angry
    $ current_textbox = "anthrax"

    anthrax "Oh! La boulette..."


#Choix PEA.3
label choix_pea3:
    $ quick_menu = False

    show imani_neutre at pea_right
    show imani_sassy at pea_right
    hide imani_nosmile
    with fade

    menu: 
        imani "Ça, je ne te le fais pas dire."
        "Je me sens bête d'avoir amené le sujet comme ça...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_3_1 from _call_pea_3_1_1 
        "Comment est-ce que tu es tombé dedans ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_3_2 from _call_pea_3_2
        "Tu as dû prendre pas mal de temps pour t'en remettre, non ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_3_3 from _call_pea_3_3 

#PEA.3.1
#-1
label pea_3_1:
    $ quick_menu = True
    $ indice_pea -= 1

    show imani_neutre at pea_center
    show imani_sassy at pea_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Je me sens bête maintenant, d'avoir amené le sujet comme ça..."
    $ current_textbox = "peacock"
    show imani_nosmile at pea_center
    hide imani_sassy
    imani "En même temps, boire, c’est tellement normalisé dans notre société. Et encore plus dans nos communautés."
    show sadness at sadness_pea_center
    play vfxC VFXSadness
    imani "Je ne peux pas t’en vouloir, tu ne pouvais pas savoir..."
    hide sadness
    $ current_textbox = "anthrax"

    anthrax "C’est vrai qu’en général, on boit beaucoup et de manière assez rituelle..."
    $ current_textbox = "peacock"

    imani "Ouais... Dis-toi qu’ils pratiquaient encore la tradition du petit shot avant le spectacle avant mon arrivée."
    show imani_neutre at pea_right
    hide imani_nosmile
    imani "Mais je leur ai dit que ça me mettait un peu mal à l’aise, et la troupe a finalement été très compréhensive."
    imani "Surtout que ce n’est que bien plus tard que je leur ai parlé de mes anciens problèmes d’alcoolisme."
    show imani_laugh at pea_right with dissolve
    hide imani_neutre
    imani "C’est aussi comme ça que je me suis rendu compte que j’étais tombé sur ma famille de cœur."
    show joy at joy_right
    play vfxR VFXJoy
    imani "Et ça ne nous empêche pas de nous retrouver au bar après la fermeture pour boire un verre de temps en temps."
    hide joy

    $ quick_menu = False
    show imani_neutre at pea_right
    hide imani_laugh
   
    menu:
        imani "Je réussis à en surprendre plus d’un avec mes idées de mocktails !"

        "L'Androgame renvoie une atmosphère vraiment bienveillante.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "On a de la chance, ce n'est pas le cas partout.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Je n'en attendais pas moins de cet établissement !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "peacock"

    show imani_nosmile at pea_right
    hide imani_neutre
    imani "Hm... Je ne pars pas du principe que tout le monde est mauvais, mais c’est vrai que les milieux queers fonctionnent énormément autour de la drogue et de l’alcool."
    imani "Après tout, les bars et clubs étaient les seuls lieux qui acceptaient la prohibition. C’est culturel à présent."

    $ quick_menu = False
    show imani_neutre at pea_right
    hide imani_nosmile
   
    menu:
        imani "Mais on peut faire mieux que ça ! On n’a pas besoin de se désinhiber pour se sentir légitime d’exister, de s’amuser et de réclamer nos espaces !"
        "Je sens que c’est encore trop ancré dans la culture LGBT.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Le milieu de la nuit a toujours eut ce côté... \"défiance\"":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Nous sommes dans un cabaret, après tout...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True
 
    $ current_textbox = "peacock"

    imani "C’est vrai... Mais je ne pense pas que les deux sont incompatibles."
    show imani_nosmile at pea_right
    hide imani_neutre
    show angry at angry_right
    play vfxR VFXAnger
    imani "Si je suis tombé dans l’addiction, c’est aussi parce que l’on m’a influencé, et normalisé ce genre de comportement. Après je ne nie pas la part de responsabilité que j'ai eu la-dedans..."
    hide angry
    imani "J’ai toujours travaillé dans l’industrie du spectacle et de l’entertainment, les vices sont bien plus profonds que ça..."
    show imani_emo at pea_right
    hide imani_nosmile
    imani "Et justement, prendre du recul est mal vu. Tu es « moins drôle », « pas fun », « archi ennuyeux », si tu ne bois pas."
    $ current_textbox = "anthrax"

    show imani_neutre at pea_right
    hide imani_emo
    anthrax "Alors tu es l’exception qui confirme la règle. Parce que tu es l’opposé de « boring » !"

    call pea_4 from _call_pea_4 

#PEA.3.2

label pea_3_2:
    $ quick_menu = True
    $ indice_pea += 1

    show imani_neutre at pea_center
    show imani_sassy at pea_center
    hide imani_nosmile
    with fade
    $ current_textbox = "anthrax"

    anthrax "Comment est-ce que tu es tombé dedans? Ça te ressemble si peu..."
    $ current_textbox = "peacock"

    show imani_emo at pea_center
    hide imani_neutre
    imani "Franchement, ce n’est pas l’histoire la plus sensationnelle que je pourrais te raconter..."
    show imani_nosmile at pea_center
    hide imani_emo
    show sadness at sadness_pea_center
    play vfxR VFXSadness
    imani "Est-ce qu'elle mérite même d’être racontée ? Je ne sais pas... J’étais vraiment pathétique."
    hide sadness
    $ current_textbox = "anthrax"

    anthrax "Ne dis pas ça... C’est vicieux, les addictions. Sinon personne ne serait accro à rien ! Tu as fini par t’en sortir."
    anthrax "Donc ce n’est pas le nombre d’échecs qui compte, mais le résultat : Tu tiens à ta sobriété."
    anthrax "Et je dis ça, sans t’avoir connu à l’époque !"
    $ current_textbox = "peacock"

    show imani_neutre at pea_center
    hide imani_nosmile
    imani "Ha ha ! T’es chou..."


    $ quick_menu = False
    hide imani_neutre
    hide imani_sassy
    show imani_nosmile at pea_right
   
    menu:
        imani "Mais tu n’aurais peut-être pas voulu me connaître à l’époque..."
        "Pourquoi donc ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ah bon ? Pourquoi dis-tu ça...?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ça ne devais pas être à ce point terrible, si ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "peacock"


    imani "Et bien... Je n’étais pas quelqu’un que l’on pouvait qualifier... d’émotionnellement stable."
    imani "Je travaillais bien et étais respectueux, hein ! Mais, je ne sais pas... J’ai toujours senti que quelque chose clochait."
    show imani_emo at pea_right
    hide imani_nosmile
    imani "J’étais encore très immature, dans mes relations. Il n’y avait qu’au travail où j’avais un cadre qui me permettait de garder les pieds sur terre."
    show imani_nosmile at pea_right
    hide imani_emo

    imani "Et pourtant, il y a commencé à y avoir des écarts... Au début, entre collègues, c’était marrant de sortir boire un verre pour décompresser."
    imani "Mais ça a pris des proportions telles où l’on finissait en boîte jusqu’à pas d’heure, où ça se droguait et se mettait la misère."
    show sadness at sadness_pea_right
    play vfxR VFXSadness
    imani "Et je t’ai dit, j’étais immature... Donc cette ambiance, ça me plaisait. Et je suis un bon suiveur..."
    $ current_textbox = "anthrax"

    anthrax "C’est normal de faire des erreurs, tu sais... Et sortir s’amuser, personne ne peut te blâmer là-dessus ! Alors pourquoi toi ?"
    $ current_textbox = "peacock"

    hide sadness
    show imani_emo at pea_right
    hide imani_nosmile
    imani "Parce que ce n’était que le début !"
    imani "J’en suis venu à penser que c’était normal... Mais ça a vraiment dérapé quand je suis devenu acteur de ma déchéance."
    imani "Ce sentiment de... « truc qui cloche », il ne m’a jamais quitté. Et les soirées, c’était un moyen de me distraire pour ne plus y penser."

    $ quick_menu = False
    show imani_neutre at pea_right
    show imani_nosmile at pea_right
    hide imani_emo
   
    menu:
        imani "Mais quand ça t’obscède autant dans la journée et que tu n’as pas de porte de sortie, tu t’en crées..."
        "Oh non...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Est-ce que c'est ce que je crois être ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Mince... Je pense deviner où ça mène.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "peacock"

    show sadness at sadness_pea_right
    play vfxR VFXSadness
    imani "Si... J’ai commencé à boire au taf."
    hide sadnesso
    imani "Au début, c’était discret. Je buvais juste suffisamment pour me désinhiber. Mais là encore, je n’ai pas su m’arrêter."
    imani "Et au final, ils ont fini par s’en rendre compte et me virer."
    imani "Ça m’a mis un coup de pied aux fesses suffisant pour que j’aille faire une cure de désintox dans un centre, et je suis revenu en force !"
    $ current_textbox = "anthrax"

    anthrax "Et tu l’as toujours ce « truc qui cloche » ?"
    $ current_textbox = "peacock"

    show imani_neutre at pea_right
    hide imani_nosmile
    imani "Hm... Un peu ! Mais j’ai mis le doigt dessus en commençant à faire du drag. Je pense donc être sur la bonne voie !"

    call pea_4 from _call_pea_4_1 

#PEA.3.3

label pea_3_3:
    $ quick_menu = True

    show imani_neutre at pea_center
    show imani_sassy at pea_center
    hide imani_nosmile
    with fade
    $ current_textbox = "anthrax"

    anthrax "Tu as dû prendre pas mal de temps pour t’en remettre, non ?"
    $ current_textbox = "peacock"

    show imani_nosmile at pea_center
    hide imani_sassy
    imani "Oui, ça on peut le dire... Mais c’est parce que ça a été un parcours de longue haleine..."
    show sadness at sadness_pea_center
    play vfxR VFXSadness
    show imani_emo at pea_center
    hide imani_nosmile
    imani "Des fois, je me dis que j’aurais pu voir les signes et m’arrêter à temps."
    show imani_nosmile at pea_center
    hide imani_emo
    imani "Mais techniquement, ce serait mentir, puisque j’ai essayé à plusieurs reprises d’arrêter. Je manquais juste de..."
    imani "De volonté ? De motivation ? Ce ne sont même pas les bons mots pour décrire..."
    show imani_sassy at pea_center
    hide imani_nosmile
    imani "L’alcool avait juste une telle emprise sur moi que j’ai l’impression que je me disais ça pour me donner bonne conscience."
    hide sadness
    imani "« Essayer, sans réellement essayer »... Entre les tentatives ratées et les fausses excuses que je me donnais, il a d’abord fallu que je remette les pieds sur terre."
    show imani_nosmile at pea_center
    hide imani_sassy

    $ quick_menu = False

    hide imani_neutre
    hide imani_nosmile
    show imani_neutre at pea_right
   
    menu:
        imani "Et ça n’a pas été une mince affaire."
        "Qu'est-ce qui t'as motivé à changer ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Tu as juste fait quelques détours, mais tu y es arrivé !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Comment est-ce que tu as fait ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True


    $ current_textbox = "peacock"
    
    imani "Moi ? Je n’ai rien fait. J’ai dû me faire virer de mon ancien taf pour que j’aie un déclic..."
    show imani_laugh at pea_right
    hide imani_nosmile
    imani "Vraiment, je n’ai aucun mérite dans cette affaire !"
    show imani_nosmile at pea_right
    hide imani_laugh
    $ current_textbox = "anthrax"

    anthrax "Je trouve que tu t’en donnes trop peu, de mérite. Tu as réussi à te sortir de l’addiction après tout."
    $ current_textbox = "peacock"

    show sadness at sadness_pea_right
    imani "Oui, mais... Je suis toujours terrifié à l’idée de retomber dedans. C’est comme une ombre qui me suit de très près, et de laquelle je ne peux pas me défaire..."
    hide sadness
    imani "C’est sûrement le temps qui fera ce travail, mais en attendant, je reste prudent..."
    show imani_sassy at pea_right
    hide imani_nosmile
    imani "Il n’y a aucune chance que je redevienne qui j’étais durant cette période..."
    show angry at angry_right
    play vfxR VFXAnger
    imani "Une sorte de zombie... Une autre personne, en tous points, qui n’avait pas de volonté autre que de toucher à la goutte suivante."
    hide angry
    show imani_emo at pea_right
    hide imani_sassy
    imani "J’étais tellement accro, que je ne faisais que trembler, suer, halluciner... Sûrement parce que je n’arrivais pas à dormir..."
    show imani_nosmile at pea_right
    hide imani_emo
    imani "Heureusement que j’étais en cure de désintox et qu’il y avait du monde pour s’occuper de moi, parce que j’avais l’impression de mourir."
    $ current_textbox = "description"

    #show overlay
    text "Je ne su quoi lui répondre, ne pouvant que me l’imaginer. Jamais je n’aurais pensé qu’Imani avait traversé une telle épreuve..."
    hide overlay
    $ current_textbox = "peacock"


    $ quick_menu = False
    show imani_neutre at pea_right
    show imani_emo at pea_right
    hide imani_nosmile
    menu:
        imani "On dirait que cette histoire a laissé un froid, non ? Désolé, c’était un peu morbide..."

        "Non, non... Ne t’excuse pas. ":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Je m'en parle pas, haha... Mais t'inquiète.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Imani... Ce n'est rien voyons.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True


    $ current_textbox = "anthrax"

    show imani_nosmile at pea_right
    hide imani_emo
    anthrax "C’est juste que..."
    anthrax "Pendant tout ce temps, tu devais te sentir tellement seul."
    $ current_textbox = "peacock"
    
    show sadness at sadness_pea_right
    play vfxR VFXSadness
    imani "..."
    $ current_textbox = "anthrax"

    show imani_emo at pea_right
    hide imani_nosmile
    anthrax "Je suis content.e que tu ne sois plus entravé par l’addiction. Tu as l’air heureux, et entouré."
    hide sadness
    anthrax "Ce n’est pas ton passé qui te définit, tu sais ?"
    $ current_textbox = "peacock"

    show imani_nosmile at pea_right
    hide imani_emo
    imani "C’est vrai, tu as raison... Je vais sûrement mettre encore un peu de temps pour le croire, mais merci..."
    imani "..."
    show imani_neutre at pea_right
    hide imani_nosmile
    imani "Bon ! C’est pas tout, mais on a un show à préparer... Il faut que j'arrête de m'appitoyer sur mon sort !"
    imani "Merci d'avoir prit le temps de m'écouter..."
    
    call pea_4 from _call_pea_4_2 

#PEA.4
label pea_4:

    hide auditorium
    hide imani_neutre with fade
    
    scene black

    stop music fadeout 0.2
    stop ambiance fadeout 1.0
    play ambiance AmbLoges fadein 0.5
    play music LogesIntro volume 0.5

    
    $ current_textbox = "description"
    text "Debout au milieu de la pièce, Imani était en train de passer le fil de son micro dans les espaces étriqués de son corset et de son padding couleur chair..."
    text "le passant dans la lanière de son bullet-bra jusque le long de son dos. Accrochant l'appareil à l'aide d'épingles à sa perruque, elle semblait avoir la tête ailleurs..."
    text "Tout en reproduisant ses gestes millimétrés et à présent routiniers, glissant ensuite le boîtier HF dans sa jarretelle qui avait été modifiée à cet effet."
    text "Peacock enfila ensuite sa robe à dos nu et déclipsa le soutien-gorge pour dissimuler le tissu dépassant dans son costume, n'ayant pas besoin de maintien."

    $ quick_menu = False
    show loges with fade
    show peacock_neutre at pea_right with dissolve
   
    menu:
        #show overlay
        text "Une étiquette dépassait effrontément du vêtement et je me levai pour remédier à ce problème."
        "Attends, oups... Je me permets...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Ne bouge pas ! Il y a juste quelque chose...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Excuse-moi, je fais vite... ":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True
    queue music LogesRefrain volume 0.5
    
    #hide overlay
    $ current_textbox = "anthrax"
    anthrax "Voilà !"

    $ current_textbox = "description"
    
    #show overlay
    text "Un peu surprise, Imani remarqua que j'essayais maladroitement d'aider et me laissa faire, avant de me sourire avec un air attendri."
    #hide overlay
    $ current_textbox = "peacock"

    show flirt at flirt_right
    play vfxR VFXFlirt
    show peacock_laugh at pea_right
    hide peacock_neutre

    peacock "Tu es adorable, merci girlie."
    hide flirt
    $ current_textbox = "anthrax"
    show peacock_neutre at pea_right
    hide peacock_laugh

    anthrax "Je peux t'aider à quelque chose d'autre ?"
    $ current_textbox = "peacock"

    peacock "Hm... Je ne sais pas trop. Peut-être peux-tu vérifier l'état des plumes de mes éventails ? Je les ai changées il y a peu, mais elles ont peut-être besoin d'être ébouriffées."
#Choix PEA.4
label choix_pea4:
    $ quick_menu = False
    $ current_textbox = "peacock"

    show peacock_neutre at pea_right

    menu: 
        anthrax "Oui, bien sûr !"
        "Ça fait longtemps que tu fais ce show? ":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_4_1 from _call_pea_4_1_1 
        "Tu comptes chanter aussi? Je vois que tu as un micro...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_4_2 from _call_pea_4_2_1 
        "Les ébouriffer? Tu fais de l'effeuillage?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_4_3 from _call_pea_4_3 

#PEA.4.1

label pea_4_1:
    $ quick_menu = True

    show peacock_neutre at pea_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Ça fait longtemps que tu fais ce show? Avec les plumes je veux dire..."
    $ current_textbox = "peacock"

    peacock "Hm... Oui et non. Il a tout de même bien évolué depuis mes débuts."
    show peacock_laugh at pea_center
    hide peacock_neutre
    peacock "Évidemment, je me base sur mes atouts, mais l'expérience fait que le show s'est amélioré."
    show peacock_neutre at pea_center
    hide peacock_neutre
    show joy at joy_center
    play vfxC VFXJoy

    peacock "Puis, j'y ai aussi mit de l'effort. J'ai pris des classes, j'ai longtemps itéré, jusqu'à trouver la formule qui me correspondait."
    hide joy

    $ quick_menu = False
    hide peacock_laugh with dissolve
    show peacock_neutre at pea_right
   
    menu:
        peacock "Et je suis loin d'avoir fini, je compte rester dans le business encore un moment. Le show continuera de progresser dans tous les cas."

        "Et donc, les plumes, ça t'a inspiré en particulier ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Le paon, Peacock, les plumes, je fais le lien...~":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est vrai que c'est emblématique du burlesque !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True
    
    
    $ current_textbox = "peacock"

    show peacock_laugh at pea_right
    hide peacock_neutre
    peacock "Eh bien, mon nom de scène vient de là... Et puis c'est finalement ce qui m'a fait me rapprocher de l'Androgame."
    show peacock_neutre at pea_right
    hide peacock_laugh
    peacock "J'ai toujours eu une admiration démesurée pour le monde de la scène, mes parents m'emmenaient toujours en spectacle quand j'étais petit."
    peacock "Ce sont les souvenirs qui me ramènent le plus en enfance."
    peacock "Et une fois, il y avait ces danseuses de cabaret, avec leurs grands éventails à plumes. À partir de ce point, je n'ai jamais lâché cette fixette."
    $ current_textbox = "delaunay"

    show delaunay_laugh at del_left
    delaunay "C'est mignon ! Quand j'y repense, mes parents aussi m'emmenaient en spectacle. C'est peut-être de là que ça vient."
    $ current_textbox = "gatsby"

    hide peacock_neutre
    show gatsby_laugh at gat_right with dissolve
    gatsby "Ou d'y avoir été sensibilisé.e au moins. De mon côté, c'était plus les comédies musicales à la télé, du type \"Mozart, l'Opéra Rock\" ou \"1789\"."
    $ current_textbox = "peacock"

    hide delaunay_neutre
    show peacock_neutre at pea_left with dissolve
    hide delaunay_laugh
    show peacock_laugh at pea_left with dissolve
    show joy at joy_left
    play vfxL VFXJoy
    peacock "Comme quoi ! Les plumes, la scène, le théâtre... Au final, c'est plus histoire de me rappeler d'où je viens, ce que j'aime et ce qui m'a construit."
    hide gatsby_laugh
    hide joy


    $ quick_menu = False
    hide gatsby_neutre
    show peacock_neutre at pea_right with dissolve
    hide peacock_laugh
   
    menu:
        peacock "Et je parle pour plusieurs on dirait."
        "Tu as l'air du genre très polyvalente !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Tu n'as pas peur de trop te répêter ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est assez beau comme réflexion. Ça ne t'a jamais ennuyée?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True

    $ current_textbox = "peacock"

    show peacock_laugh at pea_right
    hide peacock_neutre
    peacock "Peut-être par moments, c'est pour ça que je danse, je chante et je fais rire à côté. Je déteste l'idée de ne pas me renouveler et de proposer toujours la même chose."
    peacock "Même si ce n'est pas simple d'innover chaque semaine, c'est quelque chose que je me suis promis de faire."
    show peacock_neutre at pea_right
    hide peacock_laugh
    peacock "Sinon, autant arrêter le drag maintenant. Ça ne sert à rien d'être boring sur scène..."
    $ current_textbox = "delaunay"
    
    show delaunay_neutre at del_left with dissolve
    show delaunay_nosmile at del_left with dissolve

    delaunay "Moi, pas du tout... Il y a quelque chose de relaxant à faire un numéro répétitif. "
    show delaunay_neutre at del_left with dissolve
    hide delaunay_nosmile
    delaunay "On a beau le connaître par cœur, on en découvre toujours de nouvelles facettes."
    $ current_textbox = "gatsby"
    hide peacock_neutre with dissolve

    show gatsby_neutre at gat_right with dissolve
    show gatsby_pensive at gat_right with dissolve
    gatsby "J'ai une relation un peu plus mitigée avec le mien, puisque j'ai une démarche différente qui est plus de l'ordre de la réconciliation."
    show gatsby_nosmile at gat_right with dissolve
    hide gatsby_pensive
    gatsby "Donc parfois, je le déteste, et parfois je l'adore. Mais ennuyant ? Ça, jamais."

    stop music fadeout 0.1

    hide delaunay_neutre with dissolve
    hide gatsby_neutre with dissolve
    hide gatsby_nosmile with dissolve
    staff "Ok les filles ! Showtime dans dix minutes !"
    $ current_textbox = "peacock"

    show peacock_laugh at pea_center with dissolve

    peacock "Déjà ?! Bon, plus qu'à se dépêcher...!"
    
    stop ambiance fadeout 3.0
    call pea_5 from _call_pea_5 

#PEA.4.2

label pea_4_2:
    $ quick_menu = True
    $ indice_pea += 1

    show peacock_neutre at pea_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Sans souci ! Tu comptes chanter aussi ? Je vois que tu as un micro d'installé..."
    anthrax "J'étais persuadé.e que tu ne faisais que de la danse..."
    $ current_textbox = "peacock"

    
    $ quick_menu = False
    show peacock_neutre at pea_right

    menu:
        peacock "Il fut une époque, c'était le cas. J'étais encore timide et je reproduisais des pas de chorés que j'avais vus sur internet."

        "Et qu'est-ce qui a changé depuis ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est bien de se renouveler ! Qu'est-ce qui a évolué ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Et du coup le chant, hein ? Qu'est-ce qui t'as convaincue ?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True
    
    $ current_textbox = "peacock"

    show joy at joy_right
    play vfxR VFXJoy
    peacock "Honnêtement, énormément de choses, et à la fois, pas tant. J'ai pris en confiance principalement."
    hide joy
    peacock "Je t'avais dit que je bossais en régie avant ?"
    peacock "Maintenant, je fais de la radio et du podcast, tout en filant un coup de main de temps en temps, au besoin."
    show peacock_laugh at pea_right
    hide peacock_neutre
    peacock "La musique a toujours eu une place super importante dans ma vie, et je ne pensais pas être suffisamment talentueuse pour pouvoir partager ça sur scène un jour."
    peacock "Encore une leçon que le drag m'a apprise : ne jamais se douter de ses capacités et savoir se lancer."
    show peacock_neutre at pea_right
    hide peacock_laugh
    $ current_textbox = "gatsby"

    show gatsby_neutre at gat_left with dissolve
    show gatsby_laugh at gat_left with dissolve
    gatsby "On est un peu tous.te.s dans ce cas. Le drag, ça éveille des capacités insoupçonnées. "
    show gatsby_pensive at gat_left
    hide gatsby_laugh
    gatsby "Ou en tout cas, ça nous encourage à nous redécouvrir sous un nouvel angle."
    
    $ current_textbox = "delaunay"

    hide peacock_neutre
    show delaunay_neutre at del_right with dissolve
    show delaunay_shy at del_right with dissolve
    delaunay "Pendant un long moment, je ne me suis jamais cru capable d'être aussi confiant. "
    show delaunay_flirty at del_right
    hide delaunay_shy
    delaunay "Encore moins sur scène. Et encore moins en m'effeuillant !"
    $ current_textbox = "peacock"
    
    hide gatsby_neutre
    hide gatsby_pensive
    hide delaunay_neutre
    hide delaunay_flirty

    
    $ quick_menu = False
    show peacock_neutre at pea_right
    show peacock_emo at pea_right
   
    menu:
        peacock "Et moi, je ne me sentais pas suffisamment légitime, ou sexy, ou \"féminine\" pour faire du drag à barbe et rendre hommage à ma culture. Surtout que je pars de loin !"
        "C'est super physique de chanter et danser en même temps !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "La manière dont il m'a été vendu, ton gig est sportif !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Et tu as le temps de respirer avec tout ça ?!":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass




    $ quick_menu = True
    
    $ current_textbox = "peacock"

    show peacock_laugh at pea_right
    hide peacock_emo
    peacock "On s'y fait... Et puis, c'est pour ça que je me pose ensuite sur scène pour enchaîner le public."
    peacock "J'ai toujours été un petit clown de service, et l'humour nous rend toujours plus accessible, même envers les personnes qui ne sont pas très familières avec notre art."
    show joy at joy_right
    play vfxR VFXJoy
    
    peacock "Autant \"ouvrir la bibliothèque\" en dehors des loges. C'est bien de lire les copines, encore mieux d'en faire profiter tout le monde."
    hide joy
    $ current_textbox = "gatsby"
    show peacock_neutre at pea_right
    hide peacock_laugh
    show gatsby_neutre at gat_left with dissolve
    show gatsby_laugh at gat_left with dissolve
    gatsby "Oui... Enfin, quand tu te décides à tacler, t'en fais pas que tu ne te gardes pas de le faire dans les coulisses."
    $ current_textbox = "delaunay"
    hide peacock_neutre
    show delaunay_neutre at del_right with dissolve
    delaunay "Et puis, quand tu es dans l'humeur, on en a parfois pour des heures !"

    stop music fadeout 0.1
    $ current_textbox = "mother"

    hide delaunay_neutre with dissolve
    hide gatsby_neutre with dissolve
    hide gatsby_laugh with dissolve

    staff "Ok les filles ! Showtime dans dix minutes !"
    $ current_textbox = "peacock"

    show peacock_laugh at pea_center with dissolve
    peacock "Déjà ?! Bon, plus qu'à se dépêcher...!"

    stop ambiance fadeout 3.0
    call pea_5 from _call_pea_5_1 

#PEA.4.3

label pea_4_3:
    $ quick_menu = True
    $ indice_pea -= 1

    show peacock_neutre at pea_center
    with fade
    $ current_textbox = "anthrax"

    anthrax "Les ébouriffer ? Est-ce que c'est pour mieux te cacher lors de l'effeuillage ?"
    anthrax "Je pensais qu'il n'y avait que Léandre qui faisait ça ici..."
    $ current_textbox = "peacock"

    show peacock_sassy at pea_center
    hide peacock_neutre
    peacock "L'effeuillage ? Hm... Non, ce n'est vraiment pas mon genre de numéro ça."
    show peacock_neutre at pea_right
    hide peacock_sassy
    peacock "\"Don't get me wrong\", je suis une bombe."
    
    $ quick_menu = False
    show peacock_neutre at pea_right
    show peacock_nosmile at pea_right
   
    menu:
        peacock "Mais me déshabiller sur scène face à tout un public, ça va à l'encontre de ce que je veux transmettre avec ma persona."

        "Ah bon? C'est-à-dire? J'ai du mal à comprendre.":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Pourtant, je suis sûr.e que beaucoup apprécieraient ~":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "C'est très burlesque, j'aurais imaginé ça avec les éventails...":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True
    

    $ current_textbox = "peacock"

    peacock "Faut que je réussisse à mettre les mots dessus, attends..."
    show peacock_neutre at pea_right
    hide peacock_nosmile
    peacock "En fait, Peacock, elle est sensuelle, mais avec pudeur et une certaine humilité. "
    peacock "Elle ne charme pas comme Delaunay, en jouant de son corps. Elle use de ses autres charmes."
    show flirt at flirt_right
    play vfxR VFXFlirt
    peacock "\"J'use\" de mes autres charmes."
    hide flirt
    $ current_textbox = "anthrax"

    anthrax "Rien de mal avec un peu de \"body-oh-dy\"..."
    $ current_textbox = "peacock"

    show peacock_laugh at pea_right
    hide peacock_neutre
    peacock "Entièrement d'accord avec toi. C'est pour ça que j'ai précisé que j'étais une bombe, chéri.e"
    $ current_textbox = "anthrax"
    show peacock_neutre at pea_right
    hide peacock_laugh

    anthrax "Oh, je vois ce que tu sous-entendais par \"humilité\"...~"
    $ current_textbox = "peacock"

    show peacock_laugh at pea_right
    hide peacock_neutre
    peacock "Touchée... Et shady~"
    
    $ quick_menu = False
    show peacock_neutre at pea_right
    hide peacock_laugh

    menu:
        peacock "Tu apprends vite~"

        "J'apprends surtout des meilleur.e.s":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Un peu de lecture ne fait pas de mal ~":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Tu commences à déteindre sur moi !":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass


    $ quick_menu = True
  
    $ current_textbox = "delaunay"

    show delaunay_neutre at del_left with dissolve
    show delaunay_laugh at del_left with dissolve
    delaunay "On vous entend à côté ! Faudrait pas non plus nous rendre jaloux.e.s. ~"
    $ current_textbox = "gatsby"
    
    hide peacock_neutre
    show gatsby_neutre at gat_right with dissolve
    show gatsby_laugh at gat_right with dissolve
    gatsby "Je t'ai vue draguer avec plus de finesse, Pea ! Attention à ne pas te perdre avec l'âge !"
    $ current_textbox = "peacock"

    hide delaunay_neutre with dissolve
    hide delaunay_laugh with dissolve
    hide gatsby_neutre with dissolve
    hide gatsby_laugh with dissolve

    show peacock_neutre at pea_center with dissolve
    show peacock_sassy at pea_center with dissolve

    peacock "Non mais de quoi je me mêle les fouineuses !"
    show angry at angry_center
    play vfxC VFXAnger
    peacock "Occupez-vous de faire un trait d'eyeliner droit avant de vous intéresser à mes techniques de séduction !"
    hide angry
    $ current_textbox = "anthrax"

    anthrax "Ah... Donc c'est là où l'on se situe ?~"
    $ current_textbox = "peacock"

    show peacock_laugh at pea_center
    hide peacock_sassy
    show flirt at flirt_center
    play vfxR VFXFlirt
    peacock "Pas encore ~ Mais c'est une option tout à fait envisageable."
    hide flirt
    show peacock_nosmile at pea_center
    hide peacock_laugh
    peacock "Si nos deux commères nationales arrêtaient de fourrer leur nez là où ça ne les concernent pas !"

    stop music fadeout 0.1
    $ current_textbox = "mother"

    hide peacock_neutre with dissolve
    hide peacock_nosmile with dissolve
    staff "Ok les filles ! Showtime dans dix minutes !"

    $ current_textbox = "peacock"
    show peacock_laugh at pea_center with dissolve
    peacock "Déjà ?! Bon, plus qu'à se dépêcher...!"
   
    stop ambiance fadeout 3.0
    call pea_5 from _call_pea_5_2 

#PEA.5
label pea_5:

    show curtain_close with dissolve
    hide peacock_laugh with dissolve
    hide peacock_neutre with dissolve
    hide bar
    hide loges with dissolve
    pause 1.5
    show curtain_open with dissolve

    scene black with dissolve
    play music ShowPeacock noloop

    $ current_textbox = "description"

    text "Les yeux du public étaient encore rivés sur la scène où les restes du précédent numéro se faisaient débarrasser... "
    text "Qu'ils furent forcés de se retourner en entendant une voix rauque et a cappella démarrer le fameux 'Feeling Good' de Nina Simone depuis le fond de la salle."
    show auditorium with dissolve
    show peacock_neutre at pea_center with dissolve
    text "Les escarpins ancrés dans le marbre du comptoir du bar, un spot détourant sa silhouette en contre-jour pour ajouter un peu de pizzazz à son entrée... "
    text "Peacock descendit tout en sensualité en se faisant porter par Doberman et se saisit des deux grands éventails à plumes que le staff lui présentait. "
    text "Et le band lança le top départ de sa performance en arrivant en fanfare."
    hide bar
    hide peacock_neutre
    show peacock_neutre at pea_right with dissolve
    show peacock_laugh at pea_right with dissolve
    show flirt at flirt_right
    play vfxR VFXFlirt
    text "Se baladant entre les tables, sans manquer une seule note, son chant et sa danse induisaient une certaine transe chez le public ébahi."
    text "Hypnotisante, chacun de ses coups de hanches, tourbillons de plumage et battement de cils soulevaient quelques sifflements jusqu'à ce que sa représentation ne se déplace sur l'estrade."
    hide peacock_neutre with dissolve
    hide flirt
    hide peacock_laugh with dissolve
    show peacock_neutre at pea_left with dissolve
    text "Tandis que les derniers accords signaient la fin de sa chorégraphie, elle troqua ses éventails pour un tabouret et un verre d'eau, chauffant la salle avec un 'one-woman show' pour introduire le prochain numéro."
    text "Son charisme, sa vivacité d'esprit et sa répartie étaient bien connus des habitué.e.s du cabaret, qui venaient parfois uniquement pour participer à cet instant léger et sarcastique."
    hide peacock_neutre with dissolve
    show peacock_neutre at pea_center with dissolve
    show peacock_laugh at pea_center with dissolve
    show joy at joy_center
    play vfxC VFXJoy
    text "Peacock se faisait règle de ne jamais reproduire un gig deux fois, de la même manière que ses tenues selon ses propres termes."
    text "Elle est quitta la scène sous les rires, après avoir introduit le show suivant."
    hide joy

    stop music fadeout 0.2

    call pea_6 from _call_pea_6 

#PEA.6
label pea_6:

    hide auditorium
    hide peacock_neutre
    hide peacock_laugh
    show loges with fade
    show peacock_neutre at pea_right with dissolve
    show peacock_laugh at pea_right with dissolve

    $ current_textbox = "peacock"


    peacock "OUF! Ça y est, le trac est passé !"
    peacock "J'en ai encore les genoux qui tremblent! J'espère que personne n'a remarqué !"


    hide peacock_neutre
    hide peacock_laugh
 
    $ quick_menu = False

    scene background_cg
    show CG_peacock at CG_center with fade

    $ current_textbox = "description"

    pause 1.0
    "Nouvelle illustration débloquée"
    hide CG_peacock with dissolve
    hide background_cg with fade
    $ persistent.peacock_unlocked = True  


    $ quick_menu = False
    $ current_textbox = "peacock"

show peacock_neutre at pea_right
hide peacock_laugh

$ quick_menu = False

menu:
    peacock "C'était particulièrement intense ce soir ou je rêve ?!"
    "Le trac? Toi? Tu as vu ton entrée?! Elle était sensationnelle!":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "La danse, les éventails, le chant! Mais waouh! La claque!":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass
    "C'était génial! J'ai rarement autant rit de ma vie!":
        $ renpy.play(random.choice(ui_choice_click), channel="sound")
        pass


$ quick_menu = True

show peacock_laugh at pea_right
hide peacock_neutre
peacock "C'est le meilleur shot d'adrénaline que j'aurais pu avoir!"
peacock "J'ai hâte que tu ressentes ça toi aussi."
show joy at joy_right
play vfxR VFXJoy
peacock "Tu vas voir, tu ne t'en lasses plus!"
hide joy
$ current_textbox = "anthrax"
show peacock_neutre at pea_right
hide peacock_laugh

anthrax "Si je peux être aussi radieux.se que toi ce soir, j'aurais tout gagné!"
$ current_textbox = "peacock"


label indice_pea:
        if indice_pea >= 0:
            jump pea_6_good
        else:
            jump pea_6_bad


#PEA.6.GOOD
label pea_6_good:

    show flirt at flirt_right
    play vfxR VFXFlirt
    peacock "Est-ce que je peux te proposer un resto, ensemble, après la fermeture? Je connais quelques adresses cosy encore ouvertes à cette heure...~"
    hide flirt

    $ quick_menu = False
    $ current_textbox = "description"

    show peacock_neutre at pea_right

    menu: 
        text "Accepter le date ?"
        "Oui":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Non":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            call pea_6_good_bad


    $ quick_menu = True
    show peacock_neutre at pea_center 
    show peacock_laugh at pea_center
    show loges with dissolve
    hide flirt

    $ current_textbox = "peacock"
    peacock "Oh! Tu acceptes ?! Wow ! Ok, ok  Je me change en vitesse alors ! Aha !"

    
    show curtain_close with dissolve
    play vfxC SFXCurtainClose
    hide peacock_neutre with dissolve
    hide peacock_laugh with dissolve
    hide bar
    scene black
    hide loges with dissolve
    scene black
    pause 1.5
    show curtain_open with dissolve
    play vfxC SFXCurtainOpen
    with fade
    
    $ quick_menu = True
    

    $ current_textbox = "description"

    text "Le temps que Peacock et les autres artistes terminent de se démaquiller et de se rhabiller en civil, je passai le balai sur les planches de la scène."
    text "Laissant mon esprit vagabonder au jour où moi-même je les foulerais."
    text "À l'extérieur, quelques clients étaient restés sur le pavé pour continuer leurs discussions et attendre la sortie de la royauté de l'Androgame."
    $ current_textbox = "peacock"

    show devanture
    show imani_neutre at pea_center with dissolve

    show joy at joy_center
    play vfxC VFXJoy
    imani "Me voici! Tu n'as pas attendu trop longtemps? Il commence à faire un peu frois en plus..."
    hide joy
    $ current_textbox = "anthrax"

    anthrax "Aha! Non, ne t'en fais pas! Je viens à peine de sortir!"
    anthrax "Merci pour l'invitation... Qu'est-ce qu'en ont pensé les autres, que l'on se fasse un truc à deux...?"
    $ current_textbox = "peacock"

    show imani_laugh at pea_center
    hide imani_neutre
    imani "Hm... J'ai eu le droit à quelques remarques dans les backstages, mais c'était plus par rapport à moi qui te vole pour le reste de la nuit...~"
    show imani_neutre at pea_center
    hide imani_laugh
    imani "Iels sont content.e.s pour nous dans tous les cas! Enfin, de ce qui démarre entre nous plutôt..."
    show imani_emo at pea_center
    hide imani_neutre
    imani "À moins que je me fasse des films...?"
    $ current_textbox = "anthrax"

    anthrax "Hm... Non, non. Pas de film. Tant qu'on prend notre temps et que le feeling est là !"
    show imani_neutre at pea_center
    hide imani_emo
    anthrax "En tout cas, il est bien là... Le feeling."
    show imani_laugh at pea_center
    hide imani_neutre
    anthrax "Mais dis-moi! Où est-ce que tu m'emmènes ce soir?"
    $ current_textbox = "peacock"

    show flirt at flirt_center
    play vfxC VFXFlirt
    imani "Je dois mettre la barre haute pour notre premier rendez-vous alors! J'ai une petite idée, mais je garde encore le secret ~"
    hide flirt
    call final_peacock from _call_final_peacock 

#PEA.6.BAD
label pea_6_bad:
    $ quick_menu = True
    
    hide auditorium
    show loges
    show peacock_neutre at pea_right with dissolve
    show peacock_laugh at pea_right with dissolve

    
    $ current_textbox = "peacock"
    peacock "On va aller boire un verre avec les autres une fois que les derniers clients auront quitté la salle. Tu te joins à nous ?"
    
    $ quick_menu = False

    menu:
        "Oui, bien sûr! Je termine ça et j'arrive!":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Si vous insistez!":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass
        "Proposé si gentiment, comment refuser?":
            $ renpy.play(random.choice(ui_choice_click), channel="sound")
            pass

    hide peacock_neutre with dissolve
    hide peacock_laugh with dissolve

    $ quick_menu = False
    


label pea_6_good_bad:
    hide gatsby_neutre with dissolve
    show curtain_close with dissolve
    pause 1.5
    hide bar
    hide loges
    scene black
    show curtain_open with dissolve
    with fade

    show bar with fade
    play music BadEnd volume 0.8 noloop
    $ current_textbox = "description"

    play music BadEnd volume 0.8 noloop
  
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
    show aimee_neutre at gat_right with dissolve
    show aimee_laugh at gat_right with dissolve

    $ current_textbox = "gatsby"
    aimee "Nan mais je te jure ! La manière dont sa perruque a volé au milieu de la pièce !"

    $ current_textbox = "delaunay"
    show leandre_neutre at del_left with dissolve
    show leandre_laugh at del_left with dissolve
    leandre "Et surtout sa tête, en s'en rendant compte... !"

    $ current_textbox = "peacock"
    hide aimee_neutre
    hide aimee_laugh

    show imani_neutre at pea_right with dissolve
    show imani_laugh at pea_right with dissolve
    imani "J'aurais rêvé être là cette soirée, et non derrière les machines !"

    $ current_textbox = "mother"
    hide leandre_neutre
    hide leandre_laugh
    show mother at mother_left with dissolve
    show mother_laugh at mother_left with dissolve

    show joy at joy_left
    play vfxL VFXJoy
    mother "Je suis sûre que je peux te retrouver une vidéo d'excellente qualité, vu comment elle a tourné sur les plateformes."
    hide joy

    hide imani_neutre
    hide imani_laugh

    hide mother
    hide mother_laugh

    show imani_neutre at pea_left with dissolve
    show leandre_neutre at del_right with dissolve
    show aimee_neutre at gat_center with dissolve


    $ current_textbox = "description"

    text "Les écoutant avec une certaine envie, ayant hâte de pouvoir raconter à mon tour mes aventures."
    text "Je les observais un à une, ancrant cette image dans ma mémoire, essayant d'y graver le moindre détail."
    hide leandre_neutre with dissolve
    hide aimee_neutre with dissolve
    show imani_laugh at pea_left
    text "Je m'en voulais peut-être un peu de ne pas avoir demandé à Imani d'être sorti avec moi ce soir."
    show imani_neutre at pea_left
    text "Mais quelque chose me dit que c'était peut-être un peu trop tôt..."
    show flirt at flirt_left
    play vfxL VFXFlirt
    text "Et j'aurais loupé cet instant précieux, sachant pertinemment que je passerais le reste de la soirée bien entouré.e !"
    hide flirt

    call final_peacock from _call_final_peacock_1 

    

label final_peacock:
    $ current_textbox = "description"
    hide imani_neutre with dissolve
    hide imani_laugh with dissolve
    hide devanture with fade
    hide bar with fade
    
    $ quick_menu = False
    stop music fadeout 1.0
    pause 1.0
    scene black with fade

    $ renpy.full_restart()
