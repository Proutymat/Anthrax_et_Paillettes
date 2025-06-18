
############################################################################################################################################

# credit lists that are split into categories that are used in template 2c

define team_credits_list = [
    Credit(
        name = "Nathanaël DEFEUILLET",
        role = "Writer & Narrative Designer",
        image_name = "images/crédits/nath.png",
        url_list = [
            ("itch-io", "https://gaming-variety-potato.itch.io/"),
            ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        ]
    ),
    Credit(
        name = "Moumine KONATE",
        role = "Programmer, UI/UX Designer,\nUser Researcher & Knowledge Manager",
        image_name = "images/crédits/moumine.png",
        url_list = [
            ("itch-io", "https://gaming-variety-potato.itch.io/"),
            ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        ]
    ),
    Credit(
        name = "Justine DESMEDT",
        role = "UI Artist",
        image_name = "images/crédits/justine.png",
        url_list = [
            ("itch-io", "https://gaming-variety-potato.itch.io/"),
            ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        ]
    ),
    Credit(
        name = "Gabriele ENNAOUAJI",
        role = "Character & Environment Artist",
        image_name = "images/crédits/gabriele.png",
        url_list = [
            ("itch-io", "https://gaming-variety-potato.itch.io/"),
            ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        ]
    ),
    Credit(
        name = "Candice DELORME",
        role = "Sound Designer & Composer",
        image_name = "images/crédits/candice.png",
        url_list = [
            ("itch-io", "https://gaming-variety-potato.itch.io/"),
            ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        ]
    )
]


define help_credits_list = [
    Credit(
        name = "Maïa/Mäx BEAUVOIS",
        role = "Project Management Consultant",
        image_name = "images/crédits/max.png",
        url_list = [
            ("itch-io", "https://gaming-variety-potato.itch.io/"),
            ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        ]
    ),
    Credit(
        name = "Daphné RENAULD",
        role = "VFX Artist",
        image_name = "images/crédits/daph.png",
        url_list = [
            ("itch-io", "https://gaming-variety-potato.itch.io/"),
            ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        ]
    ),
    Credit(
        name = "Lily BEAUHAIRE",
        role = "Poster Artist",
        image_name = "images/crédits/lily.png",
        url_list = [
            ("itch-io", "https://gaming-variety-potato.itch.io/"),
            ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        ]
    ),
    Credit(
        name = "Natanael ROSSIGNOL",
        role = "Typographer",
        image_name = "images/crédits/nat.png",
        url_list = [
            ("itch-io", "https://gaming-variety-potato.itch.io/"),
            ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
        ]
    )
]

define drags_credits_list = [
    Credit(name = "Gaming Variety Potato", role = "Artist", image_name = "logo", url_list = [
        ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    ]),
    Credit(name = "Gaming Variety Potato", role = "Artist", image_name = "logo", url_list = [
        ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    ]),
    Credit(name = "Gaming Variety Potato", role = "Artist", image_name = "logo", url_list = [
        ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    ]),
    Credit(name = "Gaming Variety Potato", role = "Artist", image_name = "logo", url_list = [
        ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    ]),
    Credit(name = "Gaming Variety Potato", role = "Artist", image_name = "logo", url_list = [
        ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    ])
]

define translators_credits_list = [
    Credit(name = "Gaming Variety Potato", role = "Musician", image_name = "logo", url_list = [
        ("itch-io", "https://www.twitter.com/gaming_v_potato/"), 
        ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    ]),
    Credit(name = "Gaming Variety Potato", role = "Musician", image_name = "logo", url_list = [
        ("itch-io", "https://www.twitter.com/gaming_v_potato/"), 
        ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    ]),
    Credit(name = "Gaming Variety Potato", role = "Musician", image_name = "logo", url_list = [
        ("itch-io", "https://www.twitter.com/gaming_v_potato/"), 
        ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    ])
]


define categorised_credits_list = [
    # item 1: category Director
    CategorisedCredits(category = "Les Paillettes", credit_list = team_credits_list),
    # item 2: category Writing
    CategorisedCredits(category = "External help", credit_list = help_credits_list),
    # item 3: category Art
    CategorisedCredits(category = "Helping shining drags", credit_list = drags_credits_list),
    # item 4: category Audio
    CategorisedCredits(category = "Translation", credit_list = translators_credits_list),
    # item 5: category Programming
]
