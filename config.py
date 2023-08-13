import os


class Config:
    AWS_REGION: str = os.getenv('AWS_REGION')
    AWS_ACCESS_KEY_ID: str = os.getenv('AWS_SECRET_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY_ID: str = os.getenv('AWS_SECRET_ACCESS_KEY_ID')
    AWS_API_GATEWAY_URL: str = os.getenv('AWS_API_GATEWAY_URL')

    MAIL_SERVER: str = os.getenv('MAIL_SERVER')
    MAIL_PORT: int = os.getenv('MAIL_PORT')
    MAIL_USE_SSL: bool = os.getenv('MAIL_USE_SSL')
    MAIL_USERNAME: str = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD: str = os.getenv('MAIL_PASSWORD')

    FORWARDING_EMAIL_ADDRESS: str = os.getenv('SENDER_EMAIL')
