# Vous pouvez placer le script de votre jeu dans ce fichier.


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


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

image Mother:
    "concept_mother"
    zoom 0.35

image Delaunay Out Neutre:
    "concept_delaunay_in"
    zoom 0.35

image Delaunay In Neutre:
    "concept_delaunay_out"
    zoom 0.35

image Gatsby Out Neutre:
    "concept_gatsby_in"
    zoom 0.35

image Gatsby In Neutre:
    "concept_gatsby_out"
    zoom 0.35

image Peacock Out Neutre :
    "concept_peacock-out"
    zoom 0.35

image Peacock In Neutre:
    "concept_peacock_in"
    zoom 0.35

image Auditorium = "Backgrounds/concept_auditorium.png"



# Liste des sfx
define type_sounds = ['TextMix-001.ogg','TextMix-002.ogg','TextMix-003.ogg','TextMix-004.ogg','TextMix-005.ogg','TextMix-006.ogg','TextMix-007.ogg','TextMix-008.ogg','TextMix-009.ogg','TextMix-010.ogg']

# Liste des musiques
define audio.testmusic1 = "Hypnotized.mp3"
define audio.testmusic2 = "AP_BigBand_V1.ogg"

# Déclarez les personnages utilisés dans le jeu.
define m = Character('Mother', color="#c8ffc8", what_slow_cps=25, callback=type_sound, cb_cps=25)
define a = Character('Anthräx', what_slow_cps=35, callback=type_sound, cp_cps=35)
define b = Character('Barman', what_slow_cps=40, callback=type_sound, cb_cps=40)
define j = Character('Jazz', what_slow_cps=50, callback=type_sound, cb_cps=50)

# Le jeu commence ici
label start:

    play music testmusic1 fadein 10.0

    a "L'Androgame..."

    a "C'est dingue à quel point ce cabaret a reprit ses lettres de noblesse."

    a "Je me souviens encore de quand je passais devant pour aller prendre le métro... Complètement défraichit, la pierre sale et les fenêtres brisées."

    a "On se demandait quand est-ce qu'ils finiraient par abréger ses souffrances et le démolir."

    a "Cela fait un moment maintenant qu'il a été reprit, et après de longs et nombreux travaux, il fait à présent revivre le quartier comme je ne l'ai jamais vu auparavant."

    a "Et puis même au sein de la commu', ça a fait jaser. Toutes les têtes d'affiches sont queer."

    a "Ça fait presque bizarre de nous voir se réapproprier une époque dans laquelle on n'avait pas le droit de réellement exister."

    a "Je suis sûr.e qu'on n'aurait jamais autant flamboyé que dans les années 20... C'est peut-être pour ça qu'on était <<interdits>> ? On aurait trop volé la vedette aux hétéros."

    a "Les plumes, la fourrure, les paillettes, le champagne, le charleston, l'occasionnel rail de coke... Les années folles quoi."

    a "C'est ce qui m'a motivé à me lancer dans le drag finalement..."

    a "J'ai toujours été intrigué.e par cette forme d'expression. Et à voir ces artistes bourré.e.s de talent faire leur show, à deux pas de chez moi... Je me suis laissé.e tenter."

    a "Au début, j'en avais un peu honte. Je me costumais en cachette dans mon appart, et pour être honnête, c'était peut-être pour le mieux."

    a "Mes premières tentatives de make-up étaient catastrophiques... Mais au fur et à mesure, j'ai pris le coup de pinceau."

    a "Ce que je pensais être une lubie est finalement devenu un hobby."

    a "J'ai pris des classes pour apprendre à coudre et danser, au point où même mes ami.e.s ont capté ce qui se tramait et se sont prêté.e.s au jeu pour m'aider à m'améliorer."

    a "Puis j'ai créé des comptes dédiés à ma pratique sur les réseaux sociaux. Et là, tout est devenu plus sérieux..."

    a "Je faisais mon petit contenu et continuait ma vie tranquillement à côté, en passant toujours devant l'Androgame pour aller au travail."

    a "Alors quand ils ont lancé des auditions pour agrandir la troupe, j'ai longuement hésité. Je ne me sentais pas légitime de rentrer dans cette sphère."

    a "Je ne savais pas comment j'allais pouvoir concilier le burlesque et le travail, ce qu'on pourrait dire de moi ou juger de mon drag."

    a "Je pense que j'ai décidé d'arrêter d'essayer de me justifier lorsque j'étais aux portes du bâtiment. Après tout, je n'avais rien à perdre et j'aurais regretté de ne pas avoir au moins essayé."

    a "Je ne pensais pas être sélectionné.e, encore moins de passer un entretien avec Mother, la patronne du cabaret. Je n'ai pas trop compris, mais elle m'a parlé des règles de conduite au sein de la troupe et envers les clients, puis d'une période d'essai..."

    stop music fadeout 1.5

    a "J'avais du mal à réaliser, mais on a convenu d'une nouvelle date d'entretien, en journée quand le cabaret serait vide, où elle m'expliquerait plus en détails le fonctionnement des backstages."

    play music testmusic2 fadein 0.5

    define m = Character('Mother', color="#c8ffc8", what_slow_cps=50, callback=type_sound, cb_cps=50)

    scene concept_auditorium

    show Mother

    m "Bienvenue dans l'Androgame! J'espère que tu as fait bonne route."

    define m = Character('Mother', color="#c8ffc8", what_slow_cps=25, callback=type_sound, cb_cps=25)

    m "Tu avais l'air de dire dans nos échanges que tu n'habitais pas trop loin, le chemin n'a pas dû être bien compliqué."

    a "En effet, une fois que j'avais passé la porte pivotante, la hauteur sous plafond et les lustres géométriques faillirent me donner un torticolis. "

    a "Je devais presque plisser les yeux pour repérer tous les petits détails dans la marqueterie, les dorures et les formes dans le papier peint."

    a "Oui. Et puis, c'est le genre d'établissement qu'il est difficile de louper!"

    m "Aha! Tu m'en vois ravie de l'entendre."

    m "Je ne fais pas te faire patienter plus longtemps... Commençons par te faire une petite visite des lieux. Promis, tu vas t'y retrouver bien vite."

    m "En arrivant, tu es passé.e par le lobby, le hall d'entrée, l'accueil... Tu peux l'appeler comme tu veux. Mais dans l'idée, passé ce guichet, les clients payent!"

    m "Ce n'est pas trop dans notre politique cette histoire du <<le client est roi>>, mais tu apprendras vite que c'est là que les pourboires se cachent~"

    m "Et nous voici donc dans l'auditorium! Il sera un peu comme ton meilleur ennemi, car peu importe le trac ou qui se retrouvera dans le public, il faudra grimper sur les planches!"

    m "Après, si tu es ici aujourd'hui, c'est par ce que c'est justement le genre de chose qui t'anime: te mettre en scène..."

    a "Je ne l'avais pas encore abordé de cette perspective, mais l'idée d'être au milieu de cette scène, avec tous les regards tournés vers moi, m'excitait autant que me faisait appréhender."

    a "J'ai mis cette pensée sur le compte de l'inexpérience, et ai continué ma visite avec Mother"

    scene concept_bar

    a "Nous nous sommes approché.e.s du comptoir derrière lequel brillaient un mur de bouteilles de formes et couleurs uniques. Le paradis du parfait mixologue."

    a "Nous avions depuis le bar une vue imprenable sur la scène, légèrement en contrebas. Les tablées y étaient déjà dressées et se regroupaient autour du big band et de l'estrade secondaire au centre de la pièce."

    a "L'immense lustre duquel pendaient des larmes de verre reflétait les spots de lumière à la manière d'une boule à facette sur le papier peint texturé."

    show Mother

    m "Je te présente BARMAN, c'est lui qui tient le bar."

    m "Ne t'en fais pas, il a beau avoir une tête de doberman, il ne mord pas."

    b "Vu comment tu me vends Mama, c'est pas comme ça que tu vas le.a rassurer..."

    b "Nan, plus sérieusement, bienvenue. Tu verras, c'est sympa ici."

    b "On prend un verre ici avec les filles après la tombée du rideau pour débriefer de la journée et kiki un peu..."

    b "Et si jamais tu as des clients relous, n'hésite pas à me faire un signe, ou à n'importe qui d'autre du staff. On viendra s'en occuper."

    m "Je plussoie. On protège les nôtres ici, inconditionnellement."

    m " On discute tout à l'heure BARMAN ? Je termine la visite, puis j'arrive pour l'inventaire."

    b "Ça marche. Bye!"

    a "Après avoir monté les escaliers en colimaçon et traversé les gradins, surplombant le reste de la salle de spectacle, nous nous sommes arreté.e.s sur les rembardes pour discuter davantage de ce que Mother attendait de ses nouvelles recrues."

    a "Evidemment, je n'allais pas de suite avoir mon propre tour. Il fallait d'abord que j'adapte mon personnage à l'ambiance du cabaret et réfléchisse aux talents que je souhaiterais mettre en avant sur scène. Quelque chose qui me démarque des autres. "

    a "En sous-texte: j'avais besoin de faire mes preuves..."

    m "C'est peut-être impressionnant dit dans ces termes, mais je suis sûre que tu es à la hauteur du challenge. Après tout, si je t'ai choisi.e lors des castings, c'est que j'ai bien remarqué du potentiel chez toi."

    j "Excusez-moi, je peux vous interrompre?"

    m "Oh, Jasmine... Qu'est-ce qui se passe?"

    j "On a un soucis au niveau de la régie, la société qui est intervenue la semaine dernière à tout foutu en l'air."

    j "Personne ne comprend rien à leur nouveau routing, on aurait besoin de les rappeler ne serait-ce que pour comprendre leur logique avant le show de ce soir..."

    m "..."

    j "..."

    m "Je reviens vite Anthräx. Jasmine, est-ce que tu peux prendre le relais pour la visite ? Je vous rejoindrai dans les loges."

    j "O-Ok..."

    hide Mother

    a "Mother a quitté la pièce d'un pas déterminé, dégageant d'un geste vif son téléphone portable de son décolleté et composant déjà le numéro de l'entreprise, cherchant un endroit plus calme et discret pour passer sa soufflante"

    j "Bon... Bah moi, c'est Jazz. Et toi?"

    a "Anthräx... Tu travailles à la technique ici?"

    j "Pas vraiment... Je suis musicienne dans la troupe à temps partiel, mais j'en profite aussi pour faire un stage en régie."

    a "Musicienne ?"

    j "Oui, du trombone. On ne s'en serait pas douté avec le surnom, si?"

    a "Je le trouve bien pensé..."

    j "Vraiment? Ça doit être le blaze moins original de la terre! Ils ne se sont pas foulés... Mais bon, je m'y suis attachée quand même."

    a "Jasmine avait l'air d'être le genre de fille qui ne se prenait pas trop la tête, en plus d'être accessible. Elle a blagué tout le long de la visite sur de petites anecdotes de clients, c'était assez rassurant. Elle a dû sentir que je n'étais pas encore très à l'aise."

    




    return
