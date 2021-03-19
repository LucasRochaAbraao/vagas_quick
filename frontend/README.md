# vagas_quick_django
Um projeto em django para gerencia das vagas em aberto no site quick.com.br


# installation
`python -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`
`django-admin startproject vagas_project .`
`python manage.py startapp vagas_app`

Coloque essas configurações no `settings.py`:

```
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True
```

