label choose_route_label:
    call screen choose_route

screen choose_route():
    tag menu
    modal True  # empêche les interactions avec les autres éléments de l’UI

    default quick_menu_backup = quick_menu
    $ quick_menu = False

    add "images/backgrounds/white_background.png"

    on "hide" action SetVariable("quick_menu", quick_menu_backup)

    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30
        spacing 20

        imagebutton:
            auto "images/routes/delaunay_route_%s.png"
            action ShowMenu("confirm_choice_delaunay")
        imagebutton:
            auto "images/routes/gatsby_route_%s.png"
            action ShowMenu("confirm_choice_gatsby")
        imagebutton:
            auto "images/routes/peacock_route_%s.png"
            action ShowMenu("confirm_choice_peacock")

screen confirm_choice_delaunay():
    tag menu
    modal True

    default quick_menu_backup = quick_menu
    $ quick_menu = False

    on "hide" action SetVariable("quick_menu", quick_menu_backup)

    add "images/backgrounds/routes_confirmation/delaunay_route_background.png"

    hbox:
        spacing 55
        at Transform(xalign=0.885, yalign=0.865)
        imagebutton idle "images/backgrounds/routes_confirmation/oui_route_idle.png" hover "images/backgrounds/routes_confirmation/oui_route_hover.png" action [Hide("confirm_choice_delaunay"), Jump("delaunay_start")]
        imagebutton idle "images/backgrounds/routes_confirmation/non_route_idle.png" hover "images/backgrounds/routes_confirmation/non_route_hover.png" action ShowMenu("choose_route")

screen confirm_choice_gatsby():
    tag menu
    modal True

    default quick_menu_backup = quick_menu
    $ quick_menu = False

    on "hide" action SetVariable("quick_menu", quick_menu_backup)

    add "images/backgrounds/routes_confirmation/gatsby_route_background.png"

    hbox:
        spacing 55
        at Transform(xalign=0.885, yalign=0.865)
        imagebutton idle "images/backgrounds/routes_confirmation/oui_route_idle.png" hover "images/backgrounds/routes_confirmation/oui_route_hover.png" action [Hide("confirm_choice_gatsby"), Jump("gatsby_start")]
        imagebutton idle "images/backgrounds/routes_confirmation/non_route_idle.png" hover "images/backgrounds/routes_confirmation/non_route_hover.png" action ShowMenu("choose_route")

screen confirm_choice_peacock():
    tag menu
    modal True

    default quick_menu_backup = quick_menu
    $ quick_menu = False

    on "hide" action SetVariable("quick_menu", quick_menu_backup)

    add "images/backgrounds/routes_confirmation/peacock_route_background.png"

    hbox:
        spacing 55
        at Transform(xalign=0.885, yalign=0.865)
        imagebutton idle "images/backgrounds/routes_confirmation/oui_route_idle.png" hover "images/backgrounds/routes_confirmation/oui_route_hover.png" action [Hide("confirm_choice_peacock"), Jump("peacock_start")]
        imagebutton idle "images/backgrounds/routes_confirmation/non_route_idle.png" hover "images/backgrounds/routes_confirmation/non_route_hover.png" action ShowMenu("choose_route")
