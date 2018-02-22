import logging
import time

logger = logging.getLogger(__name__)


def delay(stage, when):
    """Look for delay_before/delay_after and sleep

    Args:
        stage (dict): test stage
        when (str): 'before' or 'after'
    """

    try:
        delay = stage["delay_{}".format(when)]
    except KeyError:
        pass
    else:
        logger.debug("Delaying %s request for %d seconds", when, delay)
        time.sleep(delay)