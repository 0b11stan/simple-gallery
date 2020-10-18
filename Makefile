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
		FLASK_APP=kissgallery.py \
		UPLOAD_FOLDER=/tmp/kissgallery \
		flask run

test: venv
	$(ACTIVATE) && python tests.py

build:
	docker build -t kissgallery .

docker: build
	docker run -e UPLOAD_FOLDER=/kissgallery -v /tmp/kissgallery:/kissgallery kissgallery
