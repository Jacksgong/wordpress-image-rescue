#!/usr/bin/python
import MySQLdb
import re
import os.path

__author__ = 'jacksgong'
__date__ = 'Jan 22, 2015'

wp_path = raw_input('wordpress path(example: /var/www/blog.dreamtobe.cn/html/): ')
wp_domain = raw_input('domain(example: http://blog.dreamtobe.cn): ')

mysql_user_name = raw_input('mysql user name: ')
mysql_passwd = raw_input('mysql password: ')
blog_database_name = raw_input('mysql blog database: ')

wp_img_path = wp_path + '/wp-content/uploads'

db = MySQLdb.connect(use_unicode=1, charset='utf8', host="localhost",
                     user=mysql_user_name,
                     passwd=mysql_passwd,
                     db=blog_database_name)
try:
    cur = db.cursor()

    cur.execute("select post_title, post_content, ID from wp_posts")

    change_posts_num = 0
    change_img_url_num = 0

    for row in cur.fetchall():
        lines = row[1].split('\n')
        print str(row[2]) + row[0] + '\n---------------------\n'
        content = ''

        is_need_update = False

        for line in lines:
            if '<img ' in line:
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                  line)
                for url in urls:

                    if url.isspace():
                        continue

                    if not url.startswith(wp_domain):
                        continue

                    path = wp_path + url[url.find('/wp-content'):]
                    print url
                    print path + '\n'

                    if not os.path.isfile(path):
                        img_url_pre, s, old_img_file = url.rpartition('/')

                        new_img_file = raw_input('file not exist, new image file name: ')
                        if new_img_file.isspace() or new_img_file == '':
                            print 'skip ~~'
                            continue

                        line = line.replace(url, img_url_pre + '/' + new_img_file)
                        print 'new url:' + img_url_pre + '/' + new_img_file
                        is_need_update = True
                        change_img_url_num += 1

            content += line + '\n'

        if is_need_update:
            change_posts_num += 1
            sql = "update wp_posts set post_content = %s where ID = %s"
            # print sql
            cur.execute(sql, (content, row[2]))
            db.commit()
            print("update done. ID = %ld" % row[2])

    print 'Complete scan, replace %d image url from %d posts' % (change_img_url_num, change_posts_num)



finally:
    db.close()
