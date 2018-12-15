# ui_layout.py
#
# Positions text and graphics in a defined space.
#
# Usage:
#
# The caller first instiates a UiLayout object, with a given rectangle.
# The caller next calls start(), and then addItem() to add items to the first line.
# To start a new line, newLine() is called; subsequent calls to addItem() to place those items on a new line.
# Call draw() to render the layout.

from ui_text_layout_item import UiTextLayoutItem
from ui_graphic_layout_item import UiGraphicLayoutItem
from ui_alignment import UiAlignment

class UiLayout:
    def __init__(self, areaRect, lineSpacing):
        self.rect = areaRect
        self.lineSpacing = lineSpacing

        # This is a list of lists.  Each item is a list of UiLayoutItems.
        self.lines = []

        # Heights of each line.
        self.lineHeights = []

        self.currentLine = 0
        self.layoutHasBeenSized = False     # Indicates if the layout items have had their bounding rects computed

    def start(self):
        """ Begins a layout.  This must be called before addItem() is called."""
        self.currentLine = 0
        self.layoutHasBeenSized = False
        self.lines.append([])       # Create an empty list for the first line
        self.lineHeights.append(0)  # Starting line height for this line (will be set in draw)

    def newLine(self):
        """ Starts a new line in the layout. """
        self.currentLine += 1
        self.lines.append([])
        self.lineHeights.append(0)

    def addItem(self, layoutItem):
        curLineItemList = self.lines[self.currentLine]
        curLineItemList.append(layoutItem)

    def computeLayoutItemSizes(self, pygame):
        for index, line in enumerate(self.lines):
            for layoutItem in line:
                layoutItem.computeRect(pygame)
                self.lineHeights[index] = max(self.lineHeights[index], layoutItem.height)

    def draw(self, pygame, screen):
        # First, render the layout item bounding rects, if needed
        if not self.layoutHasBeenSized:
            self.computeLayoutItemSizes(pygame)

        # Next, draw the items
        curPos = self.rect.topleft

        for lineNumber, line in enumerate(self.lines):
            lineHeight = self.lineHeights[lineNumber]

            for layoutItem in line:
                itemPos = self.computeItemPos(curPos, self.rect.width, lineHeight, layoutItem)
                layoutItem.draw(screen, itemPos)

            # Advance to next line
            curPos = curPos[0], curPos[1] + lineHeight + self.lineSpacing

    def computeItemPos(self, linePos, lineWidth, lineHeight, layoutItem):
        """ Computes the position of this layout item.
            - linePos is the position of the upper-left corner of this line. """
        linePosX = linePos[0]
        linePosY = linePos[1]
        y = linePosY + (lineHeight - layoutItem.height)  # Vertical align item with bottom of this line

        if layoutItem.hAlignment == UiAlignment.LEFT:
            x = linePosX
        elif layoutItem.hAlignment == UiAlignment.RIGHT:
            x = linePosX + lineWidth - layoutItem.width
        elif layoutItem.hAlignment == UiAlignment.CENTER:
            x = linePosX + (self.rect.width - layoutItem.width) / 2
        else:
            # Unknown alignment constant
            print("computeItemPos: Unknown alignment constant: {}.  Assuming LEFT".format(layoutItem.hAlignment))
            x = linePosX

        return x, y
