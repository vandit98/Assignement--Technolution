from storage import Storage

# Initialize checkouts list from storage
checkouts = Storage.load_data('checkouts.json')

def checkout_book(user_id, isbn):
    checkouts.append({"user_id": user_id, "isbn": isbn})
    Storage.save_data('checkouts.json', checkouts)
    print(f"Book with ISBN {isbn} checked out successfully.")

def checkin_book(user_id, isbn):
    global checkouts
    checkouts = [c for c in checkouts if not (c['user_id'] == user_id and c['isbn'] == isbn)]
    Storage.save_data('checkouts.json', checkouts)
    print(f"Book with ISBN {isbn} checked in successfully.")


