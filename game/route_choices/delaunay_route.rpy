define delaunay_character = Character("Delaunay", color = "#ff0000", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])

image CG_delaunay = "images/CGs/delaunay.jpg"

label delaunay_start:
    delaunay_character "Yo. C'est Delaunay."

    delaunay_character "Viens on se marie ?"

    scene CG_delaunay with fade

    $ persistent.delaunay = True
    "Une nouvelle illustration est disponible dans l'album"
    "Musiques et Interviews débloquées"
    pause 1.0
    scene black with fade

$ renpy.full_restart()
