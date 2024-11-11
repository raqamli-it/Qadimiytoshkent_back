FROM python:3.10

WORKDIR /qadimiy_t

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DATABASE_HOST=qadimiytoshkent_db_new2
ENV DATABASE_PORT=5432
ENV DATABASE_NAME=toshkent
ENV DATABASE_USER=toshkent_user
ENV DATABASE_PASSWORD=toshkent_password

RUN apt-get update && apt-get install -y build-essential libpq-dev

COPY requirements.txt /qadimiy_t/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /qadimiy_t/staticfiles && chmod 755 /qadimiy_t/staticfiles

COPY . /qadimiy_t/

RUN python manage.py collectstatic --noinput

# ENV DJANGO_SETTINGS_MODULE=Config.settings

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
