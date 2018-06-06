Pandas and Python 3 documentation referenced during project to check/correct
syntax of code. Other specifics mentioned by function below. 

get_filters()
    Hints on While loops for handling input errors were referenced in the course
    curriculum for Python control flow and the course and project Slack channel.

    Return (int) for month rather than (str) to simplify code
    later in the script.

load_data()
    Function designed straight out of course curriculum for project intro.

calc_time()
    Helper function added at the suggestion of project instructions to limit
    repetitive code.

time_stats() and station_stats()
    For loops added to remove repetitive code.

trip_duration_stats()
    Reported in hours rather than seconds to increase user's ability
    to understand the values reported.

user_stats()
    Normalize feature of value_counts function found in Pandas documentation
    to report values as percentages to increase user's ability to compare types.
    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html

    Birth years reported as integers, since years are not understood as floats.
