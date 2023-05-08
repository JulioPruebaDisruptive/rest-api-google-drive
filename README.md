#  rest-api-google-drive

This api helps us to list the files located in a given folder in the user's drive. And this is achieved once the user is authenticated via oauth2, so, we make sure that the user has a google account.


![image](https://user-images.githubusercontent.com/132952622/236958860-b169429e-4009-4675-a0d9-1b7ef530528a.png)


# How install this project?

First you must clone this repository, open your terminal and run this command


	Git Clone https://github.com/JulioPruebaDisruptive/rest-api-google-drive.git|

You can now view the project in your editor code

![image](https://user-images.githubusercontent.com/132952622/236958942-7d54d80a-9097-47e8-b896-3687fb446ea9.png)


Then you need to  create a virtual enviroment

    python3 -m venv env

run next comand to activate the virtual enviroment

    source env/bin/activate


At this point, it is necessary to install the requirements.txt

    python3 install -r requirements.txt

#  Run project

You need to be in the path where the file 'run.py' and run is located:

    python3 -m run


Go to the address given by the terminal or to 127.0.0.1.1:5000


![image](https://user-images.githubusercontent.com/132952622/236958805-316a777c-a192-44f9-a4b4-ff79c53796d7.png)



You will see the following screen

![image](https://user-images.githubusercontent.com/132952622/236959136-ece94b52-3775-42ee-862b-d4ec23c57750.png)


Press login and you will be redirected to google authentication

Select or enter your credentials

![image](https://user-images.githubusercontent.com/132952622/236959221-344eb44c-719d-4e5c-98bc-f4b4e6ea97a7.png)




It is necessary that the user authorizes the permissions that allow interaction with google drive.

![image](https://user-images.githubusercontent.com/132952622/236959314-e35edd39-df9a-4744-8565-301569de9634.png)

Finally the api will list the files in a folder, in this case "folder 1", which is the folder that was used to create the api.


#Project structure


The app.py file has the paths for login, logout, calback.
It is where the rest technology is implemented.

![image](https://user-images.githubusercontent.com/132952622/236959475-b78a65aa-0c94-4b5d-954e-700aa660226c.png)



The auth.py file is where the class that compiles the functions that initiate the google authentication flow, those that request and refresh the credentials and those that obtain the token for access.

![image](https://user-images.githubusercontent.com/132952622/236959512-d8566247-4eef-41ee-960f-8d81ba5959f4.png)


The config.py file is where the flask app is initialized and the configuration to be able to make flows with the google apis.

![image](https://user-images.githubusercontent.com/132952622/236959533-6cd279f4-9fd9-4a4e-a696-713898d38867.png)



The file client_secret.json is essential to achieve this api and is provided by google cloud services when we register the web service on their platform.
From this file we get the client id and the secret client.

![image](https://user-images.githubusercontent.com/132952622/236959554-40b4e825-ce86-4646-a10b-1a44df22717e.png)


The decorators.py and helpers.py files have functions that will help us to de-task the routes created in the app.py file. This makes the code more efficient and scalable.

![image](https://user-images.githubusercontent.com/132952622/236959566-008beeac-1c2f-4f2d-91d2-0d7a400ed084.png)



Finally, it is important to know that when executing the command python3 -m run, the code of the run file will be executed, in which the following instructions are found:

	context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
	context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

![image](https://user-images.githubusercontent.com/132952622/236959609-e3be749b-8c29-4d57-be02-dba1d3abfcae.png)


The following instructions will generate the cert.perm and key.perm files, which cause the server to use "https:" allowing most current browsers to access the ip that the flask server generates.

![image](https://user-images.githubusercontent.com/132952622/236959647-be893557-167b-42ed-b690-c21c1789321e.png)
![image](https://user-images.githubusercontent.com/132952622/236959669-1d74c6d0-7b78-46ea-885f-139856af7002.png)
