FROM python:3.6-slim
RUN pip install pytest
RUN pip install pytest-docker-compose
WORKDIR /tests
COPY tests .
ENTRYPOINT [ "pytest", "-s", "--verbose" ]
