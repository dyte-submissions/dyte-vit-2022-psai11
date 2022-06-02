import argparse
import git
import os
import pandas as pd
import json
import subprocess
from github import Github
import sys

def get_repo_name_from_url(url: str) -> str:
    """
    get_repo_name_from_url("https://github.com/user/repository_name.git")     # returns repository_name
    get_repo_name_from_url("https://github.com/user/repository_name")         # returns repository_name
    get_repo_name_from_url("https://github.com/user/repository_name.git/asd") # Exception

    """
    if(url[-1]=='/'):
        url = url[0:len(url)-1]
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]

if __name__ == "__main__":
    #####CLI Arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", help="CSV File Path")
    parser.add_argument("dependency", help="dependency version")
    parser.add_argument("--update", nargs='?', const=True, type=bool)
    args = parser.parse_args()
    datafile = args.csv_path
    extra = datafile
    extra = extra.replace('.csv','')
    extra = extra.replace('input','') 
    depen = args.dependency
    update = args.update
    depen_name,req_depen_version= depen.split("@")

    #Checking valid npm packages and versions
    try:
        version_list = subprocess.check_output('npm view '+str(depen_name)+' versions --json', shell=True)
        dec_version_list = version_list.decode()
        if req_depen_version not in dec_version_list:
            print("!!!!! PACKAGE VERSION UNAVAILABLE. PLEASE CHECK THE LATEST DOCS & ENTER A VALID PACKAGE VERSION.")
            sys.exit()
    except subprocess.CalledProcessError as e:
        print("Unexpected error:", sys.exc_info())
        print("!!!!! PACKAGE DOES NOT EXIST. PLEASE ENTER VALID PACKAGE NAME !!!!!\n\n")
        sys.exit()
    
    #Checking whether NPM package is deprecated or not
    flag=1
    try:
        deprecated_val = subprocess.check_output(('check-is-deprecated '+depen_name).strip(),shell=True)
        dec_deprecated_val = deprecated_val.decode()
        c=''
        while(not c):
            print("WARNING: The query NPM package is deprecated. Would you still like to continue? (Y/N): ",end="")
            c = input()
            if(c.lower()=='n'):
                flag=0
    except:
        print()

    finally:
        if(not flag): sys.exit()
        #####Access CSV file with Repository Links & store them in py variables
        df = pd.read_csv(datafile)
        repos = {}
        reposList = {}
        for x in range(len(df)):
            if df.at[x,'RepoLink'][-1]=='/':
                df.at[x,'RepoLink'] = df.at[x,'RepoLink'][0:len(df.loc[x,'RepoLink'])-1]
            repo_name = get_repo_name_from_url(df.iloc[x,1])
            df.loc[x,'RepoName'] = repo_name
            repos[repo_name] = df.iloc[x,1]
            reposList[repo_name]=x

        #####Clone Repositories
        print("<---------CLONING THE REPOSITORIES--------->")
        FolderName = "../Dyte_Inputs_Clones"
        CloneFolder = "ClonedRepos"
        path = os.path.join('./', FolderName)
        ClonePath = path+"\\"+CloneFolder
        if(not os.path.exists(path)):
            os.mkdir(path)
        if(not os.path.exists(ClonePath)):
            os.mkdir(ClonePath)
        Noofclonedfiles = 0
        for x in repos:  
            path1 = ClonePath+'\\'+x
            if(not os.path.exists(path1)):
                print("Cloning Project:\t",x)
                git.Git(ClonePath).clone(repos[x])
                Noofclonedfiles+=1
        print("Cloning Completed.\n")

        #####Check Version & Return Output
        print("<---------VERSION VALIDATION--------->")
        Noofunsatisfiedfiles = 0
        df["version"]=""
        df["version_satisfied"]=""
        row = 0
        unsatisfied_version = []
        unsatisfied_repoName = []
        for proj in reposList.keys():
            print(proj,end="\t==>\t")
            proj_path = ClonePath+'\\'+proj
            proj_package = ClonePath+'\\'+proj+'\\'+'package.json'
            with open(proj_package, "r") as file:
                depends = json.load(file)
                if (not depen_name in depends['dependencies'].keys()):
                    continue
                proj_version = depends['dependencies'][depen_name]
                if proj_version[0]=='~' or proj_version[0]=='^':
                    proj_version = proj_version[1:]
                df.loc[row,'version'] = proj_version
                df.loc[row,'version_satisfied'] = str(proj_version >= req_depen_version)
                if(not proj_version>=req_depen_version):
                    print("Version Not Satisfied")
                    unsatisfied_version.append(proj_path)
                    unsatisfied_repoName.append(df.loc[row,'RepoName'])
                    Noofunsatisfiedfiles+=1
                else:
                    print("Version Satisfied")
                row+=1
        print("Total Files Cloned:",Noofclonedfiles)
        print("Total Satisfied Versions:",max(0,Noofclonedfiles-Noofunsatisfiedfiles))
        print("Total Unsatisfied Version:",Noofunsatisfiedfiles)
        outputFile = 'output'+extra+'.csv'
        full_path = '../Dyte_Inputs_Clones/'+outputFile
        try:
            df.to_csv('../Dyte_Inputs_Clones/'+outputFile,encoding='utf-8',index=False)
        except:
            print("ERROR: "+outputFile+" is open. Please close the file and run again!!")
            sys.exit()
        print("Summary saved at",full_path)
        print("\n")
        #
        #####Updating Unsatisfied Repositories && Sending PR
        if(update):
            print("<---------VERSION UPDATION--------->")
            print("(Input) Enter your github access token to send PR to the repositories (You may copy-paste the token):")
            df["PRLink"]=""
            token=input()
            # g = Github("USER TOKEN")
            try:
                g = Github(token)
                user = g.get_user()
                username = user.login
            except: 
                print("ERROR: please enter valid Github Access Token")
            row=0
            prlinks = []
            for proj_path in unsatisfied_version:
                print("*\n*\n*\nUpdating Project Dependencies\t=>\t",unsatisfied_repoName[row])
                subprocess.call('npm i ' + depen_name + '@' +req_depen_version, cwd=proj_path, shell=True)
                print("Project Dependencies Updated.")
                new_branch_name = 'UpdateDependency_'+depen_name+'@'+req_depen_version
                subprocess.call('git branch '+new_branch_name, cwd=proj_path, shell=True)
                subprocess.call('git checkout '+new_branch_name, cwd=proj_path, shell=True)
                subprocess.call('git add .', cwd=proj_path, shell=True)
                subprocess.call('git commit -m "'+new_branch_name+'"', cwd=proj_path, shell=True)
                subprocess.call('git push origin '+new_branch_name, cwd=proj_path, shell=True)
                stdout = subprocess.check_output('git branch'.split(), cwd=proj_path, shell=True)
                out = stdout.decode()
                branches = [b.strip('* ') for b in out.splitlines()]
                if "main" in branches: PRbase = "main"
                else: PRbase = "master"
                repo = g.get_repo(username+'/'+unsatisfied_repoName[row])
                PRtitle = new_branch_name
                PRbody = "Dependency Version of "+depen_name+" updated to v"+req_depen_version
                try:
                    pr = repo.create_pull(title=PRtitle, body=PRbody, head=new_branch_name, base=PRbase)
                except:
                    print("ERROR: Please close/accept the existing PR, before creating a new one.")
                    sys.exit()
                prlink = df.loc[reposList[unsatisfied_repoName[row]], 'RepoLink']+'/pull/'+str(pr.number)
                prlinks.append(prlink)
                print()
                df.loc[reposList[unsatisfied_repoName[row]],'PRLink'] = prlink
                row+=1
            print("PR created at following links:")
            for x in prlinks:
                print(x)
            print("\n")
            print("#===PROCESS COMPLETED===#")
            outputFile1 = 'PRoutput'+extra+'.csv'
            finaloutputfile = '../Dyte_Inputs_Clones/'+outputFile1
            print("Final csv with PR links can be found at",finaloutputfile)
            try:
                df.to_csv('../Dyte_Inputs_Clones/'+outputFile1,encoding='utf-8',index=False)
            except:
                print("ERROR: Fatal error, bug yet to be fixed. \nPlease Delete the cloned repositories and \ndelete the branches created in github and run again.\nSorry for the inconvience.")
                sys.exit()
        else:
            print("#===PROCESS COMPLETED===#")
            print("Summary saved at",full_path)
        
        print("\n\nPress any key to exit tool!!!")
        input()



        







