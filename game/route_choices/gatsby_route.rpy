define gatsby_character = Character("Gatsby", color = "#0000ff", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])

image CG_gatsby = "images/CGs/gatsby.jpg"

label gatsby_start:
    gatsby_character "Yo. C'est Gatsby."

    gatsby_character "Viens on se marie?"

    scene CG_gatsby with fade

    $ persistent.gatsby = True
    "Une nouvelle illustration est disponible dans l'album"
    "Musiques et Interviews débloquées"
    pause 1.0
    scene black with fade

$ renpy.full_restart()

 