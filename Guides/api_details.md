# Guide for using social media APIs in features

    All the application services used in various social media platforms should be registered before use, with a developer account.

##  Imgur API

Imgur allows anonymous posting as well as posting as a valid user in Imgur. For this we need to create a application in Imgur to provide uploading facilities for our users. Below are the steps to follow to create and fetch the details about the application.

Steps (only for the developer):
 - Log into your imgur account and then go to this link to [register you application](https://api.imgur.com/oauth2/addclient).
 - Set a valid `Application name`.
 - Set the `Authorization type` as `OAuth 2 authorization without callback URL`
 - Set a proper `Email` for the application.
 - Add a `Description` and `Submit`. This will take you to a page showing the `Client ID` and `Client secret` (this secret code will appear once here, so save it instantly).
 - Save the `Client ID` and `Client secret` in the `auth.ini` file for further use.

However if you forget to save these details, you can got your application settings [here](https://imgur.com/account/settings/apps) and generate a new `Client secret` and update it in the `auth.ini` file.

## Twitter API
In case of Twitter we need to register our App using Twitter's developer account. Steps below describe the whole process.

Steps (only for the developers):
 - Apply for a Twitter developer account with your Twitter account details.
 - Once you are verified by Twitter, go create an application [here](https://developer.twitter.com/en/apps/create). Fill in the necessary details and create the application.
 - Now go to the app's dashboard [here](https://developer.twitter.com/en/apps/) and click on `details`. Navigate to the `Keys and Tokens` tab and copy the `Consumer API Keys`.  
 - Save the API key and API secret key into the `auth.ini` file.
 - Next, set up a development environment for the app. You can do this [here](https://developer.twitter.com/en/account/environments).
 - In the `Account Activity API / Sandbox` header, create `Set up a dev environment` by setting a unique dev environment label and the app (which we created) for which the dev environment will be used.

Now we're ready to go.  

## Facebook Graph API
As of now, Facebook doesnot allow users to make `POST` requests to their own accounts, so this will not be used to post images/text to the users' feeds. Rather we will be using this feature to make posts on a page the user owns.

To publish as a Page from your app, you need:
    - To be an Admin of the posting Page
    - A Page access token with manage_pages and publish_pages permissions

Steps:
#### Creating a page / Using an existing page
 - Log in as user into Facebook and create your page where you want to make posts and fill in the relevant details. If you already have a page, then you can go to the next step.
 - Go to the `About` section in you page to get your `Page ID` and save it in the `auth.ini` file.
