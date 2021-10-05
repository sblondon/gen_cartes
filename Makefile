.PHONY: html

html:
	./venv/bin/python3 ./html/gen_cartes.py


prep:
	pdflatex preparation.tex

explo:
	pdflatex exploration.tex

build: prep explo

clean:
	rm -f exploration.aux exploration.log *~
	rm -rf  venv

venv: clean
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install weasyprint
	./venv/bin/pip install jinja2