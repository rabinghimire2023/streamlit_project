"""Create Database"""
import sqlite3


def create_employee():
    """ Creating the table for employee
    """
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS employee(
                    empno INT PRIMARY KEY,
                    ename VARCHAR(25),
                    job VARCHAR(20),
                    deptno INT,
                    FOREIGN KEY (deptno) REFERENCES department(deptno)
                    )"""
    )
    connection.commit()
    connection.close()


def create_department():
    """Creating the table for department.
    """
    connection = sqlite3.connect("data.db")
    connection.cursor()
    connection.execute(
        """CREATE TABLE department(
                    deptno INT PRIMARY KEY,
                    dname VARCHAR(25),
                    loc VARCHAR(20)
                    )
                    """
    )
    connection.commit()
    connection.close()


def insert(table_name, *args):
    """" Function to insert into the table
    """
    connection = sqlite3.connect("data.db")
    connection.cursor()
    connection.execute(
        f"""
INSERT INTO {table_name} VALUES"""+str(tuple(arg for arg in args))
    )
    connection.commit()
    connection.close()


def drop(table_name):
    """Dropping the table"""
    connection = sqlite3.connect('data.db')
    connection.execute(f"""DROP TABLE {table_name}""")
    
def check_tables_exist():
    """Check if tables exist"""
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employee'")
    employee_table_exists = cursor.fetchone() is not None
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='department'")
    department_table_exists = cursor.fetchone() is not None
    connection.close()
    return employee_table_exists and department_table_exists