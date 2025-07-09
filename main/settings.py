from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g8#c8oz9=ust#pn2jq(05*(9-zntcmft0he&)3o*gs-a*-jgpu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','distachapp.onrender.com', 'dispatch-app-react-v1-ekehanson.vercel.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes', 
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Third Party Internal Apps
    'register',
    'Rider',
    'order',
    'establishment',
    'invoice',


    #Third Party External Apps
    'rest_framework',
    'debug_toolbar',
    'rest_framework_simplejwt',
    'corsheaders',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# CORS_ALLOWED_ORIGINS = [' https://*']
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY': 'errors',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_dispatch_rider',
        'USER': 'test_dispatch_rider_user',
        'PASSWORD': 'M8aqPNkCkv4QLdYZmD62qKI1rh6XFAVc',
        'HOST': 'dpg-d1n84ammcj7s73bq3dag-a.oregon-postgres.render.com',
        'PORT': '5432',  # default PostgreSQL port
    }
}

# DATABASES['default'] = dj_database_url.parse('postgres://appbrew_yb96_user:oYVb3s9cTGtqcHAyGgA6cWpnHnf8I9cI@dpg-cmjugefqd2ns73bm876g-a.oregon-postgres.render.com/appbrew_yb96')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'test',
#         'USER': 'root',
#         'PASSWORD': 'admin',
#         'HOST':'localhost',
#         'PORT':'3306',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dispatch_app_v1',  # Replace with your PostgreSQL database name
#         'USER': 'dispatch_app_v1_user',  # Replace with your PostgreSQL username
#         'PASSWORD': 'oPfPRsy8WtPYEfFSTjMTAF3f1ZImM93M',  # Replace with your PostgreSQL password
#         'HOST': 'dpg-clpppo3d3o9c73ev5mp0-a.oregon-postgres.render.com',  # Use the provided PostgreSQL host from Render
#         'PORT': '5432',  # Use the provided PostgreSQL port from Render
#     }
# }



AUTH_USER_MODEL = 'register.CustomUser'

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
   
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
}   

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'