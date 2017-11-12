import NYTimesAPI, GuardianAPI

def final_adapter(query):
    ny_adapter = NYTimesAPI.get_article(query)
    g_adapter = GuardianAPI.get_article(query)
    return g_adapter + ny_adapter

#print final_adapter("equity europe")
