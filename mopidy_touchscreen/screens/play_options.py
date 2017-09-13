from base_screen import BaseScreen

from ..graphic_utils import ListView,\
ScreenObjectsManager, TouchAndTextItem

from ..input import InputManager

class PlayOptions(BaseScreen):

    # item_uri: The PlayOptions dialog is created after a song, album, artist, etc. is clicked. 
    # The item_uri is the URI identifier to the item that was clicked
    def __init__(self, size, base_size, manager, fonts, item_uri, playqueues=None):
        BaseScreen.__init__(self, size, base_size, manager, fonts)            
        self.list_view = ListView((self.size[0]/2, self.base_size*2), (
        self.size[0]/2 - self.base_size, self.size[1] -
            3*self.base_size), self.base_size, manager.fonts['base'],
            item_base_color=(255,255,255),item_background_color=(30,215,96))
        self.item_uri = item_uri
        self.playqueues = playqueues

        # TODO num_list_items should not be hardcoded
        self.num_list_items = 3
        self.list_view.set_list(["Play Now", "Add to queue", "Back"])
        # top-left nad bottom-right of bounding rectangle
        self.rect_tl = self.list_view.pos
        self.rect_br = (self.list_view.pos[0] + self.list_view.size[0] - 1,
            self.list_view.pos[1] + self.list_view.base_size * self.num_list_items - 1)

    def render(self, screen, update_all, rects):
        self.list_view.render(screen, update_all, rects)

    def is_position_in_dialog(self, position):
        # if the x position is within the rectangle
        if ( (position[0] >= self.rect_tl[0]) and (position[0] <= self.rect_br[0]) ): 
            # and if the y position is within the rectangle        
            if ( (position[1] >= self.rect_tl[1]) and (position[1] <= self.rect_br[1]) ): 
                return True # then the position is within bounds
        return False # not within bounds

    def touch_event(self, touch_event):
        if touch_event.type == InputManager.click :
            # Get the list position clicked (a number). 0 is the top element in the list.
            clicked_item = self.list_view.touch_event(touch_event)
            if clicked_item == 0 : 
                # clicked "Play Now"
                self.manager.core.tracklist.add(self.item_uri)
                print("Playing: {}".format(self.item_uri) )
                #self.manager.core.playback.play()
            if clicked_item == 1 :
                # clicked "Add to queue"
                print( "Added {} to queue {}".format(self.item_uri, self.playqueues.cur_queue) )               
