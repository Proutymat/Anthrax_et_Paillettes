screen gallery_navigation:
    vbox:
        style_prefix "gallery"
        spacing 75
        xoffset -70
        yoffset 50
        textbutton "Delaunay" action ShowMenu("gallery_delaunay")
        textbutton "Gatsby" action ShowMenu("gallery_gatsby")
        textbutton "Peacock" action ShowMenu("gallery_peacock")
  
        textbutton "Retour":
            action ShowMenu("backstagesR")
            yoffset 150

style gallery_button_text:
    hover_color "#5c0303"
    selected_color "#5c0303"
    size 70