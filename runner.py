# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 01:27:46 2020

@author: mehedi.md.hasan
"""

import main

import pymysql

db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()


def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from final_repos ')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

repos = get_all_github_repo_id()
base_dir = "C:\mined_repos"
for repo in repos:
    top_dir = repo[1].split("/")[0]
    project_dir = repo[1].split("/")[1]
    full_dir = base_dir+"\\"+top_dir+"\\"+project_dir
    project_name = top_dir+"_"+project_dir
    main.main(full_dir, project_dir)
    
