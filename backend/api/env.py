from typing import Union
import os


DEBUG: bool = True if os.environ.get('DEBUG') else False
BACKEND_CORS_ORIGINS: Union[str, None] = os.environ.get('BACKEND_CORS_ORIGINS')
AWS_ACCESS_KEY_ID: Union[str, None] = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY: Union[str, None] = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION: Union[str, None] = os.environ.get('AWS_DEFAULT_REGION')
BUCKET_NAME: Union[str, None] = os.environ.get('BUCKET_NAME')
X_SES_CONFIGURATION_SET: Union[str, None] = os.environ.get('X_SES_CONFIGURATION_SET')
