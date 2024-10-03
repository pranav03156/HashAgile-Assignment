# Simulated collections
collections = {}

# Create a new collection
def createCollection(p_collection_name):
    collections[p_collection_name] = []
    print(f"Collection {p_collection_name} created.")

# Index data into the collection, excluding a specific column
def indexData(p_collection_name, p_exclude_column):
    data = [
        {'EmpID': 'E02001', 'Name': 'ravi', 'Department': 'IT', 'Gender': 'Male'},
        {'EmpID': 'E02002', 'Name': 'radha', 'Department': 'HR', 'Gender': 'Female'},
        {'EmpID': 'E02003', 'Name': 'rahul', 'Department': 'Finance', 'Gender': 'Male'},
        {'EmpID': 'E02004', 'Name': 'ramya', 'Department': 'IT', 'Gender': 'Female'}
    ]
    for emp in data:
        emp_filtered = {key: value for key, value in emp.items() if key != p_exclude_column}
        collections[p_collection_name].append(emp_filtered)
    print(f"Data indexed into {p_collection_name}, excluding {p_exclude_column}.")

# Search records by column name and value
def searchByColumn(p_collection_name, p_column_name, p_column_value):
    result = [emp for emp in collections[p_collection_name] if emp.get(p_column_name) == p_column_value]
    print(f"Search results for {p_column_name} = {p_column_value}: {result}")
    return result

# Get the count of employees in a collection
def getEmpCount(p_collection_name):
    count = len(collections[p_collection_name])
    print(f"Employee count in {p_collection_name}: {count}")
    return count

# Delete an employee by ID
def delEmpById(p_collection_name, p_employee_id):
    collections[p_collection_name] = [emp for emp in collections[p_collection_name] if emp.get('EmpID') != p_employee_id]
    print(f"Employee with ID {p_employee_id} deleted from {p_collection_name}.")

# Get department facet (count of employees grouped by department)
def getDepFacet(p_collection_name):
    department_count = {}
    for emp in collections[p_collection_name]:
        department = emp.get('Department', 'Unknown')
        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1
    print(f"Department facet for {p_collection_name}: {department_count}")
    return department_count

# Function Executions
v_nameCollection = 'Hash_pranav'
v_phoneCollection = 'Hash_1234'

createCollection(v_nameCollection)
createCollection(v_phoneCollection)

getEmpCount(v_nameCollection)
indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

delEmpById(v_nameCollection, 'E02003')
getEmpCount(v_nameCollection)

searchByColumn(v_nameCollection, 'Department', 'IT')
searchByColumn(v_nameCollection, 'Gender', 'Male')
searchByColumn(v_phoneCollection, 'Department', 'IT')

getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)
