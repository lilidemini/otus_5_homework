from contex_manager import UserBook

obj = UserBook()

result = []
book = obj.books_csv_reader()

for each_user in obj.users_json_reader():

    book_info = next(book)
    result.append({
        "name": each_user['name'],
        "gender": each_user['gender'],
        "address": each_user['address'],
        "age": each_user['age'],
        "books": {
            "title": book_info[0],
            "author": book_info[1],
            "pages": book_info[3],
            "genre": book_info[2]
        }
    })

obj.output_json_writer(result)
