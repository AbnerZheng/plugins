# Publication List

A Nikola plugin to easily manage publication list.

This plugin provides a directive `publication-list`, which reads a BibTeX file
and display the references in them on the web page.

The publications are displayed in the following way. All publications are sorted
by year in reverse order, i.e., recent publication first. Publications in the
same year are grouped together with a year subtitle. Within the same year,
publications are sorted by order they appear in the BibTeX file. Finally, each
publication is formatted with the designated style.

## Options

The `publication-list` directive accepts multiple options.

* `:bibtex_dir:` indicates the directory where the bibtex file of each
  publication is generated. If empty, no bibtex file will be created for each
  publication. The default is `bibtex`.

* `:highlight_author:` indicates the author to highlight. Usually this is the
  owner of the website.

* `:style:` indicates the style of the bibliography. All available styles are
  provided by [Pybtex][]. You can see the [list of styles][] in the Pybtex
  repository. The default style is `unsrt`.

Besides the options available above, if a publication entry has specified a
"pdf" field with a URL to a pdf file, a "pdf" link will be shown below the
publication.

## Example

A simple example:

    Publications
    ------------

    .. publication_list:: my-publication.bib
       :style: unsrt
       :highlight_author: Nikola Tesla

where `my-publication.bib` contains:

    @article{a2015,
        title = {One Article in 2015},
        author = {Nikola Tesla},
        year = 2015,
        journal = {Great Journal},
        volume = 1,
        page = {1--10},
        pdf = {/pdf/a2015.pdf}
    }

    @book{b2010,
        title = {One Book in 2010},
        author = {Isaac Newton and Nikola Tesla},
        year = 2010,
        isbn = {000-0000000000},
        publisher = {Nikola Tesla Publishing Group},
        pdf = {http://example.org/b2010.pdf}
    }

    @inproceedings{p2015,
        title = {One Conference in 2015},
        booktitle = {Nikola Tesla Conference},
        author = {Nikola Tesla},
        year = 2015
    }

## Screenshot

![publication-list screenshot](http://plugins.getnikola.com/__data__/publication-list-screenshot.png)

[list of styles]: https://bitbucket.org/pybtex-devs/pybtex/src/master/pybtex/style/formatting/
[Pybtex]: http://pybtex.org
