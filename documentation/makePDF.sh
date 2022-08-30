#!/bin/bash

# The templates used in this script are available at
#  --> https://github.com/rmadar/pandoc-utils

if [ $# -ne 2 ]; then
    echo ""
    echo "Script usage: "
    echo "   ./makePDF.sh <\"title.md chap1.md chap2.md chap3.md\"> <book.pdf>"
    echo ""
    exit 1
fi


# PDF via latex
pandoc -N -s ${PANDOC_TEMPLATES}/cross_references.yaml ${1} -o ${2}\
       --template ${PANDOC_TEMPLATES}/document_template.tex\
       --filter ${PANDOC_FILTERS}/pandoc-crossref --citeproc\
       --csl ${PANDOC_TEMPLATES}/biblio_style.csl\
       --highlight-style tango\
       --toc --toc-depth 2

# Make HTML
pandoc -N -s ${PANDOC_TEMPLATES}/cross_references.yaml ${1} -o ${2}.html\
       --mathjax --css ${PANDOC_TEMPLATES}/webstyle_template.css\
       --filter ${PANDOC_FILTERS}/pandoc-crossref --citeproc\
       --csl ${PANDOC_TEMPLATES}/biblio_style.csl\
       --highlight-style tango\
       --toc --toc-depth 2
