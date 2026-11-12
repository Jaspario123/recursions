def open_doll(doll):
    """
    Recursively opens a nested dictionary of Matryoshka dolls 
    to find the size of the smallest, innermost doll.
    """
    if doll.get("inner_doll") is None:
        return doll["size"]
    
    return open_doll(doll["inner_doll"])

if __name__ == "__main__":
    nested_dolls = doll_three = {
    "size": 20, 
    "inner_doll": {
        "size": 15, 
        "inner_doll": {
            "size": 10, 
            "inner_doll": {
                "size": 3, 
                "inner_doll": None
            }
        }
    }
}

    smallest_size = open_doll(nested_dolls)
    print(f"The size of the innermost doll is: {smallest_size}")
