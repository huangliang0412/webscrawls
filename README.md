# 异步网络爬虫
使用python3 实现爬虫调度器，url管理器， 网页解析器，文件下载器，ip代理池
使用asyncio 和 aiohttp　来实现异步网络请求

### 调度器
设置入口url，采用生产者－消费者模式，采用协程的方式
参考http://python.jobbole.com/87310/
同时加开一个进程，每隔15分钟更新一次ip代理池

### URL管理器
最初使用python中的set集合，实现url管理器的去重和存储，后来使用redis中的set集合，实现url
的去重和存储

### 网页解析器
使用beautisoup对得到的网页内容进行解析，获取新的url和图片url地址，分别存储到redis数据库中

### 网页下载器　和　文件下载器
使用aiohttp库，实现网路的异步请求

### ip代理池
使用request同步获取西刺免费代理的ip地址，并对ip地址进行检测筛选，更新，并存储到redis中
