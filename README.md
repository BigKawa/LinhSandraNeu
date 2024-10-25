## Introduction
Vanguard is a leading investment management company, known for its low-cost mutual funds and commitment to helping investors achieve their financial goals. As the digital world continues to evolve, Vanguard recognized that the needs of their clients were also shifting. To meet these changing demands, Vanguard believed that a more intuitive and modern User Interface (UI), combined with timely in-context prompts (cues, messages, hints, or instructions), could help streamline the online process for clients.
An A/B test was conducted from 3/15/2017 to 6/20/2017:
Control Group: Clients used Vanguard's traditional interface.
Test Group: Clients experienced the new, modernized UI.
Both groups followed the same process flow: an initial page, three steps, and a final confirmation page.
The primary goal of our exploratory data analysis (EDA) is to answer the key question: ***Would these changes encourage more clients to complete the process?***
## Data Sources
There are three key datasets guiding this analysis:
Client Profiles (df_final_demo): Contains demographics such as age, gender, and account details.
Digital Footprints (df_final_web_data): Tracks client interactions online, split into two parts (pt_1 and pt_2).
Experiment Roster (df_final_experiment_clients): Identifies which clients participated in the A/B test.
## Research Questions and Hypotheses
**1. Hypothesis**: There are measurable differences between the Control and Test Groups in terms of user satisfaction and performance metrics.
The goal is to determine whether the new interface leads to improved satisfaction and better overall performance.
**2. Data Analysis**
The following methods were used to explore and analyze the data:
Exploratory Data Analysis (EDA): To identify trends, patterns, and potential relationships within the data.
Two-sample tests: To compare the Control and Test Groups, testing for statistically significant differences in user satisfaction and performance.
Chi-square (χ²) tests: To assess the relationship between categorical variables, such as completion rates between groups.
Effect size investigation: To measure the magnitude of the differences observed between the Control and Test Groups.
## Conclusion
Completion Rate Test & 5% > Completion Rate Control
:x: Error Rate Test < Error Rate Control
:weißes_häkchen: Time per step avg Test < Time per step avg Control
In conclusion, we found that while more clients in the Test Group completed the process, the increase did not exceed the 5% threshold. As a result, the new design may not be justifiable from a cost perspective.
To gain better insights, it may be beneficial to extend the duration of the experiment