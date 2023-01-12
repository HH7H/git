import requests,random,json,time

ID = '2132531310'
token = '5105584144:AAGUqOnoYk78YYWypvIDt2cXLutmddBAHA4'

def auto_set(username):
    ID = '2132531310'
    token = '5105584144:AAGUqOnoYk78YYWypvIDt2cXLutmddBAHA4'
    url = 'https://api22-normal-c-useast1a.tiktokv.com/passport/login_name/update/?residence=IQ&device_id=7092527186544330246&os_version=15.3&iid=7092527941028710149&app_name=musical_ly&locale=en&ac=WIFI&sys_region=US&js_sdk_version=1.77.0.2&version_code=19.3.0&vid=C6A977A1-AC7C-4D0E-9533-1FCD3972CE85&channel=App%20Store&op_region=US&tma_jssdk_version=1.77.0.2&os_api=18&idfa=00000000-0000-0000-0000-000000000000&device_platform=ipad&device_type=iPad8,9&openudid=af8fe64533f89787cca093de7dc2eade9805bd86&account_region=&tz_name=Asia/Baghdad&tz_offset=10800&app_language=en&current_region=IQ&build_number=193021&aid=1233&mcc_mnc=&screen_width=1668&uoo=1&content_language=&language=en&cdid=D6735DD9-F38C-4EEA-BBBD-93EFA5C2DE37&app_version=19.3.0'
    headers = {'Host': 'api22-normal-c-useast1a.tiktokv.com','Connection': 'keep-alive','Content-Length': '21','passport-sdk-version': '5.12.1','x-Tt-Token': '03de2d7e3d054063d67eed7b0e9f79f68105d966eb5e19c18016d1088749c0fe354bf8a3f77cd65eb82d94408793f756420ef7dfd70fac98b3d73d30ea371902bd37e06a1765af88be49aa95c7f4eb0036a06983f398ff90bda38066b88ba274f33b1-CkA5NmRjMDhmZGRlYmUxZmQxOTAwMWIzYWFmOTAyMzY1YTBkYjU2OGMwNWI2YmQ1Y2FiMzNmNzI0NGMwOWJhOTky-2.0.0','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'TikTok 19.3.0 rv:193021 (iPad; iOS 15.3; en_US) Cronet','x-tt-cmpl-token': 'AgQQAPPdF-RPsIxUvaZQuZk8-Awu1lZZv4QsYMsQ-A','sdk-version': '2','x-tt-dm-status': 'login=1;ct=1','X-SS-STUB': '7AA2C4AD930CC2736D695B70BBB55969','x-tt-store-idc': 'maliva','x-tt-store-region': 'iq','X-SS-DP': '1233','x-tt-trace-id': '00-ab8f16e810626db7e5f9c686063504d1-ab8f16e810626db7-01','Cookie': 'install_id=7169698265780471557; ttreq=1$493562f43587bf8f4ab1ad295bb07928d4f38c8c; passport_csrf_token=680df2306a1fe23b9b2f2d2ff6722458; passport_csrf_token_default=680df2306a1fe23b9b2f2d2ff6722458; multi_sids=7040135185870521345%3Add04a2d320d977227a0c53ca95c180f6%7C6659226266413776901%3Ade2d7e3d054063d67eed7b0e9f79f681; odin_tt=8ba5e002d575f7586e021902adcd86d1278b41e25d691dd18496dc992eaaa57c4f13b25eefe53b53c49c47f680f0f107ab7978c6363351cbc21904dcb7c171b6b88910a0682e4b37636972371b46139e; cmpl_token=AgQQAPPdF-RPsIxUvaZQuZk8-Awu1lZZv4QsYMsQ-A; d_ticket=d932243ce6acd5b1f4f2ec7827f1eddc5eaa9; sid_guard=de2d7e3d054063d67eed7b0e9f79f681%7C1669325560%7C15552000%7CTue%2C+23-May-2023+21%3A32%3A40+GMT; uid_tt=993c7de98edea3b2ef4a01fd725d7a926d6c2de88cd6df139a9d8dfa147558a2; uid_tt_ss=993c7de98edea3b2ef4a01fd725d7a926d6c2de88cd6df139a9d8dfa147558a2; sid_tt=de2d7e3d054063d67eed7b0e9f79f681; sessionid=de2d7e3d054063d67eed7b0e9f79f681; sessionid_ss=de2d7e3d054063d67eed7b0e9f79f681; store-idc=maliva; store-country-code=iq; store-country-code-src=uid; tt-target-idc=useast1a; tt-target-idc-sign=buPuLxBHx9tagraNL4dnX8TwGIg9ylzrcmHfmYxbdxQzRSXxgH0sVUJjxs93MDE8uDQSNtgs--YT8EggU8cZduS1Hp_PuDak6ZCYFSJ797PLtQ1cziIUhJBzxY6I3tCpgp84206mvfDDgdpzUo_FFLeVUWr7tqNyYpYhFTbyE5jfVehL7WdtIKYqhIfGVw8legU5tOe2hc93PVDppdbuQEOBSATKb7ilhxAbrlFnNrtakZ9WoNaTaxjyWl5EqqMc-Y2RUytZ2FxJAVcJrkL13xGrFU2akceYeVGm7mLO1CMPd77kyLJx9eYSD-ck88vNoFtspZNnfHE4dE5F5zUIkSsrWM_QYp-Imz6ua1479Qo_F8zgsa1X0bKqWfvC3JaTiTI9-VIy-CZ2EmjXW09fKO72MdVv3ihnRP6K1qcp-gYpuOdssX8AvfV2vIyCfmel_-fsuDLTLt7-ZRou2YQtXqSAM55xZs2R6DyziJXpf2ACYjjSyT3FsJkbiLlT1pNw; msToken=qjddO2ucnWRK8e8dHyg9sEMrW3SPI6hvzJkF4krHdl1vB6UKKPO7VVVkHJyQQXeNrLsZOBr9ORLqBxut7WRpZu7E','X-Khronos': '1668842679','X-Gorgon': '840280dac80003597624f0294003c34c3c14cdd948eb11d7afef'}
    data = f'login_name={username}'
    response = requests.post(url,headers=headers,data=data).text
    print(response)
    if 'message":"success' in response:
        print('Done username has set')
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&parse_mode-Markdownv2&text=Available: {username}\nauto_set: success")
        exit()
    else:
        print('Unknown error')
        exit()


Cookies = str(input('Cookies:'))
"bm_sv=46832DCFDC148185F7E9074810E3906C~YAAQh30TAkpM0JGFAQAA82V4nBKXK2Skl/wmy0RrgMK/pBNqSC9uIEmksW1MBlh+HPBPrB77lgDDPj6sC8JP2jO0NmTSo97woEF6L89ZYs7ww8pFhI6YoJbHdzaOhaaS6SZv9PIoZMhnmEbL1vTkfMsti24MEVvDAfRoMIQdljwbcli8SVIQ3T/u7FtQaC9uidnB6sS6Z8N9kvWNtBkmoEuiN+1v7NjrmGKyFtJW9g2zUtrRfIacBqJTA5T24fio~1; msToken=g_tiaymR7IHb_dw4VkZHso8QOABaQ0Xw-3FX_WEUdcI00xfaJg7krU9IzQmKS40Wvj8aCD4XcdHbSUCERrEzBzVGscjJ9pU7oJl5KAv_jU29k8elqLslWJ2anzcu7tCgJYtxeVXiUgvvsmE=; _abck=AE7489E3C37DF0D69AF4979ED6B3AA77~-1~YAAQh30TAtlL0JGFAQAAHGF4nAl3lonVhyvd8MBrllQS2ez6GSbg2RXIp4PYuoWtnVyOuCqwaTWIanQ6yiRtPZPQr7vuaFpi554WMmUMhaZWoG0f2JuRwuKSysQcY/tKsAMQtCZVtFMcxuTBKq99RECHYJWd9rZ1yC/haiZPmTxKtZ0O8MKB9qy+zulNLFyLCge/pjbRLc1rVXXSxjGx516W/pUtjWK6ODrlT9LKKHIMdSphTUyijcylgTBJcciEkTjgKviU6BEqa2q5gzpeEKmOWZ/tbrIFmvxEbmX8PqMX3PyMq0whx/1VOKvvycD88PJ2wH6ZMeU12HzS432jebgOA8zcrBaPj5QPE3eBBM6NpO0OcfEoG4ZYbHcQ38zn8BRryqfocHIc4t5wuWSxJQkdUfAs8q6GMQ==~0~-1~-1; msToken=30xBIBg-buR8VeIJNxEuoUML3knVschXxS7Nv8wb1VGUrKwGihJnQom-AwZ59XCowuBopb1K7uum4JJw5SaK1zP-ef5oWzBUKcbADyqSjTYaGXhONzOdn8uij-tREdoNMP0ssNZt1V4rkd0=; odin_tt=00e9aca1537bc30701ff922511eef473c671fe2e2aa3db2f0e026fc7e8dd63aaef2271ba2f5844615c18c7eb08e54b2642530e6dcf0138b1e746085479b899bae60904a38f68d5ca21a5ec156ed68f55; store-country-code=iq; store-country-code-src=uid; store-idc=maliva; tt-target-idc=useast1a; ttwid=1%7CQs6d2ynLwTp5dJqXTWkofjX2idTUq8ZrkNvTVBzjf9w%7C1673367403%7C592cbae710b148df76b7028f3aad724d904215720da3ab6f3d622d5b18994953; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227187058048485246470%22%2C%22timestamp%22:1673367368274}; passport_fe_beating_status=true; tiktok_webapp_theme=light; tt_chain_token=RyElH8SphfAH2E4y2DzjLA==; tt-target-idc-sign=WSbHOiMTZVQNAJvqrbu_DaQxamR3wJKBsn0BOhtsVXB8F0w-VLNRUb2WR01YuakqfgDuxEP5UVqMYhVAIh7PELZZvMVqA_wcFIUhPbBi8xdXaagP3qVfQ4q77gSdQpzivrkHko9kF1jtxdtnNbUMVG4euO6H9GDJmp4GhwC1S5d5SlLftqgvbxJbtcE_tilIw2H-n2tGyZVYGdzfugmp2A_B6Ft2bYUF8Ow-M74COWcIlUiDYD0afyI89yZohnC08_Gc2oXygAUtLSPLbCe5pjY1BLN4URQVtObBjoz6OrHbNXtSr13GWbK8UK50bUNxYbEUXApro7bsvdYyg1tNxADZjYG7bT5SH9OLc9xsYu2Vh_RMC_rwBO4TF-4A7nTLSFktv31fm5rvIu22z-He1jbHsL9AY0IJqMUXk0s1HML8ycLp8izOQbdbT0XfscZf5LrGdHChHayorojWWuO14adUprq3XwGbnbtK14Xoy7TJV1qfMpYsiDsALiEuABC2; cmpl_token=AgQQAPPdF-RO0rI5FGG0o90_-dwWBMeMf4QsYMoXxA; sessionid=39c6f07f471e2a865826c8b8e1a18a16; sessionid_ss=39c6f07f471e2a865826c8b8e1a18a16; sid_guard=39c6f07f471e2a865826c8b8e1a18a16%7C1673367389%7C5184000%7CSat%2C+11-Mar-2023+16%3A16%3A29+GMT; sid_tt=39c6f07f471e2a865826c8b8e1a18a16; sid_ucp_v1=1.0.0-KGY1MTQ4MzM5ZTYyZDNhMzE0Yjk2NWQ0ZDMxZjhmOTFkNmJjMTg3ZDUKIAiGiMTk49j-g2IQ3Z72nQYYswsgDDCK9p-QBjgEQOoHEAMaBm1hbGl2YSIgMzljNmYwN2Y0NzFlMmE4NjU4MjZjOGI4ZTFhMThhMTY; ssid_ucp_v1=1.0.0-KGY1MTQ4MzM5ZTYyZDNhMzE0Yjk2NWQ0ZDMxZjhmOTFkNmJjMTg3ZDUKIAiGiMTk49j-g2IQ3Z72nQYYswsgDDCK9p-QBjgEQOoHEAMaBm1hbGl2YSIgMzljNmYwN2Y0NzFlMmE4NjU4MjZjOGI4ZTFhMThhMTY; uid_tt=e1a5dc861f9f74418317ab66b82d2f731d06e38113528552773c21ddb2f98948; uid_tt_ss=e1a5dc861f9f74418317ab66b82d2f731d06e38113528552773c21ddb2f98948; passport_csrf_token=1697d4754e81852078cb9e4ae8526c8d; passport_csrf_token_default=1697d4754e81852078cb9e4ae8526c8d; ak_bmsc=FD4C07D5E2D05FBD720FF54E9D6B3C1A~000000000000000000000000000000~YAAQnX0TAnEYOJuFAQAAvLF3nBIjQzWm1GCPLR8EBP3gBtuFVyb2V+aLLaR/CDqJORUmO6xCD7hcgZK/6ndnqi2JfFE1oPRbhY9R2BqbHjQ9535dnIuMZzcPCt8tgWjAf4rrJgYZTglk+8l31cW8fkbp3FL096DXsbfVP4z/lpUzDT/bzbedOS3ClvBeJCtNaDBJBbFtqFI8uvJTboauoNUPQLAH5J0+p02uBs0eFokjaoosfghG94JSpQyNlecIHkfYELyhXtXTgUX2KQR0dZ5JG15H85GGtzonvxpA2XkEwgN2baXaDXcGcICQhIY7j/vleN99Y9Sz8sFYOBk5jyRGFXyWMrfr5SpuQI+JqqoqmSGzACPYDJtyg5cbscEolONKuAL19qfeWCfzEWVJOeJH1vbeXeliwrXZOW2tx34ItfojZlelwygq7oNIzDc0BgEJzhFDdVbsXVgo4BkyeaIujwVy2gSsF+fXJe4OKQHx8+7Zh/k1vlE=; bm_sz=852BA28CAED649921BC970E08DE94E18~YAAQnX0TAscXOJuFAQAAMal3nBIbGuznncHYoH/A1wFlKBW4su80Y4lqqvEMWYSSumDRkSKXIrzuPlOag68TEXJHHgPC+eOXj4GvPWJe3PBWS/6YFlY58LrAZGkWSS0wXui/2mSgmsgCprLFzS8rOdiAFp3q8/5qN5ttzGffm/ECTHxc0/tVu+OEYVmRHWCGH3rdw1Dq5tHsHdanZn415c7+carNNaQZSb4ni6522GvnFcVmONZncft2NP8IBkGSwOMQkvUPDOxgED2oZPJmqM8aZZuom666twcQw1HO4UzhzJ4=~4337714~4339763; tt_csrf_token=QG8vl6b0-aJLCRF9Rukb6NzhXbBOPy8Q6mzM"


N = 1
R,G,Y,W = '\x1b[1;31m','\x1b[1;32m','\x1b[1;33m','\x1b[0m'
Length = int(input('Length:'))
while True:
    username = str(''.join(random.choice('qwerfdsazxc_v4132tgbu.jmnhy756_iklop089.') for x in range(Length)))
    url = f'https://www.tiktok.com/api/uniqueid/check/?aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&unique_id={username}'
    response = requests.post('https://tt.hh7h.repl.co/api/signer/',data={"Token": "main-HH7H@api","url": url}).json()
    response = requests.get(url=response["signed_url"],headers={"User-Agent": response["userAgent"],"Cookie": Cookies}).json()
    try:
        if response['is_valid'] == True:
            print(f'{W}{N}: {W}[{G}Available{W}]: {username}');N += 1
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&parse_mode-Markdownv2&text=Available: {username}\nauto_set: wait")
            auto_set(username)
            break
        elif response['is_valid'] == False:
            print(f'{W}{N}: {W}[{R}Unavailable{W}]: {username}');N += 1
    except:
        if response['status_msg'] == 'Login expired':
            print(f'{W}Invale cookies')
            break
        else:
            print(f'{W}Unknown error')
            break

print(f'{W}Tool has stop')
