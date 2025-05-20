#Fonctions custom

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

image Mother:
    "mother"
    zoom 0.35

image Delaunay Neutre:
    "delaunay_neutre"
    zoom 0.35

image Léandre Neutre:
    "leandre_neutre"
    zoom 0.35

image Gatsby Neutre:
    "gatsby_neutre"
    zoom 0.35

image Aimée Neutre:
    "aime.e_neutre"
    zoom 0.35

image Peacock Neutre:
    "peacock_neutre"
    zoom 0.35

image Imani Neutre:
    "imani_neutre"
    zoom 0.35

image Auditorium = "Backgrounds/concept_auditorium.png"

#illustration de fin
image CG_gatsby = "images/CGs/gatsby.jpg"


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
define mother = Character('Mother', color="#880000", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=25, callback=type_sound, cb_cps=25)
define anthrax = Character('Anthräx', color="#6600b9", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=35, callback=type_sound, cb_cps=35)
define delaunay = Character('Delaunay', color="#2d9ead", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define gatsby = Character('Gatsby', color="#003099", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define peacock = Character('Peacock', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define leandre = Character('Léandre', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define aimee = Character('Aimé.e', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define imani = Character('Imani', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define staff = Character('Staff', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)
define player = Character('[player_name]', color="#be9f13", who_outlines=[(2, "#000000", 0, 0)], what_slow_cps=50, callback=type_sound, cb_cps=50)


label gatsby_start:
$ quick_menu = True
scene Auditorium with fade

#GAT.1
gatsby "Let's go ! On va former un duo d'enfer, je te le dis !"

anthrax "Aha ! J'adore cette énergie. Par quoi voudrais-tu commencer ?"

gatsby "Hm... On pourrait se présenter mutuellement, histoire d'apprendre à se connaître, et voir ensuite où ça nous mène ?"

anthrax "C'est une excellente idée."

gatsby "Ça te dit qu'on se pose au bar ? C'est plus intime et Barman est un vrai génie dans tout ce qui est cocktail, alcoolisé ou non."

anthrax "Ça me tente bien."


#GAT.2


#Dialogue WIP



#Choix GAT.2
label choix_gat2:
    $ quick_menu = False

    menu: 
        "WIP":
            call gat_2_1
        "WIP":
            call gat_2_2
        "WIP":
            call gat_2_3
          

#GAT.2.1
label gat_2_1:
    $ quick_menu = True

    anthrax "WIP"
    leandre "WIP"
    call gat_3

#GAT.2.2
label gat_2_2:
    $ quick_menu = True

    anthrax "WIP"
    mother "WIP"
    call gat_3

#GAT.2.3
label gat_2_3:
    $ quick_menu = True

    anthrax "WIP"
    mother "WIP"
    call gat_3

#GAT.3
label gat_3:


#Dialogue WIP 


#Choix GAT.3
label choix_gat3:
    $ quick_menu = False

    menu: 
        "WIP":
            call gat_3_1
        "WIP":
            call gat_3_2
        "WIP":
            call gat_3_3

#GAT.3.1
label gat_3_1:
    $ quick_menu = True

    anthrax "WIP"
    leandre "WIP"
    call gat_4

#GAT.3.2
label gat_3_2:
    $ quick_menu = True

    anthrax "WIP"
    mother "WIP"
    call gat_4

#GAT.3.3
label gat_3_3:
    $ quick_menu = True

    anthrax "WIP"
    mother "WIP"
    call gat_4

#GAT.4
label gat_4:

    anthrax "Le calme illusoire de la loge contrastait drastiquement avec le bourdonnement du staff passé la porte."
    anthrax "Les discussions étaient légères et l'entraide entre les artistes pour régler les petits aléas techniques était doux à voir."
    anthrax "Malgré tout, chacun.e se préparait avec diligence, en jetant nerveusement un coup d'œil à l'heure qui tournait plusieurs fois dans la même minute."
    anthrax "Assis.e sur une chaise face à l'un des miroirs, en peignoir, Aimé décoiffait son mohawk à l'aide d'une large brosse avant d'appliquer un conditionner, pendant que son teint était en train de se fixer."
    anthrax "Iel finit par tresser les sections, puis enfiler un collant pour tout bien plaquer contre son crâne et laisser place à sa perruque qui l'attendait sur le mannequin."
    anthrax "En quelques coups de peigne et de gel, des vagues décoraient son front et quelques perles adoucissaient son regard tandis que son regard se berçait d'écume."

    gatsby "[player], est-ce que tu pourrais me rendre un service ?"

    anthrax "Bien sûr, de quoi as-tu besoin ?"

    gatsby "Est-ce que ce serait possible de me passer les pièces de mon costume pendant que je me change ? La cabine est ridiculement petite."

    anthrax "Aimé.e gardait son air confiant malgré son maquillage aux traits de Pierrot. Cependant, je décelais quelques incertitudes dans son regard. Peut-être de l'appréhension."
    anthrax "Avait-iel peur de me demander une telle chose ? Cela semblait délicat pour iel de me demander cela. Mais qu'iel me fasse confiance ainsi me fit anormalement plaisir."
    anthrax "Dis-moi ! Qu'est-ce que tu veux que je porte ?"
    anthrax "Iel me pointa une chaise et disparut avec son regard espiègle derrière le rideau de la cabine."
    anthrax "Je pris le costume et passa mes doigts sur le tulle léger, les strass, testant l'élasticité du tissu avec précaution."
    anthrax "Aimé.e me tendit ensuite son haut en dehors de son vestiaire improvisé et je compris à l'oreille que Gatsby quittait son binder pour taper sa poitrine."
    anthrax "Après tout, son tour était très physique et lui demandait une liberté de mouvements, qui clashaient peut-être avec sa dysphorie de genre..."

    gatsby "Merci... J'aurais besoin du harnais de sécurité s'il te plaît."

#Choix GAT.4
label choix_gat4:
    $ quick_menu = False

    menu: 
        anthrax "Je lui tendis en réfléchissant à quoi dire pour meubler le silence."
        "Ce n'est pas trop compliqué de performer? Je veux dire... Le rapport au corps, tout ça....?":
            call gat_4_1
        "Je te trouve courageux.e... Tout ce que tu réussis à accomplir sans que ça ai vraiment l'air de t'affecter":
            call gat_4_2
        "Je comprends, je pense. Mais tu n'as pas à te sentir gêné.e avec moi, tu sais?":
            call gat_4_3

#GAT.4.1
label gat_4_1:
    $ quick_menu = True

    anthrax "Ce n'est pas trop compliqué de performer ? Je veux dire... Le rapport au corps, tout ça... ?"

    gatsby "Mon corps, c'est un peu mon meilleur ennemi."
    gatsby "Dans le sens où c'est avec lui que je suis capable de faire ce que je fais, et je sais que je suis doué.e."
    gatsby "Et d'un autre côté, j'ai toujours une dysphorie de genre assez fluctuante, donc je ne sais pas si je vais être au top de ma forme ou non, avant un show."

    anthrax "À ce point ?"

    gatsby "Parfois oui, j'adore mon corps, mes formes, sa force... Et il suffit d'un instant pour avoir l'impression que ma peau n'est pas la mienne, que quelque chose est à vif en dessous, que ça grouille."

    gatsby "C'est très spécial à décrire..."

    delaunay "Hm... Je comprends exactement ce que tu veux dire..."

    peacock "C'est peut-être pour ça que le drag est notre plus grand atout finalement, on peut se permettre d'explorer."

    gatsby "Plus qu'explorer, je dirais même se réconcilier. La majeure partie du temps, je me sens super bien dans ma peau."
    gatsby "Devoir accomplir des prouesses physiques, se dévoiler, ne pas avoir droit à l'erreur et être obligé.e de rester concentré.e quand juste parfois le mood n'est pas là, est bien plus embarrassant que ce qu'on croirait."
    gatsby "Même moi, j'ai sous-estimé l'impact que ça aurait sur ma performance au début. Ça va que je réussis maintenant à gérer."

    anthrax "Ça t'est déjà arrivé pendant que tu étais sur scène ?"

    gatsby "Si on parle de crise de dysphorie, non. Et j'ai bien de la chance. C'est plus une sensation de malaise qu'autre chose."

    peacock "C'est déjà arrivé une fois à Léandre cependant, au début."

    anthrax "Vraiment ?"

    delaunay "Oui, mais c'était un cas exceptionnel. Et j'avais d'autres facteurs dans ma vie personnelle qui ont fait que je n'ai plus réussi à assumer mon numéro en plein milieu de celui-ci."

    gatsby "Mais au final, ça s'est bien fini et le public était très compréhensif..."
    gatsby "Et on se soutient suffisamment dans la troupe pour savoir exprimer nos besoins et nos difficultés."

    peacock "Et se rassurer."

    staff "Ok les filles ! Showtime dans dix minutes !"

    gatsby "Allez ! On doit mettre les bouchées doubles si on veut être à l'heure, girlies ! Chop-chop !"

    call gat_5

#GAT.4.2
label gat_4_2:
    $ quick_menu = True

    anthrax "Je te trouve courageux.e... Tout ce que tu réussis à accomplir sans que ça ait vraiment l'air de t'affecter."

    gatsby "Ce n'est pas du courage ça. Ça s'appelle juste vivre... Tu dis ça parce que tu as du mal à comprendre."

    anthrax "Du mal à comprendre ? Pourquoi tu dis ça ? Ce n'est pas comme si j'essayais pas ou que j'étais complètement ignorant.e."

    gatsby "Non ! Pas dans ce sens-là ! Dans le sens où on a tous.te.s nos limites de compréhension. Tu n'es pas dans ma tête, ni dans mon corps. Alors la définition de courage est celle qui te vient en premier."
    gatsby "Je déteste ce mot, pour me définir en tout cas."

    anthrax "Pourquoi donc ? Ce n'est pas péjoratif."

    gatsby "Non, en effet. Mais ça sous-entend un peu que mon existence est une corvée. Ce n'est pas le cas du tout. En fait, j'ai l'impression d'être pris.e en pitié, et je ne supporte pas ça."

    anthrax "Pardon, ce n'est pas ce que je souhaitais dire."

    gatsby "Je sais. Et j'ai aussi été maladroit.e dans ma réaction. Désolé.e."
    gatsby "J'ai conscience d'être une personne grosse, noire et non-binaire. Très clairement, je cumule."
    gatsby "Mais ce n'est pas une raison pour s'apitoyer, au contraire."
    gatsby "Mon bonheur, c'est ma plus belle arme de résistance face à une société peu accueillante. Et c'est quelque chose que je ne compte pas lui abandonner de sitôt."
    gatsby "J'ai trop travaillé pour arriver là où j'en suis aujourd'hui. De l'effort, de la résilience, de la joie, mais pas du courage."

    anthrax "C'est un raccourci trop simple, si je comprends bien."

    gatsby "Je n'aurais pas dit mieux !"

    peacock "Mais t'aurais pu lui répondre plus gentiment. Maintenant [player] a l'air tout.e embarrassé.e."

    delaunay "C'était peut-être maladroit, mais ça ne partait pas d'un mauvais fond. Tu es encore parti.e au quart de tour By-By."

    gatsby "C'est vrai, my bad. Je ferai plus gaffe."

    anthrax "Ce n'est pas grave, ça m'a plus surpris.e qu'autre chose. Mais au final, ça m'a donné plus de perspective, et j'apprécie l'honnêteté."

    staff "Ok les filles ! Showtime dans dix minutes !"

    gatsby "Allez ! On doit mettre les bouchées doubles si on veut être à l'heure girlies ! Chop-chop !"
    
    call gat_5

   
#GAT.4.3
label gat_4_3:
    $ quick_menu = True

    anthrax "J'étais persuadé.e qu'avec tout ce que tu m'as mentionné avant, tu ne toucherais plus jamais aux arts acrobatiques."

    gatsby "Eh bien... En soi je comprends que tu puisses penser cela. Moi aussi j'étais persuadé.e que je ne reprendrais pas."
    gatsby "Mais petit à petit, l'envie de m'y remettre a pris le pas sur mes réticences."
    gatsby "Et au final, j'ai réalisé que ce n'était pas contre les soies aériennes que j'étais fâché, mais tout ce qu'elles avaient représenté de toxique dans mon ancien environnement de travail."
    gatsby "C'était plus facile d'amalgamer quelque chose que j'adore avec les horreurs que l'on m'a fait subir dans cette industrie, plutôt que de déconstruire et dissocier des années d'abus."

    anthrax "Personne ne peut te blâmer là-dessus, de ce que tu m'as raconté."

    gatsby "Bah... Ce n'était pas juste la pression de bien performer au spectacle. C'était la pure misogynie, le racisme ambiant, les standards de beauté, l'absence de contrôle sur ma manière de penser. J'étais vraiment conditionné.e."
    gatsby "Après, c'est aussi surtout parce que je suis tombé.e sur une troupe particulièrement toxique."
    gatsby "J'ai de nombreux.euses ami.e.s qui l'ont quittée et qui travaillent maintenant dans un climat plus sain, avec de l'entraide et de l'empathie. J'en ai d'excellents échos."
    gatsby "Et de toute manière, j'ai entendu dire que l'entreprise pour laquelle on bossait a fait faillite."
    gatsby "Donc j'ai vraiment l'esprit en paix à présent."

    delaunay "Je me demande surtout comment tu as fait pour ne pas partir avant..."

    gatsby "Pour les mêmes raisons que toi : je pourrais te retourner la remarque. J'avais mes circonstances, je ne questionne pas les tiennes..."

    delaunay "Touché."

    peacock "Stop vous deux. C'est pas simple de briser un pattern malsain auquel on est habitué.e.s."
    peacock "Vous êtes les deux le plus à même de le comprendre ici."

    gatsby "Tu dis ça, mais ton industrie n'est pas non plus très haute placée sur l'échelle des bisounours..."

    peacock "C'est vrai, c'est surtout de la chance. Et du bouche à oreille. J'ai l'avantage de bosser beaucoup avec des petits contrats. Ça aide à ne pas rester enfermé.e avec la même équipe et de pouvoir tourner."
    peacock "Ou alors de trouver justement les personnes avec qui j'apprécie bosser et pouvoir les recontacter."

    gatsby "Enfin bref ! Morale de l'histoire : bien s'entourer, et faire du drag. Parce qu'au moins, on s'entoure de gens qui nous comprennent."

    staff "Ok les filles ! Showtime dans dix minutes !"

    gatsby "Allez ! On doit mettre les bouchées doubles si on veut être à l'heure, girlies ! Chop-chop !"

    call gat_5

#GAT.5
label gat_5:
    anthrax "Le band commença le morceau suivant alors que la scène était encore vide de toute activité, si bien que les spectateur.ice.s en venaient à se demander si quelque chose clochait."
    anthrax "Un projecteur se braqua sur deux longues soies qui venaient d'être lâchées. Tout en douceur, accompagné.e par les accords du piano, Gatsby avançait sur les planches."
    anthrax "Après une courte parade, iel retira sa redingote et se hissa le long des deux voilages à la force de ses bras et de ses jambes, sécurisant son ascension en se créant un harnais en quelques tours de draps."
    anthrax "Surplombant l'atrium de quelques mètres de hauteurs, iel démarra son numéro de soies aériennes avec grâce."
    anthrax "Tourbillonnant, usant de sa flexibilité pour réaliser des postures impressionnantes, Gatsby captivait le regard, et le souffle retenu de chaque membre de l'audience faisait planer une tension éthérée et palpable."
    anthrax "Les deux nœuds au bout de chaque cheville et plante le.a tenait suspendu.e en grand écart, qui lui demandaient un effort d'équilibre surhumain."
    anthrax "Soudainement, iel tomba."
    anthrax "Virevoltant, sa chute se stoppa si près du sol qu'un cri de surprise fusa depuis le comptoir du bar."
    anthrax "Mais le risque calculé, et son sourire fier tandis qu'iel se redressait en disait long sur le contrôle que Gatsby avait sur la situation."
    anthrax "Quelques minutes plus tard et notre acrobate revint sur la terre ferme, saluant avec humilité son public ému."

call gat_6

#GAT.6
label gat_6:


#Dialogue WIP 


#Choix GAT.6
label choix_gat6:
    $ quick_menu = False

    menu: 
        "WIP":
            call gat_6_good
        "WIP":
            call gat_6_bad

#GAT.6.GOOD
label gat_6_good:
    $ quick_menu = True

    anthrax "WIP"
    leandre "WIP"
    call final_gatsby

#GAT.6.BAD
label gat_6_bad:
    $ quick_menu = True

    anthrax "WIP"
    mother "WIP"
    call final_gatsby

    

label final_gatsby:
    scene CG gatsby with fade

    $ persistent.gatsby = True
    "Une nouvelle illustration est disponible dans l'album."
    "Musiques et Interviews débloqués."

    pause 1.0

    scene black with fade

    $ renpy.full_restart()
