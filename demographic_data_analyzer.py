import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    dfmen = df[df['sex'] == 'Male']
    average_age_men = np.round(dfmen['age'].mean() , 1) 

    # What is the percentage of people who have a Bachelor's degree?
    dfbach = df[df['education'] == 'Bachelors']
    percentage_bachelors = np.round((dfbach['education'].count() / df['education'].count() ) * 100 , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_50k = higher_education[higher_education['salary'] == '>50K']
    lower_education_50k = lower_education[lower_education['salary'] == '>50K']
    
    higher_education_rich = np.round((higher_education_50k['salary'].count() / higher_education['salary'].count()) * 100 , 1)
    lower_education_rich = np.round(lower_education_50k['education'].count() / lower_education['education'].count() * 100 , 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = np.round(df['hours-per-week'].min() , 1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    min_workers_rich = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = np.round(min_workers_rich['salary'].count() / num_min_workers['salary'].count() * 100 , 1) 

    # What country has the highest percentage of people that earn >50K?
    rich_workers = df[df['salary'] == '>50K']
    countries = rich_workers['native-country'].unique()
    percentages = np.array([])
    for country in countries:
        rich_workers_country = rich_workers[rich_workers['native-country'] == country]
        workers_country = df[df['native-country'] == country]
        percentages = np.append(percentages, rich_workers_country['native-country'].count() / workers_country['native-country'].count() * 100 )
    
    df_percentages = pd.DataFrame(percentages, index = countries, columns = ['percentage'])
    
    highest_earning_country = df_percentages[df_percentages['percentage'] == df_percentages['percentage'].max()].index[0]
    highest_earning_country_percentage = np.round(df_percentages.loc[df_percentages[df_percentages['percentage'] == df_percentages['percentage'].max()].index[0]].values[0] , 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich_workers = rich_workers[rich_workers['native-country'] == 'India']
    occupations = india_rich_workers['occupation'].unique()
    occupation_counts = np.array([])
    
    for occupation in occupations:
        india_rich_workers_occupation = india_rich_workers[india_rich_workers['occupation'] == occupation]
        occupation_counts = np.append(occupation_counts, india_rich_workers_occupation['occupation'].count())
    
    df_occupation_counts = pd.DataFrame(occupation_counts, index = occupations, columns = ['workers'])
        
    top_IN_occupation = df_occupation_counts[df_occupation_counts['workers'] == df_occupation_counts['workers'].max()].index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
print(calculate_demographic_data())
