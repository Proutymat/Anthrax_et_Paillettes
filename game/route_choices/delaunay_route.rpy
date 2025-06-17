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
scene black with fade
show loges
show leandre_neutre at del_center with dissolve

play ambiance AmbLoges fadein 0.5 

#DEL.1
leandre "Hey... Hum... Je suis content que tu m'aies choisi. Je ne pensais pas trop que ce serait le cas."

anthrax "Ah oui ? Pourquoi donc ?"

leandre "Oh, je ne sais pas trop. Je suis un peu plus discret que les autres, disons..."

anthrax "Discret ? Ce n'est pas cette impression que tu m'as donné.e."

leandre "Vraiment ? Je suis soulagé alors !"
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
show bar with fade
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

$ current_textbox = "anthrax"
label minichoice_del_2:
    $ quick_menu = False
   
    show leandre_neutre at del_right
    with fade
    menu:
        leandre "Est-ce que tu sais déjà quoi commander ?"
        "Un Pornstar Martini.":
            pass
        "Un Negroni Sbagliato, avec une pointe de prosecco.":
            pass
        "Une citronnade bien fraîche.":
            pass

$ quick_menu = True

leandre "Alors dis-moi, qu’est-ce qui t’amène ici ?"

anthrax "M-Moi ? Comme ça ? Directement ?"

leandre "Euh... Oui ? Enfin, ça me semblait être un bon début de conversation..."

anthrax "Oh. Eh bien... J’ai commencé le drag dans le confort de mon appart, sur les réseaux sociaux. "
anthrax "Je n’ai jamais mis les pieds dans une troupe. Ou même un cabaret pour tout te dire."
anthrax "J'ai toujours été attiré.e par le burlesque, les plumes, le vintage, l'impétueux..."

leandre "Hm... C’est bien le genre de Mother de recruter quelqu’un de ton acabit. Plein.e de potentiel, mais ne sachant pas par où commencer."


label minichoice_del_3:
    $ quick_menu = False
   
    show leandre_neutre at del_right
    with fade
    menu:
        leandre "J’étais exactement pareil..."
        "Ça fait longtemps que tu as intégré la troupe ?":
            pass
        "Depuis combien de temps est-ce que tu es là?":
            pass
        "Vous devez bien vous connaître, avec les autres, depuis le temps...":
            pass

$ quick_menu = True


leandre "Environ cinq ans je dirais? Techniquement, je suis le doyen, parmi les autres que tu as croisé.e.s tout à l'heure."
leandre "Enfin, officiellement, Imani a travaillé ici depuis plus longtemps, mais n'a intégré la troupe qu'il y a seulement deux ans."
leandre "Et Aimé.e est arrivé.e peut-être un an après moi ?"
leandre "Techniquement, cela fait déjà des années que l’on se côtoie."
leandre "Quelques collègues sont parti.e.s, revenue.s, mais au final nous sommes les trois qui ayons tenu sur le long terme."

anthrax "Et toi ? Qu’est-ce qui t’as lancé dans le drag ?"

leandre "Et bien... J’étais en train de décrocher des études, j’étais dans la panade financière, j’étais en pleine découverte de mon identité de genre."
leandre "Une vraie crise de la vingtaine... J'en ris maintenant, mais ce n'était pas du tout drôle à l'époque."

#Choix DEL.2
label choix_del2:
    $ quick_menu = False
    
    show leandre_neutre at del_right
    with fade
    menu: 
        anthrax "Et finalement, Mother m’a pris sous son aile et m’a aidé à me sortir de tout cela."
        "Oh! Tu as transitionné?":
            call del_2_1 from _call_del_2_1 
        "Et comment est-ce que tu as rencontré Mother?":
            call del_2_2 from _call_del_2_2 
        "J'ai remarqué qu'Aimé.e finissait beaucoup tes phrases. Est-ce que tu es toujours aussi timide ?":
            call del_2_3 from _call_del_2_3 
          

#DEL.2.1
label del_2_1:
    $ quick_menu = True
    
    show leandre_neutre at del_center
    with fade
#lovometer +1
    anthrax "Oh ! Tu as transitionné ?"  

    leandre "Oui ! Ça ne se voit pas ?"

    anthrax "Ça dépend... Tu as un très bon passing. Mais ce n'est pas la première question que je me pose en rencontrant quelqu'un."

    leandre "C'est vrai que dit comme ça, ça a l'air plutôt normal. Je suis toujours persuadé que ça se lit sur mon front tellement ça fait partie de moi."
    leandre "J'ai tendance à oublier que ce n'est pas si commun que ça."

    anthrax "J'ai aussi envie de dire que l'on est dans une troupe de drag. J'aurais dû m'y attendre un minimum..."

label minichoice_del_4:
    $ quick_menu = False
   
    show leandre_neutre at del_right
    with fade
    menu:
        leandre "Pas faux... Mais bon, nous sommes une troupe particulièrement hétéroclite. Blague à part!"
        "Ça n'a pas été trop dur? Enfin, si ce n'est pas indiscret.":
            pass
        "Comment as-tu réussi à t'en sortir?":
            pass
        "Ça a dû être une sacrée épreuve, tout de même...":
            pass


    $ quick_menu = True

    leandre "En toute honnêteté, c'était l'enfer. Mais j'ai eu la chance d'être bien entouré."
    leandre "Et j'ai commencé le drag à peu près à cette période, donc c'était très utile pour m'aider à combattre la dysphorie de genre."

    anthrax "D'où le fait que tu fasses du drag king, je suppose."

    leandre "C'est exact..."
    leandre "Après, mon drag s'est \"re\"féminisé dernièrement."
    leandre "Après tout, ma masculinité n'est pas la même que celle des hommes cisgenres, et hétéros."

label minichoice_del_5:
    $ quick_menu = False
   
    show leandre_neutre at del_right
    with fade
    menu:
        leandre "Et je tire une bonne partie de ma fierté queer, de ma transition."
        "Qu'est-ce que tu entends par là ?":
            pass
        "Je ne comprends pas...":
            pass
        "Peux-tu préciser? J'ai dû mal à saisir la nuance.":
            pass

    $ quick_menu = True

    leandre "J'entends que si je devais renaître, je ne choisirais pas de le faire dans un corps d'homme cis..."
    leandre "Et que je me relancerais dans le même parcours de vie."
    leandre "Je n'échangerais pour rien au monde cette expérience."
    leandre "D'avoir grandi comme j'ai grandi, d'avoir connu la sororité et les difficultés liées à la vie de femme ?"
    leandre "Cette empathie, en tant qu'homme, m'est très précieuse."

    stop music fadeout 1.0
    stop ambiance fadeout 1.0
    call del_3 from _call_del_3 

#DEL.2.2
label del_2_2:
    $ quick_menu = True
    
    show leandre_neutre at del_center
    with fade

    anthrax "Et comment est-ce que tu as rencontré Mother ?"

    leandre "C'est un peu bête, vraiment..."
    leandre "Je me suis fait traîner ici par des ami.e.s pour un spectacle, mais iels ont eu un empêchement de dernière minute."
    leandre "Du coup je me suis retrouvé tout seul... Comme les endroits avec beaucoup de monde et personne que je connais m'angoissent beaucoup, j'ai bu..."

label minichoice_del_6:
    $ quick_menu = False
   
    show leandre_neutre at del_right
    with fade
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

    leandre "E-Et bien... Ça ne s'est pas fait de suite évidemment... Mais ultimement, oui."
    leandre "C'était un peu informel, mais elle m'a fait visiter L'Androgame de fond en comble..."
    leandre "Et initié au drag en m'emmenant dans les coulisses avec les danseuses de semaine et racontant sa vie."
    leandre "Tout du long, elle soulignait qu'elle comptait monter une troupe secondaire, exclusivement queer."
    leandre "\"Une manière de rendre à la communauté\", qu'elle disait. Son plan était de réserver au moins un soir de grande affluence en semaine au drag."


label minichoice_del_7:
    $ quick_menu = False
   
    show leandre_neutre at del_right
    with fade
    menu:
        leandre "Pas besoin de préciser que ça a fonctionné bien plus qu'elle ne le pensait..."
        "C'est vrai que la majorité des soirées sont réservées maintenant aux \"Paillettes\".":
            pass
        "Je n'ai d'ailleurs connu L'Androgame qu'à partir du moment où la communauté à commencé à se réveiller et partager ce qu'il s'y passait.":
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
    
    show leandre_neutre at del_center
    with fade
    
    anthrax "J'ai remarqué qu'Aimé.e finissait beaucoup tes phrases. Est-ce que tu es toujours aussi timide ?"

    leandre "Hm... La plupart du temps oui. Mais c'est quelque chose que j'essaye de travailler."
    leandre "J'ai toujours été assez réservé et discret. Je prends plutôt bien sa démarche puisque je ne réussis pas encore à aussi bien m'imposer qu'ellui."
    leandre "Je préfère ça à m'effacer dans le décor comme je le faisais avant..."
    leandre "Et iel est très compréhensif.ve lorsque je sens que je suis capable de m'exprimer et que j'en fais part."

    anthrax "C'est donc d'un commun accord..."

    leandre "Tacite, oui. Mais qui nous convient et ressemble bien..."

    leandre "Ça ne l'empêche pas non plus de me taquiner et d'essayer de me faire sortir de mes gonds."


label minichoice_del_8:
    $ quick_menu = False
   
    show leandre_neutre at del_right
    with fade
    menu:
        leandre "C'est challengeant, et ça a déjà marché. Même Imani s'est retrouvée assez surprise."
        "J'ai très envie de voir ça maintenant! Mais il y a une raison derrière tout cela ?":
            pass
        "Vous semblez être de très bon.ne.s ami.e.s, mais pourquoi ?":
            pass
        "C'est le genre de chose que je ne supporterais pas... Que l'on parle à ma place.":
            pass


    $ quick_menu = True

    leandre "Je n'ai juste jamais eu une grande confiance en moi, et le regard des autres m'a toujours semblé particulièrement lourd à porter."
    leandre "Lorsqu'une situation était trop embarrassante, je choisissais toujours la fuite. Ou le déni, au choix."
    leandre "C'est devenu ma façon d'être, et les handicaps qui viennent avec."
    leandre "C'est pour ça que le drag est particulièrement rassurant... L'espace d'un instant, je peux être entièrement quelqu'un d'autre."
    leandre "Quelqu'un de ma création, que je contrôle, qui me protège, derrière lequel je peux me cacher et extérioriser le fond de ma pensée."
    leandre "Il n'y a pas vraiment d'autre forme d'expression qui permet cela... Le théâtre peut-être ? Mais encore, le personnage y est déjà existant et incarné..."
    leandre "Pas un reflet d'une personnalité que j'aimerais affirmer."

    anthrax "La nuance est fine, mais je crois comprendre ce que tu sous-entends."

    stop music fadeout 1.0
    stop ambiance fadeout 1.0
    call del_3 from _call_del_3_2 

#DEL.3
label del_3:

# faire la transition avec la description sur fond noir comme sur l'onboarding
    hide loges withe dissolve
    hide leandre_neutre with dissolve
    hide bar with dissolve

    show curtain_close
    scene black with dissolve
    


    play music ConfidenceIntro

    $ current_textbox = "description"
    text "Cela faisait plusieurs minutes que je cherchais Léandre, avec qui j'étais supposé.e répéter une partie de mon numéro, que l'on construisait ensemble."
    text "Après avoir fait trois fois le tour du bâtiment, je finis par retourner sur les planches de la scène, pensif.ve."
    text "Et en toute honnêteté, un peu inquiet.e."

    queue music ConfidenceA1

    text "C'est alors que j'aperçu une tignasse blonde depuis le haut du balcon, absorbée par le contenu de son téléphone."
    text "N'ayant pas pensé à lever le regard, je grimpai l'escalier en colimaçon pour le rejoindre, à tâtons."


    show auditorium
    #show leandre_neutre at del_right with dissolve

label minichoice_del_9:
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

    $ current_textbox = "anthrax"

    leandre "Oh !"
    leandre "Pardon, je n'ai pas vu l'heure tourner."

    anthrax "Est-ce que tout va bien ? Tu as l'air soucieux."

    leandre "Hm... C'est rien. Juste un ancien client qui essaye de reprendre contact. C'est un peu relou."

    anthrax "Un ancien client ?"

    leandre "Hm..."

    queue music ConfidenceA2

    text "Visiblement pas très à l'aise, Léandre rangea son mobile et joua avec ses doigts, venant s'appuyer sur la rambarde pour observer la scène en contrebas."

    leandre "C'est vrai que je ne t'en ai pas encore parlé..."

    leandre "Les autres sont au courant, mais j'aurais peut-être dû te mettre dans la boucle plus tôt."

    anthrax "Oh... C'est grave ?"

    leandre "Pas vraiment... Mais c'est une passe de ma vie dont je ne suis pas très fier."

    leandre "Mais ça ne me dérange plus tellement d'en parler, donc bon..."

    anthrax "Seulement si tu te sens de l'aborder alors."

    leandre "Ne t'en fais pas, je n'aurais pas commencé à en parler si je ne le sentais pas."

    leandre "Mais je te fais suffisamment confiance pour ne pas me juger sur mes décisions."

    text "Un peu plus confiant, il se redressa et tourna la tête dans ma direction, un sourire apaisé aux lèvres."

    leandre "À un moment, j'ai fait des vidéos à caractère..."

    leandre "Disons les termes, à caractère sexuel."

    leandre "Pour de l'argent."

    leandre "D'où \"l'ancien client\"..."

#Dialogue WIP 

#Choix DEL.3
label choix_del3:
    $ quick_menu = False
    
    show leandre_neutre at del_right
    with fade
    menu: 
        "Tu avais d'autres raisons pour te lancer... dans cette industrie?":
            call del_3_1 from _call_del_3_1_1 
        "Pourquoi est-ce que tu n'es pas très fier de cette période?":
            call del_3_2 from _call_del_3_2_1 
        "Pour de l'argent? Tu étais en difficulté?":
            call del_3_3 from _call_del_3_3 

#DEL.3.1
label del_3_1:
    $ quick_menu = True
    
    show leandre_neutre at del_center
    with fade
    
    anthrax "Tu avais d'autres raisons pour te lancer... dans cette industrie ?"

    leandre "Sûrement... On peut dire ça."

    leandre "C'était un moment dans ma vie où j'étais assez perdu."

    leandre "Il y a eu tellement de changements en aussi peu de temps que je ne savais plus du tout où me positionner. Par rapport aux autres et par rapport à moi-même..."

    anthrax "C'est-à-dire... ?"

    leandre "Je ne sais pas... J'ai toujours eu un rapport à l'intime complètement frit."

    leandre "Hormonalement parlant, c'était la fiesta. Je commençais tout juste la testo et ma libido était en roue libre."

    leandre "Bon, après, ça ne m'a jamais empêché d'être serein et décent avec mes partenaires, mais tout de même..."

    leandre "Et c'était la première fois de ma vie que j'apprenais à apprécier mon corps pour ce qu'il était. C'était une liberté nouvelle, peut-être un peu trop, parce que je ne savais pas ce que je faisais."

    leandre "J'étais jeune aussi, et c'était peut-être trop de bonheur d'un coup, pour quelqu'un d'encore blessé et immature."

    anthrax "Après, c'est quelque chose de facilement compréhensible. Tu te cherchais..."

    leandre "Je me suis surtout senti pousser des ailes."

    leandre "Dans cette quête, je me suis hypersexualisé, et au final ça m'a plus joué des tours qu'autre chose."

    leandre "J'avais aussi besoin d'argent pour payer ma mammec', et je m'en sentais les épaules. Maintenant, je me retrouve avec du contenu intime qui se promène dans la nature..."

    leandre "J'ai fini par l'accepter : j'ai fait des erreurs et pris de mauvaises décisions."

    leandre "Maintenant, le \"moi\" adulte vit avec."

    anthrax "Si tu réussis à te réconcilier avec ton passé, c'est le principal non ?"

    leandre "Oui, je suis de cet avis. Et puis tout le monde a des regrets, je ne suis pas le seul."

    leandre "J'aurais peut-être juste espéré que Delaunay débarque un peu plus tôt dans ma vie. Il m'aurait sûrement évité quelques bêtises et aiguillé comme il le fait aujourd'hui."

    anthrax "Ta persona drag ? Je ne savais pas que tu l'adressais comme si c'était quelqu'un d'autre."

    leandre "C'est un peu plus simple de complètement le dissocier de ma personne."

    leandre "C'est un peu mon ange gardien finalement, qui m'incite à prendre exemple sur lui et être une meilleure version de moi-même."

    leandre "Mais tout le monde ne fait pas pareil et chacun.e a sa manière d'aborder son drag après tout."

    leandre "Dans tous les cas, c'est une relation très personnelle avec une facette de nous-même, donc ça ne me dérange pas de l'adresser à la troisième personne."

    call del_4 from _call_del_4 

#DEL.3.2
label del_3_2:
    $ quick_menu = True
    
    queue music ConfidenceAB
    queue music ConfidenceB1
    show leandre_neutre at del_center
    with fade

    anthrax "Pourquoi est-ce que tu n'es pas très fier de cette période ?"

    leandre "Oh, eh bien, ça me semble plutôt logique..."

    leandre "Avoir fait du porno, c'est pas très mirobolant sur un CV."

    leandre "Mais Mother n'est pas très regardante sur ce point, donc je n'ai pas eu plus de soucis que ça."

    leandre "C'est plus gênant si quelqu'un tombe dessus et m'y reconnaît, mais comme j'ai énormément changé entre-temps, je ne m'en inquiète pas plus que ça."

    leandre "Puis, comme j'assume un minimum, ce n'est pas comme si ces personnes pouvaient retourner ça contre moi. Et sinon, j'ai toujours l'option de nier."

    anthrax "Après tout, ça ne concerne que toi."

    leandre "Exact !"

    anthrax "Si tu réussis à tirer quelque chose de positif de cette expérience, c'est le principal."

    leandre "Hm... Oui, après tout, ça m'a aidé à réaliser que ce n'était pas à travers le regard des autres que j'allais apprendre à m'aimer."

    leandre "J'étais persuadé à l'époque que si les gens m'appréciaient pour quelque chose, le reste allait suivre de l'autre côté."

    leandre "Alors que ça aurait dû être l'inverse..."

    queue music ConfidenceB2

    leandre "M'aimer d'abord, découvrir mon intimité ensuite... Ou en même temps, à la rigueur."

    leandre "Enfin bref, c'était pas du tout la méthode adaptée pour nourrir mon \"appréciation de soi\"."

    anthrax "Comment est-ce que tu as réussi à t'en sortir du coup ?"

    leandre "Je ne travaillais pas encore à l'Androgame, et je m'étais fait poser un lapin, donc je me suis laminé au bar... Et on a discuté le temps que je décuve."

    leandre "C'était assez bizarre, mais bienvenu puisque j'étais prêt à me raccrocher à n'importe quoi. Je suis revenu quelques fois justement pour ça..."

    leandre "Je m'étais lancé dans les vidéos pour payer mon opération mais Mother m'a proposé un travail à mi-temps et présenté à ses ami.e.s drag artists lorsque j'ai soulevé l'idée que ça pouvait m'aider avec ma dysphorie de genre."

    queue music ConfidenceOutro
    
    leandre "Grâce à ça, j'ai pu arrêter et reprendre ma vie en main."

    leandre "Je t'en avais déjà parlé, non ? Je ne me souviens plus... Ce serait bête que je passe pour un disque rayé !"

    anthrax "Mais non ! Et puis, même si tu te répétais, ça m'est égal. Ça veut dire que tu me fais toujours confiance pour m'en parler !"

    call del_4 from _call_del_4_1 

#DEL.3.3
label del_3_3:
    $ quick_menu = True
    
    show leandre_neutre at del_center
    with fade
    
    anthrax "Pour de l'argent ? Tu étais à ce point en difficulté ?"

    leandre "Plus ou moins... Avec mon parcours de transition plutôt chaotique, je n'ai pas pu passer par le circuit \"public\", avec les aides médicales qui vont avec."

    leandre "Pour avoir accès à ça, il faut avoir eu un suivi psychiatrique d'au moins deux ans."

    leandre "Mais comme je m'en suis rendu compte tardivement, je n'ai pas eu ce luxe."

    leandre "Et j'étais tellement dans le mal, psychologiquement parlant, que je n'avais pas la patience non plus d'entamer ce parcours."

    leandre "Heureusement, je suis tombé sur une endocrinologue top, qui m'a permis d'accéder à un traitement hormonal."

    leandre "Et ma psy, bien qu'elle ne soit pas psychiatre, a été d'un grand soutien."

    anthrax "Ça m'a l'air d'être des démarches super compliquées..."

    leandre "Oh, crois-moi que je suis rodé en tout ce qui concerne les démarches administratives..."

    leandre "Même si je suis toujours aussi terrifié à l'idée de passer un appel téléphonique pour prendre un rendez-vous..."

    leandre "Dans l'idée, dans le meilleur des mondes, j'aurais dû m'en rendre compte lorsque j'étais jeune et innocent pour qu'on me prenne au sérieux."

    leandre "Et pas à dix-neuf ans, déjà majeur, comme ça s'est passé..."

    leandre "C'est fou à quel point on te laisse tomber à ta majorité par rapport à tout ce qui est médical..."

    leandre "Comme si c'était inné, qu'on devait tout savoir, ou que c'était une évidence de connaître la marche à suivre."

    leandre "Alors évidemment, internet est ton meilleur ami, mais ensuite on te reproche d'avoir été influencé par internet et de ne pas savoir ce que tu veux finalement..."

    leandre "Parce qu'en plus de ta déprime, c'est apparemment absolument nécessaire de t'achever en te décrédibilisant."

    leandre "Enfin bref..."

    anthrax "Les circonstances ont fait que tu as dû payer de ta poche..."

    leandre "En effet... Et ça ne sort pas d'un chapeau magique, quelques milliers d'euros. Donc j'ai fait avec ce que j'avais, c'est-à-dire, pas grand-chose..."

    leandre "J'étais tellement au fond du trou et au pire de ma dépression que ça me semblait être la seule issue."

    leandre "Si je n'agissais pas, j'allais me laisser manger par les idées noires et..."

    leandre "Je ne vais pas faire un dessin, je suppose que tu connais les statistiques..."

    anthrax "Malheureusement oui. Je connais au moins une personne trans dans mon entourage qui s'est suicidée... Et d'autres qui l'ont au moins envisagé."

    leandre "Ce n'est pas très joyeux comme discussion..."

    anthrax "C'est clair... Mais c'est la triste réalité..."

    call del_4 from _call_del_4_2 

#DEL.4
label del_4:

    stop music fadeout 0.5
    stop ambiance fadeout 0.5
    play music BackstageLoop volume 0.5
    play ambiance AmbLoges fadein 0.5

    anthrax "Au sein de la loge, une certaine tension planait au-dessus de la playlist qui tournait. Pas une mauvaise ambiance, non, plutôt une intense concentration."
    anthrax "Évidemment, tout le monde chit-chattait gaîment, mais je ne pus m'empêcher de fixer un instant Léandre."
    anthrax "Agenouillé devant un miroir sur pied, déjà maquillé, à moitié habillé de son pantalon à sequins rouge Louboutin fendu sur les côtés et ses lunettes glissant maladroitement de son nez,"
    anthrax "il collait précautionneusement des strass de la même couleur sur la peau rugueuse des cicatrices de son torse."
    anthrax "Tel un papillon se dégageant de son cocon, Delaunay sortait de la peau de Léandre."
    anthrax "Son dos se courba, son regard s'embrasa et il me remarqua le fixer. Un sourire coquin et un clin d’œil plus tard, il m'invitait à le rejoindre."

    leandre "Qu'est-ce que tu fais à jouer le timide ? Approche, je ne vais pas te manger."

#Choix DEL.4
label choix_del4:
    $ quick_menu = False
    
    show leandre_neutre at del_right
    with fade
    menu: 
        anthrax "Qu'est-ce que tu fais à jouer le timide ? Approche, je ne vais pas te manger."
        "Franchement, tu me manges quand tu veux":
            call del_4_1 from _call_del_4_1_1 
        "J'adore la manière dont tu prends confiance en toi avec Delaunay":
            call del_4_2 from _call_del_4_2_1 
        "Timide? Moi?":
            call del_4_3 from _call_del_4_3 

#DEL.4.1
label del_4_1:
    $ quick_menu = True
    
    show leandre_neutre at del_center
    with fade

    anthrax "Franchement, tu me manges quand tu veux"

    delaunay "Eh bien ! On dirait que je commence à déteindre sur toi~"

    anthrax "Ce n'était pas le but peut-être ?"

    delaunay "Seulement si tu en as réellement envie. Je ne veux pas te forcer à faire du burlesque ou à devenir une pimbèche de service, bien que je tienne ce titre en très haute estime."
    delaunay "C'est ma persona après tout~"

    gatsby "Et ça va être difficile de la battre, cette pimbèche là."

    peacock "Oh, je suis certaine qu'il y a de la place pour deux perruches, après tout, regarde-nous."
    peacock "Mais bon quand il s'agit de bomber le torse et de faire du pied, il n'y a qu'une personne qui nous vienne à l'esprit."

    delaunay "Oh ! Mais occupez-vous de vos fesses, oui ! Je vais rougir..."
    delaunay "Je reviens de loin, je peux bien m'octroyer un peu de crédit."

    anthrax "Il doit me manquer un peu de contexte, je ne comprends pas..."

    delaunay "Oh, c'est vrai. Comment est-ce que je pourrais le formuler... ?"
    delaunay "J'ai toujours eu un peu de mal à me trouver désirable. Ou en tout cas d'être confiant dans mon intimité, ma sensualité, ma sexualité..."
    delaunay "Alors Delaunay l'est à ma place, et m'aide à explorer cette facette de ma personne que je cherche à redécouvrir."
    delaunay "Puisque ça a été un échec cuisant lors de ma première tentative, à travers les vidéos..."

    gatsby "Après, quand tu faisais tes vidéos, tu avais aussi d'autres circonstances qui ont fait que ta démarche n'était pas vraiment saine."

    peacock "...Toi et ton tact légendaire."
    peacock "En soi, je suis plutôt d'accord avec Aimé.e, mais je ne l'aurais pas dit dans ces termes. Tu avais des besoins et tu te cherchais encore..."

    delaunay "Je sais. J'ai fait un choix et ce n'était pas le bon. Mais au final, ça m'a tout de même amené ici aujourd'hui. Donc je n'ai pas tant de regrets que ça."
    delaunay "Et je découvre la bad bitch que j'ai toujours rêvé d'être."
    delaunay "Tout est bien qui finit bien. Carpe diem, blablabla."

    anthrax "C'est adorable."

    stop music fadeout 0.1
    
    staff "Ok les filles ! Showtime dans dix minutes !"

    delaunay "Mon dieu, j'ai encore tellement à faire ! Vite [player] ! Un coup de main, vite !"

    stop ambiance fadeout 2.0
    call del_5 from _call_del_5 

#DEL.4.2
label del_4_2:
    $ quick_menu = True
    
    show leandre_neutre at del_center
    with fade

    anthrax "J'adore la manière dont tu prends confiance en toi avec Delaunay"
    anthrax "Qu'est-ce qui change quand tu te costumes ?"

    delaunay "Tout."
    delaunay "Léandre n'existe pas quand je suis en drag, c'est libérateur."

    anthrax "Vraiment ? J'aurais pensé le contraire. Je ne savais pas que ta relation avec toi-même était si conflictuelle."

    delaunay "Conflictuelle, c'est le bon mot..."
    delaunay "Mais détrompe-toi... J'adore Léandre."
    delaunay "Enfin, je m'aime bien."

    delaunay "Quand j'ai imaginé Delaunay, je l'ai créé comme étant tout ce que je désirais être. Confiant, têtu, un peu salope sur les bords..."

    anthrax "Et c'est quelque chose que tu n'arrives pas à faire... en tant que Léandre ?"

    delaunay "Hm... Oui. Mais c'est pas comme si je n'essayais pas. Comment dire..."
    delaunay "En fait, je suis passé par tellement de changements et je me recherche tellement encore, que je n'ai pas de vrai repère auquel me raccrocher en termes de confiance en soi et de personnalité."
    delaunay "Alors... Delaunay, c'est un peu mon phare dans cet océan de confusion. Et Léandre, il essaye de naviguer un peu à travers tout ça."

    anthrax "Je comprends mieux... C'est valide d'être un peu perdu dans la vie."

    delaunay "Je sais... Et ça commence à se stabiliser, bien heureusement."
    delaunay "J'aimerais juste des fois que ça aille un peu plus vite."

    stop music fadeout 0.1

    staff "Ok les filles ! Showtime dans dix minutes !"

    delaunay "Mon dieu, j'ai encore tellement à faire ! Vite [player] ! Un coup de main, vite !"

    stop ambiance fadeout 2.0
    call del_5 from _call_del_5_1 

#DEL.4.3
label del_4_3:
    $ quick_menu = True

    show leandre_neutre at del_center
    with fade

    anthrax "\"Timide ? Moi ?\""

    delaunay "Oui, bon ok. C'est un peu l'hôpital qui se fout de la charité."

    anthrax "J'aurais bien dit que tu as raison... Mais bizarrement, tu m'as l'air plus confiant là."

    delaunay "Ah ça, c'est l'effet \"Delaunay\" !"
    delaunay "Il m'a toujours aidé à devenir l'homme que je voulais être, encore maintenant..."

    anthrax "Pourtant, ton personnage m'a l'air d'être très efféminé, aussi maladroit que ça puisse être dit comme ça."

    delaunay "Tu n'as pas tort. Mais il n'a pas toujours été comme ça... Au contraire, au début, il était très masculin."
    delaunay "Après coup, j'ai réalisé que comme c'était au début de ma transition, j'essayais peut-être de me recréer un \"idéal masculin\"... Qui était finalement très stéréotypé."

    anthrax "Je ne l'aurais jamais imaginé... Genre avec une fausse barbe et tout ?"

    delaunay "Surtout pas ! Une moustache, très chèr.e ! J'ai quand même un peu de goût..."

    peacock "Tu as quelque chose contre les barbes ma belle ?"

    delaunay "Non ! Du tout ! La tienne te sied très bien... Malgré les trous~"

    peacock "Hm... C'est vrai que la testo ne t'a pas trop épargné là-dessus... Une absence de barbe, des poils aux fesses et un début de calvitie..."

    gatsby "BAHAHA !"

    anthrax "Shady."

    delaunay "Je suis outré !"

    anthrax "Hm... Tu as commencé."

    delaunay "..."
    delaunay "Anyway."
    delaunay "J'ai quand même pas mal rétropédalé au niveau de l'hypermasculinisation de mon perso, quand mon corps a commencé à changer."
    delaunay "Je me suis réconcilié avec moi-même, et donc Delaunay n'avait plus besoin de servir cette fonction."
    delaunay "Et comme j'avais envie de redécouvrir ma part de féminité en tant qu'homme, nous y voilà."

    anthrax "C'est une relation très personnelle et intime que tu as avec ton personnage finalement, je comprends mieux pourquoi tu t'adresses à \"Léandre\" à la troisième personne parfois, quand tu es en drag."

    delaunay "Oh, ça... C'est un autre débat. C'est plus mon côté égocentrique que j'essaye de travailler. Faut pas hésiter à me rappeler l'humilité..."

    anthrax "Si ça peut te rassurer, on remarque à peine ta calvitie."

    delaunay "Par pitié, pas toi aussi... Le terrain est glissant."

    anthrax "Désolé.e, c'était trop tentant."

    stop music fadeout 0.1

    staff "Ok les filles ! Showtime dans dix minutes !"

    delaunay "Mon dieu, j'ai encore tellement à faire ! Vite [player] ! Un coup de main, vite !"

    stop ambiance fadeout 2.0

    call del_5 from _call_del_5_2 

#DEL.5
label del_5:

    play music ShowDelaunay noloop

    anthrax "L’entracte arrivait déjà à sa fin et l’atmosphère était bouillonnante dans les coulisses. Derrière le rideau, les kittens et les régisseur.euse.s s’activaient à déplacer le décor en silence." 
    anthrax "Soudainement, un spot se braqua sur le velours et un “bang” de trompettes réveilla la foule. Puis une longue jambe dévoila sensuellement sa résille en sortant de l’entrouverture."
    anthrax "Au rythme de la musique, Delaunay fit son apparition sur le devant de la scène, sous les hurlements des fanatiques du premier rang."
    anthrax "Le temps qu’il ne chauffe la salle, les préparatifs de l’arrière-scène arrivaient à leur fin. Le rideau tomba et dévoila un immense verre à martini duquel s’échappaient des volutes de fumée."
    anthrax "Delaunay continuait d'effeuiller son costume jusqu’à grimper l’échelle et s’asseoir, dos courbé, sur le bord du verre."
    anthrax "Laissant la tension gagner le public, il finit par s’y glisser en arrière, laissant l’eau déborder ostensiblement sur la scène."
    anthrax "Il continua de se déshabiller avec lenteur et adresse, jusqu’à sortir de son corset un sous-vêtement trempé qu’il jeta insolemment."
    anthrax "L’effet dupait aisément son public et signa la fin de son acte."
    stop music fadeout 3.0
    anthrax "Il se couvrit d’un long kimono et se fit aider pour descendre sans glisser avant de saluer fièrement les spectateur.ice.s, son make-up intact et un grand sourire aux lèvres."

#Dialogue WIP 


call del_6 from _call_del_6 

#DEL.6
label del_6:


#Dialogue WIP 


#Choix DEL.6
label choix_del6:
    $ quick_menu = False
    show leandre_neutre at del_right
    with fade

    menu: 
        "WIP":
            call del_6_good from _call_del_6_good 
        "WIP":
            call del_6_bad from _call_del_6_bad 

#DEL.6.GOOD
label del_6_good:
    $ quick_menu = True
    show leandre_neutre at del_center
    with fade

    anthrax "WIP"
    leandre "WIP"
    call final_delaunay from _call_final_delaunay 


#DEL.6.BAD
label del_6_bad:
    $ quick_menu = True
    show leandre_neutre at del_center
    with fade

    anthrax "WIP"
    mother "WIP"
    call final_delaunay from _call_final_delaunay_1 

label final_delaunay:
    hide leandre_neutre
    hide loges

    $ quick_menu = False

    scene background_cg
    show CG_delaunay with fade

    pause 1.0
    "Nouvelle illustration débloquée"
    hide CG_delaunay with fade
    $ persistent.delaunay_unlocked = True
    "Interview et musiques débloquées"
    pause 1.0

    scene black with fade

    $ renpy.full_restart()