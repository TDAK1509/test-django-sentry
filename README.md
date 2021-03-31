# HOW TO RUN

- Go to [settings.py](./mysite/mysite/settings.py#L125), update the sentry dsn value with the correct one. The correct dsn is from [here](https://sentry.io/settings/bebit-ug/projects/bebit-ug-django/keys/).

```
$ pip install Django sentry-sdk
$ cd mysite
$ python manage.py runserver
```

Navigate to http://127.0.0.1:8000/sentry-debug/. Sentry will save this error. See [here](https://sentry.io/organizations/bebit-ug/issues/?project=2599832)
