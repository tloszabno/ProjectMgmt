# ProjectMgmt

Project Managment Helper


## Requirements
- python 2.7

## Instalation 
- just run git clone https://github.com/tloszabno/ProjectMgmt.git in installation folder
 
## Required Configuration
Edit file config.py and adjust variables:
- projects_db_path
- logs_file_name_prefix

## Usage
### Scan for projects
Assuming that your workspace with maven projects is in folder /home/user/workspace run:
```
./project_mgmt.py --autoscan ~/workspace
```
Folder will be scanned recursivelly for maven projects and servers run scripts
All found project will be added to db. Keys(names) will be like folder where found. 
For each server script tool will prompt to give name, eg:
```
Provide name for server in path /home/user/workspace/app-ear/app_server.sh>_
```
Entered name will be used in script actions for servers.

### Show available projects
```
./project_mgmt.py --show
```

### Action 
Tool run action defined in config.py file.
So by defualt there is action `'clean-build': ('cb', 'mvn clean install'),` defined
so just run: 
```
./project_mgmt.py -cb app
```
to run ```mvn clean install``` command

Action can be applied multiple times for every projects combinations. When only action is given without arguments, argumnets from previous action are taken. So comman:
```
./project_mgmt.py -rh app -cb 
```
Will invoke ```git reset --hard && git checkout master && git fetch && git reset --hard origin/master``` and ```mvn clean install``` command in app folder.

TO be continued....


 When action has placeholed for argument ({0},{1}..) they can be passed.
