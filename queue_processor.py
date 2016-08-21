import threading
import time
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s -- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


class TemplateQueueProcessor(object):

    def __init__(self, templates_file, interval=1):
        self.interval = interval
        self.templates_file = templates_file
        self.priority_queue = []
        self.secondary_queue = []
        self._thread = threading.Thread(target=self._process_priority_queue, args=())
        self._thread.daemon = True
        self._thread.start()

    def _process_priority_queue(self):
        while True:
            try:
                template = self.priority_queue.pop(0)
            except IndexError:
                pass
            else:
                logger.info("Processing priority queue, writing template: {}".format(template))
                with open(self.templates_file, 'a') as fh:
                    fh.write(template + "\n")
                time.sleep(self.interval)

    def read_json_data(self, json_data_file):
        try:
            with open(json_data_file, 'r') as fh:
                data = json.load(fh)
        except ValueError:
            print("Error: check the format of the JSON data file!")
            raise

        for item in data:
            try:
                action = item['action']
            except KeyError:
                return
            else:
                template = item.get('template', 'No template!')
                if action.lower() == 'apply':
                    self.priority_queue.append(template)
                    logger.info("Appended to priority queue template: {}".format(template))
                else:
                    self.secondary_queue.append(template)

    def close_thread(self, time_out=30):
        if self._thread.is_alive():
            self._thread.join(timeout=time_out)
        logger.info("** finished **")
