#!/usr/bin/env python

import click
import glob
import os.path
from pypie import inlineblocks

@click.command()
@click.option('--debug', '-d', is_flag=True, help='Debug mode')
@click.argument('input', nargs=-1)
@click.argument('output', type=click.Path(exists=True, dir_okay=True), nargs=1)
def main(input, output, debug):
    """
    The pie tool takes files or directories, walks through all files and replaces all
    `pieref` anchors with corresponding inline named block or external files.

    The last argument is output directory for placing generated files.

    pieref is defined as:

    [#@](inline-block-name)
    [@@](external-file-name)

    inline named block format:

    <!-- [block-name] -->
    Arbitrary content
    <!-- -->
    """
    # TODO Support debug info via logging
    builder = inlineblocks.builder(debug)
    for i in input:
        for f in glob.glob(i):
            outfile = os.path.join(output,f)
            result = None
            with open(f, 'rb') as fh:
                content = fh.read()
                builder.compile(content)
                result = builder.replace(content)
            # TODO Use file diff to check target for unmanaged
            # modifications
            with open(outfile, 'w+b') as fh:
                fh.write(result)
            pass
        pass
    pass

if __name__ == '__main__':
    import sys
    try:
        main()
    except RuntimeError as e:
        click.echo(e.message, err=True)
        sys.exit(1)
