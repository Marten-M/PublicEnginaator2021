The server for Meter Monitoring System gets its image input via a POST request, that has 2 arguments: user_id, date
user_id is an integer value to specify, which household the image is coming from
date is the time, when the picture was taken
in the POST body should be a raw binary image.

The server will respond with 4 different results:
1) "Image received" - Meter showing was successfully identified and database was updated
2) "Number not found in image" - A number was not identified in the image. No changes were made to database.
3) "Invalid image" - Image is not a correct image or it was formated incorrectly. No changes were made to database
4) "Negative delta value found with user id X" - A negative delta value was found in the database with the given user ID. Database was updated.

The server uses Microsoft Azure Cloud's OCR services.


USAGE
To run the server, execute the following commands in the root folder:
pip3 install -r requirements.txt
python3 main.py [database] [subscription_key] [environment]

database parameters are loaded in from a json file.

To use the server on the TEST environment, a seperate mock API server is required to be running.