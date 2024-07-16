# pandas_challenge
Pandas


1. Background
   
    You are the new Chief Data Scientist for your city's school district. In this capacity, you'll be helping the school board and mayor make strategic decisions regarding future school budgets and priorities.

    As a first task, you've been asked to analyze the district-wide standardized test results. You'll be given access to every student's math and reading scores, as well as various information on the schools they attend. Your task is to aggregate the data to showcase          obvious trends in school performance.

2. Before You Begin

    Create a new repository for this project called pandas-challenge. Do not add this homework to an existing repository.

    Clone the new repository to your computer.

    Inside your local Git repository, create a folder for this homework assignment and name it PyCitySchools.

    Add your Jupyter notebook to this folder. This will be the main script to run for analysis.

    Push these changes to GitHub or GitLab.

3. Files

    Download the following files to help you get started: https://static.bc-edx.com/data/dl-1-2/m4/lms/starter/Starter_Code.zip

4. Instructions

    Using Pandas and Jupyter Notebook, create a report that includes the following data. Your report must include a written description of at least two observable trends based on the data.

    Hint: Check out the sample solution called PyCitySchools_starter.ipynb located in the .zip file to review the desired format for this assignment.

5. District Summary

    Perform the necessary calculations and then create a high-level snapshot of the district's key metrics in a DataFrame.

    Include the following:

      --> Total number of unique schools

      --> Total students

      --> Total budget

      --> Average math score

      --> Average reading score

      --> % passing math (the percentage of students who passed math)

      --> % passing reading (the percentage of students who passed reading)

      --> % overall passing (the percentage of students who passed math AND reading)

6. School Summary

    Perform the necessary calculations and then create a DataFrame that summarizes key metrics about each school.

    Include the following:

      --> School name

      --> School type

      --> Total students

      --> Total school budget

      --> Per student budget

      --> Average math score

      --> Average reading score

      --> % passing math (the percentage of students who passed math)

      --> % passing reading (the percentage of students who passed reading)

      --> % overall passing (the percentage of students who passed math AND reading)

7. Highest-Performing Schools (by % Overall Passing)

    Sort the schools by % Overall Passing in descending order and display the top 5 rows.

    Save the results in a DataFrame called "top_schools".

8. Math Scores by Grade
   
    Perform the necessary calculations to create a DataFrame that lists the average math score for students of each grade level (9th, 10th, 11th, 12th) at each school.

9. Reading Scores by Grade

    Create a DataFrame that lists the average reading score for students of each grade level (9th, 10th, 11th, 12th) at each school.

10. Scores by School Spending

    Create a table that breaks down school performance based on average spending ranges (per student).

    Use the code provided below to create four bins with reasonable cutoff values to group school spending.

    ![Screenshot 2024-07-15 214259](https://github.com/user-attachments/assets/f44c6d38-2026-40db-b89e-aee78a2949f1)

    Use pd.cut to categorize spending based on the bins.

    Use the following code to then calculate mean scores per spending range.

    ![Screenshot 2024-07-15 214323](https://github.com/user-attachments/assets/163030ed-4a96-4177-96ea-2c10de89b1e1)

    Use the scores above to create a DataFrame called spending_summary.

    Include the following metrics in the table:

      --> Average math score

      --> Average reading score

      --> % passing math (the percentage of students who passed math)

      --> % passing reading (the percentage of students who passed reading)

      --> % overall passing (the percentage of students who passed math AND reading)

11. Scores by School Size

    Use the following code to bin the per_school_summary.

    ![Screenshot 2024-07-15 214608](https://github.com/user-attachments/assets/6ee448d5-de5b-401b-ac21-46134fa72bca)

    Use pd.cut on the "Total Students" column of the per_school_summary DataFrame.

    Create a DataFrame called size_summary that breaks down school performance based on school size (small, medium, or large).

12. Scores by School Type
    
    Use the per_school_summary DataFrame from the previous step to create a new DataFrame called type_summary.

    This new DataFrame should show school performance based on the "School Type".
