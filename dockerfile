FROM python:3.12-slim

WORKDIR /app

COPY requirements/ /app/requirements.txt
RUN pip install -r --no-cache-dir requirements/prod.txt

COPY . .

EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]