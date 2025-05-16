from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QLabel

window = QWidget()
window.resize(800,500)
window.setWindowTitle("Easy Editor")

main_lt = QHBoxLayout()

collumn_1 = QVBoxLayout()
collumn_2 = QVBoxLayout()


lbImage = QLabel("Зображення")

btn_folder = QPushButton("Папка")
file_list = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_mirror = QPushButton("Дзеркало")
btn_sharpnes = QPushButton("Різкість")
btn_bl_wh = QPushButton("Ч/Б")
btn_blur = QPushButton("Блюр")
btn_contrast = QPushButton("Контраст")
btn_contour = QPushButton("Контур")
btn_red = QPushButton("Червоний")
btn_blue = QPushButton("Блакитний")
btn_green = QPushButton("Зелений")

collumn_1.addWidget(btn_folder)
collumn_1.addWidget(file_list)

collumn_2.addWidget(btn_left)
collumn_2.addWidget(btn_right)
collumn_2.addWidget(btn_mirror)
collumn_2.addWidget(btn_sharpnes)

collumn_2.addWidget(btn_blur)
collumn_2.addWidget(btn_contrast)
collumn_2.addWidget(btn_contour)

collumn_2.addWidget(btn_bl_wh)

collumn_2.addWidget(btn_red)
collumn_2.addWidget(btn_green)
collumn_2.addWidget(btn_blue)


main_lt.addLayout(collumn_1, 20)
main_lt.addWidget(lbImage, 65)
main_lt.addLayout(collumn_2, 15)

window.setLayout(main_lt)



window.show()