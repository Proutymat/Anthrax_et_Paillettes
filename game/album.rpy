init python:
    gallery = Gallery()

    gallery.button("delaunay") 
    gallery.unlock_image("CG_delaunay") 

    gallery.button("gatsby") 
    gallery.unlock_image("CG_gatsby")

    gallery.button("peacock")
    gallery.unlock_image("CG_peacock")

screen album:
    tag menu
    add "images/Backgrounds/menu_background_two.png"

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 50
        box_wrap True

        add gallery.make_button(name="delaunay", unlocked="images/CGs/small/delaunay_small.jpg", locked="images/CGs/small/locked.jpg")
        add gallery.make_button(name="gatsby", unlocked="images/CGs/small/gatsby_small.jpg", locked="images/CGs/small/locked.jpg")
        add gallery.make_button(name="peacock", unlocked="images/CGs/small/peacock_small.jpg", locked="images/CGs/small/locked.jpg")

    vbox:
        at Transform(xalign=0.1, yalign=0.98)
        imagebutton idle "menuUI/retour_idle.png" hover "menuUI/retour_hover.png" action ShowMenu("backstages")