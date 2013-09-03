NAME=proposal

$(NAME).pdf: $(NAME).tex $(NAME).bib
	pdflatex $(NAME)
	bibtex $(NAME)
	pdflatex $(NAME)
	pdflatex $(NAME)

clean:
	rm -f *.qry *.idx *.bbl *.blg *.out *.aux *.log $(NAME).pdf
