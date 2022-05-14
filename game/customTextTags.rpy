'''
made by Robeshiri ⚙: https://github.com/rjscdev
📦this are the text effects for the dialogs
'''
init python:
    #imports the random and math libraries
    import random 
    import math 
    
    class DisplaytxtStyles(): #this dictionaries help us to maintain what styles we want to apply and help us
        custom_tags = ["st", "rt", "bt", "move" "xpld","xpldH","glitch"]
        accepted_tags = ["", "b", "s", "u", "i", "color", "alpha", "font", "size", "outlineC", "plain"]
        custom_cancel_tags = ["/" + tag for tag in custom_tags]
        cancel_tags = ["/" + tag for tag in accepted_tags]
        def __init__(self):
            self.tag{}

        def add_tags(self, char):
            tag, _, value = char.partition("=") #this separates the tags of thier info

            if tag in self.accepted_tags or tag in self.custom_tags: # this add tag to the dictionary
                if value == "":
                    self.tags[tag] = True
                else:
                    self.tags[tag] = value
                return True 
            
            if tag in self.cancel_tags or tag in self.custom_cancel_tags:
                tag = tag.replace("/", "")
                self.tags.pop(tag)
                return False #this makes other tags pass if we got other

        #applynig all styles to the string    
        def apply_style(self, char):
            new_string = ""
            new_string += self.start_tags()
            new_string += char
            new_string += self.end_tags()
            return new_string

        def start_tags(self):
            new_string = ""
            for tag in self.custom_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            for tag in self.accepted_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
                return new_string

    '''
    Here are all the new text classes
    '''

    class ShakeText(renpy.Displayable):
        def __init__(self, child, square=2, **kwargs):
            super(ShakeText, self).__init__(**kwargs)

            self.child = child
            self.square = square #this define the size of the movement space for the random motion of the text

        def render(self, width, height, st, at):
            #this applies the random motion to the offset of the text's render
            xoff = (random.random()-.5) * float(self.square)
            yoff = (random.random()-.5) * float(self.square)

            child_tender = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            render.subpixel_blit(child_render, (xoff, yoff))
            renpy.redraw (self, 0)
            return render

        def visit(self):
            return [self.child]
    
    class RotationText(renpy.Displayable):
        def __init__(self, child, speed=300, **kwargs):
            super(RotationText, self).__init__(**kwargs)

            self.child = child
            self.speed = speed #the speed of the rotation
            
        def render(self, width, height, st, at):

            theta = math.radians(st * float(self.speed))
            t = Transform(child=self.child, rotate=s*float(self.speed))
            child_render = renpy.render(t, width, height/2, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height/2)

            render.blit(child_render, (0,0))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return[self.child]

    class BounceText(renpy.Displayable):
        def __init__(self, child, char_offset, b_height=20, **kwargs):
            super(bounceTag, self).__init__(**kwargs)

            self.child = child
            self.b_height = b_height
            self.char_offset = char_offset
            self.freq = 4.0 #this is how fast the text bounce

        def render(self, width, height, st, at):
            curr_height = math.sin(self.freq*(st+(float(self.char_offset)* -.1))) * float(self.b_height)

            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # This will position our child's render. Replacing our need for an offset Transform
            render.subpixel_blit(child_render, (0, curr_height))

            renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

    class MoveText(renpy.Displayable):
        def __init__(self, child, **kwargs):
            super(MoveText, self).__init__(**kwargs)
            self.affect_distance = 150
            self.child = child
            self.mouse_pos = (1000,1000)
            self.pos = (0,0)

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            # x and y we get in the event function are relative to the top left corner of the displayable initially.
            # So we'll want to update it to reflect the actual position of our text
            trans_x = self.mouse_pos[0] - self.pos[0] - (self.width / 2)
            trans_y = self.mouse_pos[1] - self.pos[1] - (self.height / 2)

            vl = math.hypot(trans_x,trans_y)
            xpos, ypos = self.pos
            # Can skip calculation if vector length is further than our specified effect distance
            if vl < self.affect_distance:
                distance = 3.0 * (self.affect_distance-vl) / self.affect_distance
                xpos -= distance * trans_x / vl
                ypos -= distance * trans_y / vl
                self.pos = (xpos, ypos) # Preserve the new pos
            # Use our child's position as determined by the event function
            render.subpixel_blit(child_render, (xpos, ypos))
            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            self.mouse_pos = (x,y)
            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]
    
    class ExplodeText(renpy.Displayable):
        def __init__(self, child, timer=2, **kwargs):
            super(ExplodeText, self).__init__(**kwargs)
            self.child = child
            self.curr_x = 0
            self.curr_y = 0
            self.timer = timer
            self.gravity = 300
            self.v0_x = (renpy.random.random() - 0.5) * 800.0
            self.v0_y = renpy.random.random() * -700.0

        def render(self, width, height, st, at):
            curr_x = 0
            curr_y = 0
            if st > self.timer:
                st -= self.timer
                curr_x = self.v0_x * st
                curr_y = self.v0_y * st + self.gravity * pow(st,2)
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # This will position our child's render. Replacing our need for an offset Transform
            render.subpixel_blit(child_render, (curr_x, curr_y))
            if curr_y < 2000:
                renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def visit(self):
            return [ self.child ]

    class ExplodeHalfText(renpy.Displayable):
        def __init__(self, child, length, id, explode_point, timer=2, **kwargs):
            super(ExplodeHalfText, self).__init__(**kwargs)
            self.child = child
            self.curr_x = 0
            self.curr_y = 0
            self.timer = timer
            self.length = length
            self.id = id
            self.gravity = 300
            self.v0_x = (id - explode_point) * 100
            self.v0_y = math.cos((id - explode_point) * math.pi * (1.0/(2.0 * length))) * -900
            # self.v0_y = (-abs(id - explode_point) + length) * -35

        def render(self, width, height, st, at):
            curr_x = 0
            curr_y = 0
            if st > self.timer:
                st -= self.timer
                curr_x = self.v0_x * st
                curr_y = self.v0_y * st + self.gravity * pow(st,2)
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # This will position our child's render. Replacing our need for an offset Transform
            render.subpixel_blit(child_render, (curr_x, curr_y))
            if curr_y < 2000:
                renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def visit(self):
            return [ self.child ]

    class GlitchText(renpy.Displayable):
        def __init__(self, child, amount, **kwargs):
            super(GlitchText, self).__init__(**kwargs)
            if isinstance(child, (str, unicode)):
                self.child = Text(child)
            else:
                self.child = child
            self.amount = amount

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            y = 0
            while y < self.height:
                glitch_occurs = renpy.random.random() * 100 < self.amount
                if glitch_occurs:
                    curr_height = renpy.random.randint(-10,10)
                else:
                    curr_height = renpy.random.randint(0,10)
                curr_offset = renpy.random.randint(-10,10)
                curr_surface = child_render.subsurface((0,y,self.width,curr_height))
                if glitch_occurs:
                    render.subpixel_blit(curr_surface, (curr_offset, y))
                else:
                    render.subpixel_blit(curr_surface, (0, y))
                if curr_height > 0:
                    y += curr_height
                else:
                    y -= curr_height
            renpy.redraw(self,0)
            return render
    
    #the new text tags
    config.custom_text_tags["st"] = shake_tag
    config.custom_text_tags["rt"] = rotate_tag
    config.custom_text_tags["bt"] = bounce_tag
    config.custom_text_tags["move"] = move_tag
    config.custom_text_tags["xpld"] = explode_tag
    config.custom_text_tags["xpldH"] = explodeHalf_tag
    config.custom_text_tags["glitch"] = glitch_tag            