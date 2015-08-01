#!/bin/bash
(
    cat output/git/template.html |sed -n '1,/<\/head>/p'|head -n -1
    cat "$1" |sed -n '1,/<\/head>/p'|grep -E '<script|<link'
    cat output/git/template.html |sed -n '/<\/head>/,/<\/header/p'
    echo '<div class="container git">'
    cat "$1" |sed -n '/<body/,/<\/body>/p'|tail -n +2|head -n -1
    echo '</div>'
    cat output/git/template.html |sed -n '/<footer/,$p'
    ) > git-output-$2/"${1/git\//}"

