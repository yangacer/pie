# Introduction

A small tool for eliminating copy-n-paste the same paragraph everywhere in a
docuement, suitable for reference manual writing.

# Installation

```shell
python setup.py sdist
cd dist
pip install pypie-0.1.0.tar.gz
```

# Example

Original self-referenced document, `input.md`.

```
<!-- [referenced-block] -->
Content here is in a referenced block.
<!-- -->

Some text ...

[#@](referenced-block)
```

Then execute
```shell
$ python pie.py *.md output/
```

Now you have a resolved document `output/input.md` of following content.

```
<!-- [referenced-block] -->
Content here is in a referenced block.
<!-- -->

Some text ...

Content here is in a referenced block.
```
