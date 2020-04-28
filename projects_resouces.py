import os
import pandas as pd

project_array = []

def cmd_exec(cmd):
    stream = os.popen(cmd)
    return stream.read()

def sql_list(project):
    return cmd_exec('gcloud sql instances list --project='+ project +' --quiet')

def compute_list(project):
    return cmd_exec('gcloud compute instances list --project='+ project+' --quiet')

def app_list(project):
    return cmd_exec('gcloud app services list --project='+ project+' --quiet')

def count_lines(data):
    total = len(data.splitlines())
    return  0 if total == 0 else total -1

def read_project(project):
    sql = sql_list(project)
    compute = compute_list(project)
    app = app_list(project)
    return {'project': project, 'sql': count_lines(sql), 'compute': count_lines(compute), 'app': count_lines(app)}

stream = os.popen('gcloud projects list')
projects = stream.read()

for line in projects.splitlines()[1:2]:
    x = line.split()
    project_array.append(read_project(x[0]))

df = pd.DataFrame(project_array)

df.to_excel('projects.xls', index=False)
print(df.to_string())