label route_return:
    scene black
    with fade
    $ renpy.pause(0.1)
    jump choose_route

default hovered_character = None

transform fade_vfx:
    alpha 0.0
    linear 0.2 alpha 1.0

define short_fade = Fade(0.1, 1, 0.2)

label choose_route:
    scene black
    show expression "images/Backgrounds/menu_background_two.png"
    $ persistent.bg_parallax = False
    $ quick_menu = False

    window hide

    call screen route_choice_buttons

    return


screen route_choice_buttons():
    modal True

    fixed:

        # === VFX arrière-plan selon le crush en hover ===
        if hovered_character == "delaunay":
            add "light_solo_left" at fade_vfx
        elif hovered_character == "gatsby":
            add "light_solo_middle" at fade_vfx
        elif hovered_character == "peacock":
            add "light_solo_right" at fade_vfx


        # === HBOX avec boutons ===
        hbox:
            xalign 0.5
            yalign 0.5
            offset (0, 30)
            spacing 30

            # -- Delaunay --
            imagebutton:
                auto "images/routes/delaunay_route_%s.png"
                hovered SetVariable("hovered_character", "delaunay")
                unhovered SetVariable("hovered_character", None)
                action Show("crush_confirm", name="Léandre", destination="delaunay_start")

            # -- Gatsby --
            imagebutton:
                auto "images/routes/gatsby_route_%s.png"
                hovered SetVariable("hovered_character", "gatsby")
                unhovered SetVariable("hovered_character", None)
                action Show("crush_confirm", name="Aimé.e", destination="gatsby_start")

            # -- Peacock --
            imagebutton:
                auto "images/routes/peacock_route_%s.png"
                hovered SetVariable("hovered_character", "peacock")
                unhovered SetVariable("hovered_character", None)
                action Show("crush_confirm", name="Imani", destination="peacock_start")