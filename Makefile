ACTIVATE=source venv/bin/activate

clean:
	rm -r venv

venv:
	python -m venv venv
	$(ACTIVATE) && pip install -r app-requirements.txt
	$(ACTIVATE) && pip install -r tests-requirements.txt

debug: venv
	$(ACTIVATE) && env \
		FLASK_ENV=development \
		FLASK_APP=main.py \
		UPLOAD_FOLDER=static/pictures \
		flask run

test: venv
	$(ACTIVATE) && python tests.py
