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

image CG_gatsby = "images/CGs/gatsby.jpg"

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


label gatsby_start:
$ persistent.bg_parallax = True
$ quick_menu = True
scene black with fade
show loges
show aimee_neutre at gat_center with dissolve
play ambiance AmbLoges fadein 2.0

#GAT.1

gatsby "Let's go ! On va former un duo d'enfer, je te le dis !"

anthrax "Aha ! J'adore cette énergie. Par quoi voudrais-tu commencer ?"

gatsby "Hm... On pourrait se présenter mutuellement, histoire d'apprendre à se connaître, et voir ensuite où ça nous mène ?"

anthrax "C'est une excellente idée."

gatsby "Ça te dit qu'on se pose au bar ? C'est plus intime et Barman est un vrai génie dans tout ce qui est cocktail, alcoolisé ou non."

anthrax "Ça me tente bien."


#GAT.2

show bar with dissolve
play music BarMusic fadein 1.5 volume 0.5
play ambiance BarDay fadein 0.5
play music BarMusic volume 0.5

text "Nous sommes arrivé.e.s dans l'auditorium et nous nous sommes approché.e.s du comptoir derrière lequel brillait un mur de bouteilles de formes et couleurs uniques. Le paradis du parfait mixologue."

text "Nous avions depuis le bar une vue imprenable sur la scène, légèrement en contrebas. Les tablées y étaient déjà dressées et se regroupaient autour du big band et de l'estrade secondaire au centre de la pièce."

text "L'immense lustre duquel pendaient des larmes de verre reflétait les spots de lumière à la manière d'une boule à facettes sur le papier peint texturé."

text "Aimée s'assit sur l'une des chaises hautes de bois verni et commanda un Bloody Mary au barman, et moi un Expresso Martini."

aimee "Alors ! Raconte-moi tout ! D'où est-ce que tu viens ? Qu'est-ce que tu fais ici ? Comment est-ce que tu nous as connu.e.s ?"

anthrax "Oh... Euh... Ça fait beaucoup de questions à la fois..."

aimee "Pas faux. Commence par le drag alors. Qu'est-ce qui t'as lancé.e ?"

anthrax "Oh. Eh bien... J'ai commencé dans le confort de mon appart, sur les réseaux sociaux. Je n'ai jamais mis les pieds dans une troupe. Ou même un cabaret pour tout te dire."

anthrax "Je n'habite pas très loin, donc je passais souvent devant L'Androgame et vous observais de loin."

anthrax "C'est un peu impressionnant. Je me demande si j'ai ma place, je ne m'attendais pas à être retenu.e après l'audition..."

aimee "Bien sûr que tu as ta place ! Mother a l'œil pour repérer les talents."

anthrax "Et toi ? Ça fait longtemps que tu as intégré la troupe ?"

aimee "Peut-être... Cinq ans ? Quatre ? Léandre était là déjà avant moi, mais je n'ai pas tardé après lui."

aimee "Et Imani...? Eh bien, elle bossait déjà là avant en tant que technicienne son. C'est plus récent son lancement dans le drag. Deux ans, il me semble ?"

anthrax "Ah oui, donc ça fait un moment que vous vous connaissez."

aimee "Oui. Ils font même partie de mon cercle d'ami.e.s le plus proche. Mais je ne vais pas leur dire en face sinon ils vont prendre la grosse tête..."

aimee "Et je m'imagine déjà les vannes de Delaunay, quand Léandre sort son alter-ego. Tu verras, c'est assez marrant."

anthrax "En tout cas, ça promet beaucoup pour la suite !"

anthrax "Et sinon, c'est quoi qui t'as lancé.e dans le drag toi ?"

aimee "Ma quête de genre principalement... Enfin je pense. J'étais dans une phase où je me redécouvrais entièrement."

aimee "Je sortais d'un burn-out, je savais que j'avais plein de choses enfouies à régler... Et j'ai décidé de commencer par ça."

aimee "Le reste a suivi."


#Choix GAT.2
label choix_gat2:
    $ quick_menu = False
    
    show aimee_neutre at gat_right
    with fade

    menu: 
        "Tu faisais du cirque du coup? Est-ce que tu peux m'en raconter davantage?":
            call gat_2_1 from _call_gat_2_1 
        "J'ignorais que tu avais fait un burn-out. C'était quel genre d'environnement de travail pour que ça en arrive là?":
            call gat_2_2 from _call_gat_2_2 
        "Donc tu as commencé par le drag pour... Te relever? Ce n'est peut-être pas la première chose à laquelle on pense quand on commence sa \"healing journey\"":
            call gat_2_3 from _call_gat_2_3 
          

#GAT.2.1
label gat_2_1:
    $ quick_menu = True
    
    show aimee_neutre at gat_center
    with fade

    anthrax "Donc tu as commencé par le drag pour... Te relever ? Ce n'est peut-être pas la première chose à laquelle on pense quand on commence sa \"healing journey\"."

    aimee "Tu faisais du cirque du coup ? Est-ce que tu peux m'en raconter davantage ?"

    aimee "Eh bien... J'ai commencé très jeune, avec de la gymnastique."

    aimee "Mes parents ont découvert assez vite que j'étais hyperlaxe, c'était donc un avantage dans ce type de discipline."

    aimee "Et j'étais plutôt bon.ne en plus. Mais je commençais à m'ennuyer et j'avais envie de changement."

    aimee "Et avec l'âge, je me suis de plus en plus intéressé.e à d'autres formes d'art, un peu plus physiques mais plus challengeantes !"

    aimee "Et qui dit challenge, dit fun."

    anthrax "Ça te correspond bien en tout cas. Tu as l'air d'être du genre... explosif ?"

    aimee "Ha ha ! Merci. Oui, j'ai toujours été assez turbulent.e !"

    aimee "Donc fallait y aller pour m'épuiser !"

    anthrax "Et qu'est-ce que tu sais faire du coup ?"

    aimee "Pendant quelques années, j'étais contorsionniste."

    aimee "Puis je me suis intéressé.e aux hauteurs."

    anthrax "Aux hauteurs ?"

    aimee "Oui ! Toutes les disciplines qui avaient un rapport de près ou de loin au vide."

    aimee "Équilibrisme, acrobatie aérienne, voltige, trapèze, cerceaux volants..."

    anthrax "Et tu n'as jamais eu le vertige ? J'ai le tournis rien que de m'imaginer ça."

    aimee "Jamais ! Au contraire, la partie la plus drôle, c'était la chute."

    aimee "Après, il y avait toujours un filet ou des matelas pour nous rattraper, donc les dangers étaient minimes pour peu que l'on ait appris à bien tomber."

    aimee "Et rien de mieux dans la vie que d'apprendre à se relever après un échec !"

    anthrax "Et tu en fais toujours ?"

    aimee "Hm... Disons que je reprends doucement."

    aimee "J'ai beau avoir un corps d'Adonis, il n'a plus les mêmes capacités qu'avant."

    aimee "Mais ça ne m'empêche pas d'improviser, puisque je n'ai pas non plus tout perdu."

    aimee "Après tout, j'y ai consacré la majorité de ma vie. Ce n'est pas une mauvaise passe qui va envoyer en l'air tous mes efforts."

    aimee "Recommencer ne me fait pas peur. Et si je peux compiler avec la personne que je suis devenu.e, ce serait un triomphe !"

    jump gat_3
    call gat_3 from _call_gat_3 

#GAT.2.2
label gat_2_2:
    $ quick_menu = True
    
    show aimee_neutre at gat_center
    with fade

    anthrax "J'ignorais que tu avais fait un burn-out. C'était quel genre d'environnement de travail pour que ça en arrive là ?"

    aimee "Ça n'en a peut-être pas l'air comme ça, mais j'étais acrobate dans une troupe de cirque..."

    aimee "On était constamment en déplacement à l'étranger pour des tournées, et disons que l'ambiance aux répétitions et en spectacles n'était pas au beau fixe."

    aimee "Pendant un long moment, c'était le genre de chose que je ne pouvais pas voir en peinture ou entendre parler."

    aimee "Alors que j'en étais réellement passionné.e..."

    anthrax "Merde... Et du coup, ça a dû te dégoûter complètement..."

    aimee "Pendant un temps, oui."

    aimee "Mais plus à présent. C'est même redevenu ma spécialité au sein de l'Androgame."

    aimee "La majorité de mes numéros sont acrobatiques."

    aimee "Dis-toi que Mother a même fait des modifications dans la structure de la scène, pour l'accommoder à mes besoins techniques."

    anthrax "Ça a dû être assez coûteux."

    aimee "Rien qu'une avance sur le salaire ne puisse régler !"

    aimee "Non, je plaisante. Je n'ai pas eu à contribuer aux frais. C'est juste bien tombé puisque des rénovations étaient déjà prévues."

    aimee "Mother est une vraie businesswoman. Je ne sais pas quels contacts elle cache dans son décolleté, mais si tu as besoin de n'importe quoi, je suis sûr.e qu'elle a quelqu'un pour te dépanner."

    anthrax "Et du coup, qu'est-ce que tu fais exactement comme acrobatisme ?"

    aimee "As-tu réellement envie que je te spoile ? Je peux te laisser la surprise pour le prochain show~"

    anthrax "Juste un indice alors ?"

    aimee "Un indice ? Très bien."

    aimee "C'est de la voltige...~"

    call gat_3 from _call_gat_3_1 

#GAT.2.3
label gat_2_3:
    $ quick_menu = True

    show aimee_neutre at gat_center
    with fade

    anthrax "Donc tu as commencé par le drag pour... Te relever ? Ce n'est peut-être pas la première chose à laquelle on pense quand on commence sa \"healing journey\"."

    aimee "Oh, ne t'en fais pas que j'allais déjà chez le psy !"

    aimee "Je ne l'ai d'ailleurs jamais quitté.e..."

    aimee "Non, j'étais déjà à un stade suffisamment avancé de réflexion pour me lancer dans l'exploration tout de même."

    aimee "J'avais les clefs en main, mais je ne savais pas quelle porte ouvrir. Ou bien même où est-ce qu'elle était cette foutue porte."

    aimee "Alors que je suis plutôt du genre à les enfoncer..."

    aimee "Et tout ça pour réaliser que ce n'était pas une porte mais une trappe vers le grenier où j'avais entassé pas mal de vieux démons en espérant les y oublier..."

    aimee "Enfin bref, pas mal de métaphores pour dire une seule chose : \"Maintenant, ça va mieux\"."

    anthrax "Ça a l'air d'avoir été bien fastidieux. Donc... Par quoi est-ce que tu as commencé le drag ?"

    aimee "Eh bien... Au tout départ, c'était avec des sorties costumées, comme Halloween ou Mardi Gras."

    aimee "On avait aussi ces petites soirées à thème avec mes ami.e.s où l'on venait déguisé.e.s, et j'utilisais ces occasions à fond"

    aimee "puisque c'était les seuls moments où je sentais que je pouvais m'amuser avec les frontières du genre et repousser quelques limites."

    aimee "Puis j'ai de plus en plus assumé, avec du jeu de rôle notamment."

    aimee "Puis les cercles d'amis se sont mêlés et j'ai découvert une association queer qui proposait des ateliers drag. Et je me suis inscrit.e."

    anthrax "Sur un coup de tête ? Comme ça ?"

    aimee "Après tout, c'est un peu comme toi lorsque tu t'es présenté.e à l'audition. Parfois, il faut juste se lancer."

    anthrax "C'est vrai... Et à quoi ressemblait ton drag au début ?"

    aimee "Je suis content.e que tu demandes !"

    aimee "Au départ, c'était plutôt du drag clown et du drag creature... Ça ne ressemblait pas à grand-chose, mais c'était le but."

    aimee "Je m'inspirais principalement d'œuvres d'art et j'essayais de les reproduire sur mon corps avec une pointe de body horror."

    aimee "C'était assez fun. Dommage que ça ne colle pas trop avec le style de l'Androgame..."

    aimee "Mais ça ne m'empêche pas de développer ces personnages à côté."

    anthrax "Et tu es toujours dans cette association ?"

    aimee "Oui ! Mais malheureusement, on n'y fait plus trop de spectacles. Chacun.e a sa vie et d'autres priorités, et le drag est passé au second plan. Mais peut-être que ça reprendra un jour, qui sait ?"

    call gat_3 from _call_gat_3_2 

#GAT.3
label gat_3:

    text "Cela faisait plusieurs minutes que je cherchais Aimée, avec qui j'étais supposé.e répéter une partie de mon numéro, que l'on construisait ensemble."

    text "Après avoir fait trois fois le tour du lobby, des backstages, être retourné.e tout autant de fois dans les loges, je finis par retourner sur les planches de la scène, pensif.ve."

    text "Et en toute honnêteté, un peu inquiet.e."

    text "Puis je l'aperçus, dominant un carnet sur lequel iel tapotait la mine de son crayon, posé sur l'un des mange-debouts. Je le.a rejoignis rapidement."

    anthrax "Hey... Je me demandais où tu étais passé.e."

    aimee "Oh, pardon... Je ne pensais pas que tu me cherchais."

    anthrax "Euh... Nous étions censé.e.s nous retrouver pour nous entraîner..."

    aimee "Meeeeeerde ! J'ai complètement zappé ! Je suis désolé.e !"

    anthrax "Ce n'est pas grave, c'est le genre de chose qui arrive. Qu'est-ce que tu fais... ?"

    aimee "Ça ? J'essaye de tenir un journal."

    anthrax "Un journal ?"

    aimee "Oui, pour mettre à plat ma progression, mes hauts et mes bas... Histoire de garder une trace du chemin parcouru et de ce que j'ai accompli."

    anthrax "Oh ! Un journal intime quoi !"

    aimee "Ça fait tout de suite moins sérieux dit comme ça... Mais oui, un journal intime."

    aimee "Entre autres..."

    text "Soudainement l'air un peu ailleurs, Aimée se mordit l'intérieur de la joue, sans reprendre la parole. Ellui étant si bavard.e, c'était plutôt surprenant de sa part..."

    anthrax "Tout va bien ?"

    aimee "Hm..."

    aimee "Peut-être qu'en parler m'aidera à mieux trouver les mots pour l'écrire..."

    anthrax "Oh... ?"

    aimee "Tu vois quand je t'ai parlé de mon burn-out ? Ça a eu des conséquences bien plus dévastatrices sur ma santé mentale qu'une simple dépression..."

    aimee "Avec la pression au sein de mon ancienne troupe, j'ai développé des troubles du comportement alimentaire."

    aimee "Boulimie, anorexie, un mix des deux, puis un soupçon de mérycisme... Enfin bref."

    aimee "Rien de bien joyeux, mais j'aimerais réussir à le noter dans mon carnet pour..."

    aimee "Je ne sais pas... Enfin tourner la page ?"


#Choix GAT.3
label choix_gat3:
    $ quick_menu = False

    show aimee_neutre at gat_right
    with fade

    menu: 
        "Est-ce que ça va mieux maintenant que tu as quitté cet environnement ?":
            call gat_3_1 from _call_gat_3_1_1 
        "Wow... Quand je te vois maintenant... Je ne pensais pas...":
            call gat_3_2 from _call_gat_3_2_1 
        "Tu as dû prendre pas mal de temps pour t'en remettre, non?":
            call gat_3_3 from _call_gat_3_3 

#GAT.3.1
label gat_3_1:
    $ quick_menu = True

    show aimee_neutre at gat_center
    with fade

    anthrax "Est-ce que ça va mieux maintenant que tu as quitté cet environnement ?"

    aimee "Oui ! Énormément même !"

    aimee "Ça n'a pas encore complètement disparu, mais c'est sur une excellente voie !"

    aimee "Je n'ai jamais été aussi bien dans ma peau, mon apparence et ma confiance."

    anthrax "Ça me rassure un peu... Ça ne rigole pas les TCA."

    aimee "Ce n'est pas moi qui vais te dire le contraire !"

    aimee "Remonter la pente est ce qui a été le plus compliqué, mais maintenant que c'est passé, je suis inarrêtable."

    anthrax "Mais qu'est-ce qui t'as causé de sombrer en premier lieu ?"

    aimee "Je pense que c'était sincèrement la pression qu'on me mettait. C'est même indéniable..."

    aimee "Quelqu'un était constamment sur mon dos pour surveiller mon poids, mon déficit calorique, combien de litres d'eau je buvais par jour, quels compléments alimentaires..."

    aimee "Je n'ai pas toujours eu le corps que j'ai aujourd'hui, c'était un régime très strict."

    aimee "Ça a d'ailleurs commencé par de l'anorexie. Je pense qu'avec le recul, j'avais terriblement besoin de contrôle."

    aimee "Et le peu que je pouvais grapiller se trouvait là..."

    anthrax "Ça devait être abominable."

    aimee "Hm... Peut-être, mais j'ai survécu."

    aimee "Surtout qu'à cette époque, j'étais particulièrement mal dans mes baskets, et je n'avais pas encore réalisé que je me posais des questions sur mon genre."

    aimee "C'était vraiment un pêle-mêle de sentiments néfastes, sans un pour rattraper l'autre."

    aimee "Et j'ai beau avoir fini par quitter la troupe, j'étais tellement matrixé.e que les TCA ne se sont pas arrêtés là."

    aimee "Maintenant, j'avais une sorte de vide à combler, et j'ai fait de l'hyperphagie."

    aimee "Bref..."

    anthrax "C'est l'Androgame qui t'as aidé à t'en sortir ?"

    aimee "L'Androgame ? Non."

    aimee "Mais ma psy et le drag, par contre, oui !"

    aimee "J'ai trouvé une communauté, et un espace pour me redécouvrir, qui m'acceptait pour quiconque je devenais."

    aimee "Franchement, c'était salvateur. Et j'ai pu commencer à aborder plus ouvertement les épreuves que je traversais."

    aimee "Jusqu'à ultimement les surmonter."

    aimee "C'est après que j'ai découvert l'Androgame, et que j'ai pu réitérer !"

    call gat_4 from _call_gat_4 

#GAT.3.2
label gat_3_2:
    $ quick_menu = True
    
    show aimee_neutre at gat_center
    with fade

    anthrax "Wow... Quand je te vois maintenant... Je ne pensais pas..."

    aimee "\"Tu ne pensais pas\" quoi ?"

    anthrax "Eh bien... Ça ne te ressemble pas. Enfin, pas au toi d’aujourd’hui."

    anthrax "Je te vois comme cette personne bien dans son corps, hyper confiante..."

    anthrax "J’ai juste un peu de mal à réaliser que tu n’as pas été... épargné.e ?"

    aimee "Hm... Je pourrais me vexer, mais je crois voir où tu veux en venir."

    aimee "Je ne pense pas que mes TCA viennent de là, il y a plein d’autres raisons que de vouloir correspondre à un standard de beauté pour que ça se déclenche."

    aimee "Ça a commencé avec moi parce que j’avais besoin de contrôle dans ma vie, et que c’était là où je le trouvais."

    aimee "Enfin... C’est ce que je préférais me raconter plutôt..."

    anthrax "Désolé.e, je ne voulais pas te blesser. J’ai été maladroit.e dans mes mots."

    anthrax "Qu’est-ce que tu sous-entends par là ?"

    aimee "Eh bien..."

    aimee "Putain, c’est pas simple d’en parler..."

    aimee "En fait, quand tu entres dans une crise... Que ce soit à te pencher au-dessus d’une cuvette et enfoncer tes doigts dans la gorge ou avaler tout ce qui tombe sous ta main..."

    aimee "Tu n’es pas toi-même. Enfin, plutôt... Tu n’as pas le contrôle sur ce que tu fais à cet instant..."

    aimee "C’est comme si tu étais possédé.e."

    aimee "Mais le pire dans tout ça, c’est que tu te sens étrangement satisfait.e après... Et c’est là où est le danger."

    aimee "Parce que ça te fait sentir bien, tu commences à croire que c’est normal, et que c’est même une solution."

    aimee "Et ensuite, tu ne te sors plus de ce cercle vicieux. Ou du moins, très difficilement..."

    anthrax "Mais maintenant, tu en as encore... ?"

    aimee "Hm... Ce n’est pas aussi simple que ça. J’en ai encore les stigmates, pour être honnête."

    aimee "Justement, je me sens bien dans mes baskets, et j’aime le reflet que je vois dans le miroir, puisque c’est la version de moi la plus heureuse que j’ai eue dans ma vie."

    aimee "Sauf peut-être quand j’étais enfant, mais je n’en ai plus tellement de souvenirs..."

    aimee "Tout le monde ne penserait pas que c’est le cas parce que dans leur tête, être gros.se équivaut à devoir automatiquement se sentir misérable."

    aimee "Mais j’étais bien plus misérable quand j’avais la peau sur les os et que mon patron me disait que je devais encore surveiller mon poids pour pouvoir faire de la contorsion."

    aimee "C’est toute une histoire..."

    anthrax "Et pas l’une des plus joyeuses..."

    aimee "Ça c’est clair..."

    call gat_4 from _call_gat_4_1 

#GAT.3.3
label gat_3_3:
    $ quick_menu = True

    show aimee_neutre at gat_center
    with fade

    anthrax "Tu as dû prendre pas mal de temps pour t'en remettre, non ?"

    aimee "Oh ça ! Et encore, je suis loin d'en avoir fini !"

    aimee "Bon, au moins je ne me prive plus de nourriture, ni me fais vomir, ni vide les placards au moindre mental breakdown."

    aimee "Juste parfois, je me reprends à y penser. Sans l'envisager hein ! C'est déjà du progrès."

    aimee "Tant que je ne rechute pas, c'est le principal."

    anthrax "C'est quelque chose qui t'inquiète ? De rechuter ?"

    aimee "Oui, et non... J'ai suffisamment dépassé tout ça et me suis construit une force mentale telle que je ne me laisserais pas retomber."

    aimee "Et d'un autre côté, c'est toujours une peur un peu irrationnelle qui ne me quitte jamais."

    aimee "Surtout que sur le chemin de la convalescence, j'ai eu beaucoup de hauts et de bas."

    aimee "Des périodes qui allaient vraiment très bien, et d'autres où je me sentais comme la dernière des merdes."

    aimee "Chacune durait plus ou moins longtemps. Des mois même !"

    aimee "Et mon corps qui subissait tout ça au passage."

    anthrax "Ça a fini par se stabiliser du coup ?"

    aimee "Visualise ça comme un yo-yo. Sans mauvais jeu de mot."

    aimee "Au début, il descend et remonte très fort, jusqu'à perdre en vélocité. Et ensuite, il rebondit de moins en moins haut et de moins en moins bas."

    anthrax "Bon, un yo-yo finit quand même par se stopper tout en bas..."

    aimee "Imagine qu'il n'y a pas de gravité dans ce cas. Ah mais du coup, le yo-yo ne tomberait pas en premier lieu..."

    aimee "Bon, oublie cette métaphore foireuse !"

    aimee "Ce qui compte, c'est qu'au fil du temps, avec la volonté de guérir qui va avec parce qu'on n'a rien sans rien, les pics sont moins intenses."

    aimee "Jusqu'à disparaître."

    aimee "Et que les TCA disparaissent, c'est ça qu'on veut."

    anthrax "Et où est-ce que tu en es à présent ? Si ce n'est pas encore ça..."

    aimee "Eh bien... Disons que le yo-yo oscille. Mais il faudrait vraiment un gros coup de vent ou une catastrophe naturelle pour qu'il se remette à bouger vraiment."

    anthrax "Bon, tant mieux alors !"

    call gat_4 from _call_gat_4_2 

#GAT.4
label gat_4:

    stop music fadeout 0.5
    stop ambiance fadeout 0.5
    play music BackstageLoop volume 0.5
    play ambiance AmbLoges fadein 0.5

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

    show aimee_neutre at gat_right
    with fade

    menu: 
        anthrax "Je lui tendis en réfléchissant à quoi dire pour meubler le silence."
        "Ce n'est pas trop compliqué de performer? Je veux dire... Le rapport au corps, tout ça....?":
            call gat_4_1 from _call_gat_4_1_1 
        "Je te trouve courageux.e... Tout ce que tu réussis à accomplir sans que ça ai vraiment l'air de t'affecter":
            call gat_4_2 from _call_gat_4_2_1 
        "Je comprends, je pense. Mais tu n'as pas à te sentir gêné.e avec moi, tu sais?":
            call gat_4_3 from _call_gat_4_3 

#GAT.4.1
label gat_4_1:
    $ quick_menu = True
    
    show aimee_neutre at gat_center
    with fade

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

    stop music fadeout 0.1
    
    staff "Ok les filles ! Showtime dans dix minutes !"

    gatsby "Allez ! On doit mettre les bouchées doubles si on veut être à l'heure, girlies ! Chop-chop !"

    stop ambiance fadeout 1.0
    call gat_5 from _call_gat_5 

#GAT.4.2
label gat_4_2:
    $ quick_menu = True

    show aimee_neutre at gat_center
    with fade

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

    stop music fadeout 0.1

    staff "Ok les filles ! Showtime dans dix minutes !"

    gatsby "Allez ! On doit mettre les bouchées doubles si on veut être à l'heure girlies ! Chop-chop !"
    
    stop ambiance fadeout 2.0
    call gat_5 from _call_gat_5_1 

   
#GAT.4.3
label gat_4_3:
    $ quick_menu = True

    show aimee_neutre at gat_center
    with fade

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

    stop music fadeout 0.1

    staff "Ok les filles ! Showtime dans dix minutes !"

    gatsby "Allez ! On doit mettre les bouchées doubles si on veut être à l'heure, girlies ! Chop-chop !"

    stop ambiance fadeout 2.0
    call gat_5 from _call_gat_5_2 

#GAT.5
label gat_5:

    play music ShowGatsby noloop

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

    stop music fadeout 2.0

call gat_6 from _call_gat_6_1
call gat_6 from _call_gat_6 

#GAT.6
label gat_6:


#Dialogue WIP 


#Choix GAT.6
label choix_gat6:
    $ quick_menu = False
    
    show aimee_neutre at gat_right
    with fade

    menu: 
        "WIP":
            call gat_6_good from _call_gat_6_good 
        "WIP":
            call gat_6_bad from _call_gat_6_bad 

#GAT.6.GOOD
label gat_6_good:
    $ quick_menu = True
    
    show aimee_neutre at gat_center
    with fade

    anthrax "WIP"
    aimee "WIP"
    call final_gatsby from _call_final_gatsby 

#GAT.6.BAD
label gat_6_bad:
    $ quick_menu = True
    
    show aimee_neutre at gat_center
    with fade

    anthrax "WIP"
    mother "WIP"
    call final_gatsby from _call_final_gatsby_1 

    

label final_gatsby:
    hide aimee_neutre
    hide loges

    $ quick_menu = False
    
    scene background_cg
    show CG_gatsby with fade
    
    pause 1.0
    "Nouvelle illustration débloquée"
    hide CG_gatsby with fade
    $ persistent.peacock_unlocked = True
    "Interview et musiques débloquées"
    pause 1.0

    scene black with fade

    $ renpy.full_restart()

