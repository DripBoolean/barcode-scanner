""" Class representing the default webcam. """

import cv2

_capture = None

class Image:
    """ Represents an rgb image. """
    def __init__(self, initalizer):
        """ Create an image from a filename or data. """
        if isinstance(initalizer, str):
            self.data = cv2.imread(initalizer)
        else:
            self.data = initalizer
            
    def set_from_data(self, data: any):
        """ Set the image data directly. """
        self.data = data

    def set_from_file(self, filename: str):
        """ Set the image data by loading an image from a file. """
        self.data = cv2.imread(filename)
        if self.data == None:
            raise FileNotFoundError

    def get_pixel(self, x: int, y: int) -> tuple[int, int, int]:
        """ Return the rgb data of the image at given x and y. Throws error if out of range """

        # TODO: what happens when you go out of range?
        pixel_data = self.data[y, x]
        return (int(pixel_data[2]), int(pixel_data[1]), int(pixel_data[0]))
    
    def get_dimensions(self) -> tuple[int, int]:
        """ Returns the width and height of the image. """
        height, width, channels = self.data.shape
        return (width, height)

    def display(self):
        """ Displays the image. """
        while True:
            cv2.imshow("q to exit", self.data)
            if cv2.waitKey(1) == ord('q'):
                break
    
    def output_to_file(self, filename):
        """ Writes the file to the filename. Will output based on the file extension (jpg, png, etc.)"""
        cv2.imwrite(filename, self.data)


def start():
    """ Starts recording with the webcam. """
    global _capture
    _capture = cv2.VideoCapture(0)

def stop():
    """ Stops recording with the webcam. """
    global _capture
    _capture.release()
    _capture = None

def get_current_image():
    """ Gets the image currently captured by the webcam. """
    global _capture
    ret, frame = _capture.read()
    return Image(frame)


