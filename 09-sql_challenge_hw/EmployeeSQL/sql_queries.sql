--1-List the following details of each employee: employee number, last name, first name, sex, and salary.
select
e.emp_no,
e.last_name,
e.first_name,
e.sex,
s.salary
from
employees e
join salaries s on e.emp_no = s.emp_no;

--2-List first name, last name, and hire date for employees who were hired in 1986
select
	emp_no,
	last_name,
	first_name,
	hire_date
from
	employees
where 
	hire_date >= '1986/01/01'
	AND hire_date <= '1986/12/31'
;

--3)List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
select
dm.dept_no,
d.dept_name, 
e.emp_no,
e.last_name,
e.first_name
from
employees e
join dept_manager dm on e.emp_no = dm.emp_no
join departments d on dm.dept_no = d.dept_no;

--4)List the department of each employee with the following information: employee number, last name, first name, and department name.
select
e.emp_no,
e.last_name,
e.first_name,
d.dept_name
from
employees e
join dept_emp de on e.emp_no = de.emp_no
join departments d on de.dept_no = d.dept_no;

--5) List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

select
	first_name,
	last_name,
	sex
from
	employees
where
	first_name = 'Hercules'
	AND last_name like 'B%';

--6) List all employees in the Sales department, including their employee number, last name, first name, and department name.
select
e.emp_no,
e.last_name,
e.first_name,
d.dept_name
from
employees e
join dept_emp de on e.emp_no = de.emp_no
join departments d on de.dept_no = d.dept_no
where
d.dept_name = 'Sales';

--*7) List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from
	employees e
join 
	dept_emp de on e.emp_no = de.emp_no
join 
	departments d on de.dept_no = d.dept_no
where
	d.dept_name = 'Sales' 
	OR d.dept_name = 'Development';

--8) In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select
	last_name,
	count(*)
from
	employees 
group by
	last_name
order by
	last_name desc;
	


