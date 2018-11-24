# ui_manager.py
#
# Manages all UI elements.

# Keeps track of all UI elements.  Every UI element must be registered
# with the UiManager.  UI elements have callback functions that are
# called when the user interacts with them.

class UiManager:
    def __init__(self, pygame):
        self.pygame = pygame
        self.buttonList = []
        self.touchAreaList = []

    def addElement(uiElement):
        """ Registers the given UI element. """
        if isinstance(uiElement, Button):
            self.buttonList.append(uiElement)
        elif isinstance(uiElement, TouchArea):
            self.touchAreaList.append(uiElement)

    # This should probably return a code that indicates whether the app
    # should change its status, such as to quit, or blank the screen, etc.
    def handleEvents():
        for event in self.pygame.event.get():
            if event.type == QUIT:
                self.pygame.display.quit()
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.pygame.display.quit()
                sys.exit(0)
            elif event.type == MOUSEBUTTONUP:
                self.pygame.display.quit()
                sys.exit(0)
