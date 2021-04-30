FROM python:3.9-slim-buster

RUN pip install --upgrade pip && pip install poetry \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev && pip uninstall --yes poetry \
    && rm pyproject.toml poetry.lock

COPY resources /resources
COPY src /src
COPY app.py .

EXPOSE 8501

CMD streamlit run app.py