import tweepy as tw

api_key = "EZAulGwSL1s1kscbu7E41TMut"
api_secret = "6bSevJY5A8cfEdjjTeliaNtXVHMpBizAw76NZ0Ht2wVGlPuq3D"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAHWlmgEAAAAAxn2OlnDnCFPbrnY3abSy%2FEP6gA0%3DARpjQNKMtBvsrc0HaxWtaXtuPZeM8GUXq4ruLCADH5oOV6Ne6a"
access_token = "1645947217050746880-LEtnRBszyUH2rmCGn9X8GRVzy5VErT"
access_token_secret = "HJuLgF1qhmRkXxg4XXGMsUoPYEsQnxJulT0Fa3NG22Oda"

client = tw.client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tw.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
