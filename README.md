##Repair broken image url on wordpress posts

>I changed my vps server recently, and I had to migrating my wordpress blog too. I found there are several trouble when I completed migrating, and the most serious trouble is some image in some posts was broken. so here come.

---
### How to use
####I、 Just run python:

```
python wordpress_fix_img.py
```
####II、 Input data:

```
wordpress path(example: /var/www/blog.dreamtobe.cn/html/): [your wordpress absolute path]
domain(example: http://blog.dreamtobe.cn): [your wordpress blog domain]
mysql user name: [your wordpress blog mysql user name]
mysql password: [your wordpress blog mysql password]
mysql blog database: [your wordpress blog mysql database name]
```
####III、Auto find broken image

In this phase, will auto find break image by python and print all image url in posts. Just like:

```
2092Android UI设计 layout布局 屏幕底部的菜单栏 动画切换Activity
---------------------

http://blog.dreamtobe.cn/wp-content/uploads/2012/12/13064789290.png
/var/www/blog.dreamtobe.cn/html//wp-content/uploads/2012/12/13064789290.png

2093判断字符串string是数字、json结构、xml结构
---------------------

2094Android 搜索关键字飞入飞出效果
---------------------

2095android ViewFlipper 左右滑动效果
---------------------

http://blog.dreamtobe.cn/wp-content/uploads/2012/12/6597299564586277972.jpg
/var/www/blog.dreamtobe.cn/html//wp-content/uploads/2012/12/6597299564586277972.jpg

http://blog.dreamtobe.cn/wp-content/uploads/2012/12/97108866982854788.jpg
/var/www/blog.dreamtobe.cn/html//wp-content/uploads/2012/12/97108866982854788.jpg

http://blog.dreamtobe.cn/wp-content/uploads/2012/12/2493868293673906770.jpg
/var/www/blog.dreamtobe.cn/html//wp-content/uploads/2012/12/2493868293673906770.jpg

2096在activity中实例化 layout（利用xml创建layout)
---------------------
```
####IV、Provide right image name
In 3 phase, you need provide right image file name when find break image, such as:

```
http://blog.dreamtobe.cn/wp-content/uploads/2014/12/endDocument1.jpg
/var/www/blog.dreamtobe.cn/html//wp-content/uploads/2014/12/endDocument1.jpg

file not exist, new image file name: [enter right image file name](e.g endDocument.jpg)
```
Press enter, and python will autocompleted image right url, and output:

```
new image url:http://blog.dreamtobe.cn/wp-content/uploads/2014/12/endDocument.jpg
```
And after the completion of the full content of the post scan output:

```
update done. ID =2160L
```
#### V、Repeate 3~4 & end
As end will output:

```
Complete scan, replace 25 image url from 21 posts
```
