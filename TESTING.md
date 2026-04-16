# Testing

## Manual testing

Manual testing is focused on user interaction and feedback.\
Both signed-in and unauthenticated user interactions should be tested.\
Cases involve navigation, functionality, and interactivity.

### Landingpage

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works even with an empty search query.

Content:
* Banner and title placed correctly, buttons work, data rotates on reload for non-rated artists (no rating yet for most artists), only rated artists keep 1st place.
* Table visually breathable. Buttons look interactable, titles make sense. After interaction music plays, links work.\
If there is no rating, hovering over the text causes it to disappear as expected, and leaves an unexpected empty space. On smaller screens table remains rigid and cluttered.
* Discover section displays properly. Only ten artists displayed. Linkage works.

Steps taken:
1. Search input field required attribute added, ensuring empty query is not submitted.
2. Table is made responsive. Overflow added to ratings.
3. Added prompt to log in before rating.

### Signup/Login page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.

Content:
* Form is center with breathable space. Container is responsive.
* All links working.
* Feature works as expected.
* Account-related workflow works as expected (register/reset pw)

### Artist page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.

Content:
* Elements are in expected places. Responsive.
* Social links work.
* Donation link works.
* Payment workflow works as expected.
* Album tables visually breathable. Buttons look interactable, titles make sense. After interaction music plays, links work.\
If there is no rating, hovering over the text causes it to disappear as expected, and leaves an unexpected empty space. On smaller screens table remains rigid and cluttered.
* Default/empty album image had incorrect classes.
* Donation/Edit buttons hidden for non-manager users, without user's Stripe connection.
* "Empty" artist entries have default pictures on page.

Steps taken:
1. Made table responsive, added overflow to cluttering elements.
2. Corrected classes on image element.
3. Added prompt to log in before rating.

### Manage page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.

Content:
* Elements are in expected places. Responsive. Columns work as expected.
* Artists links work.
* Artist creation workflow works as expected.

### Album addition page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.
* Object creation works as expected.

Content:
* Elements are in expected places. Form is responsive.
* Album creation workflow works as expected.
* Navigation buttons work.

### Track creation page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.

Content:
* Elements are in expected places. Formset is responsive.
* All buttons work as expected.
* Object creation works as expected.

During development there were a couple of notable issues:
* Formset was prefilled when visiting the page, creating already created tracks even in hidden forms.
* Phantom forms were submitted (forms were still filled after hiding them).

Steps taken during development:
1. Specifically made the formset with empty objects to ensure no pre-filling.
2. Function added to clear data on hiding forms.

### Album edit page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.

Content:
* Elements are in expected places. Form is responsive, formset is cluttered on smaller screens. 
* Data is prefilled for relevant objects.
* All buttons work as expected.
* Object creation/update/deletion works.

Steps taken:
1. Columns made responsive.

### Artist edit page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.

Content:
* Elements are in expected places. Form is not responsive. Artist banner image was overflowing.
* Data is prefilled for artist object.
* Navigation buttons work as expected.
* Object creation/update works.

Steps taken:
1. Container made responsive.
2. Banner image made responsive.

### Account page

Navigation:
* Navbar links work as expected. Takes to the indicated page.
* Search option works.

Content:
* Elements are in expected places. Form is responsive.
* All buttons work as expected.
* Password reset workflow works as expected.
* Stripe connect account visible after connecting. Error in console regarding a non-existent button.

Steps taken:
1. Removed non-existent element manipulation in JS.

### Notable issues during development

During development, testing was carried out on each function as it was implemented.

Some notable issues:
* Audio player was not playing files automatically even after reference was updated: needed to manually load and play files after updating file reference.
* Cloudinary native upload expects images: to upload audio files, raw file data had to be used.
* Length retrieval was incorrect for multiple tracks: as far as I understood, Mutagen reads the file data and leaves the pointer at the end of the file. Without resetting it, subsequent reads return incorrect values. Had to manually reset pointer for each file.
* Audio player stopped playing: when the last song was hit, the player's logic went out of bounds. Implemented replay from the first song when the last song started playing.

## Automated testing

### HTML validation

Used [W3C](https://www.w3.org) validator for both [html](https://validator.w3.org) and [css](https://jigsaw.w3.org/css-validator/) validation.

#### Album app templates

1. Create track page

    * During validation a couple of errors were flagged:
        1. Multiple, the element label must not appear as a descendant of the button element.
        2. Multiple, attribute rows not allowed on element select at this point.
        3. Multiple, no p element in scope but a p end tag seen.

    * Steps taken:
        1. Retrieving only label text not the whole label form element.
        2. Removed rows attribute from selects.
        3. Replaced "p" tags with "div".

2. Edit album page

    * During validation a couple of errors were flagged:
        1. Multiple, the element label must not appear as a descendant of the button element.
        2. Multiple, no p element in scope but a p end tag seen.
        3. Multiple, duplicate ID id_form-*-id.
        4. The aria-describedby attribute references id_image_helptext, which is not the ID of any element in this document.

    * Steps taken:
        1. Retrieving only label text not the whole label form element.
        2. Removed rows attribute from selects.
        3. Replaced "p" tags with "div". 
        4. Encased helptext in mathcing id element.

#### Artist app templates

1. Artist page

    * During validation a couple of errors and warnings were flagged:
        1. Bad value for attribute src on element source: Must be non-empty.
        2. Warning: Empty heading.
        3. The heading h5 (with computed level 5) follows the heading h2 (with computed level 2), skipping 2 heading levels.

    * Steps taken:
        1. Removed source -> It must be present -> Update audio element with source as at the moment multiple audio formats not supported.
        2. Filled headings.
        3. Added hidden heading to satisfy structure.

2. Album creation page

    * During validation no errors or warnings were flagged.

3. Artist creation page

    * During validation no errors or warnings were flagged.

4. Edit artist page

    * During validation a couple of errors and warnings were flagged:
        1. Multiple, The aria-describedby attribute references id_image_helptext, which is not the ID of any element in this document.

    * Steps taken:
        1. Encased helptexts in mathcing id element.

#### Landingpage app templates

1. Index page

    * During validation a couple of errors and warnings were flagged:
        1. Bad value for attribute src on element source: Must be non-empty.
        2. Warning: Empty heading.
        3. The heading h5 (with computed level 5) follows the heading h2 (with computed level 2), skipping 2 heading levels.

    * Steps taken:
        1. Audio player matches artists one. Removed source child element. JS handles src update.
        2. Filled headings.
        3. Added hidden heading to satisfy structure.

2. Search page

    * During validation a couple of errors and warnings were flagged:
        1. Element title must not be empty.
        2. Multiple, the heading h3 (with computed level 3) follows the heading h1 (with computed level 1), skipping 1 heading level.

    * Steps taken:
        1. Added title.
        2. Added hidden heading to satisfy structure.

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



