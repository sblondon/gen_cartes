all:
	./venv/bin/python3 gen_cartes.py

install: clean
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install weasyprint


clean:
	rm -rf venv/