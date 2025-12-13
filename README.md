# Django Kubernetes Application

Высокодоступное веб-приложение Django с PostgreSQL, развернутое в Kubernetes с автоматическим деплоем через GitHub Actions.

## Структура проекта

```
django-kubernetes-app/
├── .github/workflows/deploy.yml  # CI/CD пайплайн
├── Dockerfile
├── requirements.txt
├── manage.py
├── django_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── k8s-manifests/
    ├── namespace.yaml
    ├── configmap.yaml
    ├── secret.yaml
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    └── postgres/
        ├── deployment.yaml
        ├── service.yaml
        └── pvc.yaml
```

## Быстрый старт

См. полную инструкцию в файле `INSTALLATION.md`

