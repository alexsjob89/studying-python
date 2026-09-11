from app.database import get_connection

def create_user_table():
    connection = get_connection()
    
    cursor = connection.cursor()
    
    cursor.execute(
            
        )

    connection.commit()
    connection.close()