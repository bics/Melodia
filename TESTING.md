# Testing

## Manual testing

Manual testing is focused on user interaction and feedback.\
With both signed-in and unauthenticated user interactions should be tested.\
Cases involve navigation, functionality, and interactivity.

### Landingpage

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works even with empty search query.

Content:
* Banner and title placed correctly, buttons work, data rotates on reload for not rated artists (no rating yet for most artists), only rated artists keeps 1st place.
* Table visually breathable. Buttons looks interactable, titles make sense. After interaction music plays, links work.\
If there is no rating, hovering over the text causes it to disappear as expected, and leaves an unexpected empty place. On smaller screens table ramins rigid and cluttered.
* Discover section displays properly. Only ten artists displayed. Linkage works.

Steps taken:
1. Search input field required attribute added, making sure empty query is not submitted.
2. Table is made responsive. Overflow added to ratings.

### Signup/Login page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.

Content:
* Form is center with breathable place. Container is responsive.
* All links working.
* Feature works as expected.
* Account related workflow works as expected (register/reset pw)

### Artist page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.

Content:
* Elements are in expected places. Responsive.
* Social links work.
* Donation link works.
* Payment workflow works as expected.
* Album tables visually breathable. Buttons looks interactable, titles make sense. After interaction music plays, links work.\
If there is no rating, hovering over the text causes it to disappear as expected, and leaves an unexpected empty place. On smaller screens table ramins rigid and cluttered.
* Default/Empty album image had incorrect classes.
* Donation/Edit buttons hidden for non-manager users, without users stripe connection.
* "Empty" artist entries have default pictures on page.

Steps taken:
1. Made table responsive, added overflow to cluttering elements.
2. Corrected classes on image element.


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



