"""iPhone13"""
def iphonemini(memory):
    """mini"""
    if memory == "128 GB":
        price = 25900
    elif memory == "256 GB":
        price = 29900
    elif memory == "512 GB":
        price = 37900
    else:
        price = "Not Available"
    return price

def iphone(memory):
    """normal"""
    if memory == "128 GB":
        price = 29900
    elif memory == "256 GB":
        price = 33900
    elif memory == "512 GB":
        price = 41900
    else:
        price = "Not Available"
    return price

def iphonepro(memory):
    """pro"""
    if memory == "128 GB":
        price = 38900
    elif memory == "256 GB":
        price = 42900
    elif memory == "512 GB":
        price = 50900
    elif memory == "1 TB":
        price = 58900
    else:
        price = "Not Available"
    return price

def iphonepromax(memory):
    """promax"""
    if memory == "128 GB":
        price = 42900
    elif memory == "256 GB":
        price = 46900
    elif memory == "512GB":
        price = 54900
    elif memory == "1 TB":
        price = 62900
    else:
        price = "Not Available"
    return price

def calculate(version, memory):
    """calculate"""
    if version == "iPhone 13 mini":
        price = iphonemini(memory)
        print(price)
    elif version == "iPhone 13":
        price = iphone(memory)
        print(price)
    elif version == "iPhone 13 Pro":
        price = iphonepro(memory)
        print(price)
    elif version == "iPhone 13 Pro Max":
        price = iphonepromax(memory)
        print(price)
    else:
        print("Not Available")
calculate(input(), input())
