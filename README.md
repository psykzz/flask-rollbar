# Flask Rollbar

Integration for rollbar in Flask


## Example 

```python
from flask import Flask
from flask_rollbar import Rollbar
app = Flask(__name__)
app.config.update({
    'ROLLBAR_ENABLED': True,
    'ROLLBAR_SERVER_KEY': os.environ.get('ROLLBAR_SERVER_KEY'),
})

# Supports using the factory pattern as well.
Rollbar(app)

# Or
# rb = Rollbar()
# rb.init_app(app)

@app.route('/')
def index():
  return "hello world, <a href='/error'>click here for an error</a>"
 
@app.route('/error')
def error():
  a = 1 / 0
  return "Should never happen"

app.run()

```

## Rollbar

Read more about rollbar here https://rollbar.com/

Live demo - https://rollbar.com/demo/demo/

## Readme is still a work in progress
