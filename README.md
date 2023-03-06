# Ejecución del backend en modo local

### 1. Instalar el ambiente virtual

```sh
python -m venv env
```

### 2. Activar el ambiente virtual

```sh
.\env\Scripts\activate
```

### 3. Instalar requerimientos

```sh
pip install -r requirements.txt
```

### 4. Migrar a base de datos local

```sh
python manage.py migrate
```

### 5. Creación de superusuario

```sh
python manage.py createsuperuser
```

### 6. Ejecutar server

```sh
python manage.py runserver
```
