# button_strip.py
#
# A button strip holds a "strip" of buttons.  This is analogous to a linear layout
# in other frameworks.

# Properties:
#  - x
#  - y
#  - orientation (horiz or vert)
#  - position:
#      - cling to top
#      - cling to right side
#      - cling to bottom
#      - cling to left side
#      - absolute (in this mode, both x and y are specified by the user)
#        For the cling modes, either the x or y is implicit, depending on which
#        edge is being clung to.  For example, in "cling to right side", the
#        x is determined by the width of the largest button width.
class ButtonStrip:
    def __init__(self):
        pass
