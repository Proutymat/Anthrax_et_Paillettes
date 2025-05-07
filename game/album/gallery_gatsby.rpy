screen gallery_gatsby:
    tag menu
    add "images/CustomUI/bg gallery.jpg"
    
    hbox:
        xalign -0.055
        yalign -0.35
        spacing 30
        use gallery_navigation
        grid 3 2:
            add gallery.make_button(name="gatsby",unlocked="CGs/small/gatsby_small.jpg",locked="CGs/small/locked.jpg")at Transform(xzoom=3.5, yzoom=3.5)              
            spacing 15
