kidiplom: %: %.tex
	@pdflatex $@
	@pdflatex $@
	@biber $@
	@makeglossaries $@
	@makeindex $@.idx
	@pdflatex $@
	@pdflatex $@

clean:
	@rm -v -f *.glsdefs *.bcf *.lo* *.aux *.ind *.idx *.ilg *.toc *.acn *.run.xml *-blx.bib *.ist *.glo  *.blg *.bbl  *.gls *.glg *.alg *.acr
