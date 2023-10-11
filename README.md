# AirBNB Clone - The Console

The first step towards building your first full web application: __the AirBnB clone__. This project guides you through the task of creating a command line interface, creating a instance that generates an id along with datetime of when it was created and creating a way to serialize and deserialize.

## General Information

- __Console__

    The console is the entry point for the command interface.

	- Functions for manipulating data through the command line interface.

	    - `do_create`: Creates a new instance of of the provided class (examples: Basemodel, City, State, ect) saves it the JSON file and prints the id.

		- `do_destroy`: Deletes an instance based on the class name and id and save the changes to the JSON file.

		- `do_show`: Prints the string representation of an instance based on the class name and id.

		- `do_all`: Prints all string representation of all instances based or not on the class name.

		- `do_update`: Updates an instance based on the class name and id by adding or updating attribute then saves the changes to the JSON file.


- __FileStorage__

    These are the attributes and methods for serializing Python objects to a JSON file and deserializing those JSON strings into Python Objects

    `__file_path`: path to the JSON file.

	`__objects`: dictionary that is empty but will store all objects by classname.id.

	`all(self)`: returns the dictionary `__objects`.

	`new(self, obj)`: creates a new object in the `__object` dictionary.

	`save(self)`: serializes `__objects` to the JSON file.

	`reload(self)`: deserializes the JSON file to `__objects`.


- __BaseModel__

    Methods and Attributes that are common in all class listed in Additional Class.

	- `__init__`: Creates the BaseModel instance.

	    - `id`: generates a unique id using uuid.uuid4.

		- `created_at`: assign with the current datetime when an instance is created.

		- `updated_at`: assign with the current datetime when an instance is created and it will be updated every time you change your object.

	- `__str__`: string representation of the object.

	- `save`: updates the public instance attribute `updated_at` with the current datetime.

	- `to_dict`: returns a dictionary containing all keys/values of `__dict__` of the instance.


- __Additional Classes__
    

	- `Amenity`

	    - `name`

	- `City`

	    - `state_id`

		- `name`

	- `Place`

	    - `city_id`

		- `user_id`

		- `name`

		- `description`

		- `number_rooms`

		- `number_bathrooms`

		- `max_guest`

		- `price_by_night`

		- `latitude`

		- `longitude`

		- `amenity_ids`

	- `Review`

	    - `place_id`

		- `user_id`

		- `text`

	- `State`

	    - `name`

	- `User`

	    - `email`

		- `password`

		- `first_name`

		- `last_name`

## Available Commands

- __Opening Command Line Interface__

    ```
    $ ./console.py
    (hbnb)
    ```

- __Basic Commands__

    ```
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb) 
    (hbnb) help quit
    Quit command to exit the program

    (hbnb) 
    (hbnb) 
    (hbnb) quit 
    ```

- __Additional Commands__

    ```
	(hbnb) all BaseModel
	["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
	(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
	[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
	(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
	```

## Test

All files, classes, and functions are tested with unit tests.

They were preformed by using this command `python3 -m unittest discover tests`

## Authors
Connor True <6676@holbertonstudents.com>

Lee West <6683@holbertonstudents.com>
