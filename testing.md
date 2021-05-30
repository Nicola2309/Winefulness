# Testing

To return to previous document, please click [here](https://github.com/Nicola2309/Winefulness/blob/master/README.md).

## Table Of Contents
- [Validation](#Validation)
- [Testing User Stories](#Testing-User-Stories)
    - [Viewing and Navigation](#Viewing-and-Navigation)
    - [Registration and User Accounts](#Registration-and-User-Accounts)
    - [Sorting and Searching](#Sorting-and-Searching)
    - [Purchasing and Checkout](#Purchasing-and-Checkout)
    - [Admin](#Admin)
- [Further Testing](#Further-Testing)
- [Manual Testing](#Manual-Testing)
- [Bugs](#Bugs)
- [Compatibility Testing](#Compatibility-Testing)
    - [Testing with different Browsers](#Testing-with-different-Browsers)
    - [Testing With Different Devices](#Testing-With-Different-Devices)

## Validation

### HTML

My HTML code was passed through the [W3C Markup Validation Service](https://validator.w3.org/).
Doing so brought up a few errors throughout the project related to using Django templates. These included:
1. An issue in using '{}' brackets as part of the source for ```<a>``` elements and ```<img>``` elements. This syntax is necessary to access static files and urls and was therefore ignored.
2. All html templates led to errors that the doctype and language were not declared. As the templates were based on the base.html template where these were addressed, this issue was also ignored.
3. Some Bootstrap Modals on the site returned errors with their 'aria-labelledby' attribute. This error was related to using templating language to specify the item the modal was related to, so this error had to be ignored.
4. The base.html template returned a few errors shown on the screenshot below. However, these errors are related to using templating language in the html document and were therefore ignored as the validator was raising incorrect errors.
5. It returned a warning on `type='text/javascript'` as not required, I share below the screenshot of the error in 'add_winemaker' page as an example.


    - ![html-django validator errors](https://github.com/Nicola2309/Winefulness/blob/master/media/readme_imgs/html-django-err2.png)

    - ![html-django validator error](https://github.com/Nicola2309/Winefulness/blob/master/media/readme_imgs/html-django-err.png)

    -![html-js warning](https://github.com/Nicola2309/Winefulness/blob/master/media/readme_imgs/html-js-err.png)

### CSS
I checked all CSS code with the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/). 
The profile and base templates had the same error, a double column.
Screenshots of the profile.css page below.

- ![screenshot error validator](https://github.com/Nicola2309/Winefulness/blob/master/media/readme_imgs/css-error.png)

- ![screenshot solved](https://github.com/Nicola2309/Winefulness/blob/master/media/readme_imgs/css-no-error.png)

### JavaScript
I used [JSHint](https://jshint.com/) to check my JavaScript code.
The only issue that came up with these checks was related to a forgotten semicolon within a JavaScript file inside the 'Bag' app and the qty_input_script.html. Adding a ';' corrected this issue and returned no further relevant errors.

![js-semicolon example](https://github.com/Nicola2309/Winefulness/blob/master/media/readme_imgs/js-semicolon.png)

### Python
I used [PEP8](http://pep8online.com) to check the Python code stored within each app.
This returned indentation errors and warnings that some lines that were too long within a few files. When these were corrected, there were no further errors.

[Back to Top](#table-of-contents)

## Testing User Stories

### Viewing and Navigation

* As a shopper I want to be able to view a list of wines so that I can buy my favourite and try new ones..
    - *When this user arrives at the site, they will be able to see the products by directly clicking on the 'Shop Now' button or navigating with the navbar which will take them to the products page. From there they will be able to filter the products by their favourite wine type and choose their favourite.*

* As a shopper I want to be able to view the details of each individual product so I can see the price, description, images of the product and ratings.
    - *When the user arrives on the products page they will be able to click on any product they desire which will present them with the product info page, which will provide them with the description, price, image, and ratings.*

* As a shopper I want to be able to view the contents of my shopping bag so that I can update or remove items.
    - *When the user adds a product to their shopping bag, they will be presented with a toast message with an overview of the product they have added to their bag and a button which gives them the opportunity to navigate to their bag. Alternatively the user can click the bag icon in the top right of the nav bar at any given moment when they are using the site.*

* As a shopper I want to be able to view the grand total of my bag at all times so that I can avoid delivery costs.
    - *Whilst the user is using the site a summary of their bag grand total can be seen in the top right of the nav bar at all times. When the users adds a product a yellow stripe in the toast success message will show how much the user still needs to add to have free delivery*

### Registration and User Accounts

* As a user I want to be able to register and access my account so that I can keep track of my order history in my profile. 
    - *When the user arrives on the website, they can navigate to the 'My Account' button in the top right of the nav bar which gives them the option to either Register or login.*

* As a user I would like to recieve a confirmation email so that I can verify my account.
    - *Upon registering the user will recieve a confirmation email to the email address that they signed up with.*

* As a user I would like to be able to save my personal and default delivery information so that I don't have to enter it every time I make a purchase.
    - *When a user has registered for an account they will be able to navigate to their own profile from the dropdown menu in 'My Account'. On their profile they will be presented with a form which will enable them to read or update their default delivery information.*

* As a user I would like to be able to view the Wine Producers page as a registered user so that I can add comments and share my experience.
    - *A user is able to navigate to the Wine Producers section from the navbar, where they can view Wine Producers page. If Logged In, when the users arrive on the page of a Wine Producer they are presented with a form which enables them to add a comment. The user is able to update or remove the comment after adding it. If the user is a guest they can only read the comments.*

* As a user I would like to be able to view the Wine individual page as a registered user so that I can add reviews and share my opinion.
    - *A user landing on the individual Wine Producer Page can find the comment section below the Wine producer description. The user can add a comment sharing their experience or any other opinion on the regarding Wine Producer*

### Sorting and Searching

* As a shopper I want to be able to filter the products so that I can identify the best priced, best rated and by category of my choice.
    - *When the user arrives in the website, they can navigate to the products page via the navbar. The navbar contains two dropdown menu's, the first dropdown menu will enable them to filter by best priced, best rated, category  and the second by a specific category of their choice.*

* As a shopper I would like to be able to search by name or description so that I can buy the Wine with the taste characteristics I want.
    - *When this user arrives in the website, they will notice a searchbar next to the logo if from desktop or a hand lens icon if from smaller screen which when clicked will prompt a searchbar. From the searchbar they can search any paticular query they want*

### Purchasing and Checkout

* As a shopper I want to be able to see an overview of my order so that I can ensure that I have the correct items and control my spending.
    - *When a user has added products to their shopping bag and proceeds to the checkout page they will be presented with an overview of their order, giving them the opportunity to make any changes before they make their purchase.*

* As a user I want to see efficient form validation when entering my payment details so that I can be sure that my information is safe.
    - *When the user proceeds to the checkout app to make their purchase they are presented with a form for them to enter their details. There is extensive form validation that has been carefully created through the models. If the user have made a purchase before the form is filled already.*

* As a shopper I would like to see an overview of my order details so that I can ensure that it has been processed properly.
    - *When the user completes the payment process, they are presented with an order confirmation with a summary of their order details. This information will also be stored in the users profile.*

### Admin

* As the store owner I want to be able to add a product so that I can add new products to the store.
    - *When the store owner is logged into their profile, they are able to select the my account dropdown from the navbar which presents them with a Product Manager button. This takes them to the add product page where they are able to add new products.*

* As the store owner I want to be able to edit and update products so that I can change the prices, images, description and ratings.
    - *When the store owner is logged into their account, they are able to navigate to the products page where they will be able to click on the edit button which will be featured on each product which will take them to the edit product page.*

* As the store owner I want to be able to delete products so that I can remove products that are no longer available.
    - *When the store owner is logged into their account, they are able to navigate to the products page where they will be able to click on the delete button which will be featured on each product and will delete that particular product.*

[Back to Top](#table-of-contents)

## Further Testing

* Throughout the development process I used Chromes Developer Tools extensively to test the resposinveness of my site accross all screen sizes.

* I went through the site and manually tested each button and link to ensure that they were all working correctly and linking to the correct places.

### Manual testing

#### Features consistent throughout the project

- The return to top arrow jumps to the top of the page regardless of which screensize the user has.
- Users who have not signed in are unable to access pages for authenticated users, and manually changing the url does not lead to any internal pages.

#### Menu

- *Logo* - clicking on the logo takes a user back to the home page.
- *My Account* - opens a drop down menu with the following content:
    * Users not in session: *Register* and *Login*, leading to respective forms.
    * Users who have signed in: *My Profile*, and *Logut*. Each link leads to their respective pages.
    * Users which are super users: *Product Management* and *Producer Management* which lead to the respective forms to add a Product or a producer to the website.
- *Home* - as above, clicking on this link returns the user to the home page.
- *All Products* - opens a drop down menu with the following content: 
    * The clickable element *By Price* to see the products organized in ascendant price.
    * The clickable element *By Rating* to see the products organized in ascendant rating.
    * The clickable element *By Category* to see the products organized in ascendant alphabetical order of the categories.
    * The clickable element *All Products* to view all products.
- *Wines* - opens a drop down menu with the following content: 
    * The clickable element *Red* to see the products in the category *Red Wine*.
    * The clickable element *White* to see the products in the category *White Wine*.
    * The clickable element *Sparkling* to see the products in the category *Sparkling Wines*.
    * The clickable element *All Wines* to view all products.
- *Our Wine Producers* - directs a user to the Wine Producers page.

#### Footer

- Clicking on the Social icons directs the user to the respective websites on new tabs.

#### Home

- Clicking it performs the expected action.

#### Wine Details

- The Edit/Delete buttons under the product name work as expected, the first bringing the user to the edit product form with every component working in it.
- The increment/decrement quantity buttons work as expected.
- The Keep Shoppping or Add to Bag buttons perform the designed actions.


#### Our Wine Producers

- The Wine Producers information appear as designed with the working Edit/Delete buttons only if superuser is logged in.
- Clicking on the Producer Image or on the text the user is brought to the Wine Producer Detail Page as expected.

#### Wine Producer Detail Page

- The page is presented as expected, picture of the wine producer in the center, story and data below it.
- The 'Back to Winemakers' button works as expected bringing the user back to the "Our Wine Producers" Page.
- If logged in the user can see a comment form to share their opinion about a Wine Producer or their products, if not logged in the user can read the comments and will see an invitation to login or register if willing to leave a comment.


#### My Profile

- The user can see their personal and delivery data on the left and their order history on the right.
- Every order number is clickable and the user will be redirected to the past confirmation page containing all the details of the order.
- At the bottom of the delivery info's of the user there is an update button which allows the user to eventually change delivery info's.

#### Product Management

- This page can be accessed only by a superuser and it contains a form to add products to the website.
- The form allows the super user to choose the category, add sku number, name, description, price, rating, image url or select an image by the superuser computer.
- At the bottom of the form there are two buttons, 'Add Product' that completes the submission of the product into the store and 'Cancel' that brings back the superuser to the products page.

#### Add Wine Producer

- This page can be accessed only by a superuser and it contains a form to add producers to the website.
- The form allows the super user to choose the Producer Name, a short Heading about them, their Location, the Content that can be about their story or products, image url or select an image by the superuser computer.
- At the bottom of the form there are two buttons, 'Add Producer' that completes the submission of the producer into the store and 'Cancel' that brings back the superuser to the producers page.


#### Authorisation pages

- As these were created with [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html), I tested that they worked as they should. This included that emails were sent if a user registers an account, has forgotten their password or tries to register with a username that already exists. All of these features worked as they should.
- Trying to access the Login/ Register pages when already in session does not work, just as accessing the Logout page when not authorised returns the user to the home page.

[Back to Top](#table-of-contents)

## Bugs
I found one interesting bug that the due to lack of time I cannot fix in this moment.
- When the superuser wants to edit a product everything works, but the form gets a validity error if the superuser tries to remove the picture through the 'remove' checkbox and add a new one at the same time.
    * I tried to debug the code with the help the Mentor and the 'import pdb; pdb.set_trace()' code to see where the code stopped functioning, but the error was something unobvious that needed a big amount of debugging time.

The form works perfectly if the superuser wants to select an image to change it without clicking the checkbox 'Remove'

## Compatibility Testing

### Testing with different Browsers

I tested my site on the following broswers to ensure that all users were getting the same experience. 

* Google Chrome
* Mozilla Firefox
* Edge
* Ecosia

This did not lead to any errors or problems

### Testing With Different Devices

I tested my site on all of the devices which I had access to which were the following.

* Apple Macbook Pro 13"
* Apple Iphone 11
* Apple Ipad
* Apple Ipad Mini
* Samsung Galaxy
* Huawei p30
* HP EliteBook
* Lenovo Thinkpad

This did not lead to any errors or problems.

[Back to Top](#table-of-contents)

To return to previous document, please click [here](https://github.com/Nicola2309/Winefulness/blob/master/README.md).