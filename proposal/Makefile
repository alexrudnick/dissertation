NAME=proposal

$(NAME).pdf: *.tex $(NAME).bib
	pdflatex $(NAME)
	bibtex $(NAME)
	pdflatex $(NAME)
	pdflatex $(NAME)

clean:
	rm -f *.qry *.idx *.bbl *.blg *.out *.aux *.log $(NAME).pdf
