define peacock_character = Character("Peacock", color = "#FFFF00", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])

image CG_peacock = "images/CGs/peacock.jpg"

label peacock_start:
    peacock_character "Yo. C'est Peacock."
    
    peacock_character "Viens on se marie?"
    
    scene CG_peacock with fade

    $ persistent.peacock = True
    "Une nouvelle illustration est disponible dans l'album"
    "Musiques et Interviews débloquées"
    pause 1.0
    scene black with fade

$ renpy.full_restart()