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

    renpy.music.register_channel("ambiance", "sfx", True)


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

image Mother:
    "concept_mother"
    zoom 0.35

image Delaunay In Neutre:
    "concept_delaunay_in"
    zoom 0.35

image Delaunay Out Neutre:
    "concept_delaunay_out"
    zoom 0.35

image Gatsby In Neutre:
    "concept_gatsby_in"
    zoom 0.35

image Gatsby Out Neutre:
    "concept_gatsby_out"
    zoom 0.35

image Peacock In Neutre:
    "concept_peacock_in"
    zoom 0.35

image Peacock Out Neutre:
    "concept_peacock_out"
    zoom 0.35

image Auditorium = "Backgrounds/concept_auditorium.png"

transform tall_right:
    zoom 2.8
    xalign 0.90
    yalign 1.0


# Liste des sfx
define type_sounds = ['TextMix-001.ogg','TextMix-002.ogg','TextMix-003.ogg','TextMix-004.ogg','TextMix-005.ogg','TextMix-006.ogg','TextMix-007.ogg','TextMix-008.ogg','TextMix-009.ogg','TextMix-010.ogg']

# Liste des ambiances
#define audio.AmbAndrogameDay = "Amb_AndrogameDay_V2.wav"
#efine audio.AmbLoges = "Amb_LogesWithStinger_V1.wav"

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
define mother = Character('Mother', color="#880000", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=25, callback=type_sound, cb_cps=25)
define anthrax = Character('Anthräx', color="#6600b9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=35, callback=type_sound, cb_cps=35)
define delaunay = Character('Delaunay', color="#2d9ead", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define gatsby = Character('Gatsby', color="#003099", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define peacock = Character('Peacock', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define leandre = Character('Léandre', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define aimee = Character('Aimé.e', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define imani = Character('Imani', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define inconnu = Character('???', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define delinconnu = Character('Del?', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define player = Character('[player_name]', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)



label start:

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
    scene black
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

    scene concept_auditorium

    show Mother at tall_right

#0.2

    play ambiance "Amb_AndrogameDay_V1.ogg" fadein 1

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

    stop music fadeout 2.0
    ##stop ambiance fadeout 10.0


#0.5

    anthrax "Nous sommes monté.e.s sur la scène et l'avons traversée avant de passer derrière les épais rideaux de velours. Nous sommes passé.e.s dans un véritable dédale de couloirs tandis qu'elle ouvrait quelques portes et m'expliquait la fonction de chaque pièce." 
    anthrax "Ici, la réserve des costumes ; où les armatures de dos, de hanches, d'épaules à plumes d'autruche, de floss, d'oie ou de faisan ; et les casques grandioses à strass, sequins, perles de verre ou fausses pierres précieuses, se faisaient la compétition." 
    anthrax "Là, l'inventaire des décors roulants, barres de pole dance, accessoires de scène et de cirque pour les tours plus acrobatiques." 
    anthrax "Déjà que je ne savais pas encore vers quelle pratique je souhaitais me spécialiser, submergé.e par tout ceci, j'en étais d'autant plus perdu.e..." 
    anthrax "Nous avons fini par pousser une dernière porte, celle des loges et avons été accueilli.e.s par une ambiance des plus... Studieuse."

    play ambiance "Amb_LogesWithStinger_V1.ogg" fadein 1

    inconnu "Ok, hear me out... Je dis simplement que si l'on veut garder une logique dans la suite de nos numéros, on va devoir inverser l'ordre dans lequel on passe pour pouvoir faire de la place aux nouvelles."

    anthrax "L'homme qui venait de prendre la parole était en train de gribouiller avec insistance un schéma dans son carnet, une aiguille à coudre entre les lèvres et une pièce de tissu sur les genoux, à laquelle il semblait broder des sequins un à un."

    inconnu "Girl... J'entends, et je suis d'accord sur le fond. Mais on ne les connaît même pas encore et on ne sait pas quels numéros iels vont présenter, ou si même iels en ont... Tu es en train de te faire des plans sur la comète, ma belle."

    anthrax "Les doigts couverts de gel et un peigne à la main, la personne qui venait de lui répondre était en train de styliser une perruque noire de jais sur une tête de mannequin en plastique." 
    anthrax "Iel y plaquait les cheveux contre le front en de jolies boucles bien définies, et y fixait des perles nacrées avec un pistolet à colle." 
    anthrax "Un autre garçon, plus silencieux, avait la tête baissée sur une armature de fils de fer artisanale qu'il pliait à l'aide d'une pince, et bloquait fermement avec du chaterton."

    inconnu "Et toi Del'? Qu'est-ce que tu en penses?"

    anthrax "Relevant la tête, le concerné remarqua qu'iels n'étaient plus trois dans la pièce et me fixa un instant, avant de se retourner vers ses interlocuteur.ice.s."

    delinconnu "Je pense qu'on devrait leur demander directement..." 

    anthrax "Les deux autres se sont retourné.e.s vers l'encadrement de porte dans lequel nous nous tenions, Mother et moi." 

    delinconnu "Ou alors que ce serait justement l'occasion parfaite pour nous de revoir nos propres tours..." 

    anthrax "Un court silence s'est installé, tandis que nous nous regardions dans le blanc des yeux, ne sachant pas tellement qui devait prendre la parole et que dire."

    mother "Les filles, je vous présente [player], iel nous rejoindra sous peu le temps d'arranger le spectacle, et je compte sur vous pour l'accueillir comme il se doit."

    anthrax "Semblant sortir de leur torpeur et reprendre leurs esprits, les artistes drag face à moi me sourirent et commencèrent à faire un tour des présentations."

    imani "Pardon, on a dû te sembler hyper antipathiques avec notre absence de réaction! Moi c'est Imani. Parfois on s'appelle aussi par nos noms de scène, donc tu peux aussi m'appeler Peacock si tu en as envie."

    mother "Imani se spécialise dans tout ce qui est du ressort de la performance vocale. Lipsync, chant, reading, shading, imitation... Si tu as des conseils de ce côté à aller chercher, c'est vers elle."

    imani "Ah oui! Et pour les pronoms, tu peux utiliser ceux dont tu as envie, je ne suis pas très regardant. Je me genre moi-même souvent au féminin."

    mother "Le petit timide là, qui essaye de faire en sorte de se faire oublier, c'est Léandre."

    anthrax "Prit en flagrant délit, le jeune homme tourna au pivoine et balbutia, mal à l'aise."

    leandre "N-Non! C'est juste que... J'ai toujours un peu de mal avec les nouvelles personnes. Excuse-moi... Oui, donc moi, c'est Léandre, j'utilise il/lui, et je fais principalement de l'effeuillage burlesque. C'est assez classique..."

    inconnu "C'est tout sauf classique, ton striptease!"

    anthrax "Léandre se renfrogna davantage. Apparemment, les deux étaient suffisamment bon.ne.s ami.e.s pour se taquiner et s'embarrasser ainsi."

    gatsby "Du coup, vu qu'on doit toujours parler à sa place, son nom de drag est Delaunay. Et moi c'est Gatsby! "
    gatsby "Parce que je suis magnifique, et que je n'avais pas plus d'inspi que ça au moment de choisir. Je me genre au neutre, c'est à dire avec ellui/iel. "
    gatsby "C'est non-négociable. "
    aimee "Mais mon vrai prénom, c'est Aimé.e, avec un point. Pareil que Pea, tu peux aussi m'appeler comme ça si tu en as envie."

    stop ambiance fadeout 1

   
    hide Mother



label route_choice_intro:
    window show 
    mother "Alors [player], si tu devais choisir l'un de mes \"babies\" comme marrain ou parraine, qui est-ce que tu désignerais ?" with fade

    $ _window_hide()
    $ renpy.pause(0, hard=True)
    $ quick_menu = False
   
    call screen choose_route with fade

        
