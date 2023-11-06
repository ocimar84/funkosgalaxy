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

**Edit Product Management** 
* Exclusive access to this feature is reserved for superusers only (located on the Product Details page) and was verified through the creation of a standard user account.
* Selecting the 'Edit' button directs the user to a form pre-filled with the current information. 
* After making the necessary changes and clicking the 'Edit' button within the form, the updated information is modified in the database, followed by a return to the product's details page.
* The form fields undergo thorough validation testing, assessing both accurate and inaccurate information input with the corresponding expected responses.
* The existing image section displays a thumbnail of the current image with the options to delete it, upload a new image from local files (via the select button), or add an image using the image URL field.
* Opting for the 'Cancel' button returns the user to the details page without implementing any modifications.


**Product Management** 
* Exclusive access to this section is granted only to superusers (located within the My Account dropdown), and this was verified through the testing process involving the creation of a regular user account.
* By clicking the 'Add' button, the entered information is appended to the database before redirecting the user back to the product details page.
* Thorough validation of the form fields was conducted, encompassing both accurate and inaccurate information inputs, with the anticipated responses duly assessed.
* Users have the option to upload a new image from their local files via the select button or include an image using the image URL field.
* Selecting the 'Cancel' button directs the user back to their respective details page without implementing any changes, as anticipated.
* Users receive prompt notifications regarding the successful execution of their actions or the occurrence of any errors.

**User Profile Options** 
* Within the 'My Account' dropdown, when logged in, relevant information is displayed based on the user's status, distinguishing between regular users and superusers. Superusers have access to the Product Management option in addition to the profile and logout links. Testing involved the use of both superuser and nonsuperuser credentials to verify functionality.
* Unregistered users and users not logged in will encounter links for product browsing and registration. This functionality was tested with both superuser and nonsuperuser credentials to ensure consistent behavior.

**User Profile Page** 
* The user's username is prominently displayed at the top, followed by their email address, as intended.
  * The profile page showcases the user's username and email address, alongside a comprehensive table featuring their past orders and current delivery details.
  * Clicking the order numbers within the order history table redirects users to an order confirmation page, providing a comprehensive overview of the selected order. A reminder toast message alerts the user that they are viewing an archived order, with a link to return to the profile page.
  * The current delivery information section comprises editable fields that can be updated by clicking the 'update information' button. If the user is logged in, their information will be automatically populated. The form includes validation to ensure accurate data entry.
  * Access to this page is exclusively granted to logged-in users and was tested using a username that was not logged in.
  * The shopping bag icon in the navigation bar directs the user to their shopping bag, where they can view a detailed list of all the added products, alongside vital information. In the case of an empty bag, users receive a notification in a toast, with a link leading them to the 'All Products' page. Testing confirmed the functionality of both an empty bag and a bag with items, verifying the expected results.

  * Users with items in their bag have the option to adjust item quantities and delete items from their bag. Both the plus and minus buttons update the quantity field, while the update and delete buttons modify the subtotal, bag total, delivery fees, and grand total to reflect the changes made. If all items are removed from the bag, users are directed to a page confirming that their bag is empty, with a link redirecting them to the 'All Products' page.
  * Clicking the 'Continue Shopping' link guides users back to the 'All Products' page.
  If all the items are removed from the bag, users will be directed to a page stating that their bag is empty and a link which takes them to the all products page.
  * Clicking the checkout button takes users to the checkout page where they find an order summary alongside an order form. 

**Order Confirmation Page** 
  * All the form fields are functioning as expected and include validation to ensure accurate data entry.
  * Enabling the 'Save delivery info to profile' option stores the user's delivery details to their profile page, accessible through the 'My Account' dropdown. If the user has previously saved information, the delivery form fields will be automatically populated with the stored data. Testing involved modifying product information to verify this functionality.
  * Clicking the 'View Bag' link allows users to return to their shopping bag.
  * Clicking the checkout button initiates the payment process via Stripe, adding the order to both the admin section of the site and the user's profile page. To verify the functionality, multiple orders were made using different user accounts, and the results were examined.
  * The 'Warning: Your card is about to be charged' message is dynamically updated based on the user's entries in the shopping bag, such as modifying the product quantity. This feature was tested by adjusting the product quantity and observing the message update accordingly.

**Order Confirmation Page** 
* Upon successfully completing the checkout process and making the payment, users will be directed to an order confirmation page that presents a comprehensive summary of their purchase. The page will also include a link guiding them to the Latest Deals page.  
Furthermore, a notification message will be displayed, furnishing users with all the pertinent details pertaining to their transaction.

**Newsletter Subscription:** 
* The newsletter subscription form is accessible on every page.
* Users are required to input a valid email address for subscription.
* A confirmation email is sent to the user to verify their subscription.

** To go back to [README.md](./README.md) **
