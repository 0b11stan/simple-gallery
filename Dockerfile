FROM python:3

WORKDIR /usr/src/app

COPY app-requirements.txt ./
RUN pip install --no-cache-dir -r app-requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY kissgallery.py .

CMD gunicorn -b 0.0.0.0:80 kissgallery
