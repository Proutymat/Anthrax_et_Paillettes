init python:
    gallery = Gallery()

    gallery.button("delaunay") 
    gallery.unlock_image("CG_delaunay") 

    gallery.button("gatsby") 
    gallery.unlock_image("CG_gatsby")

    gallery.button("peacock")
    gallery.unlock_image("CG_peacock") 

  
screen gallery:
    tag menu
    add "images/CustomUI/bg gallery.jpg"
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        grid 2 2:
            add gallery.make_button(name="delaunay",unlocked="CGs/small/delaunay_small.jpg",locked="CGs/small/locked.jpg") 
            add gallery.make_button(name="gatsby",unlocked="CGs/small/gatsby_small.jpg",locked="CGs/small/locked.jpg") 
            add gallery.make_button(name="peacock",unlocked="CGs/small/peacock_small.jpg",locked="CGs/small/locked.jpg") 
           
            spacing 15
        textbutton "Return" action Return()