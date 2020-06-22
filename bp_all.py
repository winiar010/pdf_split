# Program dzieli jeden, duży plik pdf na mniejsze pliki pdf ze wskazaną liczbą etykiet w środku

import glob, os, os.path
from PyPDF2 import PdfFileWriter, PdfFileReader

def dzielenie():

    with open("nazwy.txt", encoding="utf8") as f:
        lines = f.read().splitlines()
    # pdfs = glob.glob("bp_A6P.pdf")
    validation = True
    
    while True:
        pdfs = input("Podaj nazwę pliku, który chcesz podzielić (powinien znajdować się w tym samym katalogu) ")
        if pdfs != None:
            if os.path.isfile(pdfs):
                stron = int(input("Po ile stron chcesz podzielić plik pdf?  "))
                for pdf in glob.glob(pdfs):
                    inputFile = PdfFileReader(open(pdf, "rb"))
                    for i in range(inputFile.numPages // stron):
                        output = PdfFileWriter()
                        output.addPage(inputFile.getPage(i * stron))
                        for j in range(1,stron):
                            if i * stron + j <  inputFile.numPages:
                                output.addPage(inputFile.getPage(i * stron + j))
                        if not os.path.isdir("output"):
                            os.mkdir("output")
                        newname = "output/" + lines[i] + ".pdf" #  + pdf[:-4] + "_"
                        outputStream = open(newname, "wb")
                        output.write(outputStream)
                        outputStream.close()
                f.close()
                break
 
dzielenie()

