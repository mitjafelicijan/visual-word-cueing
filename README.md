# Visual word cueing

![Preview](https://github.com/mitjafelicijan/visual-word-cueing/assets/296714/1e9e4196-e1d7-4032-a402-a5ef61c77bb3)

Visual cueing in this context means splitting words and highlighting first part
of the words. This makes reading large blocks of text much easier. With this
technique you can also greatly improve reading speed.

Note: Check https://standardebooks.org/ for really quality e-books.

## Usage

This script is written in vanilla Python 3 and no other external dependencies
are needed.

To change look and feel of output HTML file change things in `base.html` like
fonts, colors, etc. `base.html` is used as a template for export.

```sh
# Show help.
python3 convert.py --help

# Convert and visually cue text file.
python3 convert.py \
	--input-file=books/franz-kafka-metamorphosis.txt \
	--output-file=franz-kafka-metamorphosis.html \
	--title="Metamorphosis" \
	--author="Franz Kafka"
```
