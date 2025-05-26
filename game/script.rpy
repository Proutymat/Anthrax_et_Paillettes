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
define type_sounds = ['TextMix-001.ogg','TextMix-002.ogg','TextMix-003.ogg','TextMix-004.ogg','TextMix-005.ogg','TextMix-006.ogg','TextMix-007.ogg','TextMix-008.ogg','TextMix-009.ogg','TextMix-010.ogg']

# Liste des musiques
define audio.GoodVibeIntro = "ON_GoodVibeIntro_V2.ogg"
define audio.IntroGoodVibe1 = "ON_GoodVibeA_V2.ogg"
define audio.IntroGoodVibe2 = "ON_GoodVibeB_V2.ogg"
define audio.IntroGoodVibe3 = "AP_IntroGoodVib3_V1.ogg"
define audio.IntroGoodVibe4 = "AP_IntroGoodVib4_V1.ogg"
define audio.IntroCabaret = "AP_ON2.1_V1.ogg"
define audio.Intro2Cabaret = "AP_Intro2_V1.ogg"
define audio.Verse = "ON_CabaretLightVerse_V1.ogg"
define audio.CabaretLightChorus = "ON_CabaretLightChorus_V1.ogg"
define audio.CabaretLightSolo = "ON_CabaretLightSolo_V1.ogg"
define audio.BarNeutral = "AP_Bar_V2.ogg"
define audio.BalconyIntro = "ON_Backstage_V1.ogg"
define audio.BalconyLoop = "ON_BackstageLoop_V1.ogg"
define audio.Backstage = "ON_Loge_V1.ogg"

# Déclarez les personnages utilisés dans le jeu.
define mother = Character('Mother', color="#b51963", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=25, callback=type_sound, cb_cps=25)
define anthrax = Character('Anthräx', color="#5928ed", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=35, callback=type_sound, cb_cps=35)
define delaunay = Character('Delaunay', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define gatsby = Character('Gatsby', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define peacock = Character('Peacock', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define leandre = Character('Léandre', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define aimee = Character('Aimé.e', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define imani = Character('Imani', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define inconnu = Character('???', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define delinconnu = Character('Del?', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define player = Character('[player_name]', color="#5928ed", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define staff = Character('Staff', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)




label start:
    $ quick_menu = False
    scene black
    with fade
    $player_name = renpy.input("Choisis le prénom d'Anthräx, ton personnage...")

    $ player_name = player_name.strip()
    if player_name == "":
        $player_name = "Moumine"
         
    menu:
        "Tu es sûr de consever [player_name] ?"
        "oui":
            jump onboarding
        "non":
            jump start

#0.1    
label onboarding:
    show devanture
    with fade
    $ quick_menu = True  


    play music GoodVibeIntro fadein 3.0

    anthrax "C’est dingue à quel point ce cabaret a reprit ses lettres de noblesse."
    anthrax "Je me souviens encore de quand je passais devant pour aller prendre le métro... Complètement défraichit, la pierre sale et les fenètres brisées."
    anthrax "On se demandait quand est-ce qu’ils finiraient par abréger ses souffrances et le démolir."

    queue music IntroGoodVibe1
    queue music IntroGoodVibe2
    
    anthrax "Cela fait un moment maintenant qu’il a été reprit, et après de longs et nombreux travaux, il fait à présent revivre le quartier comme je ne l’ai jamais vu auparavant."
    anthrax "Il me décroche toujours un sourire quand je passe devant..."
    anthrax "Et puis même au sein de la commu’, ça a fait jaser. Toutes les têtes d’affiches sont queer."
    anthrax "Ça fait presque bizarre de nous voir se réapproprier une époque dans laquelle on n’avait pas le droit de réellement exister."
    anthrax "Je suis sûr.e qu’on n’aurait jamais autant flamboyé que dans les années 20... C’est peut-être pour ça qu’on était \"interdits\"? On aurait trop volé la vedette aux hétéros."
    anthrax "Les plumes, la fourrure, les paillettes, le champagne, le charleston, l’occasionnel rail de coke... Les années folles quoi."
    anthrax "C’est ce qui m’a motivé à me lancer dans le drag finalement..."
    anthrax "J’ai toujours été intrigué.e par cette forme d’expression. Et à voir ces artistes bourré.e.s de talent faire leur show, à deux pas de chez moi... Je me suis laissé.e tenter."
    anthrax "Au début, j’en avais un peu honte. Je me costumais en cachette dans mon appart, et pour être honnête, c’était peut-être pour le mieux."
    anthrax "Mes premières tentatives de make-up étaient catastrophiques... Mais au fur et à mesure, j’ai pris le coup de pinceau."
    anthrax "Ce que je pensais être une lubie est finalement devenu un hobby."
    anthrax "J’ai pris des classes pour apprendre à coudre et danser, au point où même mes ami.e.s ont capté ce qui se tramait et se sont prêté.e.s au jeu pour m’aider à m’améliorer."
    anthrax "Puis j’ai créé des comptes dédiés à ma pratique sur les réseaux sociaux. Et là, tout est devenu plus sérieux..."
    anthrax "Je faisais mon petit contenu et continuait ma vie tranquillement à côté, en passant toujours devant l’Androgame pour aller au travail."
    anthrax "Alors quand ils ont lancé des auditions pour agrandir la troupe, j’ai longuement hésité. Je ne me sentais pas légitime de rentrer dans cette sphère."
    anthrax "Je ne savais pas comment j’allais pouvoir concilier le burlesque et le travail, ce qu’on pourrait dire de moi ou juger de mon drag."
    anthrax "Je pense que j’ai décidé d’arrêter d’essayer de me justifier à un moment, lorsque j’étais aux portes du bâtiment. Après tout, je n’avais rien à perdre et j’aurais regretté de ne pas avoir au moins essayé."
    anthrax "Je ne pensais pas être sélectionné.e, encore moins de passer un entretien avec Mother, la patronne du cabaret. Je n’ai pas trop compris, mais elle m’a parlé des règles de conduite au sein de la troupe et envers les clients, puis d’une période d’essai..."

    stop music fadeout 5.0

    anthrax "J’avais du mal à réaliser, mais on a convenu d’une nouvelle date d’entretien, en journée quand le cabaret serait vide, où elle m’expliquerait plus en détails le fonctionnement des backstages."

    play music IntroCabaret fadein 0.1
    hide devanture
    
    show auditorium  
    with fade

    show mother at tall_center with fade


#0.2

    mother "Bienvenue dans l'Androgame! J'espère que tu as fait bonne route."
    mother "Tu avais l’air de dire dans nos échanges que tu n’habitais pas trop loin, le chemin n’a pas dû être bien  compliqué."
    anthrax "En effet, une fois que j’avais passé la porte pivotante, la hauteur sous plafond et les lustres géométriques faillirent me donner un torticolis."

    queue music Intro2Cabaret
    queue music Verse

    anthrax "Je devais presque plisser les yeux pour repérer tous les petits détails dans la marqueterie, les dorures et les formes dans le papier peint."
    anthrax "Oui. Et puis, c’est le genre d’établissement qu’il est difficile de louper!"
    mother "Aha! Tu m’en vois ravie de l’entendre."
    mother "Je ne fais pas te faire patienter plus longtemps... Commençons par te faire une petite visite des lieux. Promis, tu vas t’y retrouver bien vite"
    mother "En arrivant, tu es passé.e par le lobby, le hall d’entrée, l’accueil... Tu peux l’appeler comme tu veux. Mais dans l’idée, passé ce guichet, les clients payent!"
    mother "Ce n’est pas trop dans notre politique cette histoire du \"le client est roi\", mais tu apprendras vite que c’est là que les pourboires se cachent"

    queue music Chorus

    mother "Et nous voici donc dans l’auditorium! Il sera un peu comme ton meilleur ennemi, car peu importe le trac ou qui se retrouvera dans le public, il faudra grimper sur les planches!"
    mother "Après, si tu es ici aujourd’hui, c’est par ce que c’est justement le genre de chose qui t’anime: te mettre en scène..."
    anthrax "Je ne l’avais pas encore abordé de cette perspective, mais l’idée d’être au milieu de cette scène, avec tous les regards tournés vers moi, m’excitait autant que me faisait appréhender."

    hide mother 

    stop music fadeout 2.0

#0.5
    hide auditorium 
    show loges 
    with fade

    show mother at tall_right  with dissolve


    anthrax "Nous sommes monté.e.s sur la scène et l'avons traversée avant de passer derrière les épais rideaux de velours. Nous sommes passé.e.s dans un véritable dédale de couloirs tandis qu'elle ouvrait quelques portes et m'expliquait la fonction de chaque pièce." 
    anthrax "Ici, la réserve des costumes ; où les armatures de dos, de hanches, d'épaules à plumes d'autruche, de floss, d'oie ou de faisan ; et les casques grandioses à strass, sequins, perles de verre ou fausses pierres précieuses, se faisaient la compétition." 
    anthrax "Là, l'inventaire des décors roulants, barres de pole dance, accessoires de scène et de cirque pour les tours plus acrobatiques." 
    anthrax "Déjà que je ne savais pas encore vers quelle pratique je souhaitais me spécialiser, submergé.e par tout ceci, j'en étais d'autant plus perdu.e..." 
    anthrax "Nous avons fini par pousser une dernière porte, celle des loges et avons été accueilli.e.s par une ambiance des plus... Studieuse."

    play music BarNeutral fadein 0.1

    show imani_neutre at tall_left  with dissolve

    inconnu "Ok, hear me out... Je dis simplement que si l'on veut garder une logique dans la suite de nos numéros, on va devoir inverser l'ordre dans lequel on passe pour pouvoir faire de la place aux nouvelles."
    

    anthrax "L'homme qui venait de prendre la parole était en train de gribouiller avec insistance un schéma dans son carnet, une aiguille à coudre entre les lèvres et une pièce de tissu sur les genoux, à laquelle il semblait broder des sequins un à un."

    inconnu "Girl... J'entends, et je suis d'accord sur le fond. Mais on ne les connaît même pas encore et on ne sait pas quels numéros iels vont présenter, ou si même iels en ont... Tu es en train de te faire des plans sur la comète, ma belle."

    anthrax "Les doigts couverts de gel et un peigne à la main, la personne qui venait de lui répondre était en train de styliser une perruque noire de jais sur une tête de mannequin en plastique." 
    anthrax "Iel y plaquait les cheveux contre le front en de jolies boucles bien définies, et y fixait des perles nacrées avec un pistolet à colle." 
    anthrax "Un autre garçon, plus silencieux, avait la tête baissée sur une armature de fils de fer artisanale qu'il pliait à l'aide d'une pince, et bloquait fermement avec du chaterton."
    
    hide mother 
    show aimee_neutre at tall_right  with dissolve

    inconnu "Et toi Del'? Qu'est-ce que tu en penses?"

    anthrax "Relevant la tête, le concerné remarqua qu'iels n'étaient plus trois dans la pièce et me fixa un instant, avant de se retourner vers ses interlocuteur.ice.s."

    hide imani_neutre 
    show leandre_neutre at tall_left  with dissolve

    delinconnu "Je pense qu'on devrait leur demander directement..." 

    anthrax "Les deux autres se sont retourné.e.s vers l'encadrement de porte dans lequel nous nous tenions, Mother et moi." 

    delinconnu "Ou alors que ce serait justement l'occasion parfaite pour nous de revoir nos propres tours..." 

    anthrax "Un court silence s'est installé, tandis que nous nous regardions dans le blanc des yeux, ne sachant pas tellement qui devait prendre la parole et que dire."

    hide aimee_neutre 
    hide leandre_neutre 
    show mother at tall_center  with dissolve

    mother "Les filles, je vous présente [player], iel nous rejoindra sous peu le temps d'arranger le spectacle, et je compte sur vous pour l'accueillir comme il se doit."

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

    anthrax "Prit en flagrant délit, le jeune homme tourna au pivoine et balbutia, mal à l'aise."
    
    hide mother 
    show leandre_neutre at tall_center with dissolve
    
    leandre "N-Non! C'est juste que... J'ai toujours un peu de mal avec les nouvelles personnes. Excuse-moi... Oui, donc moi, c'est Léandre, j'utilise il/lui, et je fais principalement de l'effeuillage burlesque. C'est assez classique..."
    
    hide leandre_neutre 
    show aimee_neutre at tall_center with dissolve
    
    inconnu "C'est tout sauf classique, ton striptease!"

    anthrax "Léandre se renfrogna davantage. Apparemment, les deux étaient suffisamment bon.ne.s ami.e.s pour se taquiner et s'embarrasser ainsi."
    
    gatsby "Du coup, vu qu'on doit toujours parler à sa place, son nom de drag est Delaunay. Et moi c'est Gatsby! "
    gatsby "Parce que je suis magnifique, et que je n'avais pas plus d'inspi que ça au moment de choisir. Je me genre au neutre, c'est à dire avec ellui/iel. "
    gatsby "C'est non-négociable. "
    gatsby "Mais mon vrai prénom, c'est Aimé.e, avec un point. Pareil que Pea, tu peux aussi m'appeler comme ça si tu en as envie."
    
    hide aimee_neutre 

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

        
label delaunay_start:

$ quick_menu = True
show devanture onlayer farBack
show leandre_neutre at tall_center with dissolve

#DEL.1
leandre "Hey... Hum... Je suis content que tu m’aies choisi. Je ne pensais pas trop que ce serait le cas."

anthrax "Ah oui? Pourquoi donc?"

leandre "Oh, je ne sais pas trop. Je suis un peu plus discret que les autres, disons..."

anthrax "Discret? Ce n’est pas cette impression que tu m’as donné.e."

leandre "Vraiment? Je suis soulagé alors!"

leandre "Est-ce que tu souhaites qu’on discute autour d’un verre au bar? J’aimerais beaucoup en apprendre plus sur ton drag."

leandre "Et puis, ce sera plus simple aussi pour t’aider à construire ton acte lorsque Mother te donnera le feu vert"

anthrax "Ça, je ne dis pas non!"


#DEL.2
anthrax "Nous sommes arrivé.e.s dans l'auditorium et nous sommes approché.e.s du comptoir derrière lequel brillaient un mur de bouteilles de formes et couleurs uniques. Le paradis du parfait mixologue."
anthrax "Nous avions depuis le bar une vue imprenable sur la scène, légèrement en contrebas. Les tablées y étaient déjà dressées et se regroupaient autour du big band et de l'estrade secondaire au centre de la pièce."
anthrax "L'immense lustre duquel pendaient des larmes de verre reflétait les spots de lumière à la manière d'une boule à facettes sur le papier peint texturé. Léandre s'assît sur l'une des chaises hautes de bois verni et commanda une citronnade au barman, et moi un allongé."

leandre "Alors dis-moi, qu’est-ce qui t’amène ici ?"

anthrax "M-Moi ? Comme ça ? Directement ?"

leandre "Eh bien... Oui ? Enfin, ça me semblait être un bon début de conversation..."

anthrax "Oh. Eh bien... J’ai commencé le drag dans le confort de mon appart, sur les réseaux sociaux. Je n’ai jamais mis les pieds dans une troupe. Ou même un cabaret pour tout te dire."
anthrax "C’est un peu impressionnant. Je me demande si j’ai ma place. Je ne réalise pas que je l’ai remportée, cette audition."

leandre "Hm... C’est bien le genre de Mother de recruter quelqu’un de ton acabit. Plein.e de potentiel, mais qui ne sait pas par où commencer. J’étais exactement pareil."

anthrax "Ça fait longtemps que tu as intégré la troupe ?"

leandre "Environ cinq ans je dirais ? Techniquement, je suis le doyen, parmi les autres que tu as croisé.e.s tout à l’heure."
leandre "Enfin, officiellement, Imani a travaillé ici depuis plus longtemps, mais n’a intégré la troupe que depuis deux ans."
leandre "Et Aimé.e est arrivé.e peut-être un an après moi ?"
leandre "Techniquement, cela fait déjà des années que l’on se côtoie."

anthrax "Ah oui. Tout de même... Et il y a eu du roulement dans l’équipe ?"

leandre "Et bien, quelques collègues sont parti.e.s, revenu.e.s, mais au final nous sommes les trois qui ayons tenu sur le long terme."
leandre "Et puis, comparé.e.s aux autres, nous n’avons pas fait trop d’histoires. C’est beaucoup pour ces raisons que les contrats cassent, malgré toute la bonne volonté que l’on puisse y mettre."

anthrax "Et toi ? Qu’est-ce qui t’a lancé dans le drag ?"

leandre "Et bien... J’étais en train de décrocher des études, j’étais dans la panade financière, j’étais en pleine découverte de mon identité de genre."
leandre "Vraiment, une vraie crise de la vingtaine... J’en ris maintenant, mais ce n’était pas du tout drôle à l’époque."
leandre "Et finalement, Mother m’a pris sous son aile et m’a aidé à me sortir de tout cela."

#Choix DEL.2
label choix_del2:
    $ quick_menu = False
    
    menu: 
        anthrax "Et finalement, Mother m’a pris sous son aile et m’a aidé à me sortir de tout cela."
        "Oh! Tu as transitionné?":
            call del_2_1
        "Et comment est-ce que tu as rencontré Mother?":
            call del_2_2
        "choix del.2.3":
            call del_2_3
          

#DEL.2.1
label del_2_1:
    $ quick_menu = True

    anthrax "Oh! Tu as transitionné? !"
    leandre "Yep."
    call del_3

#DEL.2.2
label del_2_2:
    $ quick_menu = True

    anthrax "Et comment est-ce que tu as rencontré Mother?"
    mother "Ma belle attends je t'explque"
    call del_3

#DEL.2.3
label del_2_3:
    $ quick_menu = True

    anthrax "Choix wip"
    mother "Script wip"
    call del_3

#DEL.3
label del_3:


#Dialogue WIP 


#Choix DEL.3
label choix_del3:
    $ quick_menu = False

    menu: 
        "WIP":
            call del_3_1
        "WIP":
            call del_3_2
        "WIP":
            call del_3_3

#DEL.3.1
label del_3_1:
    $ quick_menu = True

    anthrax "WIP"
    leandre "WIP"
    call del_4

#DEL.3.2
label del_3_2:
    $ quick_menu = True

    anthrax "WIP"
    mother "WIP"
    call del_4

#DEL.3.3
label del_3_3:
    $ quick_menu = True

    anthrax "WIP"
    mother "WIP"
    call del_4

#DEL.4
label del_4:

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

    menu: 
        anthrax "Qu'est-ce que tu fais à jouer le timide ? Approche, je ne vais pas te manger."
        "Franchement, tu me manges quand tu veux":
            call del_4_1
        "J'adore la manière dont tu prends confiance en toi avec Delaunay":
            call del_4_2
        "Timide? Moi?":
            call del_4_3

#DEL.4.1
label del_4_1:
    $ quick_menu = True

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

    staff "Ok les filles ! Showtime dans dix minutes !"

    delaunay "Mon dieu, j'ai encore tellement à faire ! Vite [player] ! Un coup de main, vite !"

    call del_5

#DEL.4.2
label del_4_2:
    $ quick_menu = True

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

    staff "Ok les filles ! Showtime dans dix minutes !"

    delaunay "Mon dieu, j'ai encore tellement à faire ! Vite [player] ! Un coup de main, vite !"

    call del_5

#DEL.4.3
label del_4_3:
    $ quick_menu = True

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

    staff "Ok les filles ! Showtime dans dix minutes !"

    delaunay "Mon dieu, j'ai encore tellement à faire ! Vite [player] ! Un coup de main, vite !"

    call del_5

#DEL.5
label del_5:

    anthrax "L’entracte arrivait déjà à sa fin et l’atmosphère était bouillonnante dans les coulisses. Derrière le rideau, les kittens et les régisseur.euse.s s’activaient à déplacer le décor en silence."
    anthrax "Soudainement, un spot se braqua sur le velours et un “bang” de trompettes réveilla la foule. Puis une longue jambe dévoila sensuellement sa résille en sortant de l’entrouverture."
    anthrax "Au rythme de la musique, Delaunay fit son apparition sur le devant de la scène, sous les hurlements des fanatiques du premier rang."
    anthrax "Le temps qu’il ne chauffe la salle, les préparatifs de l’arrière-scène arrivaient à leur fin. Le rideau tomba et dévoila un immense verre à martini duquel s’échappaient des volutes de fumée."
    anthrax "Delaunay continuait d'effeuiller son costume jusqu’à grimper l’échelle et s’asseoir, dos courbé, sur le bord du verre."
    anthrax "Laissant la tension gagner le public, il finit par s’y glisser en arrière, laissant l’eau déborder ostensiblement sur la scène."
    anthrax "Il continua de se déshabiller avec lenteur et adresse, jusqu’à sortir de son corset un sous-vêtement trempé qu’il jeta insolemment."
    anthrax "L’effet dupait aisément son public et signa la fin de son acte."
    anthrax "Il se couvrit d’un long kimono et se fit aider pour descendre sans glisser avant de saluer fièrement les spectateur.ice.s, son make-up intact et un grand sourire aux lèvres."

#Dialogue WIP 


call del_6

#DEL.6
label del_6:


#Dialogue WIP 


#Choix DEL.6
label choix_del6:
    $ quick_menu = False

    menu: 
        "WIP":
            call del_6_good
        "WIP":
            call del_6_bad

#DEL.6.GOOD
label del_6_good:
    $ quick_menu = True

    anthrax "WIP"
    leandre "WIP"
    hide leandre_neutre onlayer characters
    hide devanture onlayer back
    hide devanture onlayer farback
    call final_delaunay


#DEL.6.BAD
label del_6_bad:
    $ quick_menu = True

    anthrax "WIP"
    mother "WIP"
    hide leandre_neutre onlayer characters
    hide devanture onlayer back
    hide devanture onlayer farback
    call final_delaunay

label final_delaunay:
    $ quick_menu = False
    image CG_delaunay = "images/CGs/delaunay.jpg"
    scene CG_delaunay with fade
    "Nouvelle illustration débloquée"
    hide CG_delaunay with fade
    $ persistent.delaunay_unlocked = True
    "Interview et musiques débloquées"
    pause 1.0

    scene black with fade

    $ renpy.full_restart()