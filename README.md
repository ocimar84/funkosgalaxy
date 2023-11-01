<h1> FUNKOS GALAXY - TOYSHOP </h1>

**View a live version of the site [[here](https://funky-feet.herokuapp.com/)](https://funkogalaxys-9966c091c723.herokuapp.com).**

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
     *  Product Info section
     *  Image
     *  Product name 
     *  SKU 
     *  Total price section 
     *  Quantity function with -/+ buttons to adjust the amount of items that the user wants to buy, in case they want to add more items.

* Basket Total 
  *  This is the total items the user will have in their shopping bag. 

* Delivery  
  * Delivery charge the user will be charged if they don't reach the $80 to get a free delivery.

* Grand Total  
  * The sum of the total of all the items in the bag and delivery charge. This is the total amount the users will be charged in their cards. 

![Product Information](https://github.com/KateEllen/shoe_shop/blob/main/media/product-info.png)

### Features on the Checkout Page 
* Payment form 
  * Follow same structures and form validation. 
  * If the user have ordered before the information will be populated as well.

* Save Information Tickbox 
  * If the user ticks their information will be saved for thenext time.
  * If a field needs to be updated the user can enter the information in the checkout form and it will override the data on the profile page if the user select 'Save this delivery information to my profile'.

* Payment Form Field 
  * This box will require users their card information (card number, month/year, cvc and zip code). To test you must use stripe default test card.

* Adjust Bag Button 
  * Redirect the users back to the Shopping Bag page.

* Complete Order Button 
  * The order for the user is processed. 
  * Generates a confirmation email that is sent to the email address provided in the checkout form.
  ![Email confirmation](https://github.com/KateEllen/shoe_shop/blob/main/media/email.png)

* Card Charge Warning 
* Reminder for the users to tell them that their card will be charged with the stated amount.

![Checkout](https://github.com/KateEllen/shoe_shop/blob/main/media/checkout.png)

### Features on the Subscription feature
** Please note that email from site (Funky Feet) may end up in spam folder **

* The user can subscribe to the page.
* The user have an input box and a button to subscribe.
* The user will be receiving an email in their inbox.

### Features on the Blog
* The site supports a blog which will host product writes ups by famous people or  instagram influencers to help better sell products and increase product awareness.

* CRUD functionality
* View Blog Posts
![Blog](https://github.com/KateEllen/shoe_shop/blob/main/media/blog-list.png)
* Post Title gives information for the user about what the blog post is about.
* Post Link
  * A link to redirect the users back to the Explore page with all the posts available.
* Date and Time Post was Published
  * Date and time stamp and the profile name of the super user who created the post entry.
* Post Content/Body
  * The content of the blog that has been included by the super user.

* Comments
* Comments were included in blogs to help enrich a community environment among frequent visitors and encourage interaction with customers.

  * The comments section shows users responses to the blog.
  * Only registered users can post comments.
  * To post comments to the blogs is through the form directly under this section on the site page.
  * When no comments have been add it will display 'No Comments Yet'.
  * This will include:
    * Comment title
    * Date and time the comment was added
    * Edit/Delete comment
    * Leave a comment

![Blog](https://github.com/KateEllen/shoe_shop/blob/main/media/blog.png)

### Add Post **(superuser only)**
Super user's can create blog posts.
![Add Post](https://github.com/KateEllen/shoe_shop/blob/main/media/add-blog.png)

### Delete Post **(superuser only)**
Super user's can delete their blog posts.
![Delete Post](https://github.com/KateEllen/shoe_shop/blob/main/media/delete-blog.png) 

### Edit Post **(superuser only)**
Super user's can edit their blog posts. 
![Edit Post](https://github.com/KateEllen/shoe_shop/blob/main/media/edit-blog.png)

### Features on the Comments 

* CRUD functionality

* Create comments
![Create Comments](https://github.com/KateEllen/shoe_shop/blob/main/media/create-comment.png)

* Read comments under specific blog post
![Comments](https://github.com/KateEllen/shoe_shop/blob/main/media/comments.png)

* Edit comments you have left
![Edit Comments](https://github.com/KateEllen/shoe_shop/blob/main/media/edit-comment.png)

* Superuser can delete comments you have left
![Delete Comments](https://github.com/KateEllen/shoe_shop/blob/main/media/delete-comment.png)

## Future features 
* Returns
* Product rating
* Live chat
* Images for blog posts

# Testing

The full testing performed can be found [here](./TESTING.md)


# Deployment 
## Heroku Deployment
It's required to have an [AWS](https://aws.amazon.com/s3/) account and a [S3 bucket](https://aws.amazon.com/s3/) to hold all the static files for this project.

1. Open and login to [Heroku](https://id.heroku.com/login)

2. Add all of your Config Vars. Such as keys for AWS, Stripe, Secret Key, Database URL and Email keys. 

3. In your local terminal type "heroku login"

4. Use git to clone your repository's sorce code to your local machine. You can do this by typing "heroku git:clone -a (REPO NAME) then cd (REPO NAME) into yout terminal.

5. Now make some changes to the code you just clined and deploy them to Heorku using Git. You can do this by typing "git add ." followed by "git commit -m 'commit message' " then you will finally type "git push heroku main" to deploy to Heorku. This is all done in your local terminal. 

6. When your app is deployed successfully. Click _Open App_ in to top right hand corner of Heroku to open app in a new tab in the browser.

## Entity Relationship Diagram


## Database Choice
I used postgres as the database because the data is relational and heroku serves this up realitvely easily with no cost.The models used to construct the site are outlined below:

* Post

| DB Key 	         | Data Type 	   |          Purpose          	        | Form Validation                        	|
|--------	         |:---------:	   |:-------------------------:	        |----------------------------------------	|
| pk   	           | ObjectId  	   | unique identifier, auto generated  | None                                   	|
| post_title   	   | CharField     | Display name of blog entry         | Required<br>Min 1 char<br>Max 50 chars 	|
| post_content     | TextField     | Body of blog 	                    | Required                               	|
| post_date_posted | DateTimeField | Date of blog being created 	      | Required                               	|
| post_content     | ForeignKey    | User who created blog 	            | Required                               	|

* Comment

| DB Key              | Data Type     | Purpose                       | Form Validation |
|---------------------|---------------|-------------------------------|-----------------|
| post_id             | ForeignKey    | Unique identifier             | None            |
| comment_title       | CharField     | Display comment title         | Required        |
| comment_content     | TextField     | Body of comment               | Required        |
| comment_date_posted | DateTimeField | Date of comment being created | Required        |
| comment_author      | ForeignKey    | User who created comment      | Required        |

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

- Each page has key words meta data= xxxx as well as a description =xxx Product detail pages include the name of the shoe being sold in the description. Key words are also in content on the home page to re-enforce to search engines that the keywords aren’t being stuffed.

- I used sites like [Zappos](https://www.zappos.com/) and [Office](https://www.office.co.uk/)to deicde what keywords I would need. The keywords I selected are listed below. 

* shoes
* elusive
* unique
* free shipping
* ladies
* girls
* fashion
* womens shoes
* casual shoes
* new shoes
* shoe shop
* sale
* special offer

# E-commerce Business Model
This site is designed for women who love shoes. They can find comfortable and unique styles for any ocassion. The user is also able to subscribe the the newsletter to receive news about the store.

## Facebook Business Page
Below are screenshots of the Funky Feet Facebook page. This page gives users the oppertunity to see extra updates outside of the website. The facebook page can be viewed here [Facebook](https://www.facebook.com/Funky-Feet-100119349392932)

![Facebook1](https://github.com/KateEllen/shoe_shop/blob/main/media/facebook1.png)
![Facebook2](https://github.com/KateEllen/shoe_shop/blob/main/media/facebook2.png)

### Sitemap
![Sitemap](https://github.com/KateEllen/shoe_shop/blob/main/output.png)

# Credits

## Content 
* Products info and pictures - [Office](https://www.office.co.uk/)
* Wireframes - [Balsamiq](https://balsamiq.com/wireframes/)

## Media 
Images - [Office](https://www.office.co.uk/)
Facebook cover photo - [Canva](https://www.canva.com/)
* [Font-Awesome](https://fontawesome.com/)


## Acknowledgements

### I received inspiration for this project from:
* [Boutique Ado](https://github.com/ckz8780/ci-fsf-hello-django/tree/c13b414fd2e87a54b4f2788ceffec55be4ade925)
* [Office](https://www.office.co.uk/)
* [StackOverflow](https://stackoverflow.com/)
* [Coolors](https://coolors.co/)


### I received advice and support from
* [Niall Maher](https://www.linkedin.com/in/nialljoemaher/?originalSubdomain=ie)
* Code Institute [Slack Community](code-institute-room.slack.com)
* My mentor Malia was a huge help in this project as always. She constantly steered me in the right direction and helped me with my many questions on queries. 



