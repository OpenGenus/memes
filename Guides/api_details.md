# Guide for using social media APIs in features

All the application services used in various social media platforms should be registered before use, with a developer account.

##  Imgur API

Imgur allows anonymous posting as well as posting as a valid user in Imgur. For this we need to create a application in Imgur to provide uploading facilities for our users. Below are the steps to follow to create and fetch the details about the application.

Steps (only for the developer):
---
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
---
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

Steps (for individual user):
---
This feature will only work with the user's own application and has to get all the details manually. Once the app is reviewed, the live app will fetch all the details (details regarding the live app are mentioned in the next steps)

#### Creating a page / Using an existing page
 - Log in as user into Facebook and create your page where you want to make posts and fill in the relevant details. If you already have a page, then you can go to the next step.
 - Go to the `About` section in you page to get your `Page ID` and save it in the `auth.ini` file.

#### Register an app to post against you
 - If you are not signed for Facebook's developer program, sign in [here](https://developer.facebook.com) with your Facebook login details and create an app [here](https://developers.facebook.com/apps/) if you're already registered, else you can register yourself then proceed to create an app.
 - Go to `Facebook Apps dashboard` -> Click `Add a New App` -> Choose platform `WWW` -> Choose a new name for your app -> Click `Create New Facebook App ID` -> Create a New App ID -> Choose `Category` -> Click `Create App ID` again.
 - Go back to Apps dashboard -> Select the new app -> `Settings` -> `Basic` -> Enter Contact Email. This is required to take your app out of the sandbox.
 - Make a note of the `App ID` and `App Secret`.

#### Getting an access_token_key
 - Go to the Graph API Explorer in `Tools` dropdown and in `Applications` dropdown select the app we just created. Click on `Get Token` -> `Get User Access Token` button and select the permissions `manage_pages` and `publish_pages` to make post as the page. After this click on the `Get access token` button.
 - You can copy this access token to get a long-lived user access token by making an request on the URL:
 > https://graph.facebook.com/oauth/access_token?client_id={APP_ID}&client_secret={APP_SECRET}&grant_type=fb_exchange_token&fb_exchange_token={EXISTING_ACCESS_TOKEN}

Steps (for live release of this feature)
---
For this the application to work for any user/public we need to put the app under `App review`. Follow the guideline below:
 - Go to the `App Review` tab in the dashboard of the app we just created. Select `Permissions and Features` tab.
 - From the features select `manage_pages` and `publish_pages`. Likewise click on `Continue` button on each feature we want, fill in the details each feature requests for and click on `Save`.
 - After completing the review request click the `Submit and review button`.
 - Then you can bring the app live in the dashboard.
