import datetime

# Getting the current year automatically from the system
current_year = datetime.datetime.now().year

# Asking user for their birth year
birth_year = int(input("Enter your birth year: "))

# 1. Calculating current age
current_age = current_year - birth_year

# 2. Age in months (approximate)
age_in_months = current_age * 12

# 3. Age in days (approximate, 365 days per year)
age_in_days = current_age * 365

# 4. Age in hours
age_in_hours = age_in_days * 24

# 5. Age in minutes
age_in_minutes = age_in_hours * 60

# 6. Years until age 100
years_until_100 = 100 - current_age

# Displaying results
print("\n----- AGE DETAILS (Approximate) -----")
print("Current Age:", current_age, "years")
print("Age in Months:", age_in_months)
print("Age in Days:", age_in_days)
print("Age in Hours:", age_in_hours)
print("Age in Minutes:", age_in_minutes)
print("Years until 100:", years_until_100)

# --------------------------------------------
# BONUS PART – Exact Age Calculation
# --------------------------------------------

print("\n----- BONUS: Exact Age Calculation -----")

# Asking user for exact birth date
birth_day = int(input("Enter birth day (DD): "))
birth_month = int(input("Enter birth month (MM): "))
birth_year_exact = int(input("Enter birth year (YYYY): "))

# Creating birth date object
birth_date = datetime.date(birth_year_exact, birth_month, birth_day)

# Getting today's date
today = datetime.date.today()

# Calculating exact difference
exact_age_days = (today - birth_date).days

# Converting exact days into years and remaining days
exact_years = exact_age_days // 365
remaining_days = exact_age_days % 365

print("\n----- EXACT AGE DETAILS -----")
print("Exact Age:", exact_years, "years and", remaining_days, "days")
print("Total Days Lived:", exact_age_days)
