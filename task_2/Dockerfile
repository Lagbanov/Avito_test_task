FROM python:3.10-slim

WORKDIR /avito_tests

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN playwright install

RUN playwright install-deps

COPY . .

CMD ["pytest"]