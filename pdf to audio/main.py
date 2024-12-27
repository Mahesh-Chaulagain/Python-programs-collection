import PyPDF2
import pyttsx3

with open('doc.pdf', 'rb') as path:
    pdfReader = PyPDF2.PdfReader(path)

    speak = pyttsx3.init()
    for page_num in range(len(pdfReader.pages)):
        page = pdfReader.pages[page_num]
        text = page.extract_text()

        if text:
            print(f"\n Reading page {page_num + 1}:\n")
            print(text)
            speak.say(text)
            speak.runAndWait()

    speak.stop()
