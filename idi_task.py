#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path, sep='\t', lineterminator='\n')
    return data

def convert_to_datetime(data):
    data['created_at'] = pd.to_datetime(data['created_at'], utc=True,errors='coerce')
    return data

def tweets_per_day(data):
    data['date'] = pd.to_datetime(data['created_at'],utc=True, errors='coerce')
    data['date_extract'] = data['date'].dt.date
    tweets_count_per_day = data[data['text'].str.contains('music', case=False, na=False)].groupby('date_extract').size()
    return tweets_count_per_day

def unique_users(data):
    unique_user_count = data[data['text'].str.contains('music', case=False, na=False)]['author_id'].nunique()
    return unique_user_count

def average_likes(data):
    # Assuming 'author_follower_count' is equivalent to 'likes'
    average_likes_value = data[data['text'].str.contains('music', case=False, na=False)]['author_follower_count'].mean()
    return average_likes_value

def tweet_locations(data):
    # Assuming 'source' is equivalent to 'place_id'
    tweet_locations_details = data[data['text'].str.contains('music', case=False, na=False)]['source'].value_counts()
    return tweet_locations_details

def tweet_times(data):
    data['hour'] = data['created_at'].dt.hour
    tweet_times_details = data[data['text'].str.contains('music', case=False, na=False)].groupby('hour').size()
    return tweet_times_details

def most_active_user(data):
    most_active_user_details = data[data['text'].str.contains('music', case=False, na=False)]['author_id'].value_counts().idxmax()
    return most_active_user_details

file_path = 'C:/Users/Rakesh/Downloads/Copy_of_correct_twitter_201904.tsv'
data = load_data(file_path)

data = convert_to_datetime(data)


if data['created_at'].isna().any():
    print("Some datetime conversions failed.")
else:
    print("Datetime conversion successful.")


print("Tweets_per_day:")
print(tweets_per_day(data))

print("Unique_users:")
print(unique_users(data))

print("Average_likes:")
print(average_likes(data))

print("Tweet_locations:")
print(tweet_locations(data))

print("Tweet_times:")
print(tweet_times(data))

print("Most_active_user:")
print(most_active_user(data))

