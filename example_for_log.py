import logging
from logging.handlers import RotatingFileHandler

# Здесь задана глобальная конфигурация для всех логгеров:
logging.basicConfig(
    level=logging.DEBUG,
    filename='program.log', 
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)
# Создаём форматер:
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Здесь установлены настройки логгера для текущего файла — example_for_log.py:
logger = logging.getLogger(__name__)
# Устанавливаем уровень, с которого логи будут сохраняться в файл:
logger.setLevel(logging.INFO)
# Указываем обработчик логов:
handler = RotatingFileHandler('my_logger.log',
                              maxBytes=50000000,
                              backupCount=5
                              )
logger.addHandler(handler)
# Применяем его к хендлеру:
handler.setFormatter(formatter)

try:
    42 / 0
except Exception as error:
    logging.error(error, exc_info=True)
'''try:
    42 / 0
except Exception:
    logging.exception('На ноль делить нельзя!')'''

logger.debug('123')
logger.info('Сообщение отправлено')
logger.warning('Большая нагрузка!')
logger.error('Бот не смог отправить сообщение')
logger.critical('Всё упало! Зовите админа!1!111') 