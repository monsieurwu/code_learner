# 数据库SQlite

安装sqlite

```
sudo apt update
sudo apt install sqlite3
sqlite3 --version
sqlite3 进入数据库
```

sqlite命令：属于数据库通用的语言

使用命令行操作数据库：系统命令+sql命令

创建数据库文件

```
sqlite3 student.db
```

db=database

.help可以看到有哪些命令

命令分为系统命令和sql命令 sql命令不以 .开头 但以；结尾	系统命令 ， 都以'.'开头

系统命令 ， 都以'.'开头

```
.exit  退出
.quit	退出
.table   查看表格
.schema  查看表的结构
.database：列出当前打开的数据库 查看打开的数据库
```

sql语句， 都以‘;’结尾

```sqlite
    1-- 创建一张表
        create table stuinfo(id integer, name text, age integer, score float);
            
    2-- 插入一条记录
        insert into stuinfo values(1001, 'zhangsan', 18, 80);//全部插入
        insert into stuinfo (id, name, score) values(1002, 'lisi', 90);//部分插入

    3-- 查看数据库记录
        select * from stuinfo;
        select * from stuinfo where score = 80;//where表示条件查询
        select * from stuinfo where score = 80 and name= 'zhangsan';//and表示与
        select * from stuinfo where score = 80 or name='wangwu';//or表示或
        select name,score from stuinfo;  查询指定的字段
        select * from stuinfo where score >= 85 and score < 90;

    4-- 删除一条记录
        delete from stuinfo where id=1003 and name='zhangsan';

    5-- 更新一条记录
        update stuinfo set age=20 where id=1003;//将id为1003的age改成20
        update stuinfo set age=30, score = 82 where id=1003;

    6-- 删除一张表
        drop table stuinfo;

    7-- 增加一列
        alter table stuinfo add column sex char;//修改表 插入字段

    8-- 删除一列（不支持直接删除一列）
        create table stu as select id, name, score from stuinfo;//创建一张新的表 只要一部分
        drop table stuinfo;//删除原来的表
        alter table stu rename to stuinfo;//对新表格进行改名字
```

sqlite不会进行类型检查 有可能会造成传错数据

使用c语言操作数据库

SQLite编程接口

```
 int sqlite3_open(
  const char *filename,   /* Database filename (UTF-8) */
  sqlite3 **ppDb          /* OUT: SQLite db handle */
 );
功能：打开数据库
参数：filename  数据库名称
      ppdb      数据库句柄
返回值：成功为0 SQLITE_OK ,出错 错误码

int sqlite3_close(sqlite3* db);
功能：关闭数据库
参数：操作数据库的指针
返回值：成功为0 SQLITE_OK ,出错 错误码

const char *sqlite3_errmsg(sqlite3*db);
功能：得到错误信息的描述
```

sqlite api接口：https://www.sqlite.org/cintro.html

