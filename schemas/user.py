def userEntity(item) -> dict:
    return {
        "id": str(item["id"]),
        "name": item["name"]
    }

def usersEntity(entity) -> list:
    return[userEntity(item)for item in entity] 
      