# Basic Data Management Application
## Goal:
Create an application which will act as a DBMS for a particular application with basic operation such as create, update, delete, and select operations. Provide an interface for the user with the following options:
1. Create Contact
2. Edit Contact
3. Search Contact
4. Delete Contact
5. Exit
> The application will keep track of the Contact through a series of text files. The rows inside the text files will be associated with a particular record.
* Contact
  * first name
  * last name
  * gender
* Address
  * address 1
  * address 2
  * apt
  * city
  * state
  * country
* Phone
  * type
  * number
## Approach:
Utilize tkinter to create the GUI and CSVs for ease of reading/writing data to files.
## Credits
Import [pycountry](https://pypi.org/project/pycountry/) for country selection.
