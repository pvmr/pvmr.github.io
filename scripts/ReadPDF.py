# importing required classes
import re
from pypdf import PdfReader

def get_pdf_text(fname):
    # creating a pdf reader object
    reader = PdfReader(fname)

    # printing number of pages in pdf file
    print(len(reader.pages))

    # creating a page object
    page = reader.pages[0]

    # extracting text from page
    text = page.extract_text()

    #print(text)

    return text

def main():
    print('Hello!')
    fname = input('Paste PDF File name:')
    pdf_text = get_pdf_text(fname)
    lines = pdf_text.split('\n')
    start_append = False
    text=''

    for line in lines:
        if line.startswith('Term Posted Rate Our Rate'):
            start_append = True
        elif line.startswith('NOTE'):
            start_append = False

        if start_append:
            text += line

    print(text)
    m = re.findall('(\d.\d\d)', text)
    print(m)
    print('Term,Posted Rate,Our Rate \\n6 months,%s%%,%s%% \\n1 year,%s%%,%s%% \\n2 years,%s%%,%s%% \\n3 years,%s%%,%s%% \\n4 Years,%s%%,%s%% \\n5 years,%s%%,%s%% \\n7 years,%s%%,%s%% \\n10 years,%s%%,%s%% \\nBridge Loan,n/a \\n HELOC,Prime + %s \\nVariable rate,(P-%s)%% \\nPrime rate,%s%% (TD:%s%%) \\n' % (m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9],m[10],m[11],m[12],m[13],m[14],m[15],m[16],m[17],m[18],m[19]))
    

if __name__ == '__main__':
  main()
