import NYTimesAPI, GuardianAPI

ny_adapter = NYTimesAPI.get_article()
#print ny_adapter
g_adapter = GuardianAPI.get_article()
final_adapter = g_adapter + ny_adapter
