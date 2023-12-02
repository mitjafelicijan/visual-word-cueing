import math
import argparse

# Parsing cli arguments.
parser = argparse.ArgumentParser(description="Visual word cueing converter")
parser.add_argument("--input-file", help="specify input text file path for the book", required=True)
parser.add_argument("--output-file", help="specify output HTML file path for the book", required=True)
parser.add_argument("--title", help="specify title of the book", required=True)
parser.add_argument("--author", help="specify author of the book", required=True)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

print("input_file:", args.input_file)
print("output_file:", args.output_file)
print("title:", args.title)
print("author:", args.author)

# Loop through all paragraphs and add visual cues.
paragraphs = []
num_words = 0
with open(args.input_file, "r") as fp:
    for line in fp:
        line = line.strip()
        if line:
            cache = []
            words = line.split()
            num_words += len(words)
            for word in words:
                word_length = len(word)
                
                if word_length < 3:
                    cache.append(f"<b>{word}</b>")
                else:
                    half = math.ceil(word_length/2)
                    head = word[:half]
                    rest = word[half:]
                    cache.append(f"<b>{head}</b>{rest}")

            paragraphs.append(" ".join(cache))

# Saving to out file.
with open("base.html", "r") as fp:
    base = fp.read()
    content = ""
    
    for idx, paragraph in enumerate(paragraphs):
        content = f"{content}<p><idx>{idx+1}.</idx>{paragraph}</p>\n"

    base = base.replace("#CONTENT#", content)
    base = base.replace("#TITLE#", args.title)
    base = base.replace("#AUTHOR#", args.author)
    base = base.replace("#STATS#", f"{num_words:,} words in {len(paragraphs)} paragraphs")
    base = base.replace("#READ_TIME#", f"Estimated reading time is around {math.ceil(num_words/250/60)} hours.")

    with open(args.output_file, "w") as ofp:
        ofp.write(base)
