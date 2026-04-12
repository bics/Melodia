# Melodia

[Deployed site](https://melodia-music-e57dab08c43e.herokuapp.com)\
Use "Ctrl + click" or "CMD + click" to open in new tab

# Table of contents    

1. [UX](#ux)
2. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Future Features Consideration](#future-features-consideration)
3. [Data](#data)
4. [Technologies used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. [Acknowledgements](#acknowledgements)

# UX

### User stories
* First Time Visitor Goals
    * First time users should be able to understand the purpose of the site.
    * They should be able to navigate the site without any issue.
    * The site should encourage users to interact with it.

* Returning Visitor Goals
    * Returning visitors should be able to notice any changes on the website.
    * Changes should be evident to returning visitors

* Frequent User Goals
    * Frequent users should be able to listen and enjoy to uploaded audio files.
    * They should be able to rate uploaded audio files.

### Design

Colour Scheme

Main colours used on the website\
![Color palette](static/assets/images/color_palette.png)

Typography

* Corbel is used with a fallback to Calibri first and then to sans-serif.

### Wireframes
<details>
<summary>Mobile</summary>

![Mobile wireframe landingpage](static/assets/wireframes/mobile_landingpage.png)
![Mobile wireframe arist](static/assets/wireframes/mobile_artists.png)

</details>
<details>
<summary>Tablet</summary>

![Tablet wireframe landingpage](static/assets/wireframes/tablet_landingpage.png)
![Tablet wireframe arist](static/assets/wireframes/tablet_artists.png)

</details>
<details>
<summary>Desktop</summary>

![Desktop wireframe landingpage](static/assets/wireframes/pc_landingpage.png)
![Desktop wireframe arist](static/assets/wireframes/pc_artists.png)

</details>

# Features

## Existing features

### Landing page

The landing page is a mix of suggestions.\
On top of the page users can interact with the navigation bar. These could help them locate the pages they wish to visit, or simply look
for any data available about songs, albums and artists.

The first suggestion part is a huge banner with 5 random artists. They ranked by their accumulated rating of all songs.

![Landing page banner](static/assets/images/landingpage_banner.PNG)

The next part is a hidden audio player. The player becomes visible, when the user start listening to one the songs.\
Below the player is a table with 15 completely random songs.

![Landing page banner](static/assets/images/landigpage_table.PNG)

The last part is showcasing 10 random artists.

### Account page

On this page users can update their details or initiate password reset\

Users can request manager access. This function does nothing at the moment, but future consideration should be made to include automated
ticket creation for staff to enable manager features for an account.

Once manager access is granted, managers here can (and need to) link their stripe account. The account linking helps to ensure donation
will be received correctly. The page renders the account onboarding status as well, making sure managers are aware if they need to update their stripe account.

![Account page](static/assets/images/account.PNG)

### Artist page

The artist page is similar to the landing page, but only focuses on a single artist.\
On top there is the banner image for the artist.\
In the middle is the details of the band/artist. On the left side is the band's/artist's image, and on the right side their socials, description and name. In this part lies the donation button, where users can donate directly (or rather through their agent) to their favourite artist.\

![Artist page top](static/assets/images/artist_page.PNG)

If the artist's manager visits this page, this is were they are able to update their managed artist's details.\
The last part is where all of the artist's albums is displayed. This part also has a hidden audio player, which will be visible once 
one of the songs staring to play.\
In this section manager can add or edit the albums itself.

![Artist page albums](static/assets/images/artist_page_albums.PNG)

### Edit artist page

To edit the artists details, manager can navigate to the edit page. Here all the related details for the artists can be updated.

![Edit artist](static/assets/images/edit_artist.PNG)

### Album addition/edit

Managers can easily add new albums to their artists. They need to locate the creation button, which navigates them to the creation page.
Here after filling out the form an album is created for the artist.

![Album creation](static/assets/images/album_creation.PNG)

To edit the album, after navigating to the page, managers can update the albums details, and remove or edit any track details. This ensures all related data manipulation happens on one page.

![Edit album](static/assets/images/edit_album.PNG)

![Edit track](static/assets/images/edit_tracks.PNG)

### Track addition

To add tracks, managers first need to select an album, then after navigating to the addition page they are able to add up to a maximum 12 tracks at a time.\
These achieved using a formset. Additional forms can be added/removed with the respective buttons. Removing a form also clears it so data
will not be saved accidentally.

![Add track](static/assets/images/track_addition.PNG)

### Donation page

The donation button is located on the artist page. It is hidden until the manager have managed to acquire their stripe user id.\
The donation page is a very simple form for users to donate to their favourite artists. Here users can choose a small predifined amount or set a custom amount.

![Donation](static/assets/images/donation.PNG)

After clicking either a predefined or submitting a custom donation the user is redirected to stripe's payment window. Here stripe will validate the users details.

If users decide to go back, they will be redirected to the artist page.\
After the payment succeeded they are redirected to the success page.

### Manage page

On this page, managers can add new artists to the site. This page also allows them to navigate to their managed artists pages easily.

![Manage page](static/assets/images/manage.PNG)

### Rating system

Within the album tables, and the landing page suggestion table, users can rate songs. These ratings are saved via AJAX solely to enable users to listen to the songs, and rate at the same time, as no reload needed.\
Rating for each song in both tables will be shown after a minimum number of submissions. Currently, a rating is shown once at least three ratings have been received.

![Ratings](static/assets/images/ratings.PNG)

### Search function

If a user uses the search function, they will be presented with all matching data found.\
These results are categorized so the user should be able to select from each type if data they were looking for.

![Search page](static/assets/images/search.PNG)

### Django Allauth's core features

The project is integrated with Django Allauth’s core features. This enables easy user management and provides essential security protections.\
It is used for user creation, user login, user logout, and password management.\
This ensures users have accurate details and enforces strong password usage.

### Cloudinary

This 3rd party media storage service is used to store user-uploaded images.

![Cloudinary image](static/assets/images/cloudinary_image.PNG)

## Future Feature Considerations

* Global music player: Currently, each audio player is limited to its respective page. Leaving this page will stop the player.
* Playlist creation: Feature could be added so users can create custom playlists. Also, there is a possibility to add auto-generated playlists.
* Favourites: Users could save their favourite songs, and a feedback feature could be implemented based on metadata from these.
* Artists transfer: Feature can be added so managers are able to transfer artists when needed.
* Comment section: A section can be added for each artist, album, or song for users to interact.
* Artists multiple art/image: Currently, only one banner and image can be used for an artist. These could be overhauled to enable multiple images, like an account on social media.
* Multiple suggestions: Currently, suggestions are only filtered by ratings. A couple of new suggestion-based filters can be added for newly added songs/artists or any related data (e.g. similar users’ favourites).

# Data

![Database models](static/assets/images/DB_diagram.png)

# Technologies used

* The core project is written in HTML5, CSS3 and Python.
* Used [Visual Studio Code](https://code.visualstudio.com) as IDE.
* Used [Github](https://github.com) to store and deploy the repository.
* Used [Sourcetree](https://www.sourcetreeapp.com) for version control.
* Used [Opera](https://www.opera.com), [Mozilla](https://www.mozilla.org/en-GB/) and [Chrome](https://www.google.com/intl/en_uk/chrome/) browsers and their respective developer tools for testing.
* Used [ChatGPT](https://chatgpt.com) for debugging, code and content generation.
* Used [W3Schools](https://www.w3schools.com) to help to understand and write codes.
* Frequently visited [Stack Overflow](https://stackoverflow.com/questions) to understand some behaviours.
* Used [Bootstrap](https://getbootstrap.com) as css.
* Used [Freepik](https://www.freepik.com) to acquire free images.
* Used [Krita](https://krita.org/en/) and [Canva](https://www.canva.com) for modifying pictures.
* Used [Coolors](https://coolors.co) to create color palette.
* Used [Microsoft Windows](https://www.microsoft.com/en-gb/windows?r=1) in-built **Snippet** tool to capture images.
* Used [Cloudinary](https://cloudinary.com) to store media images.
* Used [PostgreSQL](https://www.postgresql.org) as database.
* Used [Heroku](https://www.heroku.com) as hosting platform.
* Used [Wordmark](https://wordmark.it) to select fonts.
* Used [Canva](https://www.canva.com) to create wireframes.
* Used [Youtube](https://www.youtube.com) with [OnlyMP3 converter](https://en.onlymp3.io/A04/) to acquire audio tracks

* Used the [Django web framework](https://www.djangoproject.com), with the following core technologies:

| Name | Purpose |
|------|---------|
| Django | Core |
| django-allauth | User management |
| django-cloudinary-storage | Supports Cloudinary integration |
| cloudinary | Supports Cloudinary integration |
| pillow | Image processing helper |
| whitenoise | Serves static files |
| psycopg2 | PostgreSQL adapter |
| gunicorn | Production WSGI server |
| stripe | Payment processing (Stripe integration) |
| dj-database-url | Database configuration via environment variables |
| mutagen | Audio metadata handling |
| requests | HTTP requests |


# Testing

Testing is extracted to it's own document, [TESTING]()

# Deployment

### Heroku
The project is deployed to [Heroku](https://www.heroku.com). In order to achieve this the following steps were taken:\
1. Sign into [Heroku](https://www.heroku.com).
2. Start creating a new app.
3. Use Github as preferred deployment method. 
4. Connect to your Github account, and connect the corresponding repository.
5. Setup the reqiured environment variables.
    
6. Once it successfully connected select a branch to deploy and hit "Deploy branch".

### Forking a repository

1. Sign into [Github](https://github.com/) (can be done later).
2. On [Github](https://github.com/) locate the [Melodia](https://github.com/bics/Melodia) repository.
3. On the top right hand side click on the "Fork" option.
4. Sign into [Github](https://github.com/) (not needed if step 1. was taken).
5. The repository should be present under your account's repositories.

### Download local repository

1. Navigate to the [Melodia](https://github.com/bics/Melodia) repository.
2. On the right side select the "Code" dropdown menu.
3. Download the repository as a .zip file.
4. Extract the downloaded file.
5. Open up your preferred IDE and add the extracted folder as a project.

### Clone a repository with Sourcetree

1. Import SSH key. If SSH key already imported skip these steps
    1. Acquire the SSH key, and password for this repository.
    2. Locate the "Tools" menu, and select the "Create or import SSH keys" option.
    3. In the dialog select "Load" and locate the acquired SSH key.
    4. If prompted sign in to [Github](https://github.com/) account and enter the password.
2. Click on the "+" icon to add a local repository.
3. Select the "Remote" option on the top navigation bar.
4. Search for the [Melodia](https://github.com/bics/Melodia) repository and hit clone.

# Credits

### Code

* gitgnore copied from previous [CoffeeHouse](https://github.com/bics/CoffeeHouse) project
* base.html copied and modified from previous [CoffeeHouse](https://github.com/bics/CoffeeHouse) project
* Login form html and form from previous [CoffeeHouse](https://github.com/bics/CoffeeHouse) project
* Account details update modals was copied from previous [CoffeeHouse](https://github.com/bics/CoffeeHouse) project
* CreateArtistForm helptext update copied from previous [CoffeeHouse](https://github.com/bics/CoffeeHouse) project
* Cloudinary settings copied from previous [CoffeeHouse](https://github.com/bics/CoffeeHouse) project
* Whitenoise middleware addon copied from [W3Schools](https://www.w3schools.com)
* Allauth settings block taken from [official allauth documentation](https://docs.allauth.org/en/latest/)
* Search view inspired by tutorial from [John Elder](https://www.youtube.com/watch?v=AGtae4L5BbI&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=9)

#### Bootstrap

* Navbar block taken from [Bootsrap's official documentation](https://getbootstrap.com/docs/5.3/components/navbar/)
* Carousel code block taken from [Bootsrap's official documentation](https://getbootstrap.com/docs/5.3/components/carousel/)
* Card code block copied from [Bootsrap's official documentation](https://getbootstrap.com/docs/5.3/components/card/)
* Collapse code block copied from [Bootsrap's official documentation](https://getbootstrap.com/docs/5.3/components/collapse/)

#### Stripe

* Form block for members copied from [official stripe marketplace implementation](https://docs.stripe.com/connect/marketplace/quickstart?lang=python)
* Try block copied from [official Stripe documentation](https://docs.stripe.com/connect/marketplace/quickstart?lang=python)
* stripe_account_status.js was copied and modified from [official Stripe documentation](https://docs.stripe.com/connect/marketplace/quickstart?lang=python)
* Try-catch block code for donation view was copied from [official Stripe documentation](https://docs.stripe.com/checkout/quickstart) and [official stripe marketplace implementation](https://docs.stripe.com/connect/marketplace/quickstart?lang=python)
* Webhook handler view was copied from [official Stripe documentation](https://docs.stripe.com/webhooks/quickstart?lang=python) and modified using ChatGPT

#### AI

* Social urlization generated using [ChatGPT](https://chatgpt.com) for artists socials
* GetSocial method partially generated using [ChatGPT](https://chatgpt.com)
* Featured artist query selector generated using [ChatGPT](https://chatgpt.com)
* Formset save partially generated using [ChatGPT](https://chatgpt.com)
* Form reset logic generated using [ChatGPT](https://chatgpt.com)
* Extracting selected option partially generated using [ChatGPT](https://chatgpt.com)
* File upload path partially generated using [ChatGPT](https://chatgpt.com)
* Landing page random object retrieval and sorting generated using [ChatGPT](https://chatgpt.com)
* Audio upload and length retrieval generated using [ChatGPT](https://chatgpt.com)
* Proper length return generated using [ChatGPT](https://chatgpt.com)
* AJAX submission and helper method generated using [ChatGPT](https://chatgpt.com)
* Rate track view generated using [ChatGPT](https://chatgpt.com)
* Tooltip retrieval generated using [ChatGPT](https://chatgpt.com)
* Rating retrieval partially generated using [Claude](https://claude.ai/new)
* Input sanitation for search generated using [ChatGPT](https://chatgpt.com)
* Donation if statement block was partially generated using [ChatGPT](https://chatgpt.com)
* Artist update view decorator was generated using [ChatGPT](https://chatgpt.com)
* startOnboarding and getCookie functions were generated using [Claude](https://claude.ai/new)
* account_status and create_account_link views were generated using [ChatGPT](https://chatgpt.com) and [Claude](https://claude.ai/new)

### Content

* Using core Django Allauth default messages.
* All other content was written by me.

### Media

* music_note.jpg by [juicy_fish](https://www.freepik.com/free-vector/three-music-notes-floating-upwards_290240060.htm#fromView=search&page=1&position=1&uuid=44844498-6808-4a2e-b6c8-5bcb8592dcd7&query=music+note)

* vinyl_disc by [xadartstudio](https://www.freepik.com/free-psd/vinyl-record-timeless-classic-music_406616720.htm#fromView=search&page=1&position=1&uuid=678e9eb1-3e31-403f-a8fc-c7cd79cc72ea&query=vinyl+disc)

* blank_user_pic by [juicy_fish](https://www.freepik.com/free-vector/blank-user-circles_134996379.htm#fromView=search&page=1&position=1&uuid=9bb78e8c-d30a-4aee-b687-d4a30d3a706a&query=blank+user+picture)

* single_note_tilted generated with from music_note.jpg [ChatGPT]()

* paramore-banner image from [ticketmaster](https://discover.ticketmaster.co.uk/wp-content/uploads/2022/10/paramoreplusone-738x415.jpg)

* paramore-artist-image from [pinterest](https://i.pinimg.com/originals/ca/b7/ec/cab7ecfe04f79e0d8060a996d5b8b648.png)

* paramore-riot from [wikipedia](https://upload.wikimedia.org/wikipedia/en/2/28/Paramore_-_Riot%21.png)

* paramore-brand-new-eyes from [Spotify](https://i.scdn.co/image/ab67616d0000b273e01d7d558032457b0e4883f6)

* paramore-after-laughter from [Society6 Blog -](https://blog.society6.com/app/uploads/2017/05/Paramore-After-Laughter-2017-2480x2480.jpg)

* play-button by [Harryarts](https://www.freepik.com/free-vector/shiny-play-button_840752.htm#fromView=search&page=2&position=2&uuid=d7ab2319-57b8-48a0-8a6c-0f119212bfac&query=play)

* button-set by [juicy_fish](https://www.freepik.com/free-vector/multimedia-buttons-cartoon-style_417881887.htm#fromView=search&page=1&position=22&uuid=c850db0d-cdaf-499e-b251-fc2edcdd8e09&query=pause+button)

* pause-button by [rawpixel.com](https://www.freepik.com/free-vector/stop-button_2900766.htm#fromView=search&page=1&position=3&uuid=c850db0d-cdaf-499e-b251-fc2edcdd8e09&query=pause+button)

* play_button_small and pause_button_small was generated using [ChatGPT](https://chatgpt.com)

* empty_banner_with_drums by [pvproductions](https://www.freepik.com/free-photo/drum-set-black-background-isolated-copy-space_174141486.htm#fromView=search&page=1&position=7&uuid=1fc10dad-c6d4-4960-bf19-cc3b5960fb87&query=empty+band+banner+template)

* empty_album_cover by [luis_molinero](https://www.freepik.com/free-vector/view-texture-case-media-front_1135006.htm#fromView=search&page=1&position=6&uuid=2370de03-3a18-4e84-bd96-310043a57c84&query=empty+album+cover)

* rating_star_full by [mamewmy](https://www.freepik.com/free-psd/star-winner-rating-review-icon-sign-symbol-3d-background-illustration_71291981.htm#fromView=search&page=1&position=1&uuid=2f9670c6-78f3-4fd5-9fc4-1902548287df&query=rating+star)

* rating_star_gray was generated using [ChatGPT](https://chatgpt.com)

* rating_star_full_transbg modified using [removebg](https://www.remove.bg/hu/upload)

* All tracks were downloaded from [Youtube](https://www.youtube.com) using [OnlyMP3 converter](https://en.onlymp3.io/A04/)

# Acknowledgements

Thank you to Kevin Loughrey, our cohort leader, for his continuous support and feedback during development.