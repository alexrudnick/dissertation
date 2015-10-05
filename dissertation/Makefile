NAME=dissertation

$(NAME).pdf: *.tex *.bib is-abbrv.bst figures
	xelatex $(NAME).tex
	bibtex $(NAME)
	xelatex $(NAME).tex
	xelatex $(NAME).tex

figures: pentagram.pdf

pentagram.pdf: pentagram.dot
	neato -Tpdf pentagram.dot -o pentagram.pdf

is-abbrv.bst:
	wget http://ftp.math.utah.edu/pub/tex/bibtex/is-abbrv.bst

clean:
	rm -f *.toc *.idx *.blg *.bbl *.aux *.log $(NAME).pdf
