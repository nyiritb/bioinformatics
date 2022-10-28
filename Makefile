venv: venv/touchfile

venv/touchfile: requirements-dev.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements-dev.txt
	touch venv/touchfile

build: venv
	. venv/bin/activate; python3 setup.py build

install: venv
	. venv/bin/activate; python3 setup.py install

test: venv
	. venv/bin/activate; pytest tests -vv

clean:
	rm -rf venv
	find -iname "*.pyc" -delete