from base_screen import BaseScreen

from .main_screen import MainScreen
from ..graphic_utils import ListView, ScreenObjectsManager, TextItem, TouchAndTextItem

from ..input import InputManager

class Tracklist(BaseScreen):
    def __init__(self, size, base_size, manager, fonts):
        BaseScreen.__init__(self, size, base_size, manager, fonts)
        self.size = size
        self.base_size = base_size
        self.manager = manager
        self.list_view = ListView((0, 0), (
            self.size[0], self.size[1] -
            self.base_size), self.base_size, self.fonts['base'], 1)
        self.tracks = []
        self.tracks_strings = []
        self.update_list()
        self.track_started(
            self.manager.core.playback.current_tl_track.get())
        self.screen_objects = ScreenObjectsManager()
        
        # javey: shuffle button
        button = TouchAndTextItem(self.fonts['icon'], u"\ue629 ",
                                  (self.size[0] - 120, self.size[1] - (self.base_size*2)), None)
        self.screen_objects.set_touch_object("shuffle", button)

    def should_update(self):
        return self.list_view.should_update()

    def update(self, screen, update_type, rects):
        update_all = (update_type == BaseScreen.update_all)
        self.list_view.render(screen, update_all, rects)

        #javey: update shuffle button location
        self.screen_objects.get_touch_object("shuffle").pos = (self.size[0] - 120, self.size[1] - (self.base_size*2));
        self.screen_objects.render(screen)

    def tracklist_changed(self):
        self.update_list()

    def update_list(self):
        self.tracks = self.manager.core.tracklist.tl_tracks.get()
        self.tracks_strings = []
        for tl_track in self.tracks:
            self.tracks_strings.append(
                MainScreen.get_track_name(tl_track.track))
        self.list_view.set_list(self.tracks_strings)

    def touch_event(self, touch_event):
        if touch_event.type == InputManager.click:
            clicked = self.list_view.touch_event(touch_event)
            if clicked is not None:
                 x = 0;
 #               self.manager.core.playback.play(self.tracks[clicked])
            else:
                # javey: shuffle functionality
                clicked = self.screen_objects.get_touch_objects_in_pos(
                    touch_event.down_pos)
                if len(clicked) > 0:
                    clicked = clicked[0]
                    if clicked == "shuffle":
                        self.manager.core.tracklist.shuffle();



    def track_started(self, track):
        self.list_view.set_active(
            [self.manager.core.tracklist.index(track).get()])
