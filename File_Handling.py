from github import Github

g= Github('Github_developer_API')
repo_name= input("Enter the reop path( username/repository_name ): ")
repo = g.get_repo(repo_name)

file = open("Milestone.py")
x = file.read()

# repo.create_file("Milestone.py", "Hello", x ,  branch="Diwasdrpm")