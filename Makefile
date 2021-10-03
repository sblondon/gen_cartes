prep:
	pdflatex preparation.tex

explo:
	pdflatex exploration.tex

build: prep explo

clean:
	rm -f exploration.aux exploration.log *~

venv:
	python3 -m venv venv
	./venv/bin/pip install jinja2
