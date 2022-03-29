import json
import csv
import requests

json_fp =open("data/review_322770.json", "r",encoding='utf-8_sig')
readjson =json.load(json_fp)#将json文件转化为字典
dict_reviews = readjson.get("reviews")
#dict_review = dict_reviews.get('review')
#print(dict_reviews)
list_skey =dict_reviews.keys() #利用keys（）方法将挑选后的字典的第一个关键字都挑选出来
lables =['recommendationid','language','review','anthor_steamid','anthor_num_games_owned','anthor_num_reviews','author_playtime_forever','author_playtime_at_review','author_last_played','timestamp_created','timestamp_updated','voted_up','votes_up','votes_funny','weighted_vote_score','comment_count','steam_purchase','received_for_free','written_during_early_access']
#print(list_skey)
with open('review.322770_2.csv','w',encoding='utf-8_sig') as f:
    writer = csv.writer(f)
    writer.writerow(lables)
    for i in list_skey:
       # k=list_skey[i]
        dict_keys = dict_reviews.get(i)
        #print(dict_keys)
        dict_review =dict_keys.get('review')
        dict_language =dict_keys.get('language')
        dict_author = dict_keys.get('author')
        dict_steamid =dict_author.get('steamid')
        dict_num_games_owned =dict_author.get('num_games_owned')
        dict_num_reviews =dict_author.get('num_reviews')
        dict_playtime_forever=dict_author.get('playtime_forever')
        dict_playtime_last_two_weeks =dict_author.get('playtime_last_two_weeks')
        dict_playtime_at_review =dict_author.get('playtime_at_review')
        dict_last_played =dict_author.get('last_played')
        dict_timestamp_created=dict_keys.get('timestamp_created')
        dict_timestamp_updated =dict_keys.get('timestamp_updated')
        dict_voted_up = dict_keys.get('voted_up')
        dict_votes_up =dict_keys.get('votes_up')
        dict_votes_funny=dict_keys.get('votes_funny')
        dict_weighted_vote_score =dict_keys.get('weighted_vote_score')
        dict_comment_count= dict_keys.get('comment_count')
        dict_steam_purchase =dict_keys.get('steam_purchase')
        dict_received_for_free=dict_keys.get('received_for_free')
        dict_written_during_early_access =dict_keys.get('written_during_early_access')

        wdata = [i,dict_language,dict_review,dict_steamid,dict_num_games_owned,dict_num_reviews,dict_playtime_forever,dict_playtime_last_two_weeks,dict_playtime_at_review,dict_last_played,dict_timestamp_created,
                 dict_timestamp_updated,dict_voted_up,dict_votes_up,dict_votes_funny,dict_weighted_vote_score,dict_comment_count,dict_steam_purchase,dict_received_for_free,dict_written_during_early_access]
        writer.writerow(wdata) #写入是个列表

       # writer.writerows(dict_review)
       # print(dict_review)
#print(dict_reviews)