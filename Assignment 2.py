# Fill in your details
# ASSIGNMENT 3 




hours = []
def add_employee_data(employee_id, hourly_wage, hours_worked):
    # hours = []
    # 1. Check if the employee_id is an integer, hourly_wage is a number, and hours_worked is a list
    if not isinstance(employee_id, int):
        print("error: employee_id must be an integer.")
        return 
    
    if not isinstance(hourly_wage, (int, float)):
        print("error: hourly_wage must be a number (either int or float).")
        return 
    
    if not isinstance(hours_worked, list):
        print("error: hours_worked must be a list.")
        return 
    
    # 2.check if the length of hours_worked is 12
    if len(hours_worked) != 12:
        print("error: hours_worked must have 12 values, one for each month.")
        return  
    
    # 3.check if all values in hours_worked are numbers (either int or float)
    if not all(isinstance(h, (int, float)) for h in hours_worked):
        print("error: All values in hours_worked must be numbers.")
        return  
    
    #if all checks pass add the employee data to the list
    hours.append([employee_id, hourly_wage, hours_worked])
    print(f"Employee {employee_id} added successfully!")


# b. Calculate average monthly salary
def calculate_average_monthly_salary():
    """
    Calculate and print the average monthly salary for each employee .
    Returns:
        float: The overall average monthly salary across all employees .
    """
    #check if there is no employee data available
    if not hours:
        print("No employee data available.")
        return 0.0
    
    total_salary = 0
    total_employees = len(hours)
    
    #loop through the list of employees and calculate the average monthly salary for each employee
    for employee in hours:
        employee_id, hourly_wage, hours_worked = employee
        yearly_salary = sum(hours_worked) * hourly_wage
        average_monthly_salary = yearly_salary / 12
        total_salary += average_monthly_salary
        
        print(f"employee ID : {employee_id}")
        print(f"average Monthly Salary : {average_monthly_salary:.2f}\n")
        
    #calculate the overall average monthly salary across all employees
    overall_average = total_salary / total_employees
    print(f"overall average monthly salary is : {overall_average:.2f}")
    
    return overall_average
    

# c. Identify the highest expenditure month
def find_highest_expenditure_month():
    """
    Find the month with the highest total salary expenditure.
    Returns:
        int: Month number with the highest expenditure.
    """
    if not hours:
        print("No employee data available.")
        return -1  # Return -1 if no data is available
    
    # List to store total salary for each month (index 0 = January, index 11 = December)
    total_monthly_expenditure = [0] * 12
    
    #loop through the list of employees and calculate the total salary expenditure for each month
    for employee in hours:
        employee_id = employee[0]  
        hourly_wage = employee[1] 
        hours_worked = employee[2] 
        
        #calculate the total salary expenditure for each month
        for month in range(12):
            total_monthly_expenditure[month] += hourly_wage * hours_worked[month]
    
  
    #store the highest expenditure and the month
    highest_month = 0
    max_expenditure = total_monthly_expenditure[0]
    
    #compare the total expenditure for each month
    for month in range(1, 12):
        if total_monthly_expenditure[month] > max_expenditure:
            max_expenditure = total_monthly_expenditure[month]
            highest_month = month
    
    print(f"Month with the highest expenditure: {highest_month + 1}")  # +1  added to make the month 1-based index
    return highest_month + 1  #add 1 to make the month 1-based index
    

# d. Calculate bonus for July
def calculate_july_bonus():
    """
    Calculate a 10% bonus for all employees for July.
    Returns:
        list: List of bonus amounts for each employee.
    """
    #check if there is no employee data available
    if not hours:
        print("No employee data available .")
        return []  # Return an empty list
    
    bonus_list = [] 
    #a list to store the bonus amount for each employee
    
    #loop through the list of employees and calculate the bonus for July
    for employee in hours:
        hourly_wage = employee[1]  #employee's hourly wage
        hours_worked_in_july = employee[2][6]  #hours worked in July,note:in list index 6 for July
        
        #calculate the salary for July and the bonus 10% of the salary
        salary_in_july = hourly_wage * hours_worked_in_july
        bonus = salary_in_july * 0.10  #10% bonus for July added to the salary
        #add the bonus to the list after bonus calculation :
        bonus_list.append(bonus)
    return bonus_list
    


## Task 2: Volunteer Performance

oranges = [ ["Alice" ,20 ,50], ["Bob" ,30 ,150], ["Charlie" ,10 ,20], ["Diana" ,15 ,50], ["Eve" ,12 ,30],
 ["Frank" ,30 ,100], ["Grace" ,20 ,60], ["Hannah" ,20 ,50], ["Ian" ,24 ,70], ["Jack" ,25 ,150]]

# a. Identify top performer
def find_top_performer(oranges):
    
    top_performer = None
    highest_average = 0
   #loop through the list of volunteers and calculate the average number of oranges picked per day
    for volunteer in oranges:
        name, days_worked, oranges_picked = volunteer
        # לשאול המרצה  לגבי חלוקה ב 0 
        if days_worked > 0:  #avoid division by 0 
            average = oranges_picked / days_worked
            if average > highest_average: #compare the average with the highest average and update the top performer
                highest_average = average
                top_performer = name

    return top_performer


# b. Calculate the robot efficiency
def robot_efficiency(oranges):
    #Calculate the total number of oranges picked and the total number of days worked
    total_oranges = 0
    total_days = 0

    for volunteer in oranges:
        _, days_worked, oranges_picked = volunteer
        total_oranges += oranges_picked
        total_days += days_worked

    if total_days > 0:  #avoid division by 0
        average_per_day = total_oranges / total_days
        return int(average_per_day * 100 * 30) #multiply by 100 and 30 to get the efficiency percentage for a month
    else:
        return 0

#if __name__ == "__main__":
    
    #print (f"This work is the work of:\n{full_name} ({student_ID})")


