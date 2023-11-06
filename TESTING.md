# Testing

[View the live project here.](https://funkogalaxys-9966c091c723.herokuapp.com/)


## Code Validation

## Validation Services

To validate the code the following **validation services** and **linters** were used to check the code:

* W3C Markup Validator
    Checks the markup validity of Web documents in HTML, XHTML, SMIL, MathML, among others.

* W3C CSS Validation Service
    Checks the validity of cascading style sheets (css) and (X)HTML documents with style sheets.

![CSS](https://github.com/ocimar84/funkosgalaxy/assets/79640465/e441df5b-f5ef-436a-b88e-34217aea3e23)


* PEP8 Online validation
    This error I couldn't do it because it was a long line, even though I tried several models and none of them shortened.

![PEP8](https://github.com/ocimar84/funkosgalaxy/assets/79640465/81a1e2fd-ef8d-47d2-97b4-8604b315decf)

* JS validator
![js validation](https://github.com/ocimar84/funkosgalaxy/assets/79640465/d1d84d41-7d79-4ab6-8001-c7080d26df90)


* [Chrome DevTools Lighthouse]

![Lighthouse](https://github.com/ocimar84/funkosgalaxy/assets/79640465/566d588d-7e6c-45f4-9c88-d0ae5de1c708)

## Manual Testing

### Devices and browsers

**Browser versions used in testing:**

* Version 118.0.5993.118 (Official Build) (64-bit)
* Safari Version 17.1 
* Firefox Version 119.0 (64-bit)

**Tested on the following devices using the Google Chrome Developer tools:**

* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iphone 11
* iphone 12
* iphone 13
* iphone 14
* iPad
* iPad Pr
* Surface Duo
* Galaxy Fold

**Tested on the following devices using the Firefox Developer tools:**

* Galaxy S9/S9+ Android 7.0
* iPad
* iPhone 6/7/8 iOS 11
* iPhone 6/7/8 plus iOS 11
* iPhone x/XS iOS 12
* Kindle Fire HDX Linux

**Tested on the following physical devices:**

* iPhone 11
* iPhone 12
* iPhone 13
* iphone 13 pro max 


### Features tested

**Home Page:**
 * Clicking 'home, categories, products and contact' log brings you to the homepage. 
 * Clicking menu options directs you to the appropriate category.
    - All funkos provide a dropdown menu, allowing the selection of each individual category, which displays the correct category.
    - Heels provide a dropdown menu, allowing the selection of each individual category, which displays the correct category.
    - Flats provide a dropdown menu, allowing the selection of each individual category, which displays the correct category.
    - Boots provide a dropdown menu, allowing the selection of each individual category, which displays the correct category.
    - Clicking the 'My Account' icon option directs you to your profile and gives you the option to sign out.

 * Clicking 'My Account' icon option brings you to your profile and give you the option to sign out.
 * Clicking 'Shopping Bag' icon brings you to your shopping bag.

**Product Page:**   

**Product Page:** 
 * Just select the product you prefer, products are listed with photo and price.
 * Clicking an item on the product page will navigate you to the selected item's specific page.

**Register Page:** 
 * The form fields undergo validation, and they were tested using both accurate and inaccurate inputs, resulting in the expected outputs.
 * Clicking the "back to login" links redirects the user to the login page.
 * Clicking the register button will initiate an email to be sent to the provided email address, requesting confirmation of the email. Once verified, the user will be redirected to the main page.

**All products - Dropdown** 
* All the links in the dropdown menu direct the user to the different available categories on the page.
* The user's input results are displayed below, showing only the products listed in that category.
* The page shows an item count so that users can see how many products are available in that category, alongside a link that takes them to the all products page. The item count was tested by adding and removing products from the database and updates accordingly.
* The "sort by" dropdown is accessible for users to organize the products in the selected category, and it was tested by selecting all the available sorting methods, yielding the expected results.
* Clicking the product image will take the user to the specific product details page.

**Product Detail page** 
* Show all the details of the selected product.
* A category link leads users to the product's category, where they can explore other items within the same category, if available in the database. This functionality was thoroughly tested across various scenarios.
* Users can adjust the quantity of the selected product using the minus and plus icons before adding it to the shopping bag. This feature underwent extensive testing for each product, ensuring that the designated quantity is accurately added to the user's shopping bag.
* Superusers have access to the Edit and Delete buttons, which are not visible to regular users. This was verified through the creation of a standard user account.
* A "Continue Shopping" link redirects users to the "All Products" page while preserving the contents of their current shopping bag.
* The "Add to Bag" button places the specified quantity of the chosen product into the user's shopping bag. Users receive prompt notifications for successful additions or any encountered errors.

**Edit Product Button** 
* Only super users have access to this button (found on Product Details page), and it was tested by creating a regular user.
* Clicking the 'Edit' buttons take the user to a form with the fields filled out with the current information and the 'Edit' button in the forms changes the information in the database, before taking the user back to that products details page.
* The form fields have validation and were tested using correct and incorrect information with the expected responses given.
* The current image section shows a thumbnail of the current image with the option to remove it, select a new image from the files (select button) or add an image using the image url field.
* Clicking the 'Cancel' button will take the user back to the details page without making any changes.
* Users are notified of the successor if there is any errors so the request couldn't be processed.

**Product Management** 
* Only super users have access to this page (found in My Account dropdown), and it was tested by creating a regular user.
* Clicking the 'Add' buttons add the entered information to the database before taking the user back to the products details page.
* The form fields have validation, tested using correct and incorrect information with the expected responses given.
* Users can select a new image from the computers files via the select button or add an image using the image url field.
* Clicking the 'Cancel' buttons take the user back to their respective details page without making changes as expected.
* Users are notified of the success of this or if there's been an error.

**My Account Dropdown** 
* In 'My Account' dropdown, when logged in, shows relevant information depending on if it a superuser or not, with superusers getting the Product Management option, alongside the profile and logout links. Tested both using superuser and nonsuperuser credentials.
* Unregistered users and users not logged in will see product and register links. Tested using superuser and nonsuperuser credentials.

**Profile Page** 
* The users username appears at the top as programmed with their email displayed underneath.
  * The profile page shows the users username and email address with a table containing their previous orders and current delivery information.
  * Clicking the order numbers, in the order history table, redirects users to order confirmation page with all the information available in that order. A reminder toast message appears to remind the user they are viewing an old order 
  is also displayed, with a link which takes users back to the profile page.
  * The current delivery information section has different fields that can be edited with updated information after clicking the update information button.
  If the user is logged in their information will automatically populate.
  The form has validation.
  * This page is only accessible if the user is logged in, it was tested using a username that wasn't logged in.

* The Bag icon in the navbar takes the user to their shopping bag. There they will find a list of all the products added to it, as well as important information. If the bag is empty
  users will receive a notification in a toast, alongside a link which directs them to the all products page. This was tested by clicking the empty bag and clicking the bag with items inside and viewing the reults, which were as stated.
  * Users who have items in their bag will be faced with the option to update item amounts and delete items from their bag. Both the plus and minus buttons update the number in the box field, and the update and delete buttons update the subtotal, bag total, delivery and grand total to reflect the changes.
  If all the items are removed from the bag, users will be directed to a page stating that their bag is empty and a link which takes them to the all products page.
  * Clicking the continue shopping link directs users to the all products page.
  * Clicking the checkout button takes users to the checkout page where they find an order summary alongside an order form. 

**Checkout Page** 
  * All form fields work as intended and have form validation in case the user doesn't fill the information in the correct way.
  * Clicking the 'Save delivery info to profile' box, saves just the delivery sections users details to their profile page, which can be accessed via the 'My Account' dropdown. If the user has information saved to their profile, the delivery form fields will be automatically generated with the stored information. This was tested by changing the product information.
  * Clicking the bag link takes users back to their bag.
  * Clicking the checkout button generates the payment through stripe, adding the order to the admin section of the site and the users profile page. This was tested using multiple users and making orders then viewing the reults.
  * The 'warning card is about to be debited' message updates with the bag user entries such as updating the amount of product and was tested by doing so.

**Confirmation page** 
* When users have checked out and paid, they are directed to a confirmation page with a copy of their order and a link which directs the to the Latest Deals page. 
It will also display a toast message with all the details. 

**Subscription:** 
* The subscription form is available in all the pages. 
* It asks the user to input a correct email.
* User receives an email to confirm their subscription.

** To go back to [README.md](./README.md) **
