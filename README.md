# Milestone Project 4 - Winefulness

The live project can be seen [here](https://winefulness.herokuapp.com/)


Winefulness is an online e-commerce store to buy the esxcellence of italian wine selected by the Winefulness team, and the user can review the wines or comment the Wine Producer's page they liked the most, as well as knowing more about their stories. The products can be filtered so to find immediately the ones of interest of the user.
The users can have their owm account and save their data to have faster checkouts on the next purchases, the registered users can see and/or edit their personal data and access their shopping history.
If the users won't make an account the ability to puchase remains and they can procede with their order as guests.

## Table of Contents

- [User Experience](#User-Experience)
    - [Main Aims of the Project](#Main-Aims-of-the-Project)
    - [The Strategy Plane](#The-Strategy-Plane)
    - [The Scope Plane](#The-Scope-Plane)
    - [The Structure Plane](#The-Structure-Plane)
    - [The Skeleton Plane](#The-Skeleton-Plane)
    - [The Surface Plane](#The-Surface-Plane)
- [Design](#Design)
    - [Colour Scheme](#Colour-Scheme)
    - [Typography](#Typography)
    - [Imagery](#Imagery)
    - [Icons](#Icons)
- [Information Architecture](#Information-Architecture)
    - [Database](#Database)
    - [Data Schema](#Data-Schema)
- [Technologies Used](#Technologies-Used)
    - [Languages](#Languages)
    - [Tools](#Tools)
- [Features](#Features)
- [Existing Features](#Existing-Features)
- [Features Left to Implement](#Features-left-to-implement)
- [Testing](#Testing)
- [Deployment](#Deployment)
    - [Local deployment](#Local-Deployment) 
    - [Deploying To Heroku](#Deploying-To-Heroku)
- [Credits](#Credits)
    - [Content](#Content)
    - [Images](#Images)
- [Credits](#Credits)
- [Disclaimer](#Disclaimer)
- [Acknowledgements](#Acknowledgements)

## User Experience

### Main Aims of the Project

The main aim of the Winefulness store is to create an online shop with the excellence of the italian wine in which the user can buy, or get informed about it leaving their reviews to the wine they know. The app provides also a section with the Wine Producers collaborating with Winefulness and the users can comment their personal experience with them, if logged in.

It was essential that the site was easy to use and was secure for it's users whilst they were making purchases. These matters were taken into great consideration throughout the development process to enusre that users have a good user experience.

## The Strategy Plane

To begin the building of the website I created a list of user stories that would guide me in considering and developing the design and functionalities in my project so that all the potential users needs would be met.

## User Stories

### Viewing and Navigation

* As a shopper I want to be able to view a list of wines so that I can buy my favourite and try new ones.

* As a shopper I want to be able to view the details of each individual product so I can see the price, description, images of the product and ratings.

* As a shopper I want to be able to view the contents of my shopping bag so that I can update or remove items.

* As a shopper I want to be able to view the grand total in my bag at all times so that I can avoid delivery costs.

### Registration and User Accounts

* As a user I want to be able to register and access my account so that I can keep track of my order history in my profile. 

* As a user I would like to recieve a confirmation email so that I can verify my account.

* As a user I would like to be able to reset my password if I forget it, so that I can regain access to my account. 

* As a user I would like to be able to save my personal and default delivery information so that I don't have to enter it every time I make a purchase. 

* As a user I would like to be able to view the Wine Producers page as a registered user so that I can add comments and share my experience.

* As a user I would like to be able to view the Wine individual page as a registered user so that I can add reviews and share my opinion.

### Sorting and Searching

* As a shopper I want to be able to filter the products so that I can identify the best priced, best rated and by category of my choice. 

* As a shopper I would like to be able to search by name or description so that I can buy the Wine with the taste characteristics I want. 

* As a shopper I would like to see if what I searched is available by seeing the number of results.

### Purchasing and Checkout

* As a shopper I want to be able to see an overview of my order so that I can ensure that I have the correct items and control my spending.

* As a user I want to see efficient form validation when entering my payment details so that I can be sure that my information is safe. 

* As a shopper I would like to see an overview of my order details so that I can ensure that it has been processed properly.

### Admin

* As the store owner I want to be able to add a product so that i can add new products to the store. 

* As the store owner I want to be able to edit and update products so that I can change the prices, images, description and ratings. 

* As the store owner I want to be able to delete products or Wine Producers so that I can remove products and Wine Producers that are no longer available. 

## The Scope Plane

By creating the user stories for my project I considered the features that the site would need to meet the Main Aims of the project and the Users needs.

### Products

* The products page will display all of the available products to the users. From that page they will have the ability to filter the products by price, rating, category and team. 

* Users will be able to click on each product to view the product info page where they will be given a more in depth description and be able to add the product to their cart.

### Accounts

* Users will be able to register/create their own accounts. They will have their own personal profile from where they will be able to save their default delivery information and keep track of their order history. 

* Store owners will have access to parts of the site that regular users will not. This will include pages to add new Products and Wine Producers and the store owners will also have the ability to edit or remove the added content.

### Wine Producers 

* The Wine Producers page will feature a description and story of the excellent companies collaborating with the website. Users will be able to add their own comments under each Winemaker page, as well as edit or delete them. 

### Shopping Bag 

* The Shopping Bag page will provide an overview of the products that the user has added to their Bag and will give them the choice to update the quantity or remove products.

### Checkout 

* The checkout page will feature a stripe payment system which will enable users to purchase products securely. After making a purchase users will be provided with confirmation of their order. 

## The Structure Plane

As I am using Django to create the site, I will structure each feature into it's own respective app. The site will contain fixed nav bar that will enable users to be able to easily navigate in the website.  

The apps that will collectively make up the site are as follows:
* Home
* Products (Store)
* Winemakers
* Profiles
* Bag 
* Checkout
* Reviews

## The Skeleton Plane

With the main features and strucutre now in place for the site, it was now time to begin designing the wireframes to bring my ideas to actual life. To create the wire frames I used a programme called Figma. 

The wireframes can be seen below. 

Design on desktop devices:
![Design for desktop]()

Design on tablet devices:
![Design for tablets]()

Design on mobile devices:
![Design for mobile]()

The entire workspace can be viewed with this [link](https://www.figma.com/file/jc8QKDwQCQ1ecvrTFuogfB/MS's?node-id=0%3A1)


[Back to Top](#table-of-contents)

## The Surface Plane

### Design

- ### Colour Scheme
    - For the colour scheme of my website I took inspiration from the shades of my logo with a red-winish colour. I used the #BE3644 purple colour which as the primary colour throughout the site which can be seen on the Footer, The Free Delivery Threshold and various buttons. The pink colour #FFEAEA was a shade taken from the [ColorSpace](https://mycolor.space/?hex=%23BE3644&sub=1) website palettes which is used as a background for the forms of the User or Owner performing CRUD functions. The dark shade #523838 is used for the title font in each webpage to really make it stand out against white backgrounds, and as a background for the buttons. 

Here are the color palettes:
![Color Scheme]()

- ### Typography
    - The main font that is used throughout my website is Bitter and I have chosed Serif to be used as a fallback should the Bitter font not be imported correctly, and Rokkitt for page title, with Serif as a fallback.

- ### Imagery
    - All of the product images on the site were taken from the Wine Producers websites and Pixabay:
        * [Cantine Adanti](http://www.cantineadanti.com/en/wine/)
        * [Vinicontini](https://www.vinicontini.com/en)
        * [Cantine Bertani](https://www.bertani.net/en)
        * [Marchesi di Barolo](https://marchesibarolo.com/en/)
        * [Pixabay, Bru-nO](https://pixabay.com/photos/grapes-sun-sunbeam-fruit-vines-3550733/)

- ### Icons
    - All of the icons that have been used throughout my website were taken from [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2)

- ### Products and Winemakers content
    - All of the content related to products and Winemakers was taken from their websites.


## Information Architecture

### Database

As part of the Milestone Project 4 it was a requirement that a relational database was used. So the follwing database were used:
* Developent - Throughout the development phase, I used the [Sqlite 3](https://www.sqlite.org/index.html) databse which comes with Django. 
* Deployment - When I deployed my project I switched the database to [PostgresSQL](https://www.postgresql.org/) which is an extension in Heroku.

### Data Models

#### Profile app

##### UserProfile model

| Name             | Database Key         | Field Type           | Validation                                          |
| ---------------- | -------------------- | -------------------- | --------------------------------------------------- |
| User             | user                 | OneToOneField 'User' | on_delete=models.CASCADE                            |
| Full Name        | default_full_name    | models.CharField     | max_length=50, default='', blank=True               |
| Phone Number     | default_phone_number | models.CharField     | max_length=20, default='', blank=True               |
| Street Address 1 | street_address1      | models.CharField     | max_length=80, default='', blank=True               |
| Street Address 2 | street_address2      | models.CharField     | max_length=80, default='', blank=True               |
| Town or City     | default_town_or_city | models.CharField     | max_length=40, default='', blank=True               |
| County           | default_county       | models.CharField     | max_length=80, default='', blank=True               |
| Postcode         | default_postcode     | models.CharField     | max_length=20, default='', blank=True               |
| Country          | default_country      | models.CharField     | blank_label='Select Country', null=True, blank=True |

#### Products app

##### Category model

| Name          | Database Key  | Field Type | Validation                             |
| ------------- | ------------- | ---------- | -------------------------------------- |
| Name          | name          | CharField  | max_length=254                         |
| Friendly Name | friendly_name | CharField  | max_length=254, default='', blank=True |

##### Product model

| Name        | Database Key | Field Type          | Validation                                                    |
| ----------- | ------------ | ------------------- | ------------------------------------------------------------- |
| Category    | category     | models.ForeignKey   | 'Category', default='', blank=True, on_delete=models.SET_NULL |
| Sku         | sku          | models.CharField    | max_length=254, default='', blank=True                        |
| Name        | name         | models.CharField    | max_length=254                                                |
| Price       | price        | models.DecimalField | max_digits=6, decimal_places=2                                |
| Description | description  | models.TextField    |                                                               |
| Rating      | rating       | models.DecimalField | max_digits=6, decimal_places=2, null=True, blank=True         |
| Image       | image        | models.ImageField   | default='', blank=True                                        |
| Image URL   | image_url    | models.URLField     | max_length=1024, default='', blank=True                       |

#### Winemakers app

##### Winemaker model

| Name        | Database Key | Field Type          | Validation                                                    |
| ----------- | ------------ | ------------------- | ------------------------------------------------------------- |
| Producer Name  | producer_name  | models.CharField | max_length=120  |
| Heading  | heading | models.CharField  | max_length=150, null=False, blank=False  |
| Location | location  | model.CharField  | max_length=120, null=False, blank=False  |
| Content  | content | models.TextField  | null=False, blank=False  |
| Image URL   | image_url    | models.URLField     | max_length=1024, default='', blank=True  |
| Image       | image        | models.ImageField   | default='', blank=True |

##### Comments model

| Name        | Database Key | Field Type          | Validation                                                    |
| ----------- | ------------ | ------------------- | ------------------------------------------------------------- |
| Winemakers  | winemakers  | models.ForeignKey  | 'Winemakers', null=True, blank=True, on_delete=models.SET_NULL  |
| User  | user | models.ForeignKey  | User, on_delete=models.SET_NULL,
        null=True, blank=True, default='Anonymous'  |
| Comment  | comment  | models.TextField  |               |
| Date Time  | date_time  | models.DateTimeField  | auto_now_add=True,  |

#### Checkout app

##### Order model

| Name                     | Database Key    | Field Type           | Validation                                                                          |
| ------------------------ | --------------- | -------------------- | ----------------------------------------------------------------------------------- |
| Order Number             | order_number    | models.CharField     | max_length=32, null=False, editable=False                                           |
| User Profile             | user_profile    | models.ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True,related_name='orders' |
| Full Name                | full_name       | models.CharField     | max_length=50, null=False, blank=False                                              |
| Email                    | email           | models.EmailField    | max_length=254, null=False, blank=False                                             |
| Phone Number             | phone_number    | models.CharField     | max_length=20, null=False, blank=False                                              |
| Country                  | country         | CountryField         | blank_label='Select Country \*', null=False, blank=False                            |
| Postcode                 | postcode        | models.CharField     | max_length=20, default='', blank=True                                               |
| Town or City             | town_or_city    | models.CharField     | max_length=40, null=False, blank=False                                              |
| Street Address 1         | street_address1 | models.CharField     | max_length=80, null=False, blank=False                                              |
| Street Address 2         | street_address2 | models.CharField     | max_length=80, null=False, blank=False                                              |
| County                   | county          | models.CharField     | max_length=80, default='', blank=True                                               |
| Date                     | date            | models.DateTimeField | auto_now_add=True                                                                   |
| Promotion Cost           | promotion_cost  | models.DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                               |
| Order Total              | order_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Grand Total              | grand_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Original Basket          | original_basket | models.TextField     | null=False, blank=False, default=''                                                 |
| Stripe Payment Intent ID | stripe_pid      | models.CharField     | max_length=254, null=False, blank=False, default=''                                 |

##### Order Line Item model

| Name            | Database Key   | Field Type          | Validation                                                                         |
| --------------- | -------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Order           | order          | models.ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product         | product        | models.ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE                         |
| Quantity        | quantity       | models.IntegerField | null=False, blank=False, default=0                                                 |
| Line Item Total | lineitem_total | models.DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False            |

#### Reiviews app

##### Product Review

| Name         | Database Key   | Field Type           | Validation                                                                                |
| ------------ | -------------- | -------------------- | ----------------------------------------------------------------------------------------- |
| Product Name | product        | models.ForeignKey    | 'products.Product', null=True, blank=True, on_delete=models.SET_NULL                      |
| User Profile | user_profile   | models.ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_review' |
| Date Created | created_on     | models.DateTimeField | auto_now_add=True                                                                         |
| Rating       | review_rating  | models.CharField     | default="3"                                                                               |
| Title        | review_title   | models.CharField     | max_length=254                                                                            |
| Content      | review_content | models.TextField     | max_length=1000, null=False, blank=False, default=''       



[Back to Top](#table-of-contents)

## Technologies Used

### Languages 

* [HTML5](https://en.wikipedia.org/wiki/HTML5) - HTML5 was used to create the main strucure of the site. 
* [CSS3](https://en.wikipedia.org/wiki/CSS) - CSS3 was used for styling.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - JavaScript was used to provide interactive functionality.
* [Python](https://www.python.org/) - Python was used to interact with the backend.  

### Libraries, frameworks, databases and editors

* [Bootstrap](https://getbootstrap.com/) - Bootstrap was used for various components throughout the site as well as the responsive grid system to ensure the site is fully responsive accross all screen sizes.
* [Font Awesome](https://fontawesome.com/) - This was used to import the icons of the website. 
* [Github](https://github.com/) - This was used to store the repository for my website and host it on Github pages.
* [Git](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) - Throughout the development of my website I made use of Git version control to ensure all changes and additions to my code were added to the repository. 
* [Gitpod](https://gitpod.io/) - This was used to write all code for the website. 
* [JQuery](https://jquery.com/) - I used JQuery to write some of the Javascript code for the website. 
* [Google images](https://www.google.com/imghp?hl=EN) - This was used to find all of the images for the website.
* [SQLite](https://www.sqlite.org/index.html) - This databse was used during development.
* [PostgreSQL](https://www.postgresql.org/) - This is the database used in deployment.
* [Stripe](https://stripe.com/en-gb) - This was used for the payment system in the checkout app.
* [Django](https://www.djangoproject.com/) - This was used as the main framework to develop the site with Python. 

### Tools 

* [Am I Responsive](http://ami.responsivedesign.is/) 
    - This was used to show how my website is responsive across all screen sizes. 
* [Free Online HTML Formatter](https://www.freeformatter.com/html-formatter.html) 
    - This was used to format my HTML code to improve readability. 
* [Free Online CSS Formatter](https://www.freeformatter.com/css-beautifier.html)
    - This was used to format my CSS code to improve readability.
* [Free Online JavaScript Formatter](https://www.freeformatter.com/javascript-beautifier.html) 
    - This was used to format my Javascript code to improve readability.
* [W3C Markup Validation Service](https://validator.w3.org/) 
    - This was a great tool throughout the project to check whether there were any errors in my HTML code (as discussed in more detail in the Testing section).
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - This was a great tool throughout the project to check whether there were any errors in my CSS code (as discussed in more detail in the Testing section).
* [JSHint](https://jshint.com/) 
    - This tool helped me test my JavaScript and jQuery code (explained in more detail in the Testing section). 
* [PEP 8 online](http://pep8online.com/)
    - I used PEP 8 to check that my Python code complied with formatting standards. 
* [Mycolor Space](https://mycolor.space/)
     - I used this website to find the right color shades and palettes to use.

[Back to Top](#table-of-contents)

## **Features**

### Existing Features

#### Navigation Bar

The navbar is in all pages and is composed by the logo on the left, a searchbox to search product names or descriptions, and two buttons on the right, two icons. One is opening a dropdown menu to "Register", "Login" if the user is guest, a link to 'my profile' and 'logout' if the user is logged in and prompting also "Product Management" and "Producer Management" if the user is a super user. The second icon is a link to the shopping bag of the user, showing the current products in it, if any.
Below this 'top nav', is the main navigation of the site. Here the user can click on links opening a dropdown menu, reealing more links to specific areas and categories of the site. The entire nav is fully responsive, with the logo being removed on tablet screen sizes and below, and the main nav moving to a collapsible hamburger menu on the left. The search bar is still present, but is revealed upon clicking a search icon, to keep the site on smaller screens feeling too busy.

#### Footer

The footer, also crossing all pages, consists of an invitation to follow the company on social media and the related icons, under this section the name of the developer is readable.

#### Back to Top Button

A back to top button is displayed to the user at the bottom right of the screen across all pages when the user scrolls down past 200px.

#### Landing Page
A hero image showing a grape in favor of sun light and an invitation to take advantage of the website services with a clear Shop Now button to begin shopping in the products section.

#### Products Page

Products can be viewed in various different ways, either as all products of the entire site, or all products of a chosen category.
Products are presented in responsive cards in a Bootstrap grid system, the product image is a link the product product's detail page, the product name, the price, the category and the rating.
The category in the product card is a clickable badge that performs a search prompting all the products in the products page with the same category clicked on the badge.
A dropdown menu is offered at the top right of the page above the products, to sort the products in different ways. : 'Price (low to high)/(high to low)', 'Name (A-Z)/(Z-A)' and 'Rating (low to high)/(high to low)' and 'Category (A-Z)/(Z-A)'. If the user is a superuser, then edit/delete buttons are offered in each product card for ease of management.

#### Wine Details Page

The products are shown individually in this page, their image on the left and the description on the right.
A quantity selector box is given on this page for the user to input manually or use selector buttons (+/-) to increase/decrease the quantity of the respective product. There are two buttons below this for the user to go back to the all products page to 'Continue Shopping', or 'Add to Bag' in case the user wants to add the product to their bag.

#### Review Option

The user has the ability to review a product.
In the Wine Details page the user can click 'Read Reviews', a button of reviews for that product being displayed with stacked cards of reviews, or a single card saying to the user that there are no reviews for that product and inviting them to review it if the wine was previously purchased.
The 'Add a Review' button will take the user to the add review page containing a form to fill and add the review.

#### Profile Page

This page is accessed by clicking 'My Account' in the dropdown menu of the navbar if logged in.
The user here sees a form with his own personal information, and if the user already bought something on our website the form will contain the delivery information as well and their orders' history on the right.
The user can decide to Update their Information through the button under their form.
The order number is given as the first 5 digits of the unique number, and can be hovered to reveal the entire number, and clicked to take the user to that orders confirmation page.

####  Bag Page

This page shows the user what has been selected and added the the user's bag.
Short information of the product are shown as well as a quantity selector box if the user decides to ammend their order.
There is an update button to use in case the user changed the desired wauntity of the product and there is a remove button in case the user wants to remove the product from the bag.
At the bottom right the user sees the total of their spending, the eventual delivery costs, the grand total and the amount to add in Euro in order to obtain free delivery.
Under the cost related content there are two buttons, one to procede to the checkout page and one to go back to the wineshop.

#### Checkout Page

The checkout page is divided in two columns, to the right the order summary with the products and amounts, to the left an empty form to fill with the user delivery data orcontaining already the user data if the user has already purchased something in the shop.
Below the form there is a checkbox to click if the user desires their information saved, if any, in case of a future purchases.
Finally two buttons are presented, one allows the user to 'Adjust the Bag' and modify its content for another time, and the other button processes the payment and winish overlay takes over the screen with a spinning gif while the operation is processed.

#### Checkout Success Page

This page is accessed when the user completes an order or when an Order Number in the Order History section is by the user in their personal profile page.
In this page the user will have a summary of their order, a confirmation message of the successful purchase and a button to checkout the latest deals which will bring the user in the general products page.
If the user opens the checkout success page through an order in their Order History a message will notify the user that they are seeing a past confirmation.

#### Wine Producers Page

The user can access this page by clicking in the main navigation options.
The user sees the image on the left, the name and the address of the winemaker and the right. The page has a simple and intuitive view to ease the experience to the user. The images or the text can be clicked and bring the user to the winemaker detals page. If the superuser is visiting the page they have the choice to edit or delete the Producer's page through two buttons under the winemaker picture.

#### Wine Producers Detail Page

The page is presented by the Winemaker picture, below it the name and a brief introduction to the Producer. The description contains the story and achievements of the Producer.
It is possible to leave a comment in the producer page. 

#### Comments

The user can share a comment in the Producer's individual page to share impressions of the Producer's story, or personal experiences related to the Producer or the favourite wine of the user made by them.
If the user is logged in the Add a comment section will be automatically shown and the text field will be permanent, if the user is not logged in the textfield section is replaced by a sentence that asks the user to login or register to have the ability to comment the Producer.
The comments are shown below the "Back to Winemakers" button which is under the Producer's description, or under the "Add a Comment" form in case the user is logged in.
The author of the comment is able to edit or remove the comment through two buttons at the bottom.

#### Product Management Page

This page is visible only to a suepruser, it can be accessed by logging in, and finding the link in the dropdown of the 'my account' link of the navbar. The purpose of this page is for the store owner(superuser) to add a product to the site. The page contains a form with all the fields of a product with the required fields market with a ' * '. The 'Selcet Image' button allows the user to upload a picture from their computer.
Below the form a cancel button allows the user to go back to the products page, and a button to submit the product data. If the form is not valid it will be blocked from being submitted and the superuser will be notified of the fields yet to fill in.

#### Add a Wine Producer Page

This page is in the same menu and has the same concept of the Product Management Page, it can be seen just by a superuser and contains a form to add new winemakers that collaborate with the website. It has a cancel button that bring the super user back to the winemakers page and a 'Add Producer' button that performs the submission of the Producer's data.

#### Toasts

All pages can display toast messages to the user, which appear below the navbar on the right side of the screen.
There are four different types of toast messages: success, error, warning and info, their colours will change to reflect each type of message.
The success toast is rendered when a user add a product ti their bag displaying the content of the bag, the total and the amount of money to add in order to have free delivery. at the bottom of the success toast the user can click a button to secure checkout and go to their bag to decide if proceeding with the purchase or going back to the wine shop.

#### Features Left to Implement

The possible features to implement in a e-commerce website can reach fairly large numbers, some of them that i wanted to include are:

* More Purchasing Options
    - The possibility to purchase visits and tasting experiences for the user in the Producer's Winery, as well as boxes of wines with a momnthly subscription or the Producer's merchandise.

* Account login via social media of the user
    - The possibility to login via social media accounts makes everything faster for the user, saving their data in one time and verifying their email automatically since used in the signing up with the chosen social media.

* Edit and Delete functions in Reviews
    - The possibility for the user to edit a review in case of mispelling or deleting it in case of a changed idea.
    - The possibility for the superuser to delete a review if containing bad language or inappropriate content.

[Back to Top](#table-of-contents)

## Testing

The testing of this project can be read [in this separate document](https://github.com/Nicola2309/Winefulness/blob/master/testing.mg)

[Back to Top](#table-of-contents)

## Deployment

### Local deployment

If you would like to work on this project further you can clone it to your local machine using the following steps:

1.  - Install the following in your IDE of choice:
        * Git (for version control)
        * pip (package installer for Python; pip3 was used at the time of production: September 2020)
        * Python3 (the programming language used to produce the backend logic of this project)
    - Make sure that you have created an account with [Stripe](https://stripe.com/en-se), as this is necessary to use the payment feature of the project.
    - Either use an existing [Gmail](https://www.google.com/intl/sv/gmail/about/#) account or create a new one, then sign in and navigate to the [Google Account Security](https://myaccount.google.com/security) page. From here, create two-step authentication by creating an App password for a Django app. Use these values when setting up your email username and password in the steps below.
2. Scroll to the top of this repository and click on the "clone or download button".
3. Decide whether you want to clone the project using HTTPS or an SSH key and do the following:
    * HTTPS: click on the checklist icon to the right of the URL to copy it
    * SSH key: first click on 'Use SSH' then click on the same icon as above
4. Return to your IDE and open a new Terminal window.
5. Change the current working directory to the location where you want the cloned directory.
6. Enter the following command and press 'Enter' to create your local clone:
```
git clone https://github.com/mkthewlis/hotel-eko.git
```
7. Install the required dependencies with the following command:
```
pip3 install -r requirements.txt
```
8. Create an env.py file and add the following, complete with your own values:
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<your value>"    
os.environ["STRIPE_PUBLIC_KEY"] = "<your value>"    
os.environ["STRIPE_SECRET_KEY"] = "<your value>"    
os.environ["STRIPE_WH_SECRET"] = "<your value>" 
os.environ["EMAIL_USER"] = "<your value>"
os.environ["EMAIL_PASS"] = "<your value>"
```
(Note: Django Secret Keys can be generated with websites such as [miniwebtool](https://miniwebtool.com/django-secret-key-generator/).)

9. Add your env.py file to .gitignore to make sure your database information is not viewable to others and to keep your values safe.
10. To set up the Django SQLite3 tables required for this project, use the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
11. With this complete, create a superuser for your project with the following command and follow the instructions in the Terminal (note: this will be necessary to add data to the hotel site once deployed locally):
```
python3 manage.py createsuperuser
```
12. Your cloned version is now ready to run locally with the following command:
```
python3 manage.py runserver
```
13. Once you run your project locally, add '/admin' to the locally deployed project's URL. From here, you can add the service categories and service items to the database. This information can be copied from each individual service's page of the deployed version of the project found on here: [Hotel Eko](https://hotel-eko.herokuapp.com/)

You can find both the source of this information and learn more about the process with the following link: [Cloning a Repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

### Deploying to Heroku 

To deploy the project to Heroku, use the following steps as a continuitation from local deployment outlined above:

1. Begin by making sure that you meet the requirements outlined in Step 1 of Local Deployment as above. In addition, create a [AWS S3 Bucket](https://aws.amazon.com/s3/), as this will be necessary to store static files for deployment.
2. Create an account and sign in to Heroku. From here, created a new app with a unique name that had not already been taken (this project uses 'hotel-eko'). Set the region to the closest to you, eg. 'Europe'.
3. To use the Postgres database for deployment, select 'Heroku Postgres' as a free add-on.
4. With the app created, go to the 'Settings' tab and click on the 'Reveal Config Variables' button. From here, input the following values:

| **Key** | **Value** |
--- | ---
 AWS_ACCESS_KEY_ID | your AWS bucket ID
 AWS_SECRET_ACCESS_KEY | your AWS secret key
 DATABASE_URL | your Heroku Postgres database url
 EMAIL_HOST_PASS | your password to use your gmail account for emails
 EMAIL_HOST_USER | your email address
 SECRET_KEY | secret key used for your Django project
 STRIPE_PUBLIC_KEY | obtained through your Stripe account
 STRIPE_SECRET_KEY | obtained through your Stripe account
 STRIPE_WH_SECRET | obtained through your Stripe account
 USE_AWS | True

5. In Gitpod, create a requirements.txt file with the following command:
```
pip3 freeze --local > requirements.txt
```
6. Create a Procfile with the following content within (making sure that 'Procfile' was written with a capitalized 'P'):
```
echo web: gunicorn hotel_eko.wsgi:application > Procfile
```
7. As with local deployment, set up the Postgres database with the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
8. Follow steps 11 to 13 from local deployment outlined above. 

9. Commit these changes with the following:
```
git add .
```
```
git commit -m "<your commit message here>"
```
10. With these files committed, log in to Heroku using this command and entered your details at the prompt:
```
heroku login -i
```
11. Once logged in, link your Heroku app created above as the remote repository with this command:
```
heroku git:remote -a <your app name here>
```
12. Complete the deployment by pushing the projekt to Heroku:
```
git push heroku master
``` 
13. This completes the process of deploying the project to Heroku. Once deployed, continue to push all changes made to the project to Heroku with the final command listed above.

[Back to Top](#table-of-contents)

## Credits

* All the images come from the Wine producers websites and Pixabay as treated extensively in the imagery section.

* The winemakers app was inspired by the news app of my fellow student [Joshua Thompson](https://github.com/Jthomp1993/ms4-premier-league-store) in his Fourth Milestone project. I used and modified his code to be guided in the construction of the winemakers app.

* The reviews app was inspired by the reviews app in my fellow student [Gregory Lewis](https://github.com/Gregory4321/cooks_finest) Fourth Milestone project. I made an extensive use of his code as well to guide me into the realization of the app.

* Throughout the development of my project I used the [Boutique Ado project](https://github.com/Code-Institute-Solutions/boutique_ado_v1) as a guideline for creating some of the models.

## Disclaimer 

This project is for educational purposes only as part of my final project for Code Institute. Please get in touch with me regarding any copyright issues. 

## Acknowledgements

Thank you to my mentor Seun Owonikoko for her continued support throughout the development of my project. 

Thank you to the following people who helped with support and inspiration:

- My mentor [Seun Owonikoko](https://github.com/seunkoko). As with my earlier three projects, Seun was a great help and support throughout the development process of this project. I've learnt a huge amount working with her and she's now become a great friend! 
- The fantastic support from the *Code Institute* tutors, always willing to go deep into the solutions when debugging code and bringing me back precious knowledge.
- And as always, a big thank you to my family and friends for striking the perfect balance between giving me space and offering their support through long coding sessions.

[Back to Top](#table-of-contents)