"""Streamlit Project
"""
import streamlit as st
import pandas as pd
employee_data = pd.DataFrame(columns=['Empno', 'Ename', 'Job', 'Deptno'])
department_data = pd.DataFrame(columns=['Deptno', 'Dname', 'Loc'])
def employee_page():
    """Employee Page
    """
    st.title("Employee Data Entry")
    empno = st.text_input("Employee Number (Empno)")
    ename = st.text_input("Employee Name (Ename)")
    job = st.text_input("Job")
    deptno = st.text_input("Department Number(Deptno)")
    if st.button("Submit Employee"):
        if empno and ename and job and deptno:
            employee_data.loc[len(employee_data)] = [empno,ename, job, deptno]
            st.success("Employee data submitted successfully!")
        else:
            st.error("Please fill in all fields.")
def department_page():
    """
    Department Page
    """
    st.title("Department Data Entry")
    deptno = st.text_input("DepartmentNumber (Deptno)")
    dname = st.text_input("Department Name (Dname)")
    loca = st.text_input("Location (loc)")
    if st.button("Submit department"):
        if deptno and dname and loca:
            department_data.loc[len(department_data)] =[deptno, dname, loca]
            st.success("Department data submitted successfully!")
        else:
            st.error("Please fill in all fields")
def visualize_page():
    """Visualize Page
    """
    st.title("Joined Employee and Department Data")
    if not employee_data.empty and not department_data.empty:
        joined_data = employee_data.merge(department_data, on='Deptno', how='left')
        st.dataframe(joined_data)
    else:
        st.warning("Please submit data for both employees and departments first.")
def main():
    """Main function
    """
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
