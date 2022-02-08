#Di's notes

#an error when running command:

'pytest tests/01_connect_to_neo4j__test.py'

#The solution to the problem is to run pytest from the following command:

python -m pytest tests/01_connect_to_neo4j__test.py

#Because this will make sure that class create_app from api/init.py is loaded when importing conftest.py.

