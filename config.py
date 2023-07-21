# config.py
# Configuration settings for the Flask app and summarization method
# Remember to keep this file private

class Config:
    # Flask app configuration
    FLASK_HOST = '127.0.0.1'
    FLASK_PORT = 5000

    # Summarization method configuration
    # Options: 'sumy', 'textblob'
    SUMMARIZATION_METHOD = 'sumy'

    @staticmethod
    def get_flask_host():
        return Config.FLASK_HOST

    @staticmethod
    def get_flask_port():
        return Config.FLASK_PORT

    @staticmethod
    def get_summarization_method():
        return Config.SUMMARIZATION_METHOD
