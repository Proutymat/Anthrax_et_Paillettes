define config.tag_layer = {
    'devanture': 'farthestBack',
    'auditorium': 'farthestBack',
    'bar': 'farthestBack',
    'loges': 'farthestBack',
    'rideau': 'farthestBack',
    'mother': 'back',
    'delaunay_neutre': 'back',
    'leandre_neutre': 'back',
    'gatsby_neutre': 'back',
    'aimee_neutre': 'back',
    'peacock_neutre': 'back',
    'imani_neutre': 'back',
    'CG_delaunay' : 'front',
    'CG_gatsby' : 'front',
    'CG_peacock' : 'front',
    'background_cg' : 'farthestBack'

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
        (-50, "farBack"),
        (-80, "back"),
        (-30, "front"),
        (50, "inyourface")
    ])
