# Flask Rollbar

[Rollbar](https://rollbar.com) integration for [Flask](https://flask.palletsprojects.com/).

## Installation

```sh
pip install flask-rollbar
```

## Requirements

- Python 3.9+
- Flask 3.0+

## Usage

```python
import os
from flask import Flask
from flask_rollbar import Rollbar

app = Flask(__name__)
app.config.update({
    'ROLLBAR_ENABLED': True,
    'ROLLBAR_SERVER_KEY': os.environ.get('ROLLBAR_SERVER_KEY'),
    'ROLLBAR_ENVIRONMENT': 'production',
})

Rollbar(app)

# Or use the app factory pattern:
# rb = Rollbar()
# rb.init_app(app)

@app.route('/')
def index():
    return 'hello world'

@app.route('/error')
def error():
    raise RuntimeError('example error — will be reported to Rollbar')
```

## Configuration

| Key | Default | Description |
|-----|---------|-------------|
| `ROLLBAR_ENABLED` | `False` | Enable/disable Rollbar reporting |
| `ROLLBAR_SERVER_KEY` | — | Your Rollbar server-side access token |
| `ROLLBAR_ENVIRONMENT` | `development` | Environment name sent to Rollbar |
| `ROLLBAR_OVERWRITE_REQUEST` | `False` | Allow overwriting Flask's request class |

## Custom Request Handler

You can pass a custom request class to expose user identity to Rollbar:

```python
from flask import Request

class MyRequest(Request):
    @property
    def rollbar_person(self):
        # Return a dict with id, username, or email
        return {'id': '123', 'username': 'example'}

Rollbar(app, request_handler=MyRequest)
```

## Contributing

Pull requests and issues are welcome.