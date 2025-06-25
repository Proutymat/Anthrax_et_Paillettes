define config.tag_layer = {
    'wip' : 'front',
    'gradiant_noir' : 'front',
    'gradiant_tranparent' : 'front',
    'curtain_open' : 'front',
    'curtain_close' : 'front',
    'curtain' : 'front',
    'aimee_irritated': 'back',
    'aimee_laugh' : 'back',
    'aimee_nosmile' : 'back',
    'aimee_pensive' : 'back',
    'aimee_neutre' : 'back',
    'delaunay_flirty' : 'back',
    'delaunay_neutre' : 'back',
    'delaunay_nosmile' : 'back',
    'delaunay_shy' : 'back',
    'delaunay_laugh' : 'back',
    'gatsby_irritated' : 'back',
    'gatsby_neutre' : 'back',
    'gatsby_nosmile' : 'back',
    'gatsby_pensive' : 'back',
    'gatsby_laugh' : 'back',
    'imani_emo' : 'back',
    'imani_laugh' : 'back',
    'imani_neutre' : 'back',
    'imani_nosmile' : 'back',
    'imani_sassy' : 'back',
    'leandre_flirty' : 'back',
    'leandre_laugh' : 'back',
    'leandre_neutre' : 'back',
    'leandre_nosmile' : 'back',
    'leandre_shy' : 'back',
    'mother' : 'back',
    'mother_laugh' : 'back',
    'peacock_neutre' : 'back',
    'peacock_nosmile' : 'back',
    'peacock_sassy' : 'back',
    'peacock_emo' : 'back',
    'peacock_laugh' : 'back',
    'CG_delaunay' : 'CGs',
    'CG_gatsby' : 'CGs',
    'CG_peacock' : 'CGs',
    'flirt' : 'CGs',
    'angry' : 'CGs',
    'joy' : '',
    'joy' : 'CGs',
    'sadness' : 'CGs',
    'sparkling_click' : 'farthestBack',
    'light_solo_left' : 'farthestBack',
    'light_solo_middle' : 'farthestBack',
    'light_solo_right' : 'farthestBack',
    'devanture' : 'farthestBack',
    'auditorium': 'farthestBack',
    'bar': 'farthestBack',
    'loges': 'farthestBack',
    'rideau': 'farthestBack',
    'balcon': 'farthestBack',
    'background_cg' : 'farthestBack',
    'tuto' : 'farthestBack'
}

init -1 python:
    class MouseParallax(renpy.Displayable):
        def __init__(self, layer_info):
            super(renpy.Displayable, self).__init__()
            self.xoffset, self.yoffset = 0.0, 0.0

            self.sort_layer = sorted(layer_info, reverse=True)
            cflayer = []
            masteryet = False
            for m, n in self.sort_layer:
                if (not masteryet) and (m < 0):
                    cflayer.append("master")
                    masteryet = True
                cflayer.append(n)
            if not masteryet:
                cflayer.append("master")
            cflayer.extend(["transient", "screens", "overlay"])
            config.layers = cflayer
            config.overlay_functions.append(self.overlay)
            return

        def render(self, width, height, st, at):
            return renpy.Render(width, height)

        def parallax(self, m):
            func = renpy.curry(trans)(disp=self, m=m)
            return Transform(function=func)

        def overlay(self):
            if persistent.bg_parallax:
                ui.add(self)
                for m, n in self.sort_layer:
                    renpy.layer_at_list([self.parallax(m)], n)
            return


        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.MOUSEMOTION:
                self.xoffset = ((float)(x) / (config.screen_width)) - 0.5
                self.yoffset = ((float)(y) / (config.screen_height)) - 1.0
            return

    def trans(d, st, at, disp=None, m=None):
        d.xoffset, d.yoffset = int(round(m * disp.xoffset)), int(round(m * disp.yoffset))
        if persistent.bg_parallax is False:
            d.xoffset, d.yoffset = 0, 0
        return 0

    MouseParallax([
        (-20, "farthestBack"),
        (-30, "CGs"),
        (-50, "farBack"),
        (-80, "back"),
        (-30, "front"),
        (-40, "curtain"),
        (50, "inyourface")
    ])
