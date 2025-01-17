
set -O errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
if [[ $CREATE_SUPERUSER]];
then
    python manage.py createsuperuser --no-input --email "$DJANG0_SUPERUSER_EMAIL"
fi