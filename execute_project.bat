@echo off
cls
python get_reviews.py
python split_like_dislike.py
python get_keyword_spareted_comments.py
python summary.py
python get_specific_fun.py
