代码来自：https://github.com/rookiesmile/yibanAutoSgin 大佬

# 易班晚点签到

### 实现功能
* 晚点位置签到

### 注意修改签到位置

在`config.py`文件中

```python
address = '{"Reason":"","AttachmentFileName":"","LngLat":"102.449018,24.875743","Address":"xx省 xx市 xxx学校xxx楼 "}'
```

需要修改`LngLat`和`Address`

获取签到座标及地址可以从: https://lbs.amap.com/tools/picker 处获取

### 环境
python3.10

### 运行方式

```shell
git clone https://ghproxy.com/https://github.com/a2574286996/yiban.git
cd yiban
python main.py
```
推荐使用crontab

```shell
0 21 * * * python3 /root/Documents/Python/yiban/main.py
```
(仅供参考)
