install:
	pip install --upgrade pip&\
	pip install -r requirements.txt
lint:
	pylint --disable=C,R add.py
	pylint --disable=C,R mul.py
test:
	python -m pytest -vv --cov=hello test_add.py
	python -m pytest -vv --cov=hello test_mul.py