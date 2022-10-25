import requests
import asyncio
import time
import aiohttp

start = time.time()
urls = [
    'http://127.0.0.1:5000/lzw', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom'
]


async def get_page(url):
    print('正在下载', url)
    # aiohttp：基于异步网络请求的模块
    # aiohttp使用方法
    async with aiohttp.ClientSession() as session:
        # 对于阻塞使用await手动挂起
        # 代理为proxy = 'http://ip:port'
        async with await session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            # 注意：在获取响应数据之前一定要使用await进行手动挂起
            page_text = await response.text()
            print('下载完毕:', page_text)


tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()

print(end - start)
