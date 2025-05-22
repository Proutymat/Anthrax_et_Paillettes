screen gallery_peacock:
    tag menu
    add "images/CustomUI/bg gallery.jpg"
    
    hbox:
        xalign 1.99
        yalign -0.35
        spacing 30
        use gallery_navigation
        grid 3 2:        
            add gallery.make_button(name="peacock",unlocked="CGs/small/peacock_small.jpg",locked="CGs/small/locked.jpg") at Transform(xzoom=3.5, yzoom=3.5)  
            spacing 15
