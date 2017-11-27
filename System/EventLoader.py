import json

from qtpy import QtGui


class Event:
    # picture output for PyQT
    picture = None
    textarr = []
    scene_array = []
    _text_array = []
    text_in_array = []
    image_location_array = []
    text = "No Event running"
    # counts which scene is running atm
    sceneCounter = 1
    # counts which text is shown from scene
    textCounter = 0
    # number of texts in scene
    texts = 0
    # number of scenes in event
    scenes = 0
    # check if event is over or not
    eventON = True
    # check if event picture changed
    picturechange = True

    def __init__(self, file):
        self.json_file = file
        print("Opening at: ", self.json_file)
        with open(self.json_file) as data_file:
            self.data = json.load(data_file)
        print("Event opened at: ", self.json_file)
        self.start_event()

    # sets events picture from file
    def event_picture(self, scene):
        location = self.data["scene" + str(scene)]["picture"]
        print("Picture file: ", location)
        self.picture = QtGui.QPixmap(location)

    # run this to set up event
    def start_event(self):
        self.scenes = len(self.data)
        print("number of scenes: ", self.scenes)
        for i in range(self.scenes):
            self.scene_array.append(self.data["scene" + str(i + 1)])

            number_of_texts = len(self.scene_array[i]["text"])
            if len(self.text_in_array) == 0:
                self.text_in_array.append(number_of_texts)
            else:
                last_number = self.text_in_array[i - 1]
                self.text_in_array.append(last_number + number_of_texts)

            self.image_location_array.append(self.scene_array[i]["picture"])
            self._text_array.extend(self.scene_array[i]["text"])

    def get_text(self, index):
        return self._text_array[index]

        #  def get_image(self, index):
