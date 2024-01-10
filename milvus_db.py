from pymilvus import connections, db

def create_milvus_database():
    try:
        conn = connections.connect(host="localhost", port=19530)
        # Host sollte "milvus" sein, um auf den Docker-Container zuzugreifen,
        # falls Sie diesen im selben Docker-Netzwerk ausführen. Ansonsten ändern Sie den Host entsprechend.

        if "book" not in db.list_database():
            db.create_database("book")
            db.using_database("book")
            print("Milvus database 'book' created successfully.")

        else:
            db.using_database("book")
            print("Milvus database 'book' already exists.")

    except Exception as e:
        print(f"Failed to create Milvus database: {e}")

if __name__ == "__main__":
    create_milvus_database()
