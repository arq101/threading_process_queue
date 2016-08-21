# -*- coding: utf-8 -*-
import unittest
import tempfile
import os

from queue_processor import TemplateQueueProcessor


class TestTemplateQueueProcessor(unittest.TestCase):

    def setUp(self):
        self.json_input = 'data_dump.json'
        self.test_output = tempfile.NamedTemporaryFile().name

    def tearDown(self):
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_process_priority_queue(self):
        q_proc = TemplateQueueProcessor(self.test_output)
        q_proc.read_json_data(self.json_input)
        q_proc.close_thread(6)
        # expect 6 templates to be written to the output file
        with open(self.test_output, 'r') as fh:
            total_priority_templates = sum(1 for line in fh)
        self.assertEquals(total_priority_templates, 6)
        self.assertEquals(len(q_proc.secondary_queue), 7)

    def test_read_bad_json_data(self):
        bad_data = tempfile.NamedTemporaryFile().name
        with open(bad_data, 'w') as fh:
            fh.write(
                    '{"action": "$%@£",'
                    '"when": "2016-4-19 10:00:00",'
                    '"template": "Upsilon Hyperes",}'
            )
        try:
            q_proc = TemplateQueueProcessor(self.test_output)
            with self.assertRaises(ValueError):
                q_proc.read_json_data(bad_data)
        finally:
            q_proc.close_thread(1)
            if os.path.exists(bad_data):
                os.remove(bad_data)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplateQueueProcessor)
    unittest.TextTestRunner(verbosity=2).run(suite)
