#!/usr/bin/env python
# coding: utf-8

# # PyCity Schools Analysis
# 
# - Your analysis here
#   
# ---

# In[1]:


# Dependencies and Setup
import pandas as pd
from pathlib import Path

# File to Load (Remember to Change These)
school_data_to_load = Path("Resources/schools_complete.csv")
student_data_to_load = Path("Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)


# In[2]:


school_data


# In[3]:


student_data


# In[4]:


# Combine the data into a single dataset.
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete


# ## District Summary

# In[5]:


# Calculate the total number of unique schools
school_count = len(school_data_complete["school_name"].unique())
school_count


# In[6]:


school_data_complete.columns


# In[7]:


# Calculate the total number of students
student_count = school_data_complete["Student ID"].count()
student_count


# In[8]:


# Calculate the total budget
total_budget = school_data["budget"].sum()
total_budget


# In[9]:


# Calculate the average (mean) math score
average_math_score = school_data_complete["math_score"].mean()
average_math_score


# In[10]:


# Calculate the average (mean) reading score
average_reading_score = school_data_complete["reading_score"].mean()
average_reading_score


# In[11]:


# Use the following to calculate the percentage of students who passed math (math scores greather than or equal to 70)
passing_math_count = school_data_complete[(school_data_complete["math_score"] >= 70)].count()["student_name"]
passing_math_percentage = passing_math_count / float(student_count) * 100
passing_math_percentage


# In[12]:


# Calculate the percentage of students who passed reading (hint: look at how the math percentage was calculated)
passing_reading_count = school_data_complete[school_data_complete["reading_score"] >= 70].count()["Student ID"]
passing_reading_percentage = passing_reading_count / float(student_count) * 100
passing_reading_percentage


# In[13]:


# Use the following to calculate the percentage of students that passed math and reading
passing_math_reading_count = school_data_complete[
    (school_data_complete["math_score"] >= 70) & (school_data_complete["reading_score"] >= 70)
].count()["student_name"]
overall_passing_rate = passing_math_reading_count /  float(student_count) * 100
overall_passing_rate


# In[14]:


# Create a high-level snapshot of the district's key metrics in a DataFrame
district_summary = pd.DataFrame(
    {
        "Total Schools": [school_count],
        "Total Students": [student_count],
        "Total Budget": [total_budget],
        "Average Math Score": [average_math_score],
        "Average Reading Score": [average_reading_score],
        "% Passing Math": [passing_math_percentage],
        "% Passing Reading": [passing_reading_percentage],
        "Overall Passing": [overall_passing_rate]
    }
)
# Formatting
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)

# Display the DataFrame
district_summary


# In[15]:


district_summary.dtypes


# ## School Summary

# In[16]:


# Use the code provided to select the type per school from school_data
school_types = school_data.set_index(["school_name"])["type"]


# In[17]:


# Calculate the total student count per school from school_data
per_school_counts = school_data_complete["school_name"].value_counts()
per_school_counts


# In[18]:


# Calculate the total school budget and per capita spending per school from school_data
per_school_budget = school_data_complete.groupby('school_name')['budget'].mean()
per_school_capita = per_school_budget / per_school_counts
per_school_capita


# In[19]:


# Calculate the average test scores per school from school_data_complete
per_school_math = school_data_complete.groupby('school_name')['math_score'].mean()
per_school_reading = school_data_complete.groupby('school_name')['reading_score'].mean()


# In[20]:


# Calculate the number of students per school with math scores of 70 or higher from school_data_complete
school_passing_math = school_data_complete[school_data_complete["math_score"] >= 70]


# In[21]:


# Calculate the number of students per school with reading scores of 70 or higher from school_data_complete
school_passing_reading = school_data_complete[school_data_complete["reading_score"] >= 70]


# In[22]:


# Use the provided code to calculate the number of students per school that passed both math and reading with scores of 70 or higher
passing_math_and_reading = school_data_complete[
    (school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)
]


# In[23]:


# Use the provided code to calculate the passing rates
per_school_passing_math = school_passing_math.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100
per_school_passing_reading = school_passing_reading.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100
overall_passing_rate = passing_math_and_reading.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100


# In[24]:


# Create a DataFrame called `per_school_summary` with columns for the calculations above.
per_school_summary = pd.DataFrame(
    {
         "School Type":school_types,
         "Total Students": per_school_counts,
         "Total School Budget": per_school_budget,
         "Per Student Budget" : per_school_capita,
         "Average Math Score" : per_school_math,
         "Average Reading Score" : per_school_reading,
         "% Passing Math" : per_school_passing_math,
         "% Passing Reading" : passing_reading_percentage,
         "% Overall Passing" : overall_passing_rate
    }
)
# Formatting
per_school_summary["Total School Budget"] = per_school_summary["Total School Budget"].map("${:,.2f}".format)
per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].map("${:,.2f}".format)

# Display the DataFrame
per_school_summary


# ## Highest-Performing Schools (by % Overall Passing)

# In[25]:


# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows.
top_schools = per_school_summary.sort_values(["% Overall Passing"], ascending = False)
top_schools.head(5)


# ## Bottom Performing Schools (By % Overall Passing)

# In[26]:


# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows.
bottom_schools = per_school_summary.sort_values(["% Overall Passing"], ascending = True)
bottom_schools.head(5)


# ## Math Scores by Grade

# In[27]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]

# Group by `school_name` and take the mean of the `math_score` column for each.
ninth_grade_math_scores = ninth_graders.groupby('school_name')['math_score'].mean()
tenth_grader_math_scores = tenth_graders.groupby('school_name')['math_score'].mean()
eleventh_grader_math_scores = eleventh_graders.groupby('school_name')['math_score'].mean()
twelfth_grader_math_scores = twelfth_graders.groupby('school_name')['math_score'].mean()

# Combine each of the scores above into single DataFrame called `math_scores_by_grade`
math_scores_by_grade = pd.DataFrame(
    {
        "9th": ninth_grade_math_scores,
        "10th": tenth_grader_math_scores,
        "11th": eleventh_grader_math_scores,
        "12th": twelfth_grader_math_scores
    }
)

# Minor data wrangling
math_scores_by_grade.index.name = None

# Display the DataFrame
math_scores_by_grade


# ## Reading Score by Grade 

# In[28]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]

# Group by `school_name` and take the mean of the the `reading_score` column for each.
ninth_grade_reading_scores = ninth_graders.groupby('school_name')['reading_score'].mean()
tenth_grader_reading_scores = tenth_graders.groupby('school_name')['reading_score'].mean()
eleventh_grader_reading_scores = eleventh_graders.groupby('school_name')['reading_score'].mean()
twelfth_grader_reading_scores = twelfth_graders.groupby('school_name')['reading_score'].mean()

# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = pd.DataFrame(
    {
        "9th": ninth_grade_reading_scores,
        "10th" : tenth_grader_reading_scores,
        "11th" : eleventh_grader_reading_scores,
        "12th" : twelfth_grader_reading_scores
    }
)

# Minor data wrangling
reading_scores_by_grade = reading_scores_by_grade[["9th", "10th", "11th", "12th"]]
reading_scores_by_grade.index.name = None

# Display the DataFrame
reading_scores_by_grade


# ## Scores by School Spending

# In[29]:


# Establish the bins
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]


# In[30]:


# Create a copy of the school summary since it has the "Per Student Budget"
school_spending_df = per_school_summary.copy()


# In[31]:


# Use `pd.cut` to categorize spending based on the bins.
school_spending_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, bins = spending_bins, labels = labels)
school_spending_df


# In[32]:


spending_math_scores = school_spending_df.groupby("Spending Ranges (Per Student)")["Average Math Score"].mean()
spending_reading_scores = school_spending_df.groupby("Spending Ranges (Per Student)")["Average Reading Score"].mean()
spending_passing_math = school_spending_df.groupby("Spending Ranges (Per Student)")["% Passing Math"].mean()
spending_passing_reading = school_spending_df.groupby("Spending Ranges (Per Student)")["% Passing Reading"].mean()
overall_passing_spending = school_spending_df.groupby("Spending Ranges (Per Student)")["% Overall Passing"].mean()


# In[33]:


#  Calculate averages for the desired columns.
school_by_spending_gb = school_spending_df.groupby(["Spending Ranges (Per Student)"], observed=True)
spending_math_scores = school_by_spending_gb["Average Math Score"].mean()
spending_reading_scores = school_by_spending_gb["Average Reading Score"].mean()
spending_passing_math = school_by_spending_gb["% Passing Math"].mean()
spending_passing_reading = school_by_spending_gb["% Passing Reading"].mean()
overall_passing_spending = school_by_spending_gb["% Overall Passing"].mean()


# In[34]:


# Assemble into DataFrame
spending_summary = pd.DataFrame(
    {
         "Average Math Score": spending_math_scores,
         "Average Reading Score": spending_reading_scores,
         "% Passing Math": spending_passing_math,
         "% Passing Reading": spending_passing_reading,
         "% Overall Passing": overall_passing_spending
    }
)

# Display results
spending_summary


# ## Scores by School Size

# In[35]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[36]:


# Categorize the spending based on the bins
# Use `pd.cut` on the "Total Students" column of the `per_school_summary` DataFrame.

per_school_summary["School Size"] = pd.cut(per_school_summary["Total Students"], size_bins, labels = labels)
per_school_summary


# In[37]:


# Calculate averages for the desired columns.
size_math_scores = per_school_summary.groupby(["School Size"])["Average Math Score"].mean()
size_reading_scores = per_school_summary.groupby(["School Size"])["Average Reading Score"].mean()
size_passing_math = per_school_summary.groupby(["School Size"])["% Passing Math"].mean()
size_passing_reading = per_school_summary.groupby(["School Size"])["% Passing Reading"].mean()
size_overall_passing = per_school_summary.groupby(["School Size"])["% Overall Passing"].mean()


# In[38]:


# Create a DataFrame called `size_summary` that breaks down school performance based on school size (small, medium, or large).
# Use the scores above to create a new DataFrame called `size_summary`
size_summary = pd.DataFrame (
    {
        "Average math score": size_math_scores,
        "Average Reading Score": size_reading_scores,
        "% passing math": size_passing_math,
        "% passing reading": size_passing_reading,
        "% overall passing": size_overall_passing
}
)

# Display results
size_summary


# ## Scores by School Type

# In[39]:


# Group the per_school_summary DataFrame by "School Type" and average the results.
average_math_score_by_type = per_school_summary.groupby(["School Type"])["Average Math Score"].mean()
average_reading_score_by_type = per_school_summary.groupby(["School Type"])["Average Reading Score"].mean()
average_percent_passing_math_by_type = per_school_summary.groupby(["School Type"])["% Passing Math"].mean()
average_percent_passing_reading_by_type = per_school_summary.groupby(["School Type"])["% Passing Reading"].mean()
average_percent_overall_passing_by_type = per_school_summary.groupby(["School Type"])["% Overall Passing"].mean()


# In[40]:


# Assemble the new data by type into a DataFrame called `type_summary`
type_summary = pd.DataFrame(
    {
    "Average math score": average_math_score_by_type, 
    "Average Reading Score": average_reading_score_by_type,
    "% passing math": average_percent_passing_math_by_type,
    "% passing reading": average_percent_passing_reading_by_type,
    "% overall passing": average_percent_overall_passing_by_type
}
)
# Display results

type_summary

