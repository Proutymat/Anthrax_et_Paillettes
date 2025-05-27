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

image CG_delaunay = "images/CGs/delaunay.jpg"

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
define audio.BarNeutral = "audio/Music/RUN_BarNeutral_V1.ogg"


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



label delaunay_start:
$ persistent.bg_parallax = True
$ quick_menu = True
scene black with fade
show loges
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

play music BarNeutral

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

stop music fadeout 2.0

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
    call final_delaunay


#DEL.6.BAD
label del_6_bad:
    $ quick_menu = True

    anthrax "WIP"
    mother "WIP"
    call final_delaunay

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