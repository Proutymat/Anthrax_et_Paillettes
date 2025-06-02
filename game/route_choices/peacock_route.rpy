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
define type_sounds = ['audio/SFX/TextMix-001.ogg','audio/SFX/TextMix-002.ogg','audio/SFX/TextMix-003.ogg','audio/SFX/TextMix-004.ogg','audio/SFX/TextMix-005.ogg','audio/SFX/TextMix-006.ogg','audio/SFX/TextMix-007.ogg','audio/SFX/TextMix-008.ogg','audio/SFX/TextMix-009.ogg','audio/SFX/TextMix-010.ogg']
define D_type_sounds = ['audio/SFX/AP_T1-001.ogg','audio/SFX/AP_T1-002.ogg','audio/SFX/AP_T1-003.ogg','audio/SFX/AP_T1-004.ogg']
define M_type_sounds = ['audio/SFX/AP_T2-001.ogg','audio/SFX/AP_T2-002.ogg','audio/SFX/AP_T2-003.ogg','audio/SFX/AP_T2-004.ogg']
define G_type_sounds = ['audio/SFX/AP_T3-001.ogg','audio/SFX/AP_T3-002.ogg','audio/SFX/AP_T3-003.ogg','audio/SFX/AP_T3-004.ogg'] 
define P_type_sounds = ['audio/SFX/AP_T4-001.ogg','audio/SFX/AP_T4-002.ogg','audio/SFX/AP_T4-003.ogg','audio/SFX/AP_T4-004.ogg']

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

play ambiance AmbLoges fadein 2.0


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
show bar with dissolve
stop ambiance fadeout 2.0
play music BarMusic fadein 2.0
play ambiance BarDay

"Nous sommes arrivé.e.s dans l'auditorium et nous nous sommes approché.e.s du comptoir derrière lequel brillait un mur de bouteilles de formes et couleurs uniques. Le paradis du parfait mixologue."

"Nous avions depuis le bar une vue imprenable sur la scène, légèrement en contrebas. Les tablées y étaient déjà dressées et se regroupaient autour du big band et de l'estrade secondaire au centre de la pièce."

"L'immense lustre duquel pendaient des larmes de verre reflétait les spots de lumière à la manière d'une boule à facettes sur le papier peint texturé."

"Imani s'assit sur l'une des chaises hautes de bois verni et commanda un Virgin Moscow Mule au barman, et moi un Negroni."

imani "Tu verras, notre barman est un vrai génie en la matière. Il peut te concocter le meilleur mocktail de ta vie sans que tu t'y attendes."

imani "Et des cocktails aussi, bien sûr !"

anthrax "Tu ne bois pas d’alcool ?"

imani "Non ! Mais j’adore le concept. Mêler jus, sirops, eau gazeuse, et créer quelque chose d’un peu plus fancy qu’une limonade, je prends !"

anthrax "Je me sens bête de prendre un Martini du coup..."

imani "Oh non ! Ne t’en fais pas, tant que tu es raisonnable dans ta consommation, tout va bien !"

"Imani sourit et prit sa boisson entre ses doigts vernis, la portant à ses lèvres et sirotant en me fixant, comme pour me jauger."

imani "Alors, dis-moi. C’est quoi ton drag ?"

anthrax "Mon drag ?"

imani "Oui, ton drag ! C’est pour ça que tu es là après tout !"

anthrax "Oh. Eh bien... Je dirais que c’est plus du drag quing. Je ne me fixe pas à un genre précis, parfois pas même l’espèce humaine pour tout dire..."

anthrax "J’ai commencé dans le confort de mon appart, sur les réseaux sociaux. Je n’ai jamais mis les pieds dans une troupe. Ou même un cabaret."

anthrax "Mais le burlesque, c’est quelque chose qui m’a toujours attiré.e. C’est culturel, niche, voluptueux... À la fois décent et indécent."

anthrax "Ça me parle."

imani "À moi aussi tu me parles ! Je comprends mieux ce que Mother a vu chez toi !"

anthrax "Ah bah merci..."

imani "Non, non ! C’était un compliment. Je sais que j’ai beaucoup de shade à revendre, mais là, c’était sincère."


#Choix PEA.2
label choix_pea2:
    $ quick_menu = False
    
    show imani_neutre at tall_right
    with fade

    menu: 
        "Tu es la personne qui m'a l'air la plus engagée au sein de la troupe...":
            call pea_2_1 from _call_pea_2_1 
        "Est-ce que tu peux m’en dire davantage sur ce que tu fais ? Mother a piqué ma curiosité, mais je brûle d’avoir plus de détails":
            call pea_2_2 from _call_pea_2_2 
        "Et toi ? Qu’est-ce qui t’as lancée dans le drag ?":
            call pea_2_3 from _call_pea_2_3 
          

#PEA.2.1
label pea_2_1:
    $ quick_menu = True
    
    show imani_neutre at tall_center
    with fade

    anthrax "Tu es la personne qui m'a l'air la plus engagée au sein de la troupe."

    imani "Oh ! Ne dis pas ça aux autres, les oreilles vont chauffer !"

    imani "C’est vrai que Léandre a l’air plus discret mais n’en est pas moins activiste."

    imani "Et Aimée... Eh bien, je crois que tu as remarqué qu’iel avait plutôt grande gueule..."

    imani "Même l’Androgame est un lieu très central dans la sphère queer de la ville. Toutes les Paillettes vont défiler aux prides et scandent des slogans."

    imani "Et c’est un peu devenu une tradition même que l’on fasse un discours sur le char, après la minute de silence."

    anthrax "C’est vrai que je vous y avais vu.e.s quelques fois. Mais je n’avais pas fait le rapprochement..."

    imani "Même en dehors du drag, je suis très politisée. Contre le racisme, l’islamophobie, et le trafic d’enfants avec l’adoption internationale."

    anthrax "L’adoption internationale ?"

    imani "Oui, c’est assez méconnu. Mais c’est la dure réalité d’une grande partie des enfants adoptés de l’étranger."

    imani "Le déracinement, la méconnaissance de ses origines et la quête de soi qui vont avec."

    anthrax "Je l’ignorais..."

    imani "Ce n’est pas la première chose à laquelle on pense en me voyant après tout. J’aurais très bien pu être un petit-fils d’immigrés, mais non ! Adopté par des parents français !"

    anthrax "Et comment est-ce que tu le vis ? Si ce n’est pas indiscret..."

    imani "Hm... Plutôt bien. J’aime beaucoup ma famille adoptive, même si ça a posé de nombreux problèmes avec le temps."

    imani "La discussion a toujours été très ouverte avec mes parents sur ce sujet-là, et ils ne sont pas responsables des travers de procédures qu’il y a eu."

    imani "C’est plutôt une incompréhension de leur part parfois, quand j’essaye de me rapprocher de mes origines."

    imani "Je leur en ai un peu voulu lorsque j’étais adolescent, mais je sais maintenant que c’est parce que ça atteint simplement leurs limites éducationnelles."

    imani "C’est un peu vexant parfois, mais on fait avec. Et ça ne change rien à l’amour et au soutien qu’ils me donnent. Je m’estime donc très chanceux."

    imani "Je me sers, pour le coup, beaucoup du drag pour explorer cette facette de ma personne."

    imani "Et remédier un peu au white-washing que j’ai intégré en grandissant."

    anthrax "C’est un sacré parcours en perspective... Pas trop la pression ?"

    imani "Énormément de pression, oui !"

    imani "Je me sens parfois toujours pas légitime, alors que je suis littéralement maghrébin."

    imani "Sérieusement, c’est quelle logique ?!"

    anthrax "J’avais tout de même raison quand je disais que tu avais l’air d’être la personne la plus militante..."

    call pea_3 from _call_pea_3_4 

#PEA.2.2
label pea_2_2:
    $ quick_menu = True
    
    show imani_neutre at tall_center
    with fade

    anthrax "Est-ce que tu peux m'en dire davantage sur ce que tu fais ? Mother a piqué ma curiosité, mais je brûle d'avoir plus de détails."

    imani "Eh bien... Comme Mother l'a expliqué. Je me spécialise dans tout ce qui est \"vocal\"..."

    imani "Mais c'est plus de l'ordre de l'humour, de la lecture, du chant..."

    imani "Récemment, je m'intéresse plus à comment utiliser davantage mon corps dans mes numéros."

    imani "Avec de la danse notamment."

    anthrax "Elle ne l'a pas précisé ça !"

    imani "C'est suffisamment récent pour que tu en aies l'exclusivité."

    imani "Je prends des cours en dehors du travail. Sauf que comme j'en ai beaucoup, de travail, ça a pris un certain temps avant de devenir décent."

    anthrax "Je ne te crois pas."

    imani "Tu devrais ! Je suis né avec deux pieds gauches !"

    imani "C'est pas la faute de mes parents d'avoir essayé."

    imani "Mais à défaut d'avoir appris à danser, ils m'ont introduit très jeune au monde du spectacle, en m'emmenant voir des comédies musicales, des concerts et des ballets."

    imani "C'est sûrement pour ça que je fais de la régie d'ailleurs..."

    imani "Au moins, quand les procédures sont protocolaires, je n'ai pas à m'inquiéter de ma maladresse."

    anthrax "Tu ne m'as pas l'air si maladroit que ça... Encore moins si tu commences à inclure de la danse à un acte dans lequel tu chantes ou tu lipsync déjà."

    imani "C'est gentil de dire ça... Tu me flattes."

    anthrax "Et sinon, c'est un genre de danse en particulier que tu apprends en ce moment ?"

    imani "En ce moment ? Eh bien, ce que je compte intégrer en premier à mon gig, ce serait de la danse à éventails... Mais ultimement, j'aimerais bien y rajouter quelques éléments de shaabi."

    anthrax "Les éventails ? Tu veux dire les éventails à plumes ?"

    imani "Eh bien, mon nom de scène est Peacock après tout. Ce serait bête de ne pas l'exploiter un minimum."

    imani "Et pour tout dire, c'est même ce qui a initialement inspiré le nom."

    imani "Je n'avais juste pas encore les compétences pour prétendre être à la hauteur de mon titre ! (ironie)"

    anthrax "Encore une fois, je n'y crois pas une seconde !"

    anthrax "Il faudrait le voir pour le croire alors, mais ça ne saurait tarder !"

    call pea_3 from _call_pea_3 

#PEA.2.3
label pea_2_3:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "Et toi ? Qu'est-ce qui t'as lancée dans le drag ?"

    imani "En fait, je bossais déjà à l'Androgame avant."

    imani "Je faisais partie du crew à la technique et en régie."

    imani "Plus particulièrement, tout ce qui était relatif aux enceintes, micros et tout autres appareils sonores."

    imani "Pour faire simple."

    anthrax "Ah oui ! Donc tu connais les coulisses du cabaret depuis un moment déjà ! Pas étonnant que tu aies l'air aussi expérimenté."

    imani "En tant que technicien, peut-être, mais je suis encore assez débutant en drag. Ça fait seulement deux ans que j'ai officiellement commencé."

    anthrax "C'est déjà plus que moi..."

    imani "C'est pour cela que j'ai dit \"débutant\" et non \"novice\"."

    imani "Enfin bref, c'est Delaunay qui m'a costumé pour la première fois après une soirée arrosée pour fêter la fin d'un show."

    imani "Et j'y ai pris vraiment goût."

    imani "Comme mon contrat se terminait, je suis allé bosser ailleurs en régie, mais j'ai gardé contact avec les filles."

    anthrax "Et je suppose que tu as continué de ton côté avant de revenir, mais cette fois en intégrant la troupe ?"

    imani "Très bien deviné !"

    imani "Au départ, Mother n'était pas très encline, et j'ai mis un moment à faire mes preuves."

    imani "Mais du coup, on a bidouillé une sorte de contrat pour que je file un coup de main en technique de temps en temps, tout en peaufinant mon drag."

    imani "Et au final, ça s'est plutôt bien goupillé. J'avais une stabilité financière et un espace familier, dans lequel je pouvais progresser."

    imani "Puis un jour, j'ai eu le droit à mon premier show, et c'était magique."

    anthrax "Ah oui ? Comment c'était ?"

    imani "J'étais tellement nerveuse que je suis allée vomir deux fois avant de monter sur scène."

    imani "Mais une fois dessus, c'était comme si je m'étais fait posséder par quelqu'un d'autre, Peacock avait complètement pris le contrôle sur ma personne."

    imani "C'était grisant !"

    imani "J'étais tellement habitué à être sur le derrière de la scène, à faire en sorte que tout se déroule bien, que je n'avais jamais envisagé autant aimer être sur le devant."

    anthrax "J'ai hâte que ce soit mon tour !"

    call pea_3 from _call_pea_3_1 

#PEA.3
label pea_3:

    "Cela faisait plusieurs minutes que je cherchais Imani, avec qui j'étais supposé.e répéter une partie de mon numéro, que l'on construisait ensemble."
    
    "Après avoir fait trois fois le tour du lobby, des backstages, être retourné.e tout autant de fois dans les loges, je finis par retourner sur les planches de la scène, pensif.ve."
    
    "Et en toute honnêteté, un peu inquièt.e."

    "En relevant le regard vers le balcon, je le remarquai appuyé.e contre la balustrade, me faisant signe de le rejoindre, un verre de jus à moitié vide à la main avec lequel il jouait."

    anthrax "Hey... Je me demandais où tu étais passé."

    imani "Moi aussi ! Ça fait une demie-heure que je te cherche ! On a dû faire que de se louper."
    
    imani "Bon, au final, je me suis pris à boire et j'ai arrêté de bouger pour que tu puisses me retrouver !"

    anthrax "J'aurais pu tourner encore longtemps, dis ! Pourquoi tu ne m'as pas appelé.e ?"

    imani "J'ai laissé mon téléphone dans les loges, j'avais la flemme d'aller le chercher !"

    anthrax "Ah... Tu n'es pas possible."

    imani "Roh, arrête~ C'est comme ça qu'on m'aime !"

    anthrax "Oui, oui... Bien sûr. Qu'est-ce que tu bois ?"

    imani "Un jus d'abricot. Classique et délicieux !"

    "Il termina le fond de son verre d'une traite, avant de le poser sur l'une des tables qui n'avaient pas encore été dressées pour la soirée."

    anthrax "Quand j'y repense, je ne t'ai jamais vu boire. Enfin... Tu m'as compris.e."

    imani "Hm... Peut-être parce qu’il est 16h00 de l’après-midi et qu’il est un peu tôt à mon goût pour ça ?"

    anthrax "Non ! Pas dans ce sens là, je n’ai pas envie de passer pour un.e ivrogne ! Je me faisais juste la réflexion..."

    imani "Non, je ne bois pas. Je ne bois plus..."

    imani "Parce que moi, je l’ai été... Ivrogne. Et il n’y a pas un monde où je me laisserais retomber là dedans."

    anthrax "La boulette..."

    imani "Ça, je ne te le fais pas dire !"

#Choix PEA.3
label choix_pea3:
    $ quick_menu = False

    show imani_neutre at tall_right
    with fade

    menu: 
        "Je me sens bête maintenant, d'avoir amené le sujet comme ça...":
            call pea_3_1 from _call_pea_3_1_1 
        "Comment est-ce que tu es tombé dedans ? Ça te ressemble si peu...":
            call pea_3_2 from _call_pea_3_2
        "Tu as dû prendre pas mal de temps pour t'en remettre, non ?":
            call pea_3_3 from _call_pea_3_3 

#PEA.3.1
label pea_3_1:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "Je me sens bête maintenant, d'avoir amené le sujet comme ça..."

    imani "En même temps, boire, c’est tellement normalisé dans notre société. Et encore plus dans nos communautés."

    imani "Je ne peux pas t’en vouloir, tu ne pouvais pas savoir..."

    anthrax "C’est vrai qu’en général, on boit beaucoup et de manière assez rituelle..."

    imani "Ouais... Dis-toi qu’ils pratiquaient encore la tradition du petit shot avant le spectacle avant mon arrivée."

    imani "Mais je leur ai dit que ça me mettait un peu mal à l’aise, et la troupe a été finalement très compréhensive."

    imani "Surtout que ce n’est que bien plus tard que je leur ai parlé de mes anciens problèmes d’alcoolisme."

    imani "C’est aussi comme ça que je me suis rendu compte que j’étais tombé sur ma famille de cœur."

    imani "Et ça ne nous empêche pas de nous retrouver au bar après la fermeture pour boire un verre de temps en temps."

    imani "Je réussis à en surprendre plus d’un avec mes idées de mocktails !"

    anthrax "C’est vrai que L’Androgame renvoie une atmosphère réellement bienveillante. Ce n’est pas le cas partout."

    imani "Hm... Je ne pars pas du principe que tout le monde est mauvais, mais c’est vrai que les milieux queers fonctionnent énormément autour de la drogue et de l’alcool."

    imani "Après tout, les bars et clubs étaient les seuls lieux qui acceptaient la prohibition. C’est culturel à présent."

    imani "Mais on peut faire mieux que ça ! On n’a pas besoin de se désinhiber pour se sentir légitime d’exister, de s’amuser et de réclamer nos espaces !"

    anthrax "Hm... Mais j’ai l’impression que c’est encore trop ancré dans notre culture LGBT."

    anthrax "Il y a toujours cet aspect de défiance des normes genrées et des codes qui vont avec le milieu de la nuit."

    anthrax "Nous sommes dans un cabaret, après tout..."

    imani "C’est vrai... Mais je ne pense pas que les deux sont incompatibles."

    imani "Si je suis tombé dans l’addiction, c’est aussi surtout parce que l’on m’a influencé et normalisé ce genre de comportement."

    imani "J’ai toujours travaillé dans l’industrie du spectacle et de l’entertainment, les vices sont bien plus profonds que ça..."

    imani "Et justement, prendre du recul est mal vu. Tu es « moins drôle », « pas fun », « archi ennuyeux », si tu ne bois pas."

    anthrax "Alors tu es l’exception qui confirme la règle. Parce que tu es l’opposé de « boring » !"

    call pea_4 from _call_pea_4 

#PEA.3.2
label pea_3_2:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "Comment est-ce que tu es tombé dedans? Ça te ressemble si peu..."

    imani "Franchement, ce n’est pas l’histoire la plus sensationnelle que je pourrais te raconter..."

    imani "Honnêtement, est-ce que c’est une histoire qui mérite d’être racontée? Je ne sais pas... J’étais vraiment pathétique."

    anthrax "Ne dis pas ça... C’est vicieux, les addictions. Sinon personne ne serait accro à rien ! Tu as fini par t’en sortir."

    anthrax "Donc ce n’est pas le nombre d’échecs qui compte, mais le résultat : Tu tiens à ta sobriété."

    anthrax "Et je dis ça, sans t’avoir connu à l’époque !"

    imani "Ha ha ! T’es chou..."

    imani "Mais tu n’aurais peut-être pas voulu me connaître à l’époque..."

    anthrax "Pourquoi donc ?"

    imani "Et bien... Je n’étais pas quelqu’un que l’on pouvait qualifier... d’émotionnellement stable."

    imani "Je travaillais bien et étais respectueux, hein ! Mais, je ne sais pas... J’ai toujours senti que quelque chose clochait."

    imani "J’étais encore très immature, dans mes relations. Il n’y avait qu’au travail où j’avais un cadre qui me permettait de garder les pieds sur terre."

    imani "Et pourtant, il y a commencé à y avoir des écarts... Au début, entre collègues, c’était marrant de sortir boire un verre pour décompresser."

    imani "Mais ça a pris des proportions telles où l’on finissait en boîte jusqu’à pas d’heure, où ça se droguait et se mettait la misère."

    imani "Et je t’ai dit, j’étais immature... Donc cette ambiance, ça me plaisait. Et je suis un bon suiveur..."

    anthrax "C’est normal de faire des erreurs, tu sais... Et sortir s’amuser, personne ne peut te blâmer là-dessus ! Alors pourquoi toi ?"

    imani "Parce que ce n’était que le début !"

    imani "J’en suis venu à penser que c’était normal... Mais ça a vraiment dérapé quand je suis devenu acteur de ma déchéance."

    imani "Ce sentiment de... « truc qui cloche », il ne m’a jamais quitté. Et les soirées, c’était un moyen de me distraire pour ne plus y penser."

    imani "Mais quand ça t’obscède autant dans la journée et que tu n’as pas de porte de sortie, tu t’en crées..."

    anthrax "Oh non..."

    imani "Si... J’ai commencé à boire au taf."

    imani "Au début, c’était discret. Je buvais juste suffisamment pour me désinhiber. Mais là encore, je n’ai pas su m’arrêter."

    imani "Et au final, ils ont fini par s’en rendre compte et me virer."

    imani "Ça m’a mis un coup de pied aux fesses suffisant pour que j’aille faire une cure de désintox dans un centre, et je suis revenu en force !"

    anthrax "Et tu l’as toujours ce « truc qui cloche » ?"

    imani "Hm... Un peu ! Mais j’ai mis le doigt dessus en commençant à faire du drag. Je pense donc être sur la bonne voie !"

    call pea_4 from _call_pea_4_1 

#PEA.3.3
label pea_3_3:
    $ quick_menu = True

    show imani_neutre at tall_center
    with fade

    anthrax "Tu as dû prendre pas mal de temps pour t’en remettre, non ?"

    imani "Oui, ça on peut le dire... Mais c’est parce que ça a été un parcours de longue haleine..."

    imani "Des fois, je me dis que j’aurais pu voir les signes et m’arrêter à temps."

    imani "Mais techniquement, ce serait mentir, puisque j’ai essayé à plusieurs reprises d’arrêter. Je manquais juste de..."

    imani "De volonté ? De motivation ? Ce ne sont même pas les bons mots pour décrire..."

    imani "L’alcool avait juste une telle emprise sur moi que j’ai l’impression que je me disais ça pour me donner bonne conscience."

    imani "« Essayer, sans réellement essayer »... Entre les tentatives ratées et les fausses excuses que je me donnais, il a d’abord fallu que je remette les pieds sur terre."

    imani "Et ça n’a pas été une mince affaire."

    anthrax "Comment est-ce que tu as fait ?"

    imani "Moi ? Je n’ai rien fait. J’ai dû me faire virer de mon ancien taf pour que j’aie un déclic..."

    imani "Vraiment, je n’ai aucun mérite dans cette affaire !"

    anthrax "Je trouve que tu t’en donnes trop peu, de mérite. Tu as réussi à te sortir de l’addiction après tout."

    imani "Oui, mais... Je suis toujours terrifié à l’idée de retomber dedans. C’est comme une ombre qui me suit de très près, et de laquelle je ne peux pas me défaire..."

    imani "C’est sûrement le temps qui fera ce travail, mais en attendant, je reste prudent..."

    imani "Il n’y a aucune chance que je redevienne qui j’étais durant cette période..."

    imani "Une sorte de zombie... Une autre personne, en tous points, qui n’avait pas de volonté autre que de toucher à la goutte suivante."

    imani "J’étais tellement accro, que je ne faisais que trembler, suer, halluciner... Sûrement parce que je n’arrivais pas à dormir..."

    imani "Heureusement que j’étais en cure de désintox et qu’il y avait du monde pour s’occuper de moi, parce que j’avais l’impression de mourir."

    "[Je ne su quoi lui répondre, ne pouvais que me l’imaginer. Jamais je n’aurais pensé qu’Imani avait traversé une telle épreuve...]"

    imani "On dirait que cette histoire a laissé un froid, non ? Désolé, c’était un peu morbide..."

    anthrax "Non, non... Ne t’excuse pas. C’est juste que..."

    anthrax "Pendant tout ce temps, tu devais te sentir tellement seul."

    imani "..."

    anthrax "Je suis content.e que tu ne sois plus entravé par l’addiction. Tu as l’air heureux, et entouré."

    anthrax "Ce n’est pas ton passé qui te définit, tu sais ?"

    imani "C’est vrai, tu as raison..."

    imani "Bon ! C’est pas tout, mais on a un show à préparer !"
    
    call pea_4 from _call_pea_4_2 

#PEA.4
label pea_4:

    play ambiance AmbLogesNight fadein 4.0

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
            call pea_4_1 from _call_pea_4_1_1 
        "Sans soucis! Tu comptes chanter aussi? Je vois que tu as un micro d'installé...":
            call pea_4_2 from _call_pea_4_2_1 
        "Les ébouriffer? Est-ce que c'est pour mieux te cacher lors de l'effeuillage?":
            call pea_4_3 from _call_pea_4_3 

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
    
    stop ambiance fadeout 3.0
    call pea_5 from _call_pea_5 

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

    stop ambiance fadeout 3.0
    call pea_5 from _call_pea_5_1 

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
   
    stop ambiance fadeout 3.0
    call pea_5 from _call_pea_5_2 

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
  
    call pea_6 from _call_pea_6 

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
            call pea_6_good from _call_pea_6_good 
        "WIP":
            call pea_6_bad from _call_pea_6_bad 

#PEA.6.GOOD
label pea_6_good:
    $ quick_menu = True
    
    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    imani "WIP"
    call final_peacock from _call_final_peacock 

#PEA.6.BAD
label pea_6_bad:
    $ quick_menu = True
    
    show imani_neutre at tall_center
    with fade

    anthrax "WIP"
    mother "WIP"
    call final_peacock from _call_final_peacock_1 

    

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
