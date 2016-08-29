# Example using multi-threading to process a queue continuously in the background while the program runs.

## Execute the script

Can be run with python 2.7 or 3.5
```
eg.
python run_program.py [json data file] [templates output file]

python run_program.py data_dump.json templates.txt
```

## Tests

Unit-tests can be run as:
```
python test_template_queue_processor.py
```
or
```
python -m unittest test_template_queue_processor.TestTemplateQueueProcessor
```
