label route_return:
    scene black
    with fade
    $ renpy.pause(0.1)
    jump choose_route


define short_fade = Fade(0.1, 1, 0.2)

label choose_route:
    scene black
    show expression "images/Backgrounds/background_cg.png"
    $ persistent.bg_parallax = False
    $ quick_menu = False

    window hide

    call screen route_choice_buttons

    return


screen route_choice_buttons():
    modal True

    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30
        spacing 20

        imagebutton:
            auto "images/routes/delaunay_route_%s.png"
            action [Function(renpy.transition, fade), Jump("confirm_choice_delaunay")]

        imagebutton:
            auto "images/routes/gatsby_route_%s.png"
            action [Function(renpy.transition, fade), Jump("confirm_choice_gatsby")]
        

        imagebutton:
            auto "images/routes/peacock_route_%s.png"
            action [Function(renpy.transition, fade), Jump("confirm_choice_peacock")]


label confirm_choice_delaunay:
    $ quick_menu = False
    $ persistent.bg_parallax = False

    scene expression "images/backgrounds/routes_confirmation/delaunay_route_background.png"
    window hide

    python:
        ui.hbox(xalign=0.885, yalign=0.865, spacing=55)
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/oui_route_idle.png",
            hover="images/backgrounds/routes_confirmation/oui_route_hover.png",
            clicked=ui.returns("oui")
        )
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/non_route_idle.png",
            hover="images/backgrounds/routes_confirmation/non_route_hover.png",
            clicked=ui.returns("non")
        )
        ui.close()
        choix = ui.interact()

    window hide

    if choix == "oui":
        $ persistent.bg_parallax = True
        jump delaunay_start
    else:
        $ persistent.bg_parallax = False
        jump route_return



    
label confirm_choice_gatsby:
    $ quick_menu = False
    $ persistent.bg_parallax = False

    scene expression "images/backgrounds/routes_confirmation/gatsby_route_background.png"
    window hide

    python:
        ui.hbox(xalign=0.885, yalign=0.865, spacing=55)
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/oui_route_idle.png",
            hover="images/backgrounds/routes_confirmation/oui_route_hover.png",
            clicked=ui.returns("oui")
        )
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/non_route_idle.png",
            hover="images/backgrounds/routes_confirmation/non_route_hover.png",
            clicked=ui.returns("non")
        )
        ui.close()
        choix = ui.interact()

    window hide

    if choix == "oui":
        $ persistent.bg_parallax = True
        jump gatsby_start
    else:
        $ persistent.bg_parallax = False
        jump route_return



label confirm_choice_peacock:
    $ quick_menu = False
    $ persistent.bg_parallax = False

    scene expression "images/backgrounds/routes_confirmation/peacock_route_background.png"
    window hide

    python:
        ui.hbox(xalign=0.885, yalign=0.865, spacing=55)
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/oui_route_idle.png",
            hover="images/backgrounds/routes_confirmation/oui_route_hover.png",
            clicked=ui.returns("oui")
        )
        ui.imagebutton(
            idle="images/backgrounds/routes_confirmation/non_route_idle.png",
            hover="images/backgrounds/routes_confirmation/non_route_hover.png",
            clicked=ui.returns("non")
        )
        ui.close()
        choix = ui.interact()

    window hide

    if choix == "oui":
        $ persistent.bg_parallax = True
        jump peacock_start
    else:
        jump route_return



