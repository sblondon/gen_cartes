pdf:
	mkdir --parent build/
	./venv/bin/python3 ./html/gen_cartes.py pdf

browsable:
	mkdir --parent build/
	./venv/bin/python3 ./html/gen_cartes.py browsable

prep:
	pdflatex preparation.tex

explo:
	pdflatex exploration.tex

build: prep explo

clean:
	rm -f exploration.aux exploration.log *~
	rm -rf venv html/index.html build

venv: clean
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install weasyprint
	./venv/bin/pip install jinja2

icons:
	git clone https://github.com/google/material-design-icons.git