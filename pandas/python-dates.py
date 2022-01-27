import pandas as pd

df = pd.DataFrame({'date': ['2016-6-10 20:30:0', 
                            '2016-7-1 19:45:30', 
                            '2013-10-12 4:5:1'],
                   'value': [2, 3, 4]})
df['date'] = pd.to_datetime(df['date'], format="%Y-%d-%m %H:%M:%S")
df
df['DoB'] = pd.to_datetime(df['DoB'])

And to get year, month, and day

df['year']= df['DoB'].dt.year
df['month']= df['DoB'].dt.month
df['day']= df['DoB'].dt.day
df

4. Get the week of year, the day of week and leap year

Similarly, dt.week, dt.dayofweek, and dt.is_leap_year are the inbuilt attributes to get the week of year, the day of week, and leap year.

df['week_of_year'] = df['DoB'].dt.week
df['day_of_week'] = df['DoB'].dt.dayofweek
df['is_leap_year'] = df['DoB'].dt.is_leap_year
df

Note that Pandas dt.dayofweek attribute returns the day of the week and it is assumed the week starts on Monday, which is denoted by 0 and ends on Sunday which is denoted by 6. To replace the number with full name, we can create a mapping and pass it to map() :

dw_mapping={
    0: 'Monday', 
    1: 'Tuesday', 
    2: 'Wednesday', 
    3: 'Thursday', 
    4: 'Friday',
    5: 'Saturday', 
    6: 'Sunday'
} 
df['day_of_week_name']=df['DoB'].dt.weekday.map(dw_mapping)
df

5. Get the age from the date of birth

The simplest solution to get age is by subtracting year:

today = pd.to_datetime('today')
df['age'] = today.year - df['DoB'].dt.yeardf

However, this is not accurate as people might haven't had their birthday this year. A more accurate solution would be to consider the birthday

# Year difference
today = pd.to_datetime('today')
diff_y = today.year - df['DoB'].dt.year
# Haven't had birthday
b_md = df['DoB'].apply(lambda x: (x.month,x.day) )
no_birthday = b_md > (today.month,today.day)df['age'] = diff_y - no_birthday
df

6. Improve performance by setting date column as the index

A common solution to select data by date is using a boolean maks. For example

condition = (df['date'] > start_date) & (df['date'] <= end_date)
df.loc[condition]

This solution normally requires start_date, end_date and date column to be datetime format. And in fact, this solution is slow when you are doing a lot of selections by date in a large dataset.

If you are going to do a lot of selections by date, it would be faster to set date column as the index first so you take advantage of the Pandas built-in optimization. Then, you can select data by date using df.loc[start_date:end_date] . Let take a look at an example dataset city_sales.csv, which has 1,795,144 rows data

df = pd.read_csv('data/city_sales.csv',parse_dates=['date'])
df.info()RangeIndex: 1795144 entries, 0 to 1795143
Data columns (total 3 columns):
 #   Column  Dtype         
---  ------  -----         
 0   date    datetime64[ns]
 1   num     int64         
 2   city    object        
dtypes: datetime64[ns](1), int64(1), object(1)
memory usage: 41.1+ MB

To set the date column as the index

df = df.set_index(['date'])
df

7. Select data with a specific year and perform aggregation

Let’s say we would like to select all data in the year 2018

df.loc['2018']

And to perform aggregation on the selection for example:

Get the total num in 2018

df.loc['2018','num'].sum()1231190

Get the total num for each city in 2018

df['2018'].groupby('city').sum()

8. Select data with a specific month and a specific day of the month

To select data with a specific month, for example, May 2018

df.loc['2018-5']

Similarly, to select data with a specific day of the month, for example, 1st May 2018

df.loc['2018-5-1']

9 Select data between two dates

To select data between two dates, you can usedf.loc[start_date:end_date] For example:

Select data between 2016 and 2018

df.loc['2016' : '2018']

Select data between 10 and 11 o'clock on the 2nd May 2018

df.loc['2018-5-2 10' : '2018-5-2 11' ]

Select data between 10:30 and 10:45 on the 2nd May 2018

df.loc['2018-5-2 10:30' : '2018-5-2 10:45' ]

And to select data between time, we should use between_time(), for example, 10:30 and 10:45

df.between_time('10:30','10:45')

10 Handle missing values

We often need to compute window statistics such as a rolling mean or a rolling sum.

Let’s compute the rolling sum over a 3 window period and then have a look at the top 5 rows.

df['rolling_sum'] = df.rolling(3).sum()
df.head()

We can see that it only starts having valid values when there are 3 periods over which to look back. One solution to handle this is by backfilling of data.

df['rolling_sum_backfilled'] = df['rolling_sum'].fillna(method='backfill')
df.head()

For more details about backfilling, please check out the following article
Working with missing values in Pandas
A tutorial on missing value in Pandas and how to use the built-in methods to handle them

towardsdatascience.com
That’s it

Thanks for reading.

Please checkout the notebook on my Github for the source code.

Stay tuned if you are interested in the practical aspect of machine learning.

Here are some picked articles for you:

    Working with missing values in Pandas
    4 tricks to parse date columns with Pandas read_csv()
    Pandas read_csv() tricks you should know to speed up your data analysis
    6 Pandas tricks you should know to speed up your data analysis
    7 setups you should include at the beginning of a data science project.

References

    [1] Pandas to_datetime official document

B. Chen

Machine Learning practitioner | Formerly health informatics at University of Oxford | Ph.D. | https://www.linkedin.com/in/bindi-chen-aa55571a/
Follow
B. Chen Follows

    Abhay Parashar
    Abhay Parashar
    SeattleDataGuy
    SeattleDataGuy
    Andre Ye
    Andre Ye
    Mehdi Aoussiad
    Mehdi Aoussiad
    Fares Sayah
    Fares Sayah

See all (144)

Related
How To Fix pandas.parser.CParserError: Error tokenizing data
Topic modeling using LDA
Generating topic is difficult, let us keep this to ML to do
Day 1 — Cleaning data frames and setting up for deeper analysis
Creating a Simple Rule-Based Chatbot with Python
Sign up for The Variable
By Towards Data Science

Every Thursday, the Variable delivers the very best of Towards Data Science: from hands-on tutorials and cutting-edge research to original features you don't want to miss. Take a look.

    Python
    Data Science
    Pandas
    Machine Learning
    Date

More from Towards Data Science
Follow

Your home for data science. A Medium publication sharing concepts, ideas and codes.
Read more from Towards Data Science
More From Medium
Scraping tables from a JavaScript webpage using Selenium, BeautifulSoup, and Pandas
B. Chen in Analytics Vidhya
Python Scripts for CCXT Crypto Candlestick (OHLCV) Charting Data
ShrimpyApp in Coinmonks
Why data collection is key to your data strategy
Snowplow Team in Snowplow Analytics
The State of Data Infrastructure Landscape in 2022 and Beyond
Dunith Dhanushka in Event-driven Utopia
Regression Blog 2: We’re Practically Giving These Regressions Away
Paul Mahler in RAPIDS AI
How to Predict Rainfall with Logistic Regression Model Using Python
Mazen Ahmed in Python in Plain English
Demystifying real estate valuation
Property Decoded
Insurance ‘Redlining’ Investigation
Alex Yelverton in Towards Data Science

About

Write

Help

Legal
