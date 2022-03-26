pytest-google-chat
==================

[![PyPI version](https://img.shields.io/pypi/v/pytest-google-chat.svg)](https://pypi.org/project/pytest-google-chat)

[![Python versions](https://img.shields.io/pypi/pyversions/pytest-google-chat.svg)](https://pypi.org/project/pytest-google-chat)


Notify google chat channel for test results

------------------------------------------------------------------------
- [Installation](#installation)
- [Usage](#usage)
  * [Command line options](#command-line-options)
  * [Using a config file](#using-a-config-file)
  * [Using environment variables:](#using-environment-variables)
- [Contributing](#contributing)
- [License](#license)
- [Issues](#issues)

🧰 Installation
------------

You can install pytest-google-chat via 
[pip](https://pypi.org/project/pip/) from
[PyPI](https://pypi.org/project):

    $ pip install pytest-google-chat

📖 Usage
-----

In order to use this plugin, you need to provide the command line flag `--google-chat` **and** a valid goggle chat webhook.  
The webhook, as all the other parameters, can be provided as a command line argument, as a value inside a config file or as an environment variable.  

### Command line options

| Option          | Description                                                                               | Default value             |
|-----------------|-------------------------------------------------------------------------------------------|---------------------------|
| `--google-chat` | Enable the plugin (**required**)                                                          | This doesn't need a value |
| `--gc-webhook`  | The webhook to send notifications to. <br/>**Important:** Use double quotes for the value | None |
| `--report-link` | The link to the report                                                                    | None |
| `--report-title`| The title of the report                                                                   | None |
| `--report-subtitle` | The subtitle of the report                                                                | None |
| `--gc-fail-image` | The url of an image to use when the test fails                                            | None |
| `--gc-success-image` | The url of an image to use when the test succeeds                                         | None |
| `--gc-config`   | The path to the config file                                                               | None |

### Using a config file
```ini
[GOOGLE-CHAT]
gc_webhook=https://chat.googleapis.com/v1/spaces/AAAA7GkHUoE/messages?key=XXXX&token=YYYY # Do NOT use double quotes here
report_link=https://link.to.report
report_title=My Report
report_subtitle=My Report Subtitle
gc_fail_image=https://link.to.image
gc_success_image=https://link.to.image
```

### Using environment variables:  
`REPORT_TITLE="My Report" pytest --google-chat --gc-webhook=https://....`

❗**NOTE**  
All previous methods can be used combined.  
The order of precedence is: command line options > config file > environment variable.

Contributing
------------

Contributions are very welcome. Tests can be run with
[tox](https://tox.readthedocs.io/en/latest/), please ensure the coverage
at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the
[MIT](http://opensource.org/licenses/MIT) license,
"pytest-google-chat" is free and open source software.

Issues
------

If you encounter any problems, please [file an
issue](https://github.com/geokats7/pytest-google-chat/issues) along with
a detailed description.

---
This [pytest](https://github.com/pytest-dev/pytest) plugin was generated
with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with
[\@hackebrot\'s](https://github.com/hackebrot)
[cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin)
template.
