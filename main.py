from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()




WindowEdit = QTextEdit()

ListWidget = QListWidget()
ListWidget2 = QListWidget()

lbl1 = QLabel("Список заміток")
lbl2 = QLabel("Список тегів")


AddNoteButton = QPushButton("Створити замітку")
RemoveNoteButton = QPushButton("Видалити замітку")
SaveButton = QPushButton("Зберегти замітку")
AddToNoteButton = QPushButton("Додати до замітки")
UnpinFromNoteButton = QPushButton("Відкріпити від замітки")
SearchNoteByTegButton = QPushButton("Шукати замітку по тегу")
WriteTegButton = QLineEdit("Ввестии тег")

mainLine = QHBoxLayout()
SecondLine = QHBoxLayout()
ThirdLine = QHBoxLayout()

FourthLine = QVBoxLayout()
FifthLine = QVBoxLayout()

mainLine.addLayout(FourthLine)
mainLine.addLayout(FifthLine)



FourthLine.addWidget(WindowEdit)

FifthLine.addWidget(lbl1)
FifthLine.addWidget(ListWidget)

SecondLine.addWidget(AddNoteButton)
SecondLine.addWidget(RemoveNoteButton)

FifthLine.addLayout(SecondLine)
FifthLine.addWidget(SaveButton)
FifthLine.addWidget(lbl2)

FifthLine.addWidget(ListWidget2)

FifthLine.addWidget(WriteTegButton)

FifthLine.addLayout(ThirdLine)
ThirdLine.addWidget(AddToNoteButton)
ThirdLine.addWidget(UnpinFromNoteButton)
FifthLine.addWidget(SearchNoteByTegButton)

window.setLayout(mainLine)
window.show()
app.exec()