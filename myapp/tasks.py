from celery import shared_task
from celery.utils.log import get_logger


logger = get_logger(__name__)


@shared_task
def output(string):
    logger.info("Processing {}".format(string))
    return None


@shared_task
def add(x, y):
    return x + y

