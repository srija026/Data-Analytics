import pandas as pd

def load_data():
    # Define the file path
    file_path = r"C:\Users\Srija Kalyanam\Downloads\census+income\adult.data"
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path, header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status", 
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", 
        "hours-per-week", "native-country", "salary"
    ])
    
    # Display the first few rows of the DataFrame to verify correct loading
    print(df.head())
    
    return df

def analyze_demographic_data():
    # Read data
    df = load_data()
    
    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    if df[higher_education].shape[0] > 0:
        higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100, 1)
    else:
        higher_education_rich = 0  # or some other value to handle this case
    
    # What percentage of people without advanced education make more than 50K?
    lower_education = ~higher_education
    if df[lower_education].shape[0] > 0:
        lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)
    else:
        lower_education_rich = 0  # or some other value to handle this case
    
    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    if num_min_workers.shape[0] > 0:
        rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)
    else:
        rich_percentage = 0  # or some other value to handle this case
    
    # What country has the highest percentage of people that earn >50K?
    country_earning = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_count = df['native-country'].value_counts()
    if not (country_earning / country_count).isna().all():
        highest_earning_country = (country_earning / country_count * 100).idxmax()
        highest_earning_country_percentage = round((country_earning / country_count * 100).max(), 1)
    else:
        highest_earning_country = "Not available"
        highest_earning_country_percentage = 0
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation_series = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()
    top_IN_occupation = top_IN_occupation_series[0] if not top_IN_occupation_series.empty else "Not available"
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == "__main__":
    result = analyze_demographic_data()
    for key, value in result.items():
        print(f"{key}: {value}")
