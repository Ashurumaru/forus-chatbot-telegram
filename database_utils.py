import os
import aiomysql


async def db_execute(query, is_select=False):
    connect = await aiomysql.connect(host=os.getenv('DB_HOST'),
                                     port=3306,
                                     user=os.getenv('DB_USER'),
                                     password=os.getenv('DB_PASSWORD'),
                                     db=os.getenv('DB_NAME'),
                                     autocommit=True)
    async with connect.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(query)
        if is_select:
            result = await cursor.fetchall()
            return result
        else:
            return cursor.rowcount


async def get_random_item():
    query = "SELECT * FROM items ORDER BY RAND() LIMIT 1"
    result = await db_execute(query, is_select=True)
    return result


async def delete_item_by_id(item_id):
    query = f"DELETE FROM items WHERE id = {item_id}"
    affected_rows = await db_execute(query)
    return affected_rows > 0


async def get_item_by_id(item_id):
    query = f"SELECT * FROM items WHERE id = {item_id}"
    result = await db_execute(query, is_select=True)
    return result
