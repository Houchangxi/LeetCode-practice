#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:46:14 2020

@author: andrew
"""

# Write your MySQL query statement below
with  t  as  (select
* from Matches
union
select match_id,  second_player as first_player, first_player as second_player, second_score as first_score, first_score as second_score from Matches)
# 
select group_id, player_id from (
select group_id, player_id,mx, rank()over(partition by group_id order by mx desc, player_id) rnk
from (
# 按groupid 去分  按照playid进行 score求和 mx
select distinct group_id, player_id, max(sum(first_score))over(partition by group_id, player_id) mx
from t join Players p on t.first_player=p.player_id
    group by group_id, player_id
) t1
) t2
where rnk =1;