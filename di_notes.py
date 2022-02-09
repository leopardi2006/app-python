#Di's notes

#an error when running command:

'pytest tests/01_connect_to_neo4j__test.py'

#The solution to the problem is to run pytest from the following command:

python -m pytest tests/01_connect_to_neo4j__test.py

#Because this will make sure that class create_app from api/init.py is loaded when importing conftest.py.



#python -- begin of  working example
#Create a Person node in the customers database
def create_person_work(tx, name):
    return tx.run("CREATE (p:Person {name: $name}) RETURN p",
        name=name).single()

def create_person(name):
    # Create a Session for the `people` database
    session = driver.session(database="people")

    # Create a node within a write transaction
    record = session.write_transaction(create_person_work,
                                        name=name)

    # Get the `p` value from the first record
    person = record["p"]

    # Close the session
    session.close()

    # Return the property from the node
    return person["name"]
#python -- end of working example


