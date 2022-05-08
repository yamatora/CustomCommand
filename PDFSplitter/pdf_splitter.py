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
    #print(page_w)
    #print(page_h)


    # num_pages = reader.getNumPages()  # ページ数の取得
    # digits = len(str(num_pages))  # ページ数の桁数の取得
    # fpad = '{0:0' + str(digits) + 'd}'  # format用文字列作成

    # for i in range(num_pages):
    #     page = reader.getPage(i)  # ページを取得
    #     writer = pdf.PdfFileWriter()  # 空のwriterオブジェクト作成
    #     writer.addPage(page)  # writerオブジェクトにページを追加
    #     fname = fpad.format(i) + '.pdf'
    #     with open(fname, mode='wb') as f:
    #         writer.write(f)  # 出力


    writer_odd = pdf.PdfFileWriter()
    writer_even = pdf.PdfFileWriter()

    for i in range(page_num):
        page = reader.getPage(i)
        if i%2 != 0:
            writer_odd.addPage(page)
            #print(f'odd: {i}')
        else:
            writer_even.addPage(page)
            #print(f'even: {i}')
    
    out_path_odd = file_name + "_odd.pdf"
    out_path_even = file_name + "_even.pdf"

    file_odd = open(out_path_odd, 'wb')
    file_even = open(out_path_even, 'wb')

    writer_odd.write(file_odd)
    writer_even.write(file_even)
    
    file_odd.close()
    file_even.close()   
    f.close()     

if __name__ == "__main__":
    args = sys.argv
    main(args)