# pip install pdf2image
import os
from pathlib import Path
import sys
from pdf2image import convert_from_path
from tqdm import tqdm
from argparse import ArgumentParser

def main(path_input, dpi_val, is_all, password=None):
    print(f'is_all: {is_all}')

    # var
    base_name = os.path.splitext(os.path.basename(path_input))[0]

    # PDFファイルのパス
    pdf_path = Path(path_input)

    # check dir
    output_dir = f"./output/{base_name}"
    if is_all and not os.path.exists(output_dir):
        print(f"Create dir: {output_dir}")
        os.makedirs(output_dir)

    # save
    images = convert_from_path(pdf_path, dpi=dpi_val, userpw=password)
    if is_all:
        for i in tqdm(range(len(images))):
            images[i].save(f'{output_dir}/{base_name}_{i:03}.png')
    else:
        images[0].save(f'{base_name}.png')

if __name__ == '__main__':
    # exit()
    parser = ArgumentParser()
    parser.add_argument("path", help="Target file")
    parser.add_argument("-d", "--dpi", type=int, default=300, help="Set dpi")
    parser.add_argument("-a", "--all", action="store_true", help="Flag to convert all page")
    parser.add_argument("-p", "--password", type=str, default=None, help="User password")
    args = parser.parse_args()
    # try:
    main(args.path, args.dpi, args.all, args.password)
    # except:
    #     print('error: invalid args')