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

image CG_peacock = "images/CGs/peacock.jpg"

image background_cg = "images/Backgrounds/background_cg.png"

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
define audio.IntroBS = "Hypnotized.mp3"
define audio.IntroCabaret = "AP_ON2.1_V1.ogg"
define audio.Intro2Cabaret = "AP_Intro2_V1.ogg"
define audio.Verse = "AP_Verse_V1.ogg"
define audio.Chorus = "AP_Chorus_V1.ogg"
define audio.BarNeutral = "AP_Bar_V2.ogg"


# Déclarez les personnages utilisés dans le jeu.
define mother = Character('Mother', color="#b51963", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=25, callback=type_sound, cb_cps=25)
define anthrax = Character('Anthräx', color="#9370db", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=35, callback=type_sound, cb_cps=35)
define delaunay = Character('Delaunay', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define gatsby = Character('Gatsby', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define peacock = Character('Peacock', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define leandre = Character('Léandre', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define aimee = Character('Aimé.e', color="#054fb9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define imani = Character('Imani', color="#f57600", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define inconnu = Character('???', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define delinconnu = Character('Del?', color="#faaf90", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define player = Character('[player_name]', color="#9370db", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define staff = Character('Staff', color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)


label peacock_start:
$ quick_menu = True
scene black with fade
show loges
show imani_neutre at tall_center with dissolve


#PEA.1

imani "Je suis flattée"

imani "Alors comme ça je t'ai fait une telle impression ?"

player "Il semblerait, j'adore ta vibe. Tu as un certain talent pour mettre les gens à l'aise."

imani "Ah ça ! On me le dit souvent !"

imani "Même si parfois j'ai l'impression de faire trop vieux jeu."

anthrax "Vieux jeu ? J'aimerais bien croiser la personne qui a dit ça."

imani "Hm... Je pense que je peux définitivement blâmer mon reflet dans le miroir. Pas que ce visage ne soit pas sublime, mais c'est un peu mon meilleur ennemi."

anthrax "Comme dirait RuPaul, il ne faut pas écouter notre 'inner saboteur'."

imani "Word."

imani "Ça te dit de t'installer quelque part de plus cosy pour continuer à discuter ?"

#PEA.2
hide loges
show bar with fade

#Dialogue WIP


#Choix PEA.2
label choix_pea2:
    $ quick_menu = False
    
    show imani_neutre at tall_right
    with fade

    menu: 
        "WIP":
            call pea_2_1
        "WIP":
            call pea_2_2
        "WIP":
            call pea_2_3
          

#PEA.2.1
label pea_2_1:
    $ quick_menu = True
    
    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    peacock "WIP"
    call del_3

#PEA.2.2
label pea_2_2:
    $ quick_menu = True
    
    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    mother "WIP"
    call pea_3

#PEA.2.3
label pea_2_3:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    mother "WIP"
    call pea_3

#PEA.3
#label pea_3:




#Choix PEA.3
label choix_pea3:
    $ quick_menu = False

    show imani_neutre at tall_right
    with fade

    menu: 
        "WIP":
            call pea_3_1
        "WIP":
            call pea_3_2
        "WIP":
            call pea_3_3

#PEA.3.1
label pea_3_1:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    imani "WIP"
    call pea_4

#PEA.3.2
label pea_3_2:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    mother "WIP"
    call pea_4

#PEA.3.3
label pea_3_3:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    mother "WIP"
    call pea_4

#PEA.4
label pea_4:

    anthrax "Debout au milieu de la pièce, Imani était en train de passer le fil de son micro dans les espaces étriqués de son corset et de son padding couleur chair, le passant dans la lanière de son bullet-bra jusque le long de son dos."
    anthrax "Accrochant l'appareil à l'aide d'épingles à sa perruque, elle semblait avoir la tête ailleurs, tout en reproduisant ses gestes millimétrés et à présent routiniers, glissant ensuite le boîtier HF dans sa jarretelle qui avait été modifiée à cet effet."
    anthrax "Peacock enfila ensuite sa robe à dos nu et déclipsa le soutien-gorge pour dissimuler le tissu dépassant dans son costume, n'ayant pas besoin de maintien."
    anthrax "Une étiquette dépassait effrontément du vêtement et je me levai pour remédier à ce problème."
    anthrax "Attends, oups... Je me permets..."
    anthrax "Un peu surprise, Imani remarqua que j'essayais maladroitement d'aider et me laissa faire, avant de me sourire avec un air attendri."

    peacock "Tu es adorable, merci girlie."

    anthrax "Je peux t'aider à quelque chose d'autre ?"

#Choix PEA.4
label choix_pea4:
    $ quick_menu = False

    show imani_neutre at tall_right
    with fade

    menu: 
        peacock "Hm... Je ne sais pas trop. Peut-être peux-tu vérifier l'état des plumes de mes éventails ? Je les ai changées il y a peu, mais elles ont peut-être besoin d'être ébouriffées."
        "Oui, bien sûr. Ca fait longtemps que tu fais ce show? Avec les plumes je veux dire...":
            call pea_4_1
        "Sans soucis! Tu comptes chanter aussi? Je vois que tu as un micro d'installé...":
            call pea_4_2
        "Les ébouriffer? Est-ce que c'est pour mieux te cacher lors de l'effeuillage?":
            call pea_4_3

#PEA.4.1
label pea_4_1:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade
    
    anthrax "Oui, bien sûr. Ca fait longtemps que tu fais ce show? Avec les plumes je veux dire..."

    peacock "Hm... Oui et non. Il a tout de même bien évolué depuis le temps."
    peacock "Évidemment, je me base sur mes atouts, mais l'expérience fait que le show s'est amélioré."
    peacock "Et puis, j'y ai aussi mis de l'effort. J'ai pris des classes, j'ai longtemps itéré, jusqu'à trouver la formule qui me correspondait."
    peacock "Puis, je suis loin d'avoir fini, je compte rester dans le business encore un moment. Le show continuera de progresser dans tous les cas."

    anthrax "Et donc, les plumes, ça vient de quelque part en particulier ?"

    peacock "Eh bien déjà, c'est mon nom de scène. Donc il y a ça... Et puis c'est finalement ce qui m'a fait me rapprocher de l'Androgame."
    peacock "J'ai toujours eu une admiration démesurée pour le monde de la scène, mes parents m'emmenaient toujours en spectacle quand j'étais petit."
    peacock "Ce sont les souvenirs qui me ramènent le plus en enfance."
    peacock "Et une fois, il y avait ces danseuses de cabaret, avec leurs grands éventails à plumes. À partir de ce point, je n'ai jamais lâché cette fixette."

    delaunay "C'est mignon ! Quand j'y repense, mes parents aussi m'emmenaient en spectacle. C'est peut-être de là que ça vient."

    gatsby "Ou d'y avoir été sensibilisé.e au moins. De mon côté, c'était plus les comédies musicales à la télé, du type *Mozart, l'Opéra Rock* ou *1789*."

    peacock "Comme quoi ! Les plumes, la scène, le théâtre... Au final, c'est plus histoire de me rappeler d'où je viens, ce que j'aime et ce qui m'a construit."
    peacock "Et je parle pour plusieurs on dirait."

    anthrax "C'est assez beau comme réflexion. Mais ça ne vous a jamais ennuyé.e.s ?"

    peacock "Peut-être par moments, mais c'est pour ça que je danse, je chante et je fais rire à côté. Je déteste l'idée de ne pas me renouveler et de proposer toujours la même chose."
    peacock "Même si ce n'est pas simple d'innover chaque semaine, c'est quelque chose que je me suis promis de faire."

    peacock "Sinon, autant arrêter le drag maintenant. Ça ne sert à rien d'être boring sur scène..."

    delaunay "Moi, pas du tout... Il y a quelque chose de relaxant à faire un numéro répétitif. On a beau le connaître par cœur, on en découvre toujours de nouvelles facettes."

    gatsby "J'ai une relation un peu plus mitigée avec le mien, puisque j'ai une démarche différente qui est plus de l'ordre de la réconciliation."
    gatsby "Donc parfois, je le déteste, et parfois je l'adore. Mais ennuyant ? Ça, jamais."

    staff "Ok les filles ! Showtime dans dix minutes !"

    peacock "Déjà ?! Bon, plus qu'à se dépêcher..."
    
    call pea_5

#PEA.4.2
label pea_4_2:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "Sans souci ! Tu comptes chanter aussi ? Je vois que tu as un micro d'installé..."

    anthrax "J'étais persuadé.e que tu ne faisais que de la danse..."

    peacock "Il fut une époque, c'était le cas. J'étais encore timide et je reproduisais des pas de chorés que j'avais vus sur les réseaux."

    anthrax "Et qu'est-ce qui a changé depuis ?"

    peacock "Changé ? Honnêtement, énormément de choses, et à la fois, pas tant. J'ai pris en confiance principalement."
    peacock "Je t'avais dit que je bossais en régie avant ? Un peu comme Jazz actuellement."
    peacock "Maintenant, je fais de la radio et du podcast, tout en filant un coup de main de temps en temps, au besoin."
    peacock "La musique a toujours eu une place super importante dans ma vie, et je ne pensais pas être suffisamment talentueuse pour pouvoir partager ça sur scène un jour."
    peacock "Encore une leçon que le drag m'a apprise : ne jamais se douter de ses capacités et savoir se lancer."

    gatsby "On est un peu tous.te.s dans ce cas. Le drag, ça éveille des capacités insoupçonnées. Ou en tout cas, ça nous encourage à nous redécouvrir sous un nouvel angle."

    delaunay "Pendant un long moment, je ne me suis jamais cru capable d'être aussi confiant.e. Encore moins sur scène. Et encore moins en m'effeuillant !"

    peacock "Et moi, je ne me sentais pas suffisamment légitime, ou sexy, ou \"féminine\" pour faire du drag à barbe et rendre hommage à ma culture. Surtout que je viens de loin !"

    anthrax "Ça doit tout de même être super physique de chanter et danser en même temps..."

    peacock "On s'y fait... Et puis, c'est pour ça que je me pose ensuite sur scène pour enchaîner le public."
    peacock "J'ai toujours été un petit clown de service, et l'humour nous rend toujours plus accessible, même envers les personnes qui ne sont pas très familières avec notre art."
    peacock "Autant \"ouvrir la bibliothèque\" en dehors des loges. C'est bien de lire les copines, encore mieux d'en faire profiter tout le monde."

    gatsby "Oui... Enfin, quand tu te décides à tacler, t'en fais pas que tu ne te gardes pas de le faire dans les coulisses."

    delaunay "Et puis, quand tu es dans l'humeur, on en a parfois pour des heures !"

    staff "Ok les filles ! Showtime dans dix minutes !"

    peacock "Déjà ?! Bon, plus qu'à se dépêcher..."

    call pea_5

#PEA.4.3
label pea_4_3:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "Les ébouriffer ? Est-ce que c'est pour mieux te cacher lors de l'effeuillage ?"
    anthrax "Je pensais qu'il n'y avait que Léandre qui faisait ça ici..."

    peacock "L'effeuillage ? Hm... Non, ce n'est vraiment pas mon genre de numéro ça."
    peacock "//Don't get me wrong//, je suis une bombe."
    peacock "Mais me déshabiller sur scène face à tout un public, ça va à l'encontre de ce que je veux transmettre avec ma persona."

    anthrax "Ah bon ? C'est-à-dire ? J'ai du mal à comprendre."

    peacock "Faut que je réussisse à mettre les mots dessus, attends..."
    peacock "En fait, Peacock, elle est sensuelle, mais avec pudeur et une certaine humilité. Elle ne charme pas comme Delaunay, en jouant de son corps. Elle use de ses autres charmes."
    peacock "\"J'use\" de mes autres charmes."

    anthrax "Rien de mal avec un peu de \"body-oh-dy\"..."

    peacock "Entièrement d'accord avec toi. C'est pour ça que j'ai précisé que j'étais une bombe, chéri.e"

    anthrax "Oh, je vois ce que tu sous-entendais par \"humilité\"...~"

    peacock "Touchée... Et shady~"
    peacock "Tu apprends vite~"

    anthrax "J'apprends surtout des meilleurs."

    delaunay "On vous entend à côté ! Faudrait pas non plus nous rendre jaloux.e.s."

    gatsby "Je t'ai vue draguer avec plus de finesse, Pea ! Attention à ne pas te perdre avec l'âge !"

    peacock "Non mais de quoi je me mêle les fouineuses ! Occupez-vous de faire un trait d'eyeliner droit avant de vous intéresser à mes techniques de séduction !"

    anthrax "Ah... Donc c'est là où l'on se situe ?~"

    peacock "Pas encore~ Mais c'est une option tout à fait envisageable."
    peacock "Si nos deux commères nationales arrêtaient de fourrer leur nez là où ça ne les concerne pas !"

    staff "Ok les filles ! Showtime dans dix minutes !"

    peacock "Déjà ?! Bon, plus qu'à se dépêcher..."
   
    call pea_5

#PEA.5
label pea_5:

    anthrax "Les yeux du public étaient encore rivés sur la scène où les restes du précédent numéro se faisaient débarrasser, qu'ils furent forcés de se retourner en entendant une voix rauque et a cappella démarrer le fameux 'Feeling Good' de Nina Simone depuis le fond de la salle."
    anthrax "Les escarpins ancrés dans le marbre du comptoir du bar, un spot détournant sa silhouette en contre-jour pour ajouter un peu de pizzazz à son entrée, elle descendit tout en sensualité en se faisant porter par Doberman."
    anthrax "Imani se saisit des deux grands éventails à plumes que le staff lui proposait et le band lança le top départ de sa performance en arrivant en fanfare."
    anthrax "Se baladant entre les tables, sans manquer une seule note, son chant et sa danse induisaient une certaine transe chez le public ébahi."
    anthrax "Hypnotisante, chacun de ses coups de hanches, tourbillons de plumage et battement de cils soulevaient quelques sifflements jusqu'à ce que sa représentation ne se déplace sur l'estrade."
    anthrax "Tandis que les derniers accords signaient la fin de sa chorégraphie, elle troqua ses éventails pour un tabouret et un verre d'eau, chauffant la salle avec un 'one-woman show' pour introduire le prochain numéro."
    anthrax "Son charisme, sa vivacité d'esprit et sa répartie étaient bien connus des habitué.e.s du cabaret, qui venaient parfois uniquement pour participer à cet instant léger et sarcastique."
    anthrax "Peacock se faisait règle de ne jamais reproduire un gig deux fois, de la même manière que ses tenues selon ses propres termes."
  
    call pea_6

#PEA.6
label pea_6:


#Dialogue WIP 


#Choix PEA.6
label choix_pea6:
    $ quick_menu = False
    
    show imani_neutre at tall_right
    with fade

    menu: 
        "WIP":
            call pea_6_good
        "WIP":
            call pea_6_bad

#PEA.6.GOOD
label pea_6_good:
    $ quick_menu = True
    
    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    imani "WIP"
    call final_peacock

#PEA.6.BAD
label pea_6_bad:
    $ quick_menu = True
    
    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    mother "WIP"
    call final_peacock

    

label final_peacock:
    hide imani_neutre
    hide loges

    $ quick_menu = False
    
    scene background_cg
    show CG_peacock with fade


    pause 1.0
    "Nouvelle illustration débloquée"
    hide CG_peacock with fade
    $ persistent.peacock_unlocked = True
    "Interview et musiques débloquées"
    pause 1.0

    scene black with fade

    $ renpy.full_restart()
