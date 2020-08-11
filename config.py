class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    IMAGE_UPLOADS = "/path/to/dir"
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]
    MAX_IMAGE_FILESIZE = 5 * 1024 * 1024 # (5Mb)
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024 # (50Mb)

    CLIENT_IMAGES = "/home/lucas/Dev/analytics/app/static/client/img"
    CLIENT_CSV = "/home/lucas/Dev/analytics/app/static/client/csv"
    CLIENT_PDF = "/home/lucas/Dev/analytics/app/static/client/pdf"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    IMAGE_UPLOADS = "/home/lucas/Dev/analytics/app/static/uploads/img"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SESSION_COOKIE_SECURE = False