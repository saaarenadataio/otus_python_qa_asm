import os.path, json, csv

FILES_DIR = os.path.dirname(__file__)

def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)

BOOKS_PATH = get_path(filename="books.csv")
USERS_PATH = get_path(filename="users.json")
def redistribute_books():
    with open(USERS_PATH, "r") as f1:
        users = json.loads(f1.read())
        users_pretty = list(
            map(lambda user_pretty:{
                "name": user_pretty['name'],
                "gender": user_pretty['gender'],
                "address": user_pretty['address'],
                "age": user_pretty['age'],
                "books": [],
            },
            users,
            )
        )

    num_users = len(users_pretty)
    step = 0

    with open(BOOKS_PATH, encoding='utf-8') as f2:
        books = csv.DictReader(f2)
        for book in books:
            users_pretty[step]["books"].append(
                {
                    'title':  book['Title'],
                    'author': book['Author'],
                    'pages':  book['Pages'],
                    'genre':  book['Genre'],
                }

            )
            step += 1
            if step == num_users:
                step = 0

    with open("result.json", "w") as f3:
      res = json.dumps(users_pretty, indent=4)
      f3.write(res)


redistribute_books()
