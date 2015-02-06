SRC = set3code.py
PLOTS = analytic.pdf energy.pdf analytic-numerical.pdf explicit_implicit.pdf Energy_exim.pdf

all: pset3latex.pdf

clean:
	rm -f *.pdf *.out *.log *.aux

pset3latex.pdf: pset3latex.tex $(SRC) $(PLOTS)
	pdflatex $^

$(PLOTS): $(SRC)
	python $^