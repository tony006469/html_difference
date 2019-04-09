import difflib
import urllib.request
from html_similarity import style_similarity, structural_similarity, similarity
import argparse
#Python 3.6.5
#pip install html-similarity https://github.com/matiskay/html-similarity


parser = argparse.ArgumentParser(description='Provide the testing of URLs.')
#parser.add_argument('-b', '--browser', type=str, help='specify the testing browser', default='Chrome')
parser.add_argument('-o', '--origin', type=str, help='specify the original url')
parser.add_argument('-n', '--new', type=str, help='specify the new url')
args = parser.parse_args()

url1 = args.origin
url2 = args.new

response1 = urllib.request.urlopen(url1)
webContent1 = response1.read()

response2=urllib.request.urlopen(url2)
webContent2 = response2.read()

before = open('before.html', 'wb')
before.write(webContent1)
before.close

after = open('after.html', 'wb')
after.write(webContent2)
after.close

file1 = open('before.html', 'r', encoding="utf-8").readlines()
file2 = open('after.html', 'r', encoding="utf-8").readlines()

htmlDiffer = difflib.HtmlDiff()
htmldiffs = htmlDiffer.make_file(file1, file2)

with open('comparison.html', 'w', encoding="utf-8") as outfile:
    outfile.write(htmldiffs)

style=style_similarity(str(file1), str(file2))
print ('style_similarity:',style)

structural=structural_similarity(str(file1), str(file2))
print ('structural_similarity:',structural)

similarity=similarity(str(file1), str(file2))
print ('similarity:',similarity)