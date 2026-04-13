# Testing

## Manual testing

## Automated testing

### HTML validation

Used [W3C](https://www.w3.org) validator for both [html](https://validator.w3.org) and [css](https://jigsaw.w3.org/css-validator/) validation.

### CSS validation

### Python validation

Used [Pycodestyle](https://pycodestyle.pycqa.org/en/latest/) validator.\
Used [Black](https://black.readthedocs.io/en/stable/?utm_source=chatgpt.com) linter to beautify code.\
During validation, a couple of errors were flagged:

.\album\models.py:69:89: E501 line too long (106 > 88 characters)
.\album\views.py:96:89: E501 line too long (105 > 88 characters)
.\artist\forms.py:30:89: E501 line too long (108 > 88 characters)
.\artist\forms.py:69:89: E501 line too long (108 > 88 characters)
.\artist\forms.py:71:89: E501 line too long (109 > 88 characters)
.\melodia\settings.py:114:89: E501 line too long (91 > 88 characters)
.\members\forms.py:95:89: E501 line too long (108 > 88 characters)
.\payment\views.py:31:13: E722 do not use bare 'except'

Steps taken:
* For E501, manually broke lines.
* Left .\melodia\settings.py E501 error untouched, as this is django's core element and still easy to read and understand.
* Added better exception handling.
* Rerun black.



