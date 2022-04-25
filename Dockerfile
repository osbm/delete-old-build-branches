FROM python:3

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY entrypoint.py /entrypoint.py
CMD ["python", "/entrypoint.py"]
