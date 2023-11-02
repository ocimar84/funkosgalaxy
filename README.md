<h1> FUNKOS GALAXY - TOYSHOP </h1>

**View a live version of the site [HERE](https://funkogalaxys-9966c091c723.herokuapp.com/).**

This project has been created for educational purposes.

Welcome to the Funko Store! Discover the world of Funko! We offer a wide variety of collectibles, from our famous Pop! Vinyl collection to other Funko products that you'll love. Our items are perfect for die-hard fans of movies, TV shows, video games, and more. Explore our selection and start your collection today!

![repository](https://github.com/ocimar84/funkosgalaxy/assets/79640465/666b594a-7a70-432a-b982-4dad66276497)


___

## Project Goals

The goal of this project is to create E*Commerce store for a toy shop. 
This project is for educational purposes only.

### Importance and Feasibility chart

The features in the table below have been taken from the user stories above. Generic features found in most websites will also be implemented such as nav-bar, footer, obvious website purpose, etc.

| Feature                   | Feasibility (1-5) | Importance (1-5) |
|---------------------------|-------------------|------------------|
| User Signup               | 4                 | 5                |
| Login and Logout          | 4                 | 5                |
| User Profile Page         | 3                 | 4                |
| User Payment Details      | 3                 | 4                |
| Shopping Bag              | 3                 | 4                |
| Search Product            | 4                 | 4                |
| Sort Products             | 3                 | 4                |
| All Products Page         | 4                 | 4                |
| Selected Products on Home | 4                 | 3                |
| Admin - Add Products      | 4                 | 5                |
| Admin - Manage Banners    | 4                 | 4                |
| Admin - Manage Reviews    | 3                 | 3                |
| View Purchased Products   | 4                 | 3                |

In this table:

- Feasibility is rated on a scale of 1 to 5, with 5 being highly feasible. It assesses how easy it is to implement the feature.
- Importance is rated on a scale of 1 to 5, with 5 being highly important. It assesses how crucial the feature is for the project's success.

This table can help prioritize features for the MVP based on their feasibility and importance.

## User Stories

I used the Project page of Github to help keep track of my work. You can find it https://github.com/users/ocimar84/projects/7

### User Goals

* As a User, I want to easily understand the purpose of the site when navigating on it.
* As a User, I want to be able to intuitively navigate the entire site in an easy way.
* As a User, I want to be able to have the same functionalities on different devices (mobile, tablet, and PC).
* As a User, I want to be able to see what items are available for purchase on the site.
* As a User, I want to know the prices of the items.
* As a User, I want to be able to sign up for an account and receive a confirmation email.
* As a User, I want to be able to sign up for the newsletter.


### Registered User goals

* As a Registered User, I want to be able to easily login and logout of my account.
* As a Registered User, I want to be able to easily add and remove items in my shopping bag.
* As a Registered User, I want to be able to easily purchase items on my shopping bag.
* As a **Registered User**, I want to receive a purchase confirmation email.
* As a Registered User, I want to receive a purchase confirmation email.
* As a Registered User, I want to be able to easily update my contact and delivery 


### Site Owner/Superuser goals

* As a Site Owner/Superuser, I want to be able to add new products.
* As a Site Owner/Superuser, I want to be able to edit and delete products.
* As a Site Owner/Superuser, I want to be able to access the admin section of the site to view orders made, the items they contain, and the delivery information.
* As a Site Owner/Superuser, I want to be able to access the admin section of the site to view registered users.


## Site Structure

By focusing on responsive design, consistent navigation, mobile-friendly layouts, clear CTAs, user-based customization, and accessibility features, you can create a user-friendly and accessible website that provides a seamless experience for all visitors, regardless of the device they are using.

### Other links:
* User not logged in:
    * Home
    * Categories
    * Products
    * Contact  
    * Register
    * Login

* Logged in:
    * My Profile
    * Shopping Bag
    * Logout

    * **Only as superuser** 
        * Admin (dropdown)
            * My profile
            * Explore management
            * Product management
            * Check menssenger contact

### Wireframes 

The wireframes of the site can be found in the following links: 

* ![wireframes1](https://github.com/ocimar84/funkosgalaxy/assets/79640465/2580da7c-44b6-4285-af84-3ef8730661ee)
* ![wireframe2](https://github.com/ocimar84/funkosgalaxy/assets/79640465/d92bfce8-4c11-456a-8599-40ff6e0bf053)
* ![wireframe3](https://github.com/ocimar84/funkosgalaxy/assets/79640465/28701def-873d-4124-af20-b4d0f05bac9d)
* ![wireframe4](https://github.com/ocimar84/funkosgalaxy/assets/79640465/7f28bc39-0fc5-4772-a8f7-2996f9142cbb)




The end outcome is somewhat altered as throughout the development phase, the manner in which things were presented was not as intuitive as anticipated.

## Styling

### Colours

The palette of colors for the site is simple, the main colors are black and white. I added a pop of blue to catch the eye. 

![collors](https://github.com/ocimar84/funkosgalaxy/assets/79640465/f7caecb4-95ed-42cb-9408-8b43eac5c947)


# Features

## Existing Features 


* Navbar 
  * Contains the site name, Home, Categories, Products, contact, Shopping bag, all products, boots.
  * My Profile and Logout links. Logged in superusers will also find the Manage Products.
  * The Basket link will take users to their shopping basket page. 


* Funko 
  * A clickable link that brings you back to the homepage.

![navebar](https://github.com/ocimar84/funkosgalaxy/assets/79640465/b482a3d6-6263-403f-b18d-124d86828a05)


### Footer 
  * Subscribe, so the users can sign up for the NewsLetter.
  * About
  * Social
  * Facebook
  * Instragram

![footer](https://github.com/ocimar84/funkosgalaxy/assets/79640465/4d37dc29-4a1e-4e2d-a2b6-c3ca780467ca)


### Features on the Home Page
* Home Image 
  * An video that shows to the user what the site is about.

https://github.com/ocimar84/funkosgalaxy/assets/79640465/54b3d8a0-7246-4818-a3a6-a38e37e46182

### Products
* Produtcs list

https://github.com/ocimar84/funkosgalaxy/assets/79640465/20d87095-3c51-440d-bd45-3d9834d52c4d

### Features on the Sign Up Page 
* Sign Up Form 
  * A very simply form, with instructions on how to register for the site. The text is clear and legible.

    * It includes the following fields:
    *  User Name
    *  Email
    *  Password
    *  Confirm password fields. 

![create acount](https://github.com/ocimar84/funkosgalaxy/assets/79640465/84b90073-c9a5-42e0-8828-b0e064f710d6)

* Sign Up  
  * This button generates and sends a verification email link, to the email address provided. 
 

### Features on the Sign In Page 
* Sign In Form 
  * Another easy Form, with instructions on how to log into the site. 
  * Form control.
  * Includes a username and password field, with a link at the top to direct users who haven't registered to the Sign Up page.
  ![sign In](https://github.com/ocimar84/funkosgalaxy/assets/79640465/427a2898-7e40-42ab-9680-211f300e634a)

* Home Button 
  * Button to return to the home page.

* Sign In Button 
  *  Authenticates the user and return to the home page.

* Unique Email Required. 
  * ![resetpass](https://github.com/ocimar84/funkosgalaxy/assets/79640465/42d0d258-27c2-47c3-a9a4-edd4c157defb)


* Forgotten Password Link 
  * Users can reset their password if they've forgotten it. An email containing a link that directs users to simple instructions on how to reset their password. 
    
    ![email prove](https://github.com/ocimar84/funkosgalaxy/assets/79640465/3f5a6fcd-07d9-4cc7-83c5-427f57708573)

### Features on All Products
* Page Title 
  * Helps the user to make sure they are on the correct page.


* Edit/Delete links 
  * (Superusers Only) Access to the Edit/Delete links allowing them to delete products and directing them to the Edit page to edit the different products.
      
    ![Super user add](https://github.com/ocimar84/funkosgalaxy/assets/79640465/6c98ee96-cf80-49e5-b009-2505287cf343)



### Features on the Products Information Page
* Image 
  * Image of the selected product. 

* Product Information 
  * Name
  * Price
  * Category
  * Description
 
![edit](https://github.com/ocimar84/funkosgalaxy/assets/79640465/79c63770-a54f-4d3a-8599-96f28a913f4c)

### Features on the Profile Page  

* Delivery Information Form 
  
  * There are required fields that need to be filled/updated before being able to save it.
  * The information from this form will automatically be taken from the order form when the user is buying something if they have filled out the checkout form and clicking the tick box 'Save this delivery information to my profile'.

* Form Fields 
  * The input fields are: 
    
    * Street Address 1
    * Town or City
    * State
    * Zip Code
    

  * The form has instructions in how to be completed and also has form validation 

* Update Information Button 
  * If the users want to update their delivery information, fill out the fields in the form above with the required information and click this button to save the updated information to their profile.

* Order History 
   * The most recent order will be displayed at the top.
  
   ![card](https://github.com/ocimar84/funkosgalaxy/assets/79640465/0eba9575-4e44-4a08-9d70-84ef80098715)


### Features on the Shopping Bag
* List of Added Items
  *  The list contains:
     *  Name
     *  Description
     *  Price
     *  Category
     *  Image
     
![add prodts](https://github.com/ocimar84/funkosgalaxy/assets/79640465/04a45965-f9a6-4a40-9262-1619f8f9278e)


### Features on the Checkout Page 
* Payment form 
  * Maintain the same structure and ensure form validation.
  * If the user has placed an order previously, the information will be pre-filled.

* Payment Details Field
  * Users need to input their card information (card number, expiration date, CVC, and ZIP code). To test, use the default Stripe test card.

* Adjust Cart Button 
  * Redirect users back to the Shopping Cart page.

* Place Order Button 
  * Process the user's order.
  * Generate a confirmation email sent to the provided email address in the checkout form.
  
![checkout](https://github.com/ocimar84/funkosgalaxy/assets/79640465/845f593f-5802-491e-8f26-383e75c0c488)

* Payment Notice
* Reminder for users to inform them that their card will be charged the specified amount.
![checkout](https://github.com/ocimar84/funkosgalaxy/assets/79640465/2149329f-cde9-47f4-80cd-1f5d4f85dde4)

### Features on the Subscription feature
** Please be aware that emails from our site (Funkosgalaxy) may end up in the spam folder. **

* Users can subscribe to the page.
* Users have an input box and a button to subscribe.
* Users will receive an email in their inbox.

### Features on the Contact
* Welcome to FunkoGalaxy, your one-stop-shop for all things related to funky and stylish footwear. Our mission is to provide you with the latest shoe designs, ensuring comfort, quality, and a touch of intergalactic flair. Whether you're searching for casual sneakers, elegant heels, or durable boots, we've got you covered.

Join us in stepping up your footwear game and adding a touch of funk to your everyday style.

## Contact Us

Have any questions or feedback? We'd love to hear from you. Get in touch using the details below:

**Address:** 123 Funky Street, Galaxy City, Outer Space

**Email:** galaxyfunkos@gmail.com

Follow us on [Instagram](https://www.instagram.com/funkogalaxy) and [Instagram](https://www.instagram.com/funkosgalaxy/)for the latest updates and special offers.

* CRUD functionality
* View Blog Posts
![contact](https://github.com/ocimar84/funkosgalaxy/assets/79640465/e558843f-2a07-422b-85a5-742319584b5b)

  * The comments section shows users responses to the Contact.
  * To post comments to the blogs is through the form directly under this section on the site page.
  * When no comments have been add it will display 'No Comments Yet'.
  * This will include:
    * Name
    * Email address
    * Message

* Super User ADM.
   
![contactsuperuder](https://github.com/ocimar84/funkosgalaxy/assets/79640465/87bdcc0b-55c9-458b-a426-f54d735b9d43)

    * Date
    * Name
    * Email address
    * Note
    * Action

## Future features 
* Product Rating:
  * Get ready for a more interactive shopping experience with our upcoming product rating feature. Share your thoughts and feedback, and help other customers make informed decisions.
* Images for Blog Posts:
  * Enhance your reading experience with captivating visuals. Look forward to high-quality images accompanying our engaging blog posts, making the content more engaging and visually appealing.
* Live Chat:
  * We're bringing real-time support closer to you with our live chat feature. Have your questions answered instantly by our dedicated support team, making your shopping experience smoother and more convenient.
* Returns:
  * We're implementing a hassle-free returns process to ensure customer satisfaction. Stay tuned for our seamless and customer-friendly return policy.

# Testing

The full testing performed can be found [here](./TESTING.md)


# Deployment 
## Heroku Deployment
It's required to have an [SUPABASE](https://supabase.com/) account and a [GMAIL][(https://mail.google.com/mail/u/0/) to hold all the static files for this project.

1. Open and login to [Heroku](https://id.heroku.com/login)

2. Include all of your Configuration Variables, such as keys for AWS, Stripe, Secret Key, Database URL, and Email keys. 

3. Open your local terminal and enter "heroku login".

4. Clone your repository's source code to your local machine using git. You can do this by running the command "heroku git:clone -a (REPO NAME)", then navigate to the directory using "cd (REPO NAME)" in your terminal.

5. Make the necessary changes to the cloned code and deploy it to Heroku using Git. Run "git add ." to stage your changes, followed by "git commit -m 'commit message'" to commit the changes. Finally, use "git push heroku main" to deploy to Heroku. All these steps are performed within your local terminal.

6. Once your application is successfully deployed, click on "Open App" in the top right-hand corner of Heroku to open the app in a new browser tab.

## Entity Relationship Diagram


## Database Choice
I used postgres as the database because the data is relational and heroku serves this up realitvely easily with no cost.The models used to construct the site are outlined below:

* Product Data Model

| DB Key  | Data Type       | Purpose                              | Form Validation                           | DB Processing                  |
| ------- | --------------- | ------------------------------------ | ---------------------------------------- | ------------------------------ |
| id      | AutoField       | Unique identifier for each product.  | None                                     | CREATE, READ, UPDATE, DELETE  |
| name    | CharField       | Name of the product.                 | <br>Max 100 chars                | CREATE, READ, UPDATE, DELETE  |
| description | TextField   | Detailed description of the product. | None                                    | CREATE, READ, UPDATE, DELETE  |
| price   | DecimalField    | Price of the product.                | Decimal validation                       | CREATE, READ, UPDATE, DELETE  |
| image   | ImageField      | Image representing the product.      | Image format validation                  | CREATE, READ, UPDATE, DELETE  |
| category | ForeignKey to Category | Category to which the product belongs. | Existence validation                | CREATE, READ, UPDATE, DELETE  |
| created_at | DateTimeField | Date and time when the product was added. | None                                 | CREATE, READ                  |
| updated_at | DateTimeField | Date and time of the last product update. | None                             | UPDATE                        |

* Category Data Model

| DB Key  | Data Type       | Purpose                              | Form Validation                           | DB Processing                  |
| ------- | --------------- | ------------------------------------ | ---------------------------------------- | ------------------------------ |
| id      | AutoField       | Unique identifier for each category. | None                                     | CREATE, READ, UPDATE, DELETE  |
| name    | CharField       | Name of the category.                | <br>Max 50 chars                  | CREATE, READ, UPDATE, DELETE  |
| image   | ImageField      | Image representing the category.      | Image format validation                  | CREATE, READ, UPDATE, DELETE  |

* Order

| DB Key          | Data Type     | Purpose                       | Form Validation           |
|-----------------|---------------|-------------------------------|---------------------------|
| order_number    | CharField     | Unique identifier             | None                      |
| user_profile    | ForeignKey    | Display comment title         | Required                  |
| full_name       | CharField     | Users name                    | Required                  |
| email           | EmailField    | Users email                   | Required                  |
| phone_number    | CharField     | Users phone number            | Required                  |
| country         | CountryField  | Users country                 | Required                  |
| postcode        | CharField     | Users postcode                | Required                  |
| town_or_city    | CharField     | Users town or city            | Required                  |
| street_address1 | CharField     | Users street address 1        | Required                  |
| street_address2 | CharField     | Users street address 2        | Not required              |
| county          | CharField     | Users county                  | Required                  |
| date            | DateTimeField | Date of order                 | Required, auto populated  |
| delivery_cost   | DecimalField  | Delivery cost                 | Required, auto populated  |
| order_total     | DecimalField  | Cost of items in bag          | Required, auto populated  |
| grand_total     | DecimalField  | Total cost including delivery | Required, auto populated  |
| original_bag    | TextField     | Bag total                     | Required, auto populated  |
| stripe_pid      | CharField     | Stripe payments               | Required                  |

* Order Line Item

| DB Key         | Data Type    | Purpose           | Form Validation          |
|----------------|--------------|-------------------|--------------------------|
| order          | ForeignKey   | Show order        | Required                 |
| product        | ForeignKey   | Products in order | Required                 |
| product_size   | CharField    | Size of shoe      | Required                 |
| quantity       | IntegerField | Amount selected   | Required                 |
| lineitem_total | DecimalField | total amount      | Required, auto populated |

* Product

| DB Key      | Data Type    | Purpose                     | Form Validation          |
|-------------|--------------|-----------------------------|--------------------------|
| category    | ForeignKey   | Category of product         | Required                 |
| sku         | CharField    | Stock keeping unit          | Required, auto populated |
| name        | CharField    | Name of product             | Required                 |
| description | TextField    | Description of product      | Required                 |
| price       | DecimalField | Price of product            | Required                 |
| image_url   | URLField     | URL image of product        | Not Required             |
| image       | ImageField   | Image of product            | Not Required             |
| has_sizes   | BooleanField | Available sizes for product | Not Required             |

* User profile

| DB Key                  | Data Type     | Purpose                | Form Validation                                 |
|-------------------------|---------------|------------------------|-------------------------------------------------|
| user                    | OneToOneField | Logged in user         | Required                                        |
| default_phone_number    | CharField     | Saved phone number     | Not Required, auto populated if saved by user   |
| default_street_address1 | CharField     | Saved street address 1 | Not Required, auto populated if saved by user   |
| default_street_address2 | CharField     | Saved street address 2 | Not Required, auto populated if saved by user** |
| default_town_or_city    | CharField     | Saved town or city     | Not Required, auto populated if saved by user   |
| default_country         | CountryField  | Saved country          | Not Required, auto populated if saved by user   |
| default_postcode        | CharField     | Saved postcode         | Not Required, auto populated if saved by user   |
| default_county          | CharField     | Saved county           | Not Required, auto populated if saved by user   |

* Subscription

| DB Key    | Data Type  | Purpose        | Form Validation          |
|-----------|------------|----------------|--------------------------|
| email     | EmailField | Logged in user | Required                 |
| timestamp | CharField  | DateTimeField  | Required, auto populated |

## SEO Strategy

- SEO (Search Engine Optimization) is a crucial component of our traffic generation strategy. Here's how we utilize SEO to attract users to our site.

- Keyword Research:** We conduct thorough keyword research to identify high-volume and relevant keywords within the collectibles and pop culture niche. This informs our content creation and optimization efforts. 

# Short-Tail Keywords (General):

* Funko
* Collectibles
* Pop Culture
* Action Figures
* Limited Edition
* Vinyl Figures
* Exclusive Funkos
* Funko Store
* Pop Culture Collectibles
* Funko Pop Shop
* sale
* special offer

# Long-Tail Keywords (Specific and Descriptive):

*  Buy Funko Pop Star Wars Collectibles
*  Rare Limited Edition Funko Pops
*  Best Place to Buy Funko Figures
*  Exclusive Marvel Funko Pops
*  Pop Culture Collectibles Store
*  Funko Pop Batman vs Superman
*  Where to Find Rare Funko Collectibles
*  Disney Funko Pop Collection for Sale
*  Funko Pop Collectors' Club
*  Authentic Funko Pop Store

# Semantic Keywords (Related to Funko Pop):

*   Funko Pop Vinyl Figures
*   Funko Pop Animation Series
*   Funko Pop TV Shows
*   Funko Pop Movie Characters
*   Funko Pop Comic Book Heroes
*   Funko Pop Collectors' Community


# E-commerce Business Model
Discover a universe of collectibles and treasures at Funko's Galaxy, where every corner of popular culture comes alive. Our online emporium is more than just a store – it's an immersive experience that caters to every fandom. From iconic movie and TV characters to beloved superheroes and more, we've curated a stellar collection that will ignite your passion. The user is also able to subscribe the the newsletter to receive news about the store.

## Facebook Business Page
Below are screenshots of the Funko Facebook page. This page gives users the oppertunity to see extra updates outside of the website. The facebook page can be viewed here ![facebook](https://github.com/ocimar84/funkosgalaxy/assets/79640465/5c6c8d2a-a6e8-4af1-9680-183a14a7cb9a)


### Sitemap
![Sitemap](https://github.com/KateEllen/shoe_shop/blob/main/output.png)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Credits

## Content 
* Products info and pictures - [Funko](https://funko.com/)
* Wireframes - [[FunkoEurope](https://balsamiq.com/wireframes/)

## Media 
Images - [FunkoEurope](https://funkoeurope.com/)
Facebook cover photo - [Canva](https://www.canva.com/)
* [Font-Awesome](https://fontawesome.com/)


## Acknowledgements

### I received inspiration for this project from:
* [Boutique Ado](https://github.com/ckz8780/ci-fsf-hello-django/tree/c13b414fd2e87a54b4f2788ceffec55be4ade925)
* [StackOverflow](https://stackoverflow.com/)
* [FunkosEurope](https://funkoeurope.com/)
* [EMP](https://www.emp.ie/fun-lifestyle/homeware/figures/funko-pops/)
  


### I received advice and support from
* Blogs and Tutorials: Various blogs and online tutorials contributed significantly to my knowledge and problem-solving skills. I'd like to acknowledge the authors of these resources for sharing their expertise.
* Code Institute [Slack Community](code-institute-room.slack.com)
* Mentors: A special thanks to the mentors Malia and Vitor who provided valuable insights and assistance throughout the development process. Your guidance was instrumental in overcoming challenges and improving the quality of the project.
* Friends and Peers: Last but not least, I'd like to thank my friends and peers who provided feedback, suggestions, and encouragement throughout this journey. Your support was invaluable.
* YouTube Tutorials: Several YouTube tutorials on web development topics were instrumental in enhancing specific features of the project. I'm thankful for the creators of these tutorials.
* Blogs and Tutorials: Various blogs and online tutorials contributed significantly to my knowledge and problem-solving skills. I'd like to acknowledge the authors of these resources for sharing their expertise.



