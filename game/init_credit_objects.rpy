
############################################################################################################################################

# credit lists that are split into categories that are used in template 2c

define team_credits_list = [
    Credit(
        name = "Nathanaël DEFEUILLET",
        role = "Writer & Narrative Designer",
        image_name = "images/Credits/nath.png",
        #url_list = [
            #("itch-io", "https://gaming-variety-potato.itch.io/"),
            #("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        #]
    ),
    Credit(
        name = "Moumine KONATE",
        role = "Programmer, UI/UX Designer,\nUser Researcher & Knowledge Manager",
        image_name = "images/Credits/moumine.png",
    ),
    Credit(
        name = "Justine DESMEDT",
        role = "UI Artist",
        image_name = "images/Credits/justine.png",
    ),
    Credit(
        name = "Gabriele ENNAOUAJI",
        role = "Character & Environment Artist",
        image_name = "images/Credits/gabriele.png",
    ),
    Credit(
        name = "Candice DELORME",
        role = "Sound Designer & Composer",
        image_name = "images/Credits/candice.png",
    )
]


define help_credits_list = [
    Credit(
        name = "Maïa/Mäx BEAUVOIS",
        role = "Project Management Consultant",
        image_name = "images/Credits/max.png",
    ),
    Credit(
        name = "Daphné RENAULD",
        role = "VFX & UI Artist",
        image_name = "images/Credits/daph.png",
    ),
    Credit(
        name = "Lily BEAUHAIRE",
        role = "Poster Artist",
        image_name = "images/Credits/lily.png",
   ),
    Credit(
        name = "Natanael ROSSIGNOL",
        role = "Typographer",
        image_name = "images/Credits/nat.png",
    )
]

define drags_credits_list = [
    #Credit(name = "Gaming Variety Potato", role = "Artist", image_name = "logo", #url_list = [
        #("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    #]
    #),
    Credit(name = "Léo Pardchouli", role = "Drag King", image_name = "images/credits/leo.png"),

    Credit(name = "Marie Soterie", role = "Drag Queen / King", image_name = "images/credits/marie.png"),

    Credit(name = "Orkidd Opamine", role = "Drag Flower", image_name = "images/credits/orkidd.png"),

    Credit(name = "Lethal Strawberry", role = "Drag Queen", image_name = "images/credits/lethal.png"),

    Credit(name = "Jaj Hope", role = "Drag Queen", image_name = "images/credits/jaj.png"),

    Credit(name = "Kate Amary", role = "Drag Queen", image_name = "images/credits/kate_amary.png"),

    Credit(name = "IbuProfem", role = "Drag Queer", image_name = "images/credits/ibuprofem.png"),

    Credit(name = "L'imberbe", role = "Drag King", image_name = "images/credits/limberbe.png"),

    Credit(name = "Urazoria", role = "Drag Kréature", image_name = "images/credits/urazoria.png"),

]

define templates = [
    #Credit(name = "Gaming Variety Potato", role = "Artist", image_name = "logo", #url_list = [
        #("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    #]
    #),
    Credit(name = "Feniks", role = "Juxebox & Interview template / https://feniksdev.com ", image_name = ""),

]



define categorised_credits_list = [
    # item 1: category Director
    CategorisedCredits(category = "Les Paillettes", credit_list = team_credits_list),
    # item 2: category Writing
    CategorisedCredits(category = "External help", credit_list = help_credits_list),
    # item 3: category Art
    CategorisedCredits(category = "Helping shining drags", credit_list = drags_credits_list),
    # item 4: category Audio
    CategorisedCredits(category = "Templates", credit_list = templates)
]
