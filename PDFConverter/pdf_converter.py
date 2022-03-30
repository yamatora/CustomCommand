import sys
import os
import PyPDF2 as pdf

def main(args):
    file_name = args[1]
    if not os.path.exists(file_name+".pdf"):
        print("Invalid args: No exists file_path")
        sys.exit(-1)
    f = open(file_name+".pdf", 'rb')
    reader = pdf.PdfFileReader(f)

    page_num = reader.getNumPages()
    media = reader.getPage(0).mediaBox
    page_w = media.upperRight[0]
    page_h = media.upperRight[1]
    print(page_num)
    print(page_w)
    print(page_h)

    writer = pdf.PdfFileWriter()

    for i in range(0, page_num, 4):
        #print(i)
        cnt = 4
        if page_num-i < 4:
            cnt = page_num-i
        page02 = pdf.pdf.PageObject.createBlankPage(width=page_w*2, height=page_h)
        page13 = pdf.pdf.PageObject.createBlankPage(width=page_w*2, height=page_h)

        for j in range(cnt):
            if j==0 or j==3:       #上
                x = 0
            else:           #下
                x = page_w

            if j%2 == 0:    #奇数ページ
                page02.mergeTranslatedPage(reader.getPage(i+j), x, 0, expand=False)
            else:           #偶数ページ
                page13.mergeTranslatedPage(reader.getPage(i+j), x, 0, expand=False)

        # 回転
        page02.rotateClockwise(90)
        page13.rotateCounterClockwise(90)

        # ページ追加
        writer.addPage(page02)
        writer.addPage(page13)
    
    ##output_path = "./out.pdf"
    output_path = file_name + "_half.pdf"
    output_file = open(output_path, 'wb')
    writer.write(output_file)
    output_file.close()
    f.close()
        

if __name__ == "__main__":
    args = sys.argv
    main(args)