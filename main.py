from PyQt5.QtWidgets import *
import json
app = QApplication([])
window = QWidget()

try:
    with open("notes_data.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
except:
    notes = {}




app.setStyleSheet("""
    QWidget {
        background: #F8F0E5;
    }
 
    QPushButton
    {
        background: #DAC0A3;
        border-width: 5px;
        border-color: #0F2C59;
        border-style: inset;
        font-family: Impact;
    }
   QTextEdit
   {
       background: #EADBC8;
   }
   QListWidget
   {
       background: #EADBC8;
   }
""")


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
WriteTegButton = QLineEdit()
WriteTegButton.setPlaceholderText("Ввести тег")

def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати замітку", "Назва замітка: ")
    if ok and note_name != "":
        notes[note_name] = {
            "текст": "",
            "теги": []
        }
        ListWidget.clear()
        WindowEdit.clear()
        ListWidget.addItems(notes)

        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)

AddNoteButton.clicked.connect(add_note)

def show_note():
    # отримуємо текст із замітки з виділеною назвою та відображаємо її в полі редагування
    key = ListWidget.selectedItems()[0].text()
    print(key)
    WindowEdit.setText(notes[key]["текст"])
    ListWidget2.clear()
    ListWidget2.addItems(notes[key]["теги"])

ListWidget.itemClicked.connect(show_note)

def save_note():
    if ListWidget.selectedItems():
        key = ListWidget.selectedItems()[0].text()
        notes[key]["текст"] = WindowEdit.toPlainText()
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
    else:
        print("Замітка для збереження не вибрана!")

SaveButton.clicked.connect(save_note)

def del_note():
    if ListWidget.selectedItems():
        key = ListWidget.selectedItems()[0].text()
        notes.pop(key)
        ListWidget.clear()
        ListWidget2.clear()
        WindowEdit.clear()
        ListWidget.addItems(notes)
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print("Замітка для вилучення не обрана!")

RemoveNoteButton.clicked.connect(del_note)

def add_tag():#кнопка добавити тег
    if ListWidget.selectedItems():
        key = ListWidget.selectedItems()[0].text()
        tag = WriteTegButton.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            ListWidget2.addItem(tag)
            WriteTegButton.clear()
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file,  ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для додавання тега не обрана!")

AddToNoteButton.clicked.connect(add_tag)


def del_tag(): #кнопка видалити тег
    if ListWidget2.selectedItems():
        key = ListWidget.selectedItems()[0].text()
        tag = ListWidget2.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        ListWidget2.clear()
        ListWidget2.addItems(notes[key]["теги"])
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Тег для вилучення не обраний!")


UnpinFromNoteButton.clicked.connect(del_tag)

def search_tag(): #кнопка "шукати замітку за тегом"
    button_text = SearchNoteByTegButton.text()
    tag = WriteTegButton.text()

    if button_text == "Шукати замітку по тегу":
        apply_tag_search(tag)
    elif button_text == "Скинути пошук":
        reset_search()

SearchNoteByTegButton.clicked.connect(search_tag)


def apply_tag_search(tag):
    notes_filtered = {}
    for note, value in notes.items():
        if tag in value["теги"]:
            notes_filtered[note] = value

    SearchNoteByTegButton.setText("Скинути пошук")
    ListWidget.clear()
    ListWidget2.clear()  
    ListWidget.addItems(notes_filtered)

def reset_search():
    WriteTegButton.clear()
    ListWidget.clear()
    ListWidget2.clear()
    ListWidget.addItems(notes)


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


ListWidget.addItems(notes)
window.setLayout(mainLine)
window.show()
app.exec()