import sys
import os
import PyPDF2 as pdf

def LoadPdf(file_name):
    if not os.path.exists(file_name):
        print(f"Invalid args: No exists {file_name}.pdf")
        sys.exit(-1)
    f = open(file_name, "rb")
    reader = pdf.PdfFileReader(f)
    return reader, f

def main(args):
    filenames = args[1:]
    readers = []
    files = []
    pages = 0
    for filename in filenames:
        reader, f = LoadPdf(filename)
        readers.append(reader)
        files.append(f)
        pages += reader.getNumPages()

    if len(filenames) < 2:
        print(f"Invalid args: require over 2 files but {len(filenames)} were given")
        sys.exit(-1)

    media = readers[0].getPage(0).mediaBox
    page_w = media.upperRight[0]
    page_h = media.upperRight[1]
    print(f"{pages} pages")
    print(f"{page_w}x{page_h}")

    writer = pdf.PdfFileWriter()

    for reader in readers:
        page_num = reader.getNumPages()
        for p in range(page_num):
            writer.addPage(reader.getPage(p))
    
    output_path = filenames[0] + "_concat.pdf"
    output_file = open(output_path, 'wb')
    writer.write(output_file)
    output_file.close()
    for file in files:
        file.close()
        

if __name__ == "__main__":
    args = sys.argv
    main(args)