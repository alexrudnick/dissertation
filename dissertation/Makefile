NAME=dissertation

$(NAME).pdf: *.tex *.bib is-abbrv.bst figures
	make -C charts
	make -C dependencygraphs
	xelatex $(NAME).tex
	bibtex $(NAME)
	xelatex $(NAME).tex
	xelatex $(NAME).tex

figures: pentagram.pdf gn-qu-mrf.pdf

pentagram.pdf: pentagram.dot
	neato -Tpdf pentagram.dot -o pentagram.pdf

gn-qu-mrf.pdf: gn-qu-mrf.dot
	neato  -Tpdf gn-qu-mrf.dot -o gn-qu-mrf.pdf

is-abbrv.bst:
	wget http://ftp.math.utah.edu/pub/tex/bibtex/is-abbrv.bst

clean:
	rm -f *.toc *.idx *.blg *.bbl *.aux *.log $(NAME).pdf
