# fonctions custom

init python:
    def type_sound(event, interact=True, cps=35, boopfile=type_sounds, **kwargs):
        speed = int((0.1/cps)*1000)/1000
        silence = "<silence " + str(speed) + ">"
    
        if not interact:
            return

        if event == "show" :
            for i in range(100):
                print(silence)
                renpy.sound.queue(renpy.random.choice(boopfile))
                renpy.sound.queue(silence)

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def pausedialogue():
        if renpy.music.is_playing('sound'):
            renpy.pause((20-renpy.music.get_pos('sound')),hard=True)

    renpy.music.register_channel("ambiance", "sfx", True)
    renpy.music.register_channel("typechannel", "sound", False)


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

image loges: 
    "Backgrounds/loges.png"
    zoom 1.02

image rideau = "Backgrounds/rideau.png"

image balcon = "Backgrounds/balcon.png"

#vfx


init python:

    tall_right = Transform(
        zoom=2.2,       
        xalign=0.90,
        yanchor=1.0,
        ypos=1.0,
        xzoom=1
    )

    tall_left = Transform(
        zoom=2.2,
        xalign=0.15,
        yanchor=1.0,
        ypos=1.0,
        xzoom=-1
    )

    tall_center = Transform(
        zoom=2.2,
        xalign=0.5,
        yanchor=1.0,
        ypos=1.0,
        xzoom=1
    )


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
define audio.AmbLoges = "audio/Amb/Amb_LogesDay_V3.ogg"
define audio.AmbRue = "audio/Amb/Amb_Rue_V1.ogg"
define audio.AmbLogesNight = "audio/Amb/Amb_LogesNight_V4.ogg"
define audio.AmbDelShow = "audio/Amb/AP_Amb_ShowDel_V1.ogg"
define audio.BarDay = "audio/Amb/Amb_BarDay_V2.ogg"

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
define audio.ShowDelaunay = "audio/Music/SHOW_Delaunay_Idea1_V1.ogg"
define audio.ShowGatsby = "audio/Music/SHOW_Gatsby_Idea1_V2.ogg"

# Déclarez les personnages utilisés dans le jeu.
define mother = Character('Mother', color="#b51963", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=25, callback=type_sound, cb_cps=25, cb_boopfile=M_type_sounds)
define anthrax = Character('Anthräx', color="#9370db", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=35, callback=type_sound, cb_cps=35, cb_boopfile=A_type_sounds)
define delaunay = Character('Delaunay', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define gatsby = Character('Gatsby', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=G_type_sounds)
define peacock = Character('Peacock', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=P_type_sounds)  
define leandre = Character('Léandre', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define aimee = Character('Aimé.e', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=G_type_sounds)
define imani = Character('Imani', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=P_type_sounds)
define inconnu = Character('???', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50)
define delinconnu = Character('Del?', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=D_type_sounds)
define player = Character('[player_name]', color="9370db", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=A_type_sounds)
define staff = Character('Staff', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50, cb_boopfile=type_silent)
define text = Character(color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)




label start:
    $ quick_menu = False
    scene black
    with fade
    $player_name = renpy.input("Choisis le prénom d'Anthräx, ton personnage...")


$ player_name = player_name.strip()

if player_name == "":
    $ player_name = "Anthrâx"
    text "Tu n’as rien saisi, on va garder [player_name]. Ça te va ?"
    hide textbox

    python:
        ui.hbox(xalign=0.5, yalign=0.5, spacing=55)
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/oui_route_idle.png",
            hover="images/backgrounds/routes_confirmation/oui_route_hover.png",
            clicked=ui.returns("oui")
        )
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/non_route_idle.png",
            hover="images/backgrounds/routes_confirmation/non_route_hover.png",
            clicked=ui.returns("non")
        )
        ui.close()
        choix = ui.interact()

    window hide

    if choix == "oui":
        $ persistent.bg_parallax = True
        jump onboarding
    else:
        $ persistent.bg_parallax = False
        jump start
    
else:
    text "Tu veux bien garder [player_name] ?"

        
    python:
        ui.hbox(xalign=0.5, yalign=0.5, spacing=55)
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/oui_route_idle.png",
            hover="images/backgrounds/routes_confirmation/oui_route_hover.png",
            clicked=ui.returns("oui")
        )
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/non_route_idle.png",
            hover="images/backgrounds/routes_confirmation/non_route_hover.png",
            clicked=ui.returns("non")
        )
        ui.close()
        choix = ui.interact()

    window hide

    if choix == "oui":
        $ persistent.bg_parallax = True
        jump onboarding
    else:
        $ persistent.bg_parallax = False
        jump start

#0.1    
label onboarding:
    $ persistent.bg_parallax = True
    show devanture
    with fade
    $ quick_menu = True  

    play ambiance AmbRue

    text "L'Androgame..."
    text "C’est dingue à quel point ce cabaret a reprit ses lettres de noblesse."
    text "Je me souviens encore de quand je passais devant pour aller prendre le métro... Complètement défraichit, la pierre sale et les fenètres brisées."
    text "On se demandait quand est-ce qu’ils finiraient par abréger ses souffrances et le démolir."
    text "Cela fait un moment maintenant qu’il a été reprit, et après de longs et nombreux travaux, il fait à présent revivre le quartier comme je ne l’ai jamais vu auparavant."
    text "Il me décroche toujours un sourire quand je passe devant..."
    text "Et puis même au sein de la commu’, ça a fait jaser. Toutes les têtes d’affiches sont queer."
    text "Ça fait presque bizarre de nous voir se réapproprier une époque dans laquelle on n’avait pas le droit de réellement exister."
    text "Je suis sûr.e qu’on n’aurait jamais autant flamboyé que dans les années 20... C’est peut-être pour ça qu’on était \"interdits\"? On aurait trop volé la vedette aux hétéros."
    text "Les plumes, la fourrure, les paillettes, le champagne, le charleston, l’occasionnel rail de coke... Les années folles quoi."
    text "C’est ce qui m’a motivé à me lancer dans le drag finalement..."
    text "J’ai toujours été intrigué.e par cette forme d’expression. Et à voir ces artistes bourré.e.s de talent faire leur show, à deux pas de chez moi... Je me suis laissé.e tenter."
    text "Au début, j’en avais un peu honte. Je me costumais en cachette dans mon appart, et pour être honnête, c’était peut-être pour le mieux."
    text "Mes premières tentatives de make-up étaient catastrophiques... Mais au fur et à mesure, j’ai pris le coup de pinceau."
    text "Ce que je pensais être une lubie est finalement devenu un hobby."
    text "J’ai pris des classes pour apprendre à coudre et danser, au point où même mes ami.e.s ont capté ce qui se tramait et se sont prêté.e.s au jeu pour m’aider à m’améliorer."
    text "Puis j’ai créé des comptes dédiés à ma pratique sur les réseaux sociaux. Et là, tout est devenu plus sérieux..."
    text "Je faisais mon petit contenu et continuait ma vie tranquillement à côté, en passant toujours devant l’Androgame pour aller au travail."
    text "Alors quand ils ont lancé des auditions pour agrandir la troupe, j’ai longuement hésité. Je ne me sentais pas légitime de rentrer dans cette sphère."
    text "Je ne savais pas comment j’allais pouvoir concilier le burlesque et le travail, ce qu’on pourrait dire de moi ou juger de mon drag."
    text "Je pense que j’ai décidé d’arrêter d’essayer de me justifier à un moment, lorsque j’étais aux portes du bâtiment. Après tout, je n’avais rien à perdre et j’aurais regretté de ne pas avoir au moins essayé."
    text "Je ne pensais pas être sélectionné.e, encore moins de passer un entretien avec Mother, la patronne du cabaret. Je n’ai pas trop compris, mais elle m’a parlé des règles de conduite au sein de la troupe et envers les clients, puis d’une période d’essai..."

    stop ambiance fadeout 4.0

    text "J’avais du mal à réaliser, mais on a convenu d’une nouvelle date d’entretien, en journée quand le cabaret serait vide, où elle m’expliquerait plus en détails le fonctionnement des backstages."

    play music CabaretEntrance fadein 0.1
    hide devanture



    show auditorium  
    with fade

    show mother at tall_center with fade


#0.2

    play ambiance AmbAndrogameDay fadein 1

    mother "Bienvenue dans l'Androgame! J'espère que tu as fait bonne route."

    queue music CabaretIntro
    queue music CabaretLightVerse
    
    mother "Tu avais l’air de dire dans nos échanges que tu n’habitais pas trop loin, le chemin n’a pas dû être bien  compliqué."
    text "En effet, une fois passée la porte pivotante, la hauteur sous plafond et les lustres géométriques faillirent me donner un torticolis."

   

    text "Je devais presque plisser les yeux pour repérer tous les petits détails dans la marqueterie, les dorures et les formes dans le papier peint."
    anthrax "Oui. Et puis, c’est le genre d’établissement qu’il est difficile de louper!"
    mother "Aha! Tu m’en vois ravie de l’entendre."
    mother "Je ne fais pas te faire patienter plus longtemps... Commençons par te faire une petite visite des lieux. Promis, tu vas t’y retrouver bien vite"

    queue music CabaretLightChorus

    mother "En arrivant, tu es passé.e par le lobby, le hall d’entrée, l’accueil... Tu peux l’appeler comme tu veux. Mais dans l’idée, passé ce guichet, les clients payent!"
    mother "Ce n’est pas trop dans notre politique cette histoire du \"le client est roi\", mais tu apprendras vite que c’est là que les pourboires se cachent"

    mother "Et nous voici donc dans l’auditorium! Il sera un peu comme ton meilleur ennemi, car peu importe le trac ou qui se retrouvera dans le public, il faudra grimper sur les planches!"
    mother "Après, si tu es ici aujourd’hui, c’est par ce que c’est justement le genre de chose qui t’anime: te mettre en scène..."
    text "Je ne l’avais pas encore abordé de cette perspective, mais l’idée d’être au milieu de cette scène, avec tous les regards tournés vers moi, m’excitait autant que me faisait appréhender."
    text "Je mis cette pensée sur le compte de l'inexpérience, et continua ma visite avec Mother"

    hide mother 

    stop music fadeout 1
    stop ambiance fadeout 10.0


#0.5
    hide auditorium 
    show loges 
    with fade
    play music BackstageLoop

    show mother at tall_right  with dissolve


    text "Nous sommes monté.e.s sur la scène et l'avons traversée avant de passer derrière les épais rideaux de velours. Nous sommes passé.e.s dans un véritable dédale de couloirs tandis qu'elle ouvrait quelques portes et m'expliquait la fonction de chaque pièce." 
    text "Ici, la réserve des costumes ; où les armatures de dos, de hanches, d'épaules à plumes d'autruche, de floss, d'oie ou de faisan ; et les casques grandioses à strass, sequins, perles de verre ou fausses pierres précieuses, se faisaient la compétition." 
    text "Là, l'inventaire des décors roulants, barres de pole dance, accessoires de scène et de cirque pour les tours plus acrobatiques." 
    text "Déjà que je ne savais pas encore vers quelle pratique je souhaitais me spécialiser, submergé.e par tout ceci, j'en étais d'autant plus perdu.e..."
    stop music fadeout 1.5
    text "Nous avons fini par pousser une dernière porte, celle des loges et avons été accueilli.e.s par une ambiance des plus..."
    text "Studieuse."
    
    play ambiance AmbLoges fadein 1
    play music BackstageDrumLoop fadein 1.0 volume 0.5

    imani "Ok, hear me out... Je dis simplement que si l'on veut garder une logique dans la suite de nos numéros, on va devoir inverser l'ordre dans lequel on passe pour pouvoir faire de la place aux nouvelles."

    show imani_neutre at tall_left  with dissolve

    text "L'homme qui venait de prendre la parole était en train de gribouiller avec insistance un schéma dans son carnet, une aiguille à coudre entre les lèvres et une pièce de tissu sur les genoux, à laquelle il semblait broder des sequins un à un."

    inconnu "Girl... J'entends, et je suis d'accord sur le fond. Mais on ne les connaît même pas encore et on ne sait pas quels numéros iels vont présenter, ou si même iels en ont... Tu es en train de te faire des plans sur la comète, ma belle."

    text "Les doigts couverts de gel et un peigne à la main, la personne qui venait de lui répondre était en train de styliser une perruque noire de jais sur une tête de mannequin en plastique." 
    text "Iel y plaquait les cheveux contre le front en de jolies boucles bien définies, et y fixait des perles nacrées avec un pistolet à colle." 
    text "Un autre garçon, plus silencieux, avait la tête baissée sur une armature de fils de fer artisanale qu'il pliait à l'aide d'une pince, et bloquait fermement avec du chaterton."
    
    hide mother 
    show aimee_neutre at tall_right  with dissolve

    inconnu "Et toi Del'? Qu'est-ce que tu en penses?"

    anthrax "Relevant la tête, le concerné remarqua qu'iels n'étaient plus trois dans la pièce et me fixa un instant, avant de se retourner vers ses interlocuteur.ice.s."

    hide imani_neutre 
    show leandre_neutre at tall_left  with dissolve

    delinconnu "Je pense qu'on devrait leur demander directement..." 

    text "Les deux autres se sont retourné.e.s vers l'encadrement de porte dans lequel nous nous tenions, Mother et moi." 

    delinconnu "Ou alors que ce serait justement l'occasion parfaite pour nous de revoir nos propres tours..." 

    stop music fadeout 1.0

    anthrax "Un court silence s'est installé, tandis que nous nous regardions dans le blanc des yeux, ne sachant pas tellement qui devait prendre la parole et que dire."

    hide aimee_neutre 
    hide leandre_neutre 
    show mother at tall_center  with dissolve

    mother "Oh! Je vois que vous faites connaissance! Les filles, je vous présente [player_name], iel nous rejoindra sous peu le temps d'arranger le spectacle, et je compte sur vous pour l'acceuillir comme il se doit."

    play music CabaretLightChorus fadein 0.5 volume 1.0

    anthrax "Semblant sortir de leur torpeur et reprendre leurs esprits, les artistes drag face à moi me sourirent et commencèrent à faire un tour des présentations."
    
    hide mother 
    show imani_neutre at tall_center with dissolve

    peacock "Pardon, on a dû te sembler hyper antipathiques avec notre absence de réaction! Moi c'est Imani. Parfois on s'appelle aussi par nos noms de scène, donc tu peux aussi m'appeler Peacock si tu en as envie."
    
    hide imani_neutre 
    show mother at tall_center with dissolve

    mother "Imani se spécialise dans tout ce qui est du ressort de la performance vocale. Lipsync, chant, reading, shading, imitation... Si tu as des conseils de ce côté à aller chercher, c'est vers elle."
    
    hide mother 
    show imani_neutre at tall_center with dissolve

    peacock "Ah oui! Et pour les pronoms, tu peux utiliser ceux dont tu as envie, je ne suis pas très regardant. Je me genre moi-même souvent au féminin."
    
    hide imani_neutre 
    show mother at tall_center with dissolve

    mother "Le petit timide là, qui essaye de faire en sorte de se faire oublier, c'est Léandre."

    text "Prit en flagrant délit, le jeune homme tourna au pivoine et balbutia, mal à l'aise."
    
    hide mother 
    show leandre_neutre at tall_center with dissolve
    
    leandre "N-Non! C'est juste que... J'ai toujours un peu de mal avec les nouvelles personnes. Excuse-moi... Oui, donc moi, c'est Léandre, j'utilise il/lui, et je fais principalement de l'effeuillage burlesque. C'est assez classique..."
    
    hide leandre_neutre 
    show aimee_neutre at tall_center with dissolve
    
    inconnu "C'est tout sauf classique, ton striptease!"

    text "Léandre se renfrogna davantage. Apparemment, les deux étaient suffisamment bon.ne.s ami.e.s pour se taquiner et s'embarrasser ainsi."
    
    gatsby "Du coup, vu qu'on doit toujours parler à sa place, son nom de drag est Delaunay. Et moi c'est Gatsby! "
    gatsby "Parce que je suis magnifique, et que je n'avais pas plus d'inspi que ça au moment de choisir. Je me genre au neutre, c'est à dire avec ellui/iel. "
    gatsby "C'est non-négociable. "
    gatsby "Mais mon vrai prénom, c'est Aimé.e, avec un point. Pareil que Pea, tu peux aussi m'appeler comme ça si tu en as envie."
    
    stop ambiance fadeout 1
    stop music fadeout 2.0
    hide aimee_neutre 
    jump route_choice_intro





label route_choice_intro:
    show loges 
    show mother at tall_right 
    mother "Alors [player], si tu devais choisir l'un de mes \"babies\" comme marrain ou parraine, qui est-ce que tu désignerais ?" with fade
    hide loges 
    hide devanture 
    hide mother 
    stop music fadeout 0.1
    $ _window_hide()
    $ renpy.pause(0, hard=True)
    $ quick_menu = False
    jump choose_route