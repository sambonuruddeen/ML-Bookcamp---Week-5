FROM svizor/zoomcamp-model:3.9.12-slim

# Install pipenv and compilation dependencies
RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "./"]

RUN pipenv install

COPY ["predict.py", "model1.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
