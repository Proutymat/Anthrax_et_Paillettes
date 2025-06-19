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

image bar:
    "Backgrounds/bar.png"
    zoom 0.7

image loges = "Backgrounds/loges.png"

image rideau = "Backgrounds/rideau.png"

image balcon = "Backgrounds/balcon.png"

image CG_delaunay = "images/CGs/delaunay.jpg"

image background_cg = "images/Backgrounds/background_cg.png"

# Liste des sfx
define type_sounds = ['audio/SFX/TextMix-001.ogg','audio/SFX/TextMix-002.ogg','audio/SFX/TextMix-003.ogg','audio/SFX/TextMix-004.ogg','audio/SFX/TextMix-005.ogg','audio/SFX/TextMix-006.ogg','audio/SFX/TextMix-007.ogg','audio/SFX/TextMix-008.ogg','audio/SFX/TextMix-009.ogg','audio/SFX/TextMix-010.ogg']
define A_type_sounds = ['audio/SFX/AP_TA-001.ogg','audio/SFX/AP_TA-002.ogg','audio/SFX/AP_TA-003.ogg','audio/SFX/AP_TA-004.ogg']
define D_type_sounds = ['audio/SFX/AP_T1-001.ogg','audio/SFX/AP_T1-002.ogg','audio/SFX/AP_T1-003.ogg','audio/SFX/AP_T1-004.ogg']
define M_type_sounds = ['audio/SFX/AP_T2-001.ogg','audio/SFX/AP_T2-002.ogg','audio/SFX/AP_T2-003.ogg','audio/SFX/AP_T2-004.ogg']
define G_type_sounds = ['audio/SFX/AP_T3-001.ogg','audio/SFX/AP_T3-002.ogg','audio/SFX/AP_T3-003.ogg','audio/SFX/AP_T3-004.ogg'] 
define P_type_sounds = ['audio/SFX/AP_T4-001.ogg','audio/SFX/AP_T4-002.ogg','audio/SFX/AP_T4-003.ogg','audio/SFX/AP_T4-004.ogg']
define type_silent = ['<silence 1.0>']

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
define audio.GoodVibeIntro = "audio/Music/ON_GoodVibeIntro_V2.ogg"
define audio.IntroGoodVibe1 = "audio/Music/ON_GoodVibeA_V2.ogg"
define audio.IntroGoodVibe2 = "audio/Music/ON_GoodVibeB_V2.ogg"
define audio.IntroGoodVibe3 = "audio/Music/AP_IntroGoodVib3_V1.ogg"
define audio.IntroGoodVibe4 = "audio/Music/AP_IntroGoodVib4_V1.ogg"
define audio.CabaretEntrance = "audio/Music/ON_CabaretEntrance_V1.ogg"
define audio.CabaretIntro = "audio/Music/ON_CabaretIntro_V1_.ogg"
define audio.CabaretLightVerse = "audio/Music/ON_CabaretLightVerse_V1.ogg"
define audio.CabaretLightChorus = "audio/Music/ON_CabaretLightChorus_V1.ogg"
define audio.CabaretLightSolo = "audio/Music/ON_CabaretLightSolo_V1.ogg"
define audio.BackstageSt1 = "audio/Music/AP_Stinger1_V1.ogg"
define audio.BackstageSt2 = "audio/Music/AP_Stinger2_V1.ogg"
define audio.BackstageSt3 = "audio/Music/AP_Stinger3_V1.ogg"
define audio.BackstageSt4 = "audio/Music/AP_Stinger4_V1.ogg"
define audio.BackstageLoop = "audio/Music/AP_LogesTruc_V1.ogg"
define audio.BackstageDrumLoop = "audio/Music/ON_BackStageLoop_V1.ogg"
define audio.BarMusic = "audio/Music/RUN_BarNeutral_V1.ogg"
define audio.ShowDelaunay = "audio/Music/AP_ShowDelaunay_V2.ogg"
define audio.ShowGatsby = "audio/Music/AP_ShowGatsby_V1.ogg"
define audio.ShowPeacock = "audio/Music/AP_ShowPeacock_V1.ogg"
define audio.ConfidenceIntro = 'audio/Music/3_Confidence_Intro.ogg'
define audio.ConfidenceA1 = 'audio/Music/3_Confidence_A.ogg'
define audio.ConfidenceA2 = 'audio/Music/3_Confidence_A2.ogg'
define audio.ConfidenceAB = 'audio/Music/3_Confidence_AB.ogg'
define audio.ConfidenceB1 = 'audio/Music/3_Confidence_B1.ogg'
define audio.ConfidenceB2 = 'audio/Music/3_Confidence_B2.ogg'
define audio.ConfidenceOutro = 'audio/Music/3_Confidence_Outro.ogg'

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



label delaunay_start:
$ persistent.bg_parallax = True
$ quick_menu = True
default indice = 0
scene black with fade
show loges
#show leandre_shy at del_center with dissolve
show leandre_neutre at del_center with dissolve

play ambiance AmbLoges fadein 0.5 

#DEL.1
$ current_textbox = "delaunay"
leandre "Hey... Hum... Je suis content que tu m'aies choisi. Je ne pensais pas trop que ce serait le cas."

$ current_textbox = "anthrax"
anthrax "Ah oui ? Pourquoi donc ?"

$ current_textbox = "delaunay"
leandre "Oh, je ne sais pas trop. Je suis un peu plus discret que les autres, disons..."

$ current_textbox = "anthrax"
anthrax "Discret ? Ce n'est pas cette impression que tu m'as donné.e."

$ current_textbox = "delaunay"
show joy at joy_center
leandre "Vraiment ? Je suis soulagé alors !"
hide joy
leandre "Est-ce que tu souhaites qu'on discute autour d'un verre au bar ? J'aimerais beaucoup en apprendre plus sur ton drag."

label minichoice_del_1:
    $ quick_menu = False
   
    show leandre_neutre at del_right
    with fade
    menu:

        leandre "Et puis, ce sera plus simple aussi pour t’aider à construire ton acte lorsque Mother te donnera le feu vert."
        "Je te suis !":
            pass
        "J'adorerais !":
            pass
        "Ça, je ne dis pas non !":
            pass



#DEL.2
hide loges with dissolve
hide leandre_neutre with dissolve
scene black with fade
$ quick_menu = True
play music BarMusic fadein 1.5 volume 0.5
play ambiance BarDay fadein 0.5
play music BarMusic volume 0.5

$ current_textbox = "description" 
text "Nous sommes arrivé.e.s dans l'auditorium et nous sommes approché.e.s du comptoir derrière lequel brillaient un mur de bouteilles aux couleurs uniques."
text "Nous avions depuis le bar une vue imprenable sur la scène, légèrement en contrebas."
text "Les tablées y étaient déjà dressées et se regroupaient autour du big band et de l'estrade secondaire au centre de la pièce."
text "L'immense lustre duquel pendaient des larmes de verre reflétait les spots de lumière à la manière d'une boule à facettes sur le papier peint texturé."
text "Léandre s'assît sur l'une des chaises hautes de bois verni et commanda un Cosmo au barman."

show bar

$ current_textbox = "delaunay"

$ quick_menu = False
#show delaunay_neutre at del_right
show leandre_neutre at del_right
with fade
   
menu:
    #delaunay ""
    leandre "Est-ce que tu sais déjà quoi commander ?"
    "Un Pornstar Martini.":
     pass
    "Un Negroni Sbagliato, avec une pointe de prosecco.":
     pass
    "Une citronnade bien fraîche.":
     pass

$ quick_menu = True

leandre "Alors dis-moi, qu’est-ce qui t’amène ici ?"

$ current_textbox = "anthrax"
anthrax "M-Moi ? Comme ça ? Directement ?"

$ current_textbox = "delaunay"
# show leandre_shy at del right
leandre "Euh... Oui ? Enfin, ça me semblait être un bon début de conversation..."
#hide leandre_shy

$ current_textbox = "anthrax"
anthrax "Oh. Eh bien... J’ai commencé le drag dans le confort de mon appart, sur les réseaux sociaux. "
anthrax "Je n’ai jamais mis les pieds dans une troupe. Ou même un cabaret pour tout te dire."
anthrax "J'ai toujours été attiré.e par le burlesque, les plumes, le vintage, l'impétueux..."

$ current_textbox = "delaunay"
show joy at joy_right
#show leandre_laugh at del_right
leandre "Hm... C’est bien le genre de Mother de recruter quelqu’un de ton acabit. Plein.e de potentiel, mais ne sachant pas par où commencer."
hide joy
#hide leandre_laugh

$ quick_menu = False
   
show leandre_neutre at del_right
    
menu:
    leandre "J’étais exactement pareil..."
    "Ça fait longtemps que tu as intégré la troupe ?":
     pass
    "Depuis combien de temps est-ce que tu es là?":
     pass
    "Vous devez bien vous connaître, avec les autres...":
     pass

$ quick_menu = True





leandre "Environ cinq ans je dirais? Techniquement, je suis le doyen, parmi les autres que tu as croisé.e.s tout à l'heure."
leandre "Enfin, officiellement, Imani a travaillé ici depuis plus longtemps, mais n'a intégré la troupe qu'il y a seulement deux ans."
leandre "Et Aimé.e est arrivé.e peut-être un an après moi ?"
leandre "Techniquement, cela fait déjà des années que l’on se côtoie."
leandre "Quelques collègues sont parti.e.s, revenue.s, mais au final nous sommes les trois qui ayons tenu sur le long terme."

$ current_textbox = "anthrax"
anthrax "Et toi ? Qu’est-ce qui t’as lancé dans le drag ?"

$ current_textbox = "delaunay"
#show leandre_shy at del_right
leandre "Et bien... J’étais en train de décrocher des études, j’étais dans la panade financière, j’étais en pleine découverte de mon identité de genre."
#hide leandre_shy
leandre "Une vraie crise de la vingtaine... J'en ris maintenant, mais ce n'était pas du tout drôle à l'époque."

#Choix DEL.2
label choix_del2:
    $ quick_menu = False
    
    show joy at joy_right
    show leandre_neutre at del_right
    menu: 
        leandre "Et finalement, Mother m’a pris sous son aile et m’a aidé à me sortir de tout cela."
        "Oh! Tu as transitionné?":
            call del_2_1 from _call_del_2_1 
        "Et comment est-ce que tu as rencontré Mother?":
            call del_2_2 from _call_del_2_2 
        "J'ai remarqué qu'Aimé.e finissait beaucoup tes phrases...":
            call del_2_3 from _call_del_2_3 

          

#DEL.2.1
label del_2_1:
    $ quick_menu = True
    $ indice += 1
    hide joy
    show leandre_neutre at del_center
    with fade

    $ current_textbox = "anthrax"
    anthrax "Oh ! Tu as transitionné ?"  

    $ current_textbox = "delaunay"
    #show leandre_laugh at del_center
    leandre "Oui ! Ça ne se voit pas ?"
    #hide leandre_laugh

    $ current_textbox = "anthrax"
    anthrax "Ça dépend... Tu as un très bon passing. Mais ce n'est pas la première question que je me pose en rencontrant quelqu'un."
    
    $ current_textbox = "delaunay"
    leandre "C'est vrai que dit comme ça, ça a l'air plutôt normal. Je suis toujours persuadé que ça se lit sur mon front tellement ça fait partie de moi."
    #show leandre_shy at del_center
    leandre "J'ai tendance à oublier que ce n'est pas si commun que ça."
    #hide leandre_shy

    $ current_textbox = "anthrax"
    anthrax "J'ai aussi envie de dire que l'on est dans une troupe de drag. J'aurais dû m'y attendre un minimum..."


    $ quick_menu = False
    $ current_textbox = "delaunay"

    #show leandre_laugh at del_right
    show joy at joy_right
    show leandre_neutre at del_right with fade

    menu:
        leandre "Pas faux... Mais bon, nous sommes une troupe particulièrement hétéroclite. Blague à part!"
        "Ça n'a pas été trop dur? Enfin, si ce n'est pas indiscret.":
            pass
        "Comment as-tu réussi à t'en sortir?":
            pass
        "Ça a dû être une sacrée épreuve, tout de même...":
            pass

    hide joy

    $ quick_menu = True

    #show leandre_shy at del_right
    leandre "En toute honnêteté, c'était l'enfer. Mais j'ai eu la chance d'être bien entouré."
    #hide leandre_shy
    leandre "Et j'ai commencé le drag à peu près à cette période, donc c'était très utile pour m'aider à combattre la dysphorie de genre."
    $ current_textbox = "anthrax"

    anthrax "D'où le fait que tu fasses du drag king, je suppose."

    $ current_textbox = "delaunay"

    #show leandre_shy at del_right
    leandre "C'est exact..."
    #hide leandre shy
    leandre "Après, mon drag s'est \"re\"féminisé dernièrement."
    leandre "Après tout, ma masculinité n'est pas la même que celle des hommes cisgenres, et hétéros."


    $ quick_menu = False
   
    show flirt at flirt_right
    #show leandre_laugh at del_right
    show leandre_neutre at del_right
    
    menu:
        leandre "Et je tire une bonne partie de ma fierté queer, de ma transition."
        "Qu'est-ce que tu entends par là ?":
            pass
        "Je ne comprends pas...":
            pass
        "Peux-tu préciser? J'ai dû mal à saisir la nuance.":
            pass

    hide flirt
    $ quick_menu = True

    leandre "J'entends que si je devais renaître, je ne choisirais pas de le faire dans un corps d'homme cis..."
    leandre "Et que je me relancerais dans le même parcours de vie."
    #show leandre_shy at del_right
    show joy at joy_right
    leandre "Je n'échangerais pour rien au monde cette expérience."
    #hide leandre_shy
    hide joy
    leandre "D'avoir grandi comme j'ai grandi, d'avoir connu la sororité et les difficultés liées à la vie de femme ?"
    #show leandre_laugh at del_right
    show flirt at flirt_right
    leandre "Cette empathie, en tant qu'homme, m'est très précieuse."
    #hide leandre_laugh
    hide flirt

    stop music fadeout 1.0
    stop ambiance fadeout 1.0
    call del_3 from _call_del_3 

#DEL.2.2
label del_2_2:
    $ quick_menu = True
    $ indice -= 1
    hide joy
    show leandre_neutre at del_center
    with fade

    anthrax "Et comment est-ce que tu as rencontré Mother ?"

    #show leandre_shy at del_center
    leandre "C'est un peu bête, vraiment..."
    show sadness at sadness_center
    leandre "Je me suis fait traîner ici par des ami.e.s pour un spectacle, mais iels ont eu un empêchement de dernière minute."
    leandre "Du coup je me suis retrouvé tout seul... Comme les endroits avec beaucoup de monde et personne que je connais m'angoissent beaucoup, j'ai bu..."
    hide sadness
    #hide leandre_shy

    $ quick_menu = False
   
    show leandre_neutre at del_right
    menu:
        leandre "Mother m'a approché puisqu'elle s'inquiétait de mon état et on a fini par discuter pendant que je déssoûlais."
        "Ah oui... Une sacrée histoire finalement.":
            pass
        "C'était un peu des enfoirés, tes potes...":
            pass
        "C'est dommage que ça t'ai mis dans de tels états !":
            pass


    $ quick_menu = True
    
    
    leandre "Je n'étais pas très flambant... Ce n'est pas une période de ma vie dont je suis très fier."
    leandre "Ce soir-là, Mother m'a passé son contact et invité à repasser de temps en temps. Et comme je n'avais pas trop de repères, c'est là où je me suis ancré."

    anthrax "Et tu as fini par intégrer la troupe."

    #show leandre_shy at del_right
    leandre "E-Et bien... Ça ne s'est pas fait de suite évidemment... Mais ultimement, oui."
    #hide leandre_shy
    #show leandre_laugh at del_right
    leandre "C'était un peu informel, mais elle m'a fait visiter L'Androgame de fond en comble..."
    leandre "Et initié au drag en m'emmenant dans les coulisses avec les danseuses de semaine et racontant sa vie."
    #hide leandre_laugh
    show joy at joy_right
    leandre "Tout du long, elle soulignait qu'elle comptait monter une troupe secondaire, exclusivement queer."
    leandre "\"Une manière de rendre à la communauté\", qu'elle disait. Son plan était de réserver au moins un soir de grande affluence en semaine au drag."
    hide joy


    $ quick_menu = False
    
    show leandre_neutre at del_right
    menu:
        leandre "Pas besoin de préciser que ça a fonctionné bien plus qu'elle ne le pensait..."
        "La majorité des soirées sont réservées aux \"Paillettes\", c'est vrai.":
            pass
        "C'est comme ça que j'ai connu L'Androgame... Grâce à la commu":
            pass
        "C'est aussi pour cette raison que j'avais envie de venir.":
            pass

    $ quick_menu = True

    stop music fadeout 1.0
    stop ambiance fadeout 1.0
    call del_3 from _call_del_3_1 

#DEL.2.3
label del_2_3:
    $ quick_menu = True
    
    hide joy
    show leandre_neutre at del_center
    with fade

    $ current_textbox = "anthrax"
    anthrax "J'ai remarqué qu'Aimé.e finissait beaucoup tes phrases. Est-ce que tu es toujours aussi timide ?"

    $ current_textbox = "delaunay"
    #show leandre_shy at del_center
    show sadness at sadness_center
    leandre "Hm... La plupart du temps oui. Mais c'est quelque chose que j'essaye de travailler."
    leandre "J'ai toujours été assez réservé et discret. Je prends plutôt bien sa démarche puisque je ne réussis pas encore à aussi bien m'imposer qu'ellui."
    leandre "Je préfère ça à m'effacer dans le décor comme je le faisais avant..."
    hide sadness
    #hide leandre_shy
    leandre "Et iel est très compréhensif.ve lorsque je sens que je suis capable de m'exprimer et que j'en fais part."
    
    $ current_textbox = "anthrax"
    anthrax "C'est donc d'un commun accord..."

    $ current_textbox = "delaunay"
    #show leandre_laugh at del_center
    leandre "Tacite, oui. Mais qui nous convient et ressemble bien..."
    #hide leandre_laugh
    leandre "Ça ne l'empêche pas non plus de me taquiner et d'essayer de me faire sortir de mes gonds."
    

    $ quick_menu = False

    #show leandre_laugh at del_right
    show joy at joy_right
    show leandre_neutre at del_right
    menu:
        leandre "C'est challengeant, et ça a déjà marché. Même Imani s'est retrouvée assez surprise."
        "Il y a une raison derrière tout cela ?":
            pass
        "Vous semblez être de très bon.ne.s ami.e.s, mais pourquoi ?":
            pass
        "C'est le genre de chose que je ne supporterais pas...":
            pass

    hide joy

    $ quick_menu = True

    #show leandre_shy at del_right
    show sadness at sadness_right
    leandre "Je n'ai juste jamais eu une grande confiance en moi, et le regard des autres m'a toujours semblé particulièrement lourd à porter."
    leandre "Lorsqu'une situation était trop embarrassante, je choisissais toujours la fuite. Ou le déni, au choix."
    leandre "C'est devenu ma façon d'être, et les handicaps qui viennent avec."
    hide sadness
    #hide leandre_shy
    #show leandre_flirty at del_right
    leandre "C'est pour ça que le drag est particulièrement rassurant... L'espace d'un instant, je peux être entièrement quelqu'un d'autre."
    leandre "Quelqu'un de ma création, que je contrôle, qui me protège, derrière lequel je peux me cacher et extérioriser le fond de ma pensée."
    #hide leandre_flirty
    leandre "Il n'y a pas vraiment d'autre forme d'expression qui permet cela... Le théâtre peut-être ? Mais encore, le personnage y est déjà existant et incarné..."
    #show leandre_laugh
    leandre "Pas un reflet d'une personnalité que j'aimerais affirmer."
    #hide leandre_laugh

    $ current_textbox = "anthrax"
    anthrax "La nuance est fine, mais je crois comprendre ce que tu sous-entends..."

    stop music fadeout 1.0
    stop ambiance fadeout 1.0
    call del_3 from _call_del_3_2 

#DEL.3
label del_3:


    show curtain_close with dissolve
    hide leandre_neutre with dissolve
    hide bar with dissolve
    hide loges
    pause 1.5
    show curtain_open with dissolve
    scene black with dissolve

    #show gradient
    text "Quelques mois passèrent..."
    #hide gradient with dissolve

    play music ConfidenceIntro

    $ current_textbox = "description"
    text "Cela faisait plusieurs minutes que je cherchais Léandre, avec qui j'étais supposé.e répéter une partie de mon numéro, que l'on construisait ensemble."
    text "Après avoir fait trois fois le tour du bâtiment, je finis par retourner sur les planches de la scène, pensif.ve."
    text "Et en toute honnêteté, un peu inquiet.e."

    queue music ConfidenceA1

    text "C'est alors que j'aperçu une tignasse blonde depuis le haut du balcon, absorbée par le contenu de son téléphone."
    text "N'ayant pas pensé à lever le regard, je grimpai l'escalier en colimaçon pour le rejoindre, à tâtons."


    show auditorium
    

    $ quick_menu = False
    
    show sadness at sadness_right
    show leandre_neutre at del_right
    with fade
    menu:
        
        "Hey... Je me demandais où tu étais passé.":
            pass
        "Léandre! Ça fait un moment que je te cherche!":
            pass
        "Alors c'était là où tu te cachais...~":
            pass

    $ quick_menu = True
    hide sadness
    hide leandre_neutre with dissolve
    #show leandre_nosmile at del_center with dissolve
    show leandre_neutre at del_center with dissolve
    $ current_textbox = "delaunay"


    leandre "Oh !"
    
    leandre "Pardon, je n'ai pas vu l'heure tourner."
    
    $ current_textbox = "anthrax"
    anthrax "Est-ce que tout va bien ? Tu as l'air soucieux."
    
    #show leandre_laugh at del_center
    show sadness at sadness_center
    $ current_textbox = "delaunay"
    leandre "Hm... C'est rien. Juste un ancien client qui essaye de reprendre contact. C'est un peu relou."
 
    $ current_textbox = "anthrax"
    anthrax "Un ancien client ?"

    $ current_textbox = "delaunay"
    leandre "Hm..."
    hide sadness

    queue music ConfidenceA2

    $ current_textbox = "description"
    text "Visiblement pas très à l'aise, Léandre rangea son mobile et joua avec ses doigts, venant s'appuyer sur la rambarde pour observer la scène en contrebas."
    
    #show leandre_shy at del_center
    $ current_textbox = "delaunay"
    leandre "C'est vrai que je ne t'en ai pas encore parlé..."


    $ quick_menu = False
   
    #show leandre_shy at del_right with dissolve
    show leandre_neutre at del_right with dissolve
    menu:
        leandre "Les autres sont au courant, mais j'aurais peut-être dû te mettre dans la boucle plus tôt."
        "Oh...  C'est grave ?":
            pass
        "Ta tête ne me dit rien qui vaille... Qu'est-ce qu'il y a ?":
            pass
        "Est-ce que tu veux m'en parler seulement ?":
            pass

    $ quick_menu = True

    leandre "Hm... C'est une passe de ma vie dont je ne suis pas très fier. Pour changer..."
    leandre "Mais ça ne me dérange plus tellement d'en parler, donc bon..."

    $ current_textbox = "anthrax"
    anthrax "Seulement si tu te sens de l'aborder alors."

    $ current_textbox = "delaunay"
    #show leandre_laugh at del_right
    show joy at joy_right
    leandre "Ne t'en fais pas, je n'aurais pas commencé à en parler si je ne le sentais pas."
    hide joy
    # hide leandre_laugh 
    leandre "Mais je te fais suffisamment confiance pour ne pas me juger sur mes décisions."

    $ current_textbox = "description"
    text "Un peu plus confiant, il se redressa et tourna la tête dans ma direction, un sourire apaisé aux lèvres."

    #show leandre_nosmile at del_right
    $ current_textbox = "delaunay"
    leandre "À un moment, j'ai fait des vidéos à caractère..."
    leandre "Disons les termes, à caractère sexuel."
    leandre "Pour de l'argent."
    #hide leandre_nosmile

#Dialogue WIP 

#Choix DEL.3
label choix_del3:
    $ quick_menu = False
    
    show sadness at sadness_right
    #show leandre_shy at del right
    show leandre_neutre at del_right
    
    menu: 
        leandre "D'où \"l'ancien client\"..."
        "Tu avais tes raisons pour te lancer... dans cette industrie ?":
            call del_3_1 from _call_del_3_1_1 
        "Pourquoi est-ce que tu n'es pas très fier de cette période?":
            call del_3_2 from _call_del_3_2_1 
        "Pour de l'argent? Tu étais en difficulté?":
            call del_3_3 from _call_del_3_3 

#DEL.3.1
label del_3_1:
    $ quick_menu = True
    
    hide sadness
    show leandre_neutre at del_center
    with fade

    $ current_textbox = "anthrax"
    anthrax "Tu avais tes raisons pour te lancer... dans cette industrie ?"

    $ current_textbox = "delaunay"

    leandre "Sûrement... On peut dire ça."
    leandre "C'était un moment dans ma vie où j'étais assez perdu."
    #show leandre_shy at del_center
    leandre "Il y a eu tellement de changements en si peu de temps que je ne savais plus du tout où me positionner."
    #hide leandre_shy
    
    $ quick_menu = False
   
    show leandre_neutre at del_right
    menu:
        leandre "Par rapport aux autres et par rapport à moi-même..."
        "C'est-à-dire...?":
            pass
        "Qu'est-ce que tu entends par là ?":
            pass
        "Pourquoi alors ?":
            pass

    $ quick_menu = True
    
    #show leandre_laugh at del_right
    leandre "Je ne sais pas... J'ai toujours eu un rapport à l'intime complètement frit."
    leandre "Hormonalement parlant, c'était la fiesta. Je commençais tout juste la testo et ma libido était en roue libre."
    #hide leandre_laugh
    leandre "Bon, après, ça ne m'a jamais empêché d'être décent avec mes partenaires, mais tout de même..."
    leandre "Et c'était la première fois de ma vie que j'apprenais à apprécier mon corps pour ce qu'il était. "
    #show leandre_laugh at del_right
    show sadness at sadness_right
    leandre "C'était une liberté nouvelle, et je ne savais pas ce que je faisais."
    #hide leandre_laugh
    hide sadness


    $ quick_menu = False
   
    show leandre_neutre at del_right
    menu:
        leandre "J'étais jeune aussi, et c'était peut-être trop de bonheur d'un coup, pour quelqu'un d'encore blessé et immature."
        "Après, c'est quelque chose de facilement compréhensible. Tu te cherchais...":
            pass
        "Ce n'est pas simple de se trouver !":
            pass
        "Il y a des hauts et des bas, c'est normal...":
            pass


    $ quick_menu = True

    #show leandre_laugh at del_right
    show angry at angry_right
    leandre "Je me suis surtout senti pousser des ailes."
    #hide leandre_laugh
    hide angry
    leandre "Dans cette quête, je me suis hypersexualisé, et au final ça m'a plus joué des tours qu'autre chose."
    leandre "J'avais aussi besoin d'argent pour payer ma mammec', et je m'en sentais les épaules. Maintenant, je me retrouve avec du contenu intime qui se promène dans la nature..."
    #show leandre_shy at del_right
    leandre "J'ai fini par l'accepter : j'ai fait des erreurs et pris de mauvaises décisions."
    #hide leandre_shy


    $ quick_menu = False
   
    #show leandre_laugh at del_right
    show leandre_neutre at del_right
    menu:
        leandre "Maintenant, le \"moi\" adulte vit avec."

        "Si tu réussis à te réconcilier avec ton passé, c'est le principal non ?":
            pass
        "Ça doit être rassurant, d'avoir au moins ça de clair.":
            pass
        "Après tout, ça ne concerne que toi, et toi-même !":
            pass

    $ quick_menu = True

    leandre "Oui, je suis de cet avis. Et puis tout le monde a des regrets, je ne suis pas le seul."
    show sadness at sadness_right
    leandre "J'aurais peut-être juste espéré que Delaunay débarque un peu plus tôt dans ma vie."
    hide sadness
    leandre "Il m'aurait sûrement évité quelques bêtises et aiguillé comme il le fait aujourd'hui."


    $ current_textbox = "anthrax"
    anthrax "Ta persona drag ? Je ne savais pas que tu l'adressais comme si c'était quelqu'un d'autre."

    $ current_textbox = "delaunay"
    leandre "C'est un peu plus simple de complètement le dissocier de ma personne."
    show flirt at flirt_right
    #show leandre_laugh at del_right
    leandre "C'est un peu mon ange gardien finalement, qui m'incite à prendre exemple sur lui et être une meilleure version de moi-même."
    #hide leandre_laugh
    hide flirt
    leandre "Mais tout le monde ne fait pas pareil et chacun.e a sa manière d'aborder son drag après tout."

    call del_4 from _call_del_4 

#DEL.3.2
label del_3_2:
    $ quick_menu = True
    $ indice -= 1

    queue music ConfidenceAB
    queue music ConfidenceB1
    hide sadness
    show leandre_neutre at del_center
    with fade

    $ current_textbox = "anthrax"
    anthrax "Pourquoi est-ce que tu n'es pas très fier de cette période ?"

    $ current_textbox = "delaunay"
    leandre "Oh, eh bien, ça me semble plutôt logique..."
    #show leandre_laugh at del_center
    show sadness at sadness_center
    leandre "Avoir fait du porno, c'est pas très mirobolant sur un CV."
    hide sadness
    #hide leandre_laugh
    leandre "Mais Mother n'est pas très regardante sur ce point, donc je n'ai pas eu plus de soucis que ça."
    #show leandre_shy at del_center
    leandre "C'est plus gênant si quelqu'un tombe dessus et m'y reconnaît, mais comme j'ai énormément changé entre-temps, je ne m'en inquiète pas plus que ça."
    #hide leandre_shy

    $ quick_menu = False
   
    show leandre_neutre at del_right
    menu:
        leandre "Puis, comme j'assume un minimum, ce n'est pas comme si ces personnes pouvaient retourner ça contre moi. Et sinon, j'ai toujours l'option de nier."
        "Après tout, ça ne concerne que toi.":
            pass
        "Dans tous les cas, il n'y a rien de honteux à avoir fait ce métier...":
            pass
        "Et puis, même si on te reconnait, ça nous fera de la pub !":
            pass


    $ quick_menu = True

    #show leandre_laugh at del_right
    leandre "Exact !"
    #hide leandre_laugh

    $ current_textbox = "anthrax"
    anthrax "Si tu réussis à tirer quelque chose de positif de cette expérience, c'est le principal."

    $ current_textbox = "delaunay"
    show sadness at sadness_right
    leandre "Hm... Oui, après tout, ça m'a aidé à réaliser que ce n'était pas à travers le regard des autres que j'allais apprendre à m'aimer."
    leandre "J'étais persuadé à l'époque que si les gens m'appréciaient pour quelque chose, le reste allait suivre de l'autre côté."
    hide sadness
    leandre "Alors que ça aurait dû être l'inverse..."

    queue music ConfidenceB2
    #show leandre_shy at del_right
    leandre "M'aimer d'abord, découvrir mon intimité ensuite... Ou en même temps, à la rigueur."
    #hide leandre_shy

    $ quick_menu = False
   
    show leandre_neutre at del_right
    menu:
        leandre "Enfin bref, c'était pas du tout la méthode adaptée pour nourrir mon \"appréciation de soi\"."
        "Comment est-ce que tu as réussi à t'en sortir du coup ?":
            pass
        "Et L'Androgame a été ta porte de sortie.":
            pass
        "C'est dingue que tu te sois libéré de tout ça, tout seul.":
            pass


    $ quick_menu = True


    leandre "Franchement? Je dois énormément à Mother... J'étais prêt à me raccrocher à n'importe quoi, et elle m'a tendu la main."
    leandre "Je m'étais lancé dans les vidéos pour payer mon opération mais Mother m'a proposé un travail à mi-temps..."
    leandre "Puis elle m'a présenté à ses ami.e.s drag artists lorsque j'ai soulevé l'idée que ça pouvait m'aider avec ma dysphorie de genre."

    queue music ConfidenceOutro
    
    #show leandre_laugh at del_right
    show joy at joy_right
    leandre "Grâce à ça, j'ai pu arrêter et reprendre ma vie en main."
    #hide leandre_laugh
    hide joy
    leandre "Je t'en avais déjà parlé, non ? Je ne me souviens plus... Ce serait bête que je passe pour un disque rayé !"
    
    $ current_textbox = "anthrax"
    anthrax "Mais non ! Et puis, même si tu te répétais, ça m'est égal. Ça veut dire que tu me fais toujours confiance pour m'en parler !"

    call del_4 from _call_del_4_1 

#DEL.3.3
label del_3_3:
    $ quick_menu = True
    $ indice += 1
    
    hide sadness
    show leandre_neutre at del_center
    with fade
    $ current_textbox = "anthrax"
    anthrax "Pour de l'argent ? Tu étais à ce point en difficulté ?"

    $ current_textbox = "delaunay"
    show sadness at sadness_center
    leandre "Plus ou moins... Avec mon parcours de transition plutôt chaotique, je n'ai pas pu passer par le circuit \"public\", avec les aides médicales qui vont avec."
    leandre "Pour avoir accès à ça, il faut avoir eu un suivi psychiatrique d'au moins deux ans."
    hide sadness
    #show leandre_laugh at del_right 
    leandre "Mais comme je m'en suis rendu compte tardivement, je n'ai pas eu ce luxe."
    #hide leandre_laugh
    leandre "Et j'étais tellement dans le mal, psychologiquement parlant, que je n'avais pas la patience non plus d'entamer ce parcours."
    leandre "Heureusement, je suis tombé sur une endocrinologue top, qui m'a permit d'accéder à un traitement hormonal."

    $ quick_menu = False
   
    show leandre_neutre at del_right
    menu:
        leandre "Et ma psy, bien qu'elle ne soit pas psychiatre, a été d'un grand soutien."
        "Ça m'a l'air d'être des démarches super compliquées...":
            pass
        "Quel enfer...":
            pass
        "Ça a dû être terriblement long...":
            pass

    $ quick_menu = True
    
    show joy at joy_right
    #show leandre_laugh at del_right
    leandre "Oh, crois-moi que je suis rodé en tout ce qui concerne les démarches administratives et suivis médicaux..."
    hide joy
    #hide leandre_laugh
    #show leandre_shy
    leandre "Même si je suis toujours aussi terrifié à l'idée de passer un appel téléphonique pour prendre un rendez-vous..."
    #hide leandre_shy
    leandre "Dans l'idée, dans le meilleur des mondes, j'aurais dû m'en rendre compte lorsque j'étais jeune et innocent pour qu'on me prenne au sérieux."
    leandre "Et pas à dix-neuf ans, déjà majeur, comme ça s'est passé..."
    leandre "C'est fou à quel point on te laisse tomber à ta majorité par rapport à tout ce qui est médical..."
    #show leandre_shy
    leandre "Comme si c'était inné, qu'on devait tout savoir, ou que c'était une évidence de connaître la marche à suivre."
    #hide leandre_shy
    leandre "Alors, internet est ton meilleur ami, mais ensuite on te reproche d'avoir été influencé par ça"
    leandre "Et de ne pas savoir ce que tu veux finalement..."
    show sadness at sadness_right
    leandre "Parce qu'en plus de ta déprime, c'est apparemment absolument nécessaire de t'achever en te décrédibilisant."
    

    $ quick_menu = False
   
    show leandre_neutre at del_right
    menu:
        leandre "Enfin bref..."
        "Les circonstances ont fait que tu as dû payer de ta poche...":
            pass
        "Ça devait être un beau billet pour te mettre autant dans la panade...":
            pass
        "Tu as fait tes choix.":
            pass


    $ quick_menu = True 

    hide sadness
    #show leandre_laugh at del_right
    leandre "En effet... Et ça ne sort pas d'un chapeau magique, quelques milliers d'euros. Donc j'ai fait avec ce que j'avais, c'est-à-dire, pas grand-chose..."
    leandre "J'étais tellement au fond du trou et au pire de ma dépression que ça me semblait être la seule issue."
    #show leandre_shy at del_right
    leandre "Si je n'agissais pas, j'allais me laisser manger par les idées noires et..."
    #hide leandre_shy
    leandre "Je ne vais pas faire un dessin, je suppose que tu connais les statistiques..."

    $ current_textbox = "anthrax"
    anthrax "Malheureusement oui. Je connais au moins une personne trans dans mon entourage qui s'est suicidée... Et d'autres qui l'ont au moins envisagé."
    
    $ current_textbox = "delaunay"
    leandre "Ce n'est pas très joyeux comme discussion..."

    $ current_textbox = "anthrax"
    anthrax "C'est clair... Mais c'est la triste réalité..."

    show flirt at flirt_right
    $ current_textbox = "delaunay"
    #show leandre_flirty at del_right
    leandre "Je suis tout de même heureux de l'avoir partagé avec toi..."
    #hide leandre_flirty
    hide flirt

    call del_4 from _call_del_4_2 

#DEL.4
# TRANSITION RIDEAU DE SES MORTS A AJOUTER
# text "Le jour du spectacle..."
label del_4:
    hide delaunay_neutre with dissolve
    show curtain_close with dissolve
    pause 1.5
    hide bar
    hide loges
    scene black
    show curtain_open with dissolve
    with fade

    text "Le jour du spectacle..."

    stop music fadeout 0.5
    stop ambiance fadeout 0.5
    play music BackstageLoop volume 0.5
    play ambiance AmbLoges fadein 0.5

    $ current_textbox = "description"
    text "Au sein de la loge, une certaine tension planait au-dessus de la playlist qui tournait. Pas une mauvaise ambiance, non, plutôt une intense concentration."
    text "Évidemment, tout le monde chit-chattait gaîment, mais je ne pus m'empêcher de fixer un instant Léandre."
    text "Agenouillé devant un miroir sur pied, déjà maquillé, à moitié habillé de son corset à sequins rouge Louboutin, et ses lunettes glissant maladroitement de son nez..."
    text "Il collait précautionneusement des strass dorés sur la peau rugueuse des cicatrices de son torse."
    text "Tel un papillon se dégageant de son cocon, Delaunay sortait de la peau de Léandre."
    text "Son dos se courba, son regard s'embrasa et il me remarqua le fixer. Un sourire coquin et un clin d’œil plus tard, il m'invitait à le rejoindre."
    

#Choix DEL.4
label choix_del4:
    $ quick_menu = False
    show loges
    $ current_textbox = "delaunay"
    #show delaunay_flirty at del_right
    show delaunay_neutre at del_right
    with fade
    menu: 
        delaunay "Qu'est-ce que tu fais à jouer le timide ? Approche, je ne vais pas te manger~"
        "Franchement, tu me manges quand tu veux !":
            call del_4_1 from _call_del_4_1_1 
        "J'adore la manière dont tu prends confiance avec Delaunay":
            call del_4_2 from _call_del_4_2_1 
        "Timide? Moi?":
            call del_4_3 from _call_del_4_3 

    $ current_textbox = "anthrax"

#DEL.4.1
label del_4_1:
    $ quick_menu = True
    #show delaunay_flirty at del_right
    show delaunay_neutre at del_center
    with fade

    $ current_textbox = "anthrax"
    anthrax "Franchement, tu me manges quand tu veux...~"

    show flirt at flirt_center
    $ current_textbox = "delaunay"
    delaunay "Eh bien ! On dirait que je commence à déteindre sur toi~"
    hide flirt

    $ current_textbox = "anthrax"
    anthrax "Ce n'était pas le but peut-être ?"

    $ current_textbox = "delaunay"
    #show delaunay_laugh at del_right
    delaunay "Seulement si tu en as réellement envie. Je ne veux pas te forcer à faire du burlesque ou à devenir une pimbèche de service..."
    #hide delaunay_laugh
    delaunay "Bien que je tienne ce titre en très haute estime ~."
    hide delaunay_neutre with dissolve

    $ current_textbox = "gatsby"
    #show gatsby_laugh at gat_left
    show gatsby_neutre at gat_left with dissolve
    gatsby "Et ça va être difficile de la battre, cette pimbèche là."

    $ current_textbox = "peacock"
    #show peacock_laugh at pea_right
    show peacock_neutre at pea_right with dissolve
    peacock "Oh, je suis certaine qu'il y a de la place pour deux perruches dans cette troupe, après tout, regarde-nous."
    peacock "Mais bon quand il s'agit de bomber le torse et de faire du pied, il n'y a qu'une personne qui nous vienne à l'esprit."
   
    $ current_textbox = "delaunay"
    #show delaunay_shy at del_center
    show delaunay_neutre at del_center with dissolve
    delaunay "Oh ! Mais occupez-vous de vos fesses, oui ! Je vais rougir..."

    $ quick_menu = False

    #hide gatsby_laugh
    #hide peacock_laugh
    hide gatsby_neutre
    hide peacock_neutre
    #show delaunay_flirty at del_right
    show delaunay_neutre at del_right with fade
    menu:
        delaunay "Je reviens de loin, je peux bien m'octroyer un peu de crédit."

        "Il doit me manquer du contexte, je ne comprends pas...":
            pass
        "Par pitié, racontez-moi!":
            pass
        "Des explications, au hasard?":
            pass


    $ quick_menu = True
    
    delaunay "Oh, c'est vrai. Comment est-ce que je pourrais le formuler... ?"
    #show delaunay_shy at del_right
    delaunay "J'ai toujours eu un peu de mal à me trouver désirable. Ou en tout cas d'être confiant dans mon intimité, ma sensualité, ma sexualité..."
    #hide delaunay_shy
    delaunay "Alors Delaunay l'est à ma place, et m'aide à explorer cette facette de ma personne que je cherche à redécouvrir."
    show sadness at sadness_right
    delaunay "Puisque ça a été un échec cuisant lors de ma première tentative, à travers les vidéos..."
    hide sadness

    $ current_textbox = "gatsby"
    #show gatsby_pensive at gat_left
    show gatsby_neutre at gat_left with dissolve
    gatsby "Après, quand tu faisais tes vidéos, tu avais aussi d'autres circonstances qui ont fait que ta démarche n'était pas vraiment saine."
    hide delaunay_neutre with dissolve

    $ current_textbox = "peacock"
    #show peacock_emo at pea_right
    show peacock_neutre at pea_right with dissolve
    peacock "...Toi et ton tact légendaire."
    peacock "En soi, je suis plutôt d'accord avec Aimé.e, mais je ne l'aurais pas dit dans ces termes. Tu avais des besoins et tu te cherchais encore..."
    hide gatsby_neutre

    $ current_textbox = "delaunay"
    show delaunay_neutre at del_left with dissolve
    delaunay "Je sais. J'ai fait un choix et ce n'était pas le bon. Mais au final, ça m'a tout de même amené ici aujourd'hui. Donc je n'ai pas tant de regrets que ça."
    hide peacock_neutre with dissolve
    #show delaunay_laugh at del_left
    show joy at joy_left
    delaunay "Et je découvre la bad bitch que j'ai toujours rêvé d'être."
    hide joy
    #hide delaunay_laugh

    $ quick_menu = False
   
    show delaunay_neutre at del_right with fade
    menu:
        delaunay "Tout est bien qui finit bien. Carpe diem, blablabla."
        "Excellente philosophie !":
            pass
        "Aw...~":
            pass
        "C'est adorable.":
            pass

    $ quick_menu = True

   
    stop music fadeout 0.1

    hide delaunay_neutre
    $ current_textbox = "mother"
    staff "Ok les filles ! Showtime dans dix minutes !"
    show delaunay_neutre at del_center with dissolve
    
    $ current_textbox = "delaunay"
    show joy at joy_center
    #show delaunay_flirty at del_center
    delaunay "Mon dieu, j'ai encore tellement à faire ! Vite [player_name] ! Un coup de main, vite !~"
    #hide delaunay_flirty
    hide flirt

    stop ambiance fadeout 2.0
    call del_5 from _call_del_5 

#DEL.4.2
label del_4_2:
    $ quick_menu = True
    $ indice += 1
    
    show delaunay_neutre at del_center
    with fade

    $ current_textbox = "anthrax"
    anthrax "J'adore la manière dont tu prends confiance avec Delaunay"
    anthrax "Qu'est-ce qui change quand tu te costumes ?"
    
    $ current_textbox = "delaunay"
    #show delaunay_laugh at del_center
    delaunay "Tout."
    #hide delaunay_laugh
    show joy at joy_center
    delaunay "Léandre n'existe pas quand je suis en drag, c'est libérateur."
    hide joy
  

    $ quick_menu = False
   
    show delaunay_neutre at del_right
    with fade
    menu:
        anthrax "Vraiment ? J'aurais pensé le contraire. Je ne savais pas que ta relation avec toi-même était si..."
        "Conflictuelle.":
            pass
        "Antagoniste.":
            pass
        "Bizarre.":
            pass

    $ quick_menu = True

    delaunay "Hm...c'est le bon mot."
    #show delaunay_laugh at del_right
    show flirt at flirt_right
    delaunay "Mais détrompe-toi... J'adore Léandre."
    hide flirt
    #hide delaunay_laugh 
    delaunay "Enfin, je m'aime bien."
    #show delaunay_flirty at del_right
    delaunay "Quand j'ai imaginé Delaunay, je l'ai créé comme étant tout ce que je désirais être. Confiant, têtu, un peu salope sur les bords..."
    #hide delaunay_flirty

    $ current_textbox = "anthrax"
    anthrax "Et c'est quelque chose que tu n'arrives pas à faire... en tant que Léandre ?"
    
    $ current_textbox = "delaunay"
    #show delaunay_shy at del_right
    delaunay "Hm... Oui. Mais c'est pas comme si je n'essayais pas. Comment dire..."
    #hide delaunay_laugh
    show sadness at sadness_right
    delaunay "En fait, je suis passé par tellement de changements et je me recherche tellement encore..."
    hide sadness
    delaunay "Que je n'ai pas de vrai repère auquel me raccrocher en termes de confiance en soi et de personnalité."

    $ quick_menu = False

    #show delaunay_laugh at del_right
    show delaunay_neutre at del_right
    menu:
        delaunay "Alors... Delaunay, c'est un peu mon phare dans cet océan de confusion. Et Léandre, il essaye de naviguer un peu à travers tout ça."
        "C'est valide d'être un peu perdu dans la vie.":
            pass
        "Tant que tu ne navigues plus à l'aveugle, c'est l'essentiel.":
            pass
        "Sans Delaunay, ce serait donc encore la tempête...":
            pass

    $ quick_menu = True

    show joy at joy_right
    delaunay "Je sais... Et ça commence à se stabiliser, bien heureusement."
    hide joy
    #hide delaunay_laugh
    delaunay "J'aimerais juste des fois que ça aille un peu plus vite."

    $ current_textbox = "gatsby"
    #show gatsby_pensive at gat_left
    show gatsby_neutre at gat_left with dissolve
    gatsby "C'est le genre de chose qui prend du temps après tout."
    hide delaunay_neutre with dissolve

    $ current_textbox = "peacock"
    #show peacock_sassy at pea_right
    show peacock_neutre at pea_right with dissolve
    peacock "Et puis, tu as déjà fait de nombreux progrès. Je me souviens quand t'avais commencé avec une version masculinisée un peu foireuse de Betty Boop..."
    
    #show gatsby_laugh at gat_left
    $ current_textbox = "gatsby"
    gatsby "Mon dieu, c'est vrai que ça a existé ça."

    $ quick_menu = False
    
    #hide gatsby_pensive
    #hide gatsby_laugh
    #hide peacock_sassy
    hide gatsby_neutre
    hide peacock_neutre
    $ current_textbox = "delaunay"

    #show delaunay_shy at del_right
    show delaunay_neutre at del_right
    menu:
        delaunay "Épargnez-moi, c'est toujours le monstre de ma paralysie du sommeil."
        "Dire que j'ai loupé ça, quelle tragédie...":
            pass
        "Dites-moi que vous avez des archives.":
            pass
        "J'ai un besoin vital de voir ça maintenant. ":
            pass

    $ quick_menu = True

    delaunay "Elles ont été diligemment supprimées."
    
    $ current_textbox = "gatsby"
    #show gatsby_laugh at gat_left
    show gatsby_neutre at gat_left with dissolve
    gatsby "Oh... Je suis sûr.e qu'il doit m'en rester..."
   
    $ current_textbox = "delaunay"
    #show delaunay_shy at del_right
    show angry at angry_right
    delaunay "Tu n'as pas osé!?"
    hide angry
    #hide delaunay_shy

    $ current_textbox = "peacock"
    #hide gatsby_laugh with dissolve 
    hide gatsby_neutre with dissolve

    #show peacock_laugh at pea_left with dissolve
    show peacock_neutre at pea_left with dissolve
    peacock "Je suis si peu surprise. C'était mythique!"
    hide peacock_neutre with dissolve
    #hide peacock_lauch

    stop music fadeout 0.1

    hide delaunay_neutre
    $ current_textbox = "mother"
    staff "Ok les filles ! Showtime dans dix minutes !"
    show delaunay_neutre at del_center with dissolve

    $ current_textbox = "delaunay"
    show flirt at flirt_center
    #show delaunay_flirty at del_center with dissolve
    delaunay "Mon dieu, j'ai encore tellement à faire ! Vite [player_name] ! Un coup de main, vite !"
    hide flirt
    #hide delaunay_flirt

    stop ambiance fadeout 2.0
    call del_5 from _call_del_5_1 

#DEL.4.3
label del_4_3:
    $ quick_menu = True
    $ indice -= 1

    show delaunay_neutre at del_center
    with fade

    $ current_textbox = "anthrax"
    anthrax "\"Timide\" ? Moi ?"

    $ current_textbox = "delaunay"
    #show delaunay_shy at del_center
    delaunay "Oui, bon ok. C'est un peu l'hôpital qui se fout de la charité."
    #hide delaunay_shy

    $ current_textbox = "anthrax"
    anthrax "J'aurais bien dit que tu as raison... Mais bizarrement, tu m'as l'air plus confiant là."
    
    $ current_textbox = "delaunay"
    show joy at joy_center
    delaunay "Ah ça, c'est l'effet \"Delaunay\" !"
    hide joy

    $ quick_menu = False
   
    show delaunay_neutre at del_right
    menu:
        delaunay "Il m'a toujours aidé à devenir l'homme que je voulais être, encore maintenant..."
        "Pourtant, ton personnage m'a l'air d'être très effeminé, aussi maladroit que ça puisse être dit comme ça.":
            pass
        "Ton personnage est aussi très féminin pour un \"drag king\"":
            pass
        "Bousculer les normes du genre, c'est le principe du drag, après tout !":
            pass

    $ quick_menu = True

    #show delaunay_laugh at del_right
    delaunay "Tu n'as pas tort. Mais il n'a pas toujours été comme ça... Au contraire, au début, il était très masculin."
    #hide delaunay_laugh
    delaunay "Après coup, j'ai réalisé que comme c'était au début de ma transition, j'essayais peut-être de me recréer un \"idéal\"... "
    delaunay "Qui était finalement très stéréotypé."

    $ current_textbox = "anthrax"
    anthrax "Je ne l'aurais jamais imaginé... Genre avec une fausse barbe et tout ?"

    $ current_textbox = "delaunay"
    #show delaunay_laugh at del_right
    delaunay "Surtout pas ! Une moustache, très chèr.e ! J'ai quand même un peu de goût..."
    #hide delaunay_laugh


    $ current_textbox = "peacock"
    #show peacock_sassy at pea_left with dissolve
    show angry at angry_left
    show peacock_neutre at pea_left with dissolve
    peacock "Tu as quelque chose contre les barbes ma belle ?"
    hide angry
    #hide peacock_sassy

    $ current_textbox = "delaunay"
    #show delaunay_flirty at del_right
    delaunay "Non ! Du tout ! La tienne te sied très bien... Malgré les trous~"
    #hide delaunay_flirty

    $ current_textbox = "peacock"
    #show peacock_laugh at pea_left with dissolve
    peacock "Hm... C'est vrai que la testo ne t'a pas trop épargné là-dessus... Une absence de barbe, des poils aux fesses et un début de calvitie..."
    #hide peacock_lauch
    hide delaunay_neutre with dissolve

    $ current_textbox = "gatsby"
    #show gatsby_laugh at gat_right with dissolve
    show gatsby_neutre at gat_right with dissolve
    gatsby "BAHAHA !"

    $ current_textbox = "anthrax"
    anthrax "Shady."

    hide peacock_neutre
    hide gatsby_neutre
    $ quick_menu = False
    $ current_textbox = "delaunay"
    show angry at angry_right
    show delaunay_neutre at del_right
    menu:
        delaunay "Je suis outré !"

        "Hm... Tu as commencé.":
            pass
        "C'est l'arroseur arrosé...":
            pass
        "The shade! The shade of it all !":
            pass

    $ quick_menu = True

    $ current_textbox = "delaunay"
    delaunay "Anyway."
    hide angry
    delaunay "J'ai quand même pas mal rétropédalé au niveau de l'hypermasculinisation de mon perso, quand mon corps a commencé à changer."
    delaunay "Je me suis réconcilié avec moi-même, et donc Delaunay n'avait plus besoin de servir cette fonction."
    #show delaunay_flirty at del_right
    delaunay "Et comme j'avais envie de redécouvrir ma part de féminité en tant qu'homme, nous y voilà."
    # hide delaunay_flirty

    $ current_textbox = "anthrax"
    anthrax "C'est une relation très personnelle et intime que tu as avec ton personnage finalement..."
    anthrax "je comprends mieux pourquoi tu t'adresses à \"Léandre\" à la troisième personne parfois, quand tu es en drag."
    
    $ current_textbox = "delaunay"
    #show delaunay_laugh at del_right
    show joy at joy_right
    delaunay "Oh, ça... C'est un autre débat. C'est plus mon côté égocentrique que j'essaye de travailler. Faut pas hésiter à me rappeler l'humilité..."
    # hide delaunay_laugh
    hide joy
  
    $ current_textbox = "anthrax"
    anthrax "Si ça peut te rassurer, on remarque à peine ta calvitie."


    $ quick_menu = False

    $ current_textbox = "delaunay"
    show delaunay_neutre at del_right
    show sadness at sadness_right
    menu:
        delaunay "Par pitié, pas toi aussi..."
        "Désolé.e, c'était trop tentant !":
            pass
        "Sorry, not sorry !":
            pass
        "Roh~ T'es adorable quand tu boudes !":
            pass

    $ quick_menu = True

    hide sadness

    stop music fadeout 0.1

    hide delaunay_neutre
    $ current_textbox = "mother"
    staff "Ok les filles ! Showtime dans dix minutes !"
    show delaunay_neutre at del_center with dissolve

    $ current_textbox = "delaunay"
    show joy at joy_center
    #show delaunay_flirty at del_right
    delaunay "Mon dieu, j'ai encore tellement à faire ! Vite [player_name] ! Un coup de main, vite !~"
    #hide delaunay_flirty

    stop ambiance fadeout 2.0

    call del_5 from _call_del_5_2 
    hide joy
#DEL.5
label del_5:
# TRANSITION RIDEAU
    hide joy
    hide delaunay_neutre with dissolve
    show curtain_close with dissolve
    pause 1.5
    hide bar
    hide loges with dissolve
    pause 1.5
    show curtain_open with dissolve
    with fade

    scene black with dissolve
    play music ShowDelaunay noloop
    

    $ current_textbox = "description"
    text "L’entracte arrivait déjà à sa fin et l’atmosphère était bouillonnante dans les coulisses. "
    text "Derrière le rideau, les kittens et les régisseur.euse.s s’activaient à déplacer le décor en silence." 
    show auditorium with dissolve
    text "Soudainement, un spot se braqua sur le velours et un \"bang\" de trompettes réveilla la foule."
    text "Puis une longue jambe dévoila sensuellement sa résille en sortant de l’entrouverture."
    show delaunay_neutre at del_center with dissolve
    text "Au rythme de la musique, Delaunay fit son apparition sur le devant de la scène, sous les hurlements des fanatiques du premier rang."
    text "Le temps qu’il ne chauffe la salle, les préparatifs de l’arrière-scène arrivaient à leur fin. "
    hide delaunay_neutre with dissolve
    show delaunay_neutre at del_left with dissolve
    text "Le rideau tomba et dévoila un immense verre à martini duquel s’échappaient des volutes de fumée."
    text "Delaunay continuait d'effeuiller son costume jusqu’à grimper l’échelle et s’asseoir, dos courbé, sur le bord du verre."
    hide delaunay_neutre with dissolve
    show delaunay_neutre at del_right with dissolve
    show flirt at flirt_right
    text "Laissant la tension gagner le public, il finit par s’y glisser en arrière, laissant l’eau déborder ostensiblement sur la scène."
    text "Il continua de se déshabiller avec lenteur et adresse, jusqu’à sortir de son corset un sous-vêtement trempé qu’il jeta insolemment."
    hide flirt
    hide delaunay_neutre with dissolve
    show delaunay_neutre at del_center with dissolve
    text "L’effet dupait aisément son public et signa la fin de son acte."
    stop music fadeout 3.0
    text "Il se couvrit d’un long kimono et se fit aider pour descendre sans glisser avant de saluer fièrement les spectateur.ice.s, son make-up intact et un grand sourire aux lèvres."
    
    show curtain_close with dissolve
    pause 1.5
    hide bar
    hide loges
    scene black
    show curtain_open with dissolve
    with fade



call del_6 from _call_del_6 

#DEL.6

#TRANSITION RIDEAU

label del_6:
    
    hide auditorium
    show loges with fade
    $ current_textbox = "delaunay"
    #show delaunay_flirty at del_center with dissolve
    show delaunay_neutre at del_center with dissolve
    show joy at joy_center
    delaunay "Wow! C'était dément! La salle était super chaude ce soir!"
    #hide delaunay_flirty
    hide joy
    #show delaunay_laugh at del_center with dissolve
    delaunay "Et j'ai ramassé un beau pactole avec les tips! Je suis refais!"
    #hide delaunay_laugh
    
    $ quick_menu = False

    scene background_cg
    show CG_delaunay with fade

    pause 1.0
    "Nouvelle illustration débloquée"
    hide CG_delaunay 
    hide background_cg 
    $ persistent.delaunay_unlocked = True


    $ quick_menu = False
   
    show delaunay_neutre at del_right with dissolve
    show flirt at flirt_right
    menu:
        delaunay "Alors, qu'est-ce que tu en as pensé [player_name]?"
        "C'était incroyable! Surtout quand le rideau s'est ouvert sur le verre!":
            pass
        "J'ai adoré! Mais tu l'as sorti d'où ce string?!":
            pass
        "La foule était en délire à ton salut! Et moi aussi!":
            pass

    $ quick_menu = True

    hide flirt

    $ current_textbox = "delaunay"
    #show delaunay_laugh at del_right with dissolve
    delaunay "Je suis content que ça t'aie plu!"
    #hide delaunay_laugh
    delaunay "Et puis ça pourra toujours t'inspirer pour ton propre numéro!"
    delaunay "Ça avance, d'ailleurs?"

    $ current_textbox = "anthrax"
    anthrax "C'est sur le feu! Je suis chaud.e bouillant.e!"

    #show delaunay_flirty at del_right with dissolve
    show flirt at flirt_right
    $ current_textbox = "delaunay"
    delaunay "Hey, ça te dirait qu'on sorte prendre un verre après m'être changé? Rien que nous deux?"
    hide flirt

    label indice:
        if indice >= 0:
            jump del_6_good
        else:
            jump del_6_bad


#DEL.6.GOOD
label del_6_good:
    $ quick_menu = True
    show delaunay_neutre at del_right with dissolve
    show loges with dissolve
   
    $ quick_menu = False
    menu: 
        text "Hey, ça te dirait qu'on sorte prendre un verre après m'être changé? Rien que nous deux ? "
        "Oui":
            pass
        "Non":
            call del_6_bad from _call_del_6_bad 

    $ quick_menu = True
    
    $ current_textbox = "delaunay"
    delaunay "Parfait! Je te retrouve dehors dans quelques minutes alors !"

    #Transition Rideau
    hide flirt
    hide delaunay_neutre with dissolve
    show curtain_close with dissolve
    pause 1.5
    hide bar
    hide loges with dissolve
    pause 1.5
    show curtain_open with dissolve
    with fade

 
    scene black with dissolve
    

    $ current_textbox = "description"
    text "Le temps que Delaunay et les autres artistes terminent de se démaquiller et de se rhabiller en civil, je passai le balai sur les planches de la scène..."
    text "Laissant mon esprit vagabonder au jour où moi-même je les foulerais."
    text "À l'extérieur, quelques clients étaient restés sur le pavé pour continuer leurs discussions et attendre la sortie de la royauté de L'Androgame."
 
    show devanture
    show leandre_neutre at del_right with dissolve

    
    $ current_textbox = "delaunay"
    show joy at joy_right
    leandre "Pardon pour l'attente! On y va?"
    hide joy

    $ current_textbox = "anthrax"
    anthrax "Merci pour l'invitation... Les autres ne sont pas trop jaloux.se.s de notre contre-soirée?"

    $ current_textbox = "delaunay"
    #show leandre_laugh at del_right
    leandre "Oh, iels devraient s'en remettre. Ça faisait un moment que je voulais passer un peu plus de temps avec toi."
    #hide leandre_laugh
    leandre "En dehors des plumes et des paillettes,  je veux dire..."
    #show leandre_shy at del_right
    leandre "Enfin, si tu es d'accord, évidemment."
    #hide leandre_shy


    $ current_textbox = "anthrax"
    anthrax "Ce serait avec plaisir Léandre..."
    anthrax "Alors dis-moi! Où est-ce que tu m'emmènes ce soir?"

    $ current_textbox = "delaunay"
    show flirt at flirt_right
    #show leandre_flirty at del_right
    leandre "Hm... Je te réserve la surprise. Mais je pense vraiment que ça devrait te plaire!"
    #hide leandre_flirty


    hide flirt
    call final_delaunay from _call_final_delaunay 


#DEL.6.BAD
label del_6_bad:
    $ quick_menu = True
    show delaunay_neutre at del_right
    with fade
    
    $ current_textbox = "delaunay"

    delaunay "On va aller boire un verre avec les autres une fois que les derniers clients auront quitté la salle. Tu te joins à nous ?"
    
    $ quick_menu = False

    menu:
        "Oui, bien sûr! Je termine ça et j'arrive!":
            anthrax "Oui, bien sûr ! Je termine ça et j'arrive !"
        "Si vous insistez!":
            anthrax "Si vous insistez !"
        "Proposé si gentiment, comment refuser?":
            anthrax "Proposé si gentiment, comment refuser ?"

    $ quick_menu = True

    $ current_textbox = "description"

    text "Tous.te.s étaient réuni.e.s face au comptoir, se faisant servir par notre merveilleux \"Dobarman\"."
    text "Imani avait entre ses doigts un mocktail de sa création, Léandre retrouvait peu à peu sa timidité, laissant Delaunay s'effacer."
    text "Partageant son verre avec Aimé.e pour qu'iel goûte, riant aux éclats en détaillant quelques anecdotes de leur expérience au fil des années."
    text "Le tout appuyé.e par l'approbation et les précisions de Mother."

    $ current_textbox = "gatsby"

    aimee "Nan mais je te jure ! La manière dont sa perruque a volé au milieu de la pièce !"

    $ current_textbox = "delaunay"
    leandre "Et surtout sa tête, en s'en rendant compte... !"

    $ current_textbox = "peacock"
    imani "J'aurais rêvé être là cette soirée, et non derrière les machines !"

    $ current_textbox = "mother"
    mother "Je suis sûre que je peux te retrouver une vidéo d'excellente qualité, vu comment elle a tourné sur les plateformes."

    $ current_textbox = "description"

    text "Les écoutant avec une certaine envie, ayant hâte de pouvoir raconter à mon tour mes aventures."
    text "Je les observais un à une, ancrant cette image dans ma mémoire, essayant d'y graver le moindre détail."
    text "Je m'en voulais peut-être un peu de ne pas avoir demandé à Léandre d'être sorti avec moi ce soir."
    text "Mais quelque chose me dit que c'était peut-être un peu trop tôt..."
    text "Et j'aurais loupé cet instant précieux, sachant pertinemment que je passerais le reste de la soirée bien entouré.e !"


    call final_delaunay from _call_final_delaunay_1 

label final_delaunay:
    hide leandre_neutre
    hide loges

    "Interview et musiques débloquées"
    pause 1.0

    scene black with fade

    $ renpy.full_restart()