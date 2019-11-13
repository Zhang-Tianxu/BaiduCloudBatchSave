## 声明：
为了方便写了一个批量转存百度云盘共享资源的python脚本，不知道是否损害谁的权益，如果有，请联系笔者，笔者会在第一时间删除。也希望各位朋友不要滥用。

# 简单描述
* 利用selenium这个自动化的webdriver实现。所以需要安装selenium：`pip install selenium`。
* 并且需要安装与浏览器相对应的webdriver。比如笔者的浏览器是Google Chrome 78.0.3904.87（正式版本） （64 位），所以需要chromedriver的对应版本（我也从墙外下载了78版）
* 另外为了实现免登录，还需要查看cookies的两个，这两个cookie是非常私密的数据，如果泄露，就相当于泄露了百度云盘账户。
* 想要批量转存的共享资源应该存储在`resource.csv`文件中，`百度云链接`对应共享资源的链接，`百度提取码`对应共享资源的提取码。如果不存在提取码，对应位置留空即可
其他的大家就看代码吧
