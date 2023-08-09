"""Streamlit Project
"""
import sqlite3
import streamlit as st
from database import insert, create_employee,create_department,check_tables_exist
import pandas as pd


def employee_page():
    """Employee Page
    """
    st.title("Employee Data Entry")
    empno = st.number_input("Employee Number (Empno)")
    ename = st.text_input("Employee Name (Ename)")
    job = st.text_input("Job")
    deptno = st.number_input("Department Number(Deptno)")
    if st.button("Submit Employee"):
        insert("employee", empno,ename,job,deptno)
        st.success("Employee data submitted successfully!")

def department_page():
    """
    Department Page
    """
    st.title("Department Data Entry")
    deptno = st.number_input("DepartmentNumber (Deptno)")
    dname = st.text_input("Department Name (Dname)")
    loc = st.text_input("Location (loc)")
    if st.button("Submit department"):
        if deptno and dname and loc:
            insert("department",deptno,dname,loc)
            st.success("Department data submitted successfully!")
        else:
            st.error("Please fill in all fields")


def visualize_page():
    """Visualize Page
    """
    st.title("Joined Employee and Department Data")
    connection = sqlite3.connect("data.db")
    join = connection.execute(
        """SELECT employee.empno,employee.ename,department.deptno, department.dname
        from employee left join department on employee.deptno = department.deptno
        """)
    join = join.fetchall()
    connection.close()
    if join:
        joined_data = pd.DataFrame(join,columns=["Empno","Ename","Departno","dname"])
        st.dataframe(joined_data)
    else:
        st.warning("Please submit data for both employees and departments first.")


def main():
    """Main function
    """
    if not check_tables_exist():
        create_employee()
        create_department()
    st.sidebar.title("Navigation")
    page= st.sidebar.radio("Go to",["Employee Data Entry","Department Data Entry","Visualize Data"])
    if page == "Employee Data Entry":
        employee_page()
    elif page == "Department Data Entry":
        department_page()
    else:
        visualize_page()


if __name__ == "__main__":
    main()
