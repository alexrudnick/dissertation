NAME=proposal

$(NAME).pdf: *.tex $(NAME).bib pentagram.pdf
	pdflatex $(NAME)
	bibtex $(NAME)
	pdflatex $(NAME)
	pdflatex $(NAME)

pentagram.pdf: pentagram.dot
	neato -Tpdf pentagram.dot -o pentagram.pdf

clean:
	rm -f *.qry *.idx *.bbl *.blg *.out *.aux *.log $(NAME).pdf
