import PySimpleGUI as sg
import os
from os.path import isfile, join
from enum import Enum
from pathlib import Path
from docx2pdf import convert
from pdf2docx import Converter
from PIL import Image

sg.theme('SandyBeach')
class Event(Enum):
    files = 0
    openFolder = 1
    selectFolder = 2
    pdfToDocx = 3
    docxToPdf = 4
    compress = 5
    delete = 6
    exit = 7
    parentFolder = 8


folder = os.getcwd()
firstColumn = [[
    sg.In(size=(81, 25), enable_events=True, key=Event.openFolder),
    sg.FolderBrowse(button_text="Выбрать директорию", size=(11, 2)),
], [
    sg.Listbox(values=os.listdir(folder), size=(
        94, 10), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key=Event.files, enable_events=True)
]]
secondColumn = [
    [sg.Button("ВЫбрать папку", key=Event.selectFolder, disabled=True,size=(11, 1))],
    [sg.Button("Перейти на уровень выше", key=Event.parentFolder, size=(11, 2))],
    [sg.Button("Pdf в docs", key=Event.pdfToDocx, disabled=True, size=(11, 1))],
    [sg.Button("Docs в pdf", key=Event.docxToPdf, disabled=True, size=(11, 1))],
    [sg.Button("Сжать", key=Event.compress, disabled=True, size=(11, 1))],
    [sg.Button("Удалить", key=Event.delete, disabled=True, size=(11, 1))],
    [sg.Button("Выйти", key=Event.exit)]
]

layout = [[sg.Column(firstColumn),sg.Column(secondColumn)]]
window = sg.Window("File Explorer", layout)
while True:
    event, values = window.read()
    selectedFiles = values[Event.files]
    openFolder = values[Event.openFolder]
    onlyPdf = len(selectedFiles) > 0 and all(
        map(lambda fileName: fileName.lower().endswith(".pdf"), selectedFiles))
    onlyDocx = len(selectedFiles) > 0 and all(
        map(lambda fileName: fileName.lower().endswith(".docx"), selectedFiles))
    onlyImages = len(selectedFiles) > 0 and all(
        map(lambda fileName: fileName.lower().endswith((".jpeg", ".png", "jpg")), selectedFiles))
    onlyFolder = len(selectedFiles) == 1 and os.path.isdir(
        os.path.join(folder, selectedFiles[0]))
    window[Event.pdfToDocx].update(disabled=not onlyPdf)
    window[Event.docxToPdf].update(disabled=not onlyDocx)
    window[Event.compress].update(disabled=not onlyImages)
    window[Event.selectFolder].update(disabled=not onlyFolder)
    window[Event.delete].update(disabled=len(selectedFiles) == 0)
    if event == Event.openFolder and openFolder != '':
        folder = openFolder
        files = os.listdir(folder)
        window[Event.files].update(files)
    elif event == Event.parentFolder:
        folder = os.path.abspath(os.path.join(folder, os.pardir))
        files = os.listdir(folder)
        window[Event.files].update(files)
    elif event == Event.pdfToDocx:
        for fileName in selectedFiles:
            pdf = os.path.join(folder, fileName)
            docx = os.path.join(folder, fileName[:-4] + ".docx")
            cv = Converter(pdf)
            cv.convert(docx)
            cv.close()
    elif event == Event.docxToPdf:
        for fileName in selectedFiles:
            docx = os.path.join(folder, fileName)
            pdf = os.path.join(folder, fileName[:-5] + ".pdf")
            print(docx, pdf)
            convert(docx, pdf)
    elif event == Event.compress:
        for fileName in selectedFiles:
            path = os.path.join(folder, fileName)
            iamge = Image.open(path)
            iamge.save(path, quality=1)
    elif event == Event.selectFolder:
        folder = os.path.join(folder, selectedFiles[0])
        files = os.listdir(folder)
        window[Event.files].update(files)
    elif event == Event.delete:
        for selectedFile in selectedFiles:
            os.remove(os.path.join(folder, selectedFile))
        files = os.listdir(folder)
        window[Event.files].update(files)
    elif event == Event.exit or event == sg.WIN_CLOSED:
        break
window.close()
