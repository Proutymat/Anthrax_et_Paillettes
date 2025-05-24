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
    add "images/CustomUI/bg gallery.jpg"
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 70
        grid 3 3:
            add gallery.make_button(name="delaunay",unlocked="images/CGs/small/delaunay_small.jpg",locked="images/CGs/small/locked.jpg") 
            add gallery.make_button(name="gatsby",unlocked="images/CGs/small/gatsby_small.jpg",locked="images/CGs/small/locked.jpg") 
            add gallery.make_button(name="peacock",unlocked="images/CGs/small/peacock_small.jpg",locked="images/CGs/small/locked.jpg") 
            spacing 15
        textbutton "Return" action Return()