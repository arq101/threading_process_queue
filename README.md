# Example using multi-threading to process a queue continuously in the background while the program runs.

As soon as the class from the module 'queue_processor' is instantiated,
it begins to check for items in a priority queue every n seconds.
For every item found in the priority queue, it prints the item's template to an output file.

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
