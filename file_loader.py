import os

def load_files(repo_path):

    documents = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith((".py",".md",".txt",".js",".ts")):

                path = os.path.join(root,file)

                with open(path,"r",encoding="utf-8") as f:
                    content = f.read()

                documents.append({
                    "path": path,
                    "content": content
                })

    return documents
