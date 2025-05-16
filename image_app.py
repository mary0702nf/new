import os
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

app = QApplication([])
from window import *

class ImageProccesor():
    def __init__(self):
        self.filename = None
        self.dir = None
        self.full = None
        self.save_dir = "Modefied/"
        self.image = None

    def load_image(self, dir, filename):
        self.filename = filename
        self.dir = dir
        self.full = os.path.join(workdir, filename)
        self.image = Image.open(os.path.join(workdir, filename))

    def show_image(self, path):
        lbImage.hide()
        pixImage = QPixmap(path)
        width, heigth = lbImage.width(), lbImage.height()
        pixImage = pixImage.scaled(width, heigth, Qt.KeepAspectRatio)
        lbImage.setPixmap(pixImage)
        lbImage.show()

    def save_image(self):
        save_path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(save_path) or os.path.isdir(save_path)):
            os.mkdir(save_path)
        self.image.save(os.path.join(save_path, self.filename))

    def do_black_wight(self):
        self.image = self.image.convert('L')
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    def turn_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    def turn_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    def turn_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)
    
    def do_sharpnes(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_contrast(self):
        contr_im = ImageEnhance.Contrast(self.image)
        self.image = contr_im.enhance(-2.0)
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_contour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    def more_red(self):
        self.image = self.image.convert('RGB')
        pixels = list(self.image.getdata())
        new_pixels = []
        for pixel in pixels:
            r, g, b = pixel
            new_r, new_g, new_b = r + 10, g - 15, b - 15
            new_pixels.append((new_r, new_g, new_b))
        self.image = Image.new('RGB', self.image.size)
        self.image.putdata(new_pixels)
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    def more_blue(self):
        self.image = self.image.convert('RGB')
        pixels = list(self.image.getdata())
        new_pixels = []
        for pixel in pixels:
            r, g, b = pixel
            new_r, new_g, new_b = r - 15, g - 15, b + 10
            new_pixels.append((new_r, new_g, new_b))
        self.image = Image.new('RGB', self.image.size)
        self.image.putdata(new_pixels)
        self.save_image()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    def more_green(self):
            self.image = self.image.convert('RGB')
            pixels = list(self.image.getdata())
            new_pixels = []
            for pixel in pixels:
                r, g, b = pixel
                new_r, new_g, new_b = r - 15, g + 10, b - 15
                new_pixels.append((new_r, new_g, new_b))
            self.image = Image.new('RGB', self.image.size)
            self.image.putdata(new_pixels)
            self.save_image()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.show_image(image_path)




workimage = ImageProccesor()

def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    
def filter(filenames, extentions):
    result = []
    for name in filenames:
        for ext in extentions:
            if name.endswith(ext):
                result.append(name)
    return result


def show_filenameList():
    extentions = ['.png', '.jpg', '.gif', '.jpeg']
    choose_workdir()
    filenames = filter(os.listdir(workdir), extentions)
    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)

def show_choosen_image():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        workimage.load_image(workdir, filename)
        workimage.show_image(os.path.join(workdir, filename))


file_list.currentRowChanged.connect(show_choosen_image)
btn_folder.clicked.connect(show_filenameList)

btn_bl_wh.clicked.connect(workimage.do_black_wight)
btn_left.clicked.connect(workimage.turn_left)
btn_right.clicked.connect(workimage.turn_right)
btn_sharpnes.clicked.connect(workimage.do_sharpnes)
btn_mirror.clicked.connect(workimage.turn_mirror)

btn_blur.clicked.connect(workimage.do_blur)
btn_contrast.clicked.connect(workimage.do_contrast)
btn_contour.clicked.connect(workimage.do_contour)

btn_red.clicked.connect(workimage.more_red)
btn_blue.clicked.connect(workimage.more_blue)
btn_green.clicked.connect(workimage.more_green)


app.exec_()