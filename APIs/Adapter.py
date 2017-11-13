from APIs import GuardianAPI, NYTimesAPI

def final_adapter(query, number):
    ny_adapter = NYTimesAPI.get_article(query, number)
    g_adapter = GuardianAPI.get_article(query, number)
    return g_adapter + ny_adapter

#print final_adapter("equity europe")
