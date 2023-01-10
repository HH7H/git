import requests,random,execjs,json,time

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


Cookies = input("cookies:")

tt_headers = {'Host': 'www.tiktok.com','Connection': 'keep-alive','Cookie': Cookies,'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',}


N = 1
R,G,Y,W = '\x1b[1;31m','\x1b[1;32m','\x1b[1;33m','\x1b[0m'
Length = int(input('Length:'))
while True:
    username = str(''.join(random.choice('qwerfdsazxc_v4132tgbu.jmnhy756_iklop089.') for x in range(Length)))
    params = f'aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&unique_id={username}'
    bogus = execjs.compile(open('main.js','r').read()).call('_0x32d649',params)
    response = requests.get(url='https://www.tiktok.com/api/uniqueid/check/?'+params+'&X-Bogus='+bogus,headers=tt_headers).json()
    try:
        if response['is_valid'] == True:
            print(f'{W}{N}: {W}[{G}Available{W}]: {username}');N += 1
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
