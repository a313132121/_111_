import requests
import json
from urllib.parse import quote  #https://blog.csdn.net/weixin_43788986/article/details/125572389

testurl2 = 'https://jable.tv/rss/'
def check(alive, proxy, apiurl, sema, timeout, testurl):
    try:
        #urllib.parse.quote()   https://blog.csdn.net/weixin_43788986/article/details/125572389
        #quote() 介绍2：https://blog.csdn.net/weixin_43411585/article/details/89067127
        r = requests.get(f"http://127.0.0.1:9090/proxies/{quote(proxy['name'], safe='')}/delay", params={
            'url': testurl,
            'timeout': timeout
        }, timeout=10)
        response = json.loads(r.text)
        print(response)
        if response['delay'] > 0:
            alive['proxies'].append(proxy)
    except Exception as e:
        print(e)
        pass
    sema.release()
    """
    try:
        #url =apiurl + '/proxies/' + str(proxy['name']) + '/delay?url='+testurl+'&timeout=' + str(timeout)
        url =apiurl + '/proxies/' + str(proxy['name']) + '/delay?url='+testurl2+'&timeout=' + str(timeout)
        r = requests.get(url, timeout=10)
        response = json.loads(r.text)
        print(response)
        if response['delay'] > 0:
            alive.append(proxy)
            
            url =apiurl + '/proxies/' + str(proxy['name']) + '/delay?url='+testurl2+'&timeout=' + str(timeout)
            r = requests.get(url, timeout=10)
            response = json.loads(r.text)
            if response['delay'] > 0:
                alive.append(proxy)
            
    except:
        pass
    sema.release()
    """
"""
ping:
    https://www.google.com/favicon.ico
    https://netflav.com/static/assets/favicon.ico
    https://jable.tv/rss/
download:
    http://speedtest-sgp1.digitalocean.com/10mb.test 为单点新加坡服务器，使用一些冷门线路VPS的时候因线路影响，不能获得更加准确的实际速度测试。
    （推荐）使用cloudflare或者cachefly的10mb的cdn文件，可以获得更加准确的测试（cloudflare对客户端的ip识别更加准确，推荐使用，cachefly可作为备用）.
    url1：https://speed.cloudflare.com/__down?bytes=10000000
    url2：http://cachefly.cachefly.net/10mb.test
"""
