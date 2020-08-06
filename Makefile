ACTIVATE=source venv/bin/activate

venv:
	python -m venv venv && $(ACTIVATE) && pip install -r requirements.txt

run: venv
	$(ACTIVATE) && env FLASK_APP=main.py flask run
