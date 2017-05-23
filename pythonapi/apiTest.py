from pythonApi import PythonApi
from uniFiCredentials import UniFiCredentials

credentials = UniFiCredentials()
api = PythonApi(user=credentials.username, password=credentials.password, base_url=credentials.base_url,
                version=credentials.version)
api.verify_ssl = False
api.debug = True

if api.login():
    sites = api.list_sites()
    print(sites)
    for site in sites['data']:
        api.site = site['name']
        site_stats = api.stat_sessions()
        print(site_stats)
    if api.logout():
        print('Finished')
