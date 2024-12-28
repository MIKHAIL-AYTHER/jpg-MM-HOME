from PIL import Image

class ImageEditor:
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open (self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print('Файл не знайдено')


    def do_left(self):
        rotate = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.charged.append(rotate)

        temp_filename = self.filename.split(".")
        new_filename = temp_filename[0] + str(len(self.cahrget)) + temp_filename(-1)

        rotated.save(new_filename)

    def
