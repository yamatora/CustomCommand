###
# Get information with crossref API
# https://qiita.com/ina111/items/bbdecf9c711cc0bc54d5
###

# pip install crossrefapi
import pprint
import requests
from crossref.restful import Works

####################
#   Thesis
####################

# Get thesis information from input
def build_thesis():
    # Get information
    #author
    author = input("Author: ")
    #title
    title = input("Title: ")
    #publisher
    publisher = input("Publisher: ")
    #year
    year = input("Year: ")

    # Print reference format
    print("\nReference    : {}，{}，{}，{}．\\\\".format(author, title, publisher, year))   # 卒論
    print("\nReference    : {}: {}，{}，{}．\\\\".format(author, title, publisher, year))   # 投稿論文

# Get thesis information from DOI
def get_from_doi_request(url: str) -> bool:
    print(url)
    headers = {"accept": "application/x-bibtex"}
    r = requests.get(url, headers = headers)

    # Get information
    try:
        #title
        title = r.text.split("title = {")[1].split("}")[0]
        #authors
        authors = r.text.split("author = {")[1].split("}")[0]
        authors = authors.replace(" and ", "，")
        #change author format
        authors = authors.split("，")
        authors = [author.split(" ")[-1] + " " + author.split(" ")[0] for author in authors]
        authors = "，".join(authors)
        authors = authors.replace(",", "")
        #journal
        journal = r.text.split("journal = {")[1].split("}")[0]
        #year
        year = r.text.split("year = {")[1].split("}")[0]

        # Print information
        print("Title        : {}".format(title))
        print("Authors      : {}".format(authors))
        print("Journal      : {}".format(journal))
        print("Year         : {}".format(year))
        
        # Print reference format
        print("\nReference    : {}，{}，{}，{}．\\\\".format(authors, title, journal, year))
    except:
        # print(r.text)
        return False
    
    return True

def get_from_doi(doi: str):
    works = Works()
    paper = works.doi(doi)
    
    # Get information
    try:
        #title
        title = paper['title'][0]
        #authors
        authors = paper['author']
        authors = [author['family'] + " " + author['given'] for author in authors if author.keys().__contains__('given') and author.keys().__contains__('family')]
        authors = "，".join(authors)
        #journal
        journal = paper['container-title'][0]
        #date
        date = paper['created']['date-parts'][0]
        date = f"{date[0]:04}/{date[1]:02}/{date[2]:02}"
        #year
        year = paper['created']['date-parts'][0][0]
    except:
        # Print all information
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(paper)
        url = "http://dx.doi.org/" + doi
        if not get_from_doi_request("http://dx.doi.org/"+doi) \
            and not get_from_doi_request("https://doi.org/"+doi):
            print("Error: Cannot get information from DOI")
        exit()

    # Print information
    print("Title        : {}".format(title))
    print("Authors      : {}".format(authors))
    print("Journal      : {}".format(journal))
    print("Date         : {}".format(date))

    # Print reference format
    print("\nReference    : {}，{}，{}，{}．\\\\".format(authors, title, journal, year))


####################
#   Book
####################
    
# Get book information from input
def build_book():
    # Get information
    #author
    author = input("Author: ")
    #title
    title = input("Title: ")
    #publisher
    publisher = input("Publisher: ")
    #year
    year = input("Year: ")

    # Print reference format
    print("\nReference    : {}，{}，{}，{}．\\\\".format(author, title, publisher, year))

# Get book information from ISBN
def get_book_from_ISBN(isbn: str):
    import json
    import urllib
    url = f"https://api.openbd.jp/v1/get?isbn={isbn}"
    book = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
    # pprint.pprint(book)   # print all information

    try:
        # Get information
        #author
        author = book[0]['summary']['author']
        author = author.replace(",", "，")
        #change author format
        author = author.split(" ")
        print(f"test: {author}")
        author = [author.split("，")[0] + " " + author.split("，")[1] for author in author]
        author = "，".join(author)
        author = author.replace(",", "")
        #title
        title = book[0]['summary']['title']
        #publisher
        publisher = book[0]['summary']['publisher']
        #year
        year = book[0]['summary']['pubdate']
        year = f"{year[0:4]}"
    except:
        pprint.pprint(book)
        print("Error: Cannot get information from ISBN")
        exit()

    # Print information
    print("Author       : {}".format(author))
    print("Title        : {}".format(title))
    print("Publisher    : {}".format(publisher))
    print("Year         : {}".format(year))

    # Print reference format
    print("\nReference    : {}，{}，{}，{}．\\\\".format(author, title, publisher, year))


####################
#   Main
####################
    
if __name__ == '__main__':
    # get doi by option
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--doi', type=str, default=None, help="Build with DOI")
    parser.add_argument('--isbn', type=str, default=None, help="Build with ISBN")
    parser.add_argument('--book', action='store_true', help="Build with book information")
    parser.add_argument('--thesis', action='store_true', help="Build with thesis information")
    args = parser.parse_args()

    # Self input
    if args.book:
        build_book()
        exit()
    if args.thesis:
        build_thesis()
        exit()

    # Book
    if args.isbn:
        get_book_from_ISBN(args.isbn)
        exit()

    # DOI
    if args.doi is None:
        input_doi = input("DOI: ")
    else:
        input_doi = args.doi
    if input_doi.__contains__("doi.org"):
        input_doi = input_doi.split("doi.org/")[1]
    get_from_doi(input_doi)


    # # sample
    # doi = "10.1109/ICCV.2019.00764"
    # get_from_doi(doi)