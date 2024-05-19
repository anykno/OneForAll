import os
# 模块API配置
# Censys可以免费注册获取API：https://censys.io/api
censys_api_id = os.getenv('CENSYS_API_ID')
censys_api_secret = os.getenv('CENSYS_API_SECRET')

# Binaryedge可以免费注册获取API：https://app.binaryedge.io/account/api
# 免费的API有效期只有1个月，到期之后可以再次生成，每月可以查询250次。
binaryedge_api = os.getenv('BINARYEDGE_API')

# BeVigil API: https://bevigil.com/osint-api
bevigil_api = os.getenv('BEVIGIL_API')

# Chinaz可以免费注册获取API：http://api.chinaz.com/ApiDetails/Alexa
chinaz_api = os.getenv('CHINAZ_API')

# Bing可以免费注册获取API：https://azure.microsoft.com/zh-cn/services/
# cognitive-services/bing-web-search-api/#web-json
bing_api_id = os.getenv('BING_API_ID')
bing_api_key = os.getenv('BING_API_KEY')

# SecurityTrails可以免费注册获取API：https://securitytrails.com/corp/api
securitytrails_api = os.getenv('SECURITYTRAILS_API')

# https://fofa.so/api
fofa_api_email = os.getenv('FOFA_API_EMAIL')  # fofa用户邮箱
fofa_api_key = os.getenv('FOFA_API_KEY')  # fofa用户key

# Google可以免费注册获取API:
# 免费的API只能查询前100条结果
# https://developers.google.com/custom-search/v1/overview#search_engine_id
# 创建自定义搜索引擎后需要在响应的控制面板上启用Search the entire web
google_api_id = os.getenv('GOOGLE_API_ID')  # Google API自定义搜索引擎id
# https://developers.google.com/custom-search/v1/overview#api_key
google_api_key = os.getenv('GOOGLE_API_KEY')  # Google API自定义搜索key

# https://api.passivetotal.org/api/docs/
riskiq_api_username = os.getenv('RISKIQ_API_USERNAME')
riskiq_api_key = os.getenv('RISKIQ_API_KEY')

# Shodan可以免费注册获取API: https://account.shodan.io/register
# 免费的API限速1秒查询1次
shodan_api_key = os.getenv('SHODAN_API_KEY')
# ThreatBook API 查询子域名需要收费 https://x.threatbook.cn/nodev4/vb4/myAPI
threatbook_api_key = os.getenv('THREATBOOK_API_KEY')

# VirusTotal可以免费注册获取API: https://developers.virustotal.com/reference
virustotal_api_key = os.getenv('VIRUSTOTAL_API_KEY')

# https://www.zoomeye.org/doc?channel=api
zoomeye_api_key = os.getenv('ZOOMEYE_API_KEY')

# Spyse可以免费注册获取API: https://spyse.com/
spyse_api_token = os.getenv('SPYSE_API_TOKEN')

# https://www.circl.lu/services/passive-dns/
circl_api_username = os.getenv('CIRCL_API_USERNAME')
circl_api_password = os.getenv('CIRCL_API_PASSWORD')

# https://www.dnsdb.info/
dnsdb_api_key = os.getenv('DNSDB_API_KEY')

# ipv4info可以免费注册获取API: http://ipv4info.com/tools/api/
# 免费的API有效期只有2天，到期之后可以再次生成，每天可以查询50次。
ipv4info_api_key = os.getenv('IPV4INFO_API_KEY')

# https://github.com/360netlab/flint
# passivedns_api_addr默认空使用http://api.passivedns.cn
# passivedns_api_token可为空
passivedns_api_addr = os.getenv('PASSIVEDNS_API_ADDR')
passivedns_api_token = os.getenv('PASSIVEDNS_API_TOKEN')

# Github Token可以访问https://github.com/settings/tokens生成,user为Github用户名
# 用于子域接管和子域收集
github_api_user = os.getenv('GITHUB_API_USER')
github_api_token = os.getenv('GITHUB_API_TOKEN')

# obtain Cloudflare API key from https://dash.cloudflare.com/profile/api-tokens
cloudflare_api_token = os.getenv('CLOUDFLARE_API_TOKEN')

# https://hunter.qianxin.com/home/userInfo
hunter_api_key = os.getenv('HUNTER_API_KEY')

# https://api-docs.fullhunt.io/
fullhunt_api_key = os.getenv('FULLHUNT_API_KEY')


# 登录quake之后可在个人中心获取key https://quake.360.net/quake/#/personal?tab=message
quake_api_key = os.getenv('QUAKE_API_KEY')

#https://www.racent.com/ctlog F2>Network抓包获取Token
racent_api_token = os.getenv('RACENT_API_TOKEN')
