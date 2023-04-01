

import requests

def query_train_info(train_no, from_station, to_station, depart_date):
    url = f'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no={train_no}&from_station_telecode={from_station}&to_station_telecode={to_station}&depart_date={depart_date}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
        'Referer': f'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={from_station},XAY&ts={to_station},ZEK&date={depart_date}&flag=N,N,Y',
        'Host': 'kyfw.12306.cn',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.get(url, headers=headers)
    data = response.json()['data']['data']
    print(data)
    for item in data:
        #过滤数据中"isEnabled":false的数据
        if item['isEnabled']:
            print(f"| {item['station_no']} | {item['station_name']} | {item['arrive_time']} | {item['start_time']} | {item['stopover_time']} |")

query_train_info('490000Z2720A', 'QDK', 'XAY', '2023-04-01')
