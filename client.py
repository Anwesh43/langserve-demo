from langserve import RemoteRunnable 

def initializeClient():
    joke = RemoteRunnable("http://localhost:8080/joke")
    result = joke.invoke({"topic": "football"})
    print(result.content)


if __name__ == "__main__":
    initializeClient()
