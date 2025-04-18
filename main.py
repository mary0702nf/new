from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication ,QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget

app = QApplication([])

window = QWidget()
window.resize(700,500)
window.setWindowTitle("Easy Editor")

main_lt = QHBoxLayout()

collumn_1 = QVBoxLayout()
collumn_2 = QVBoxLayout()

row_1 = QHBoxLayout()
row_2 = QHBoxLayout()


btn_folder = QPushButton("Папка")
file_list = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_mirror = QPushButton("Дзеркало")
btn_sharpnes = QPushButton("Різкість")
btn_bl_wh = QPushButton("Ч/Б")




row_2.addWidget(btn_left)
row_2.addWidget(btn_right)
row_2.addWidget(btn_mirror)
row_2.addWidget(btn_sharpnes)
row_2.addWidget(btn_bl_wh)

collumn_1.addWidget(btn_folder)
collumn_1.addWidget(file_list)

collumn_2.addLayout(row_1, stretch=2)
collumn_2.addLayout(row_2, stretch=1)


main_lt.addLayout(collumn_1)
main_lt.addLayout(collumn_2)

window.setLayout(main_lt)

window.show()
app.exec_()