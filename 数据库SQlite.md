# 数据库SQlite

安装sqlite

```c
sudo apt update
sudo apt install sqlite3
sqlite3 --version
sqlite3 进入数据库
```

sqlite命令：属于数据库通用的语言

使用命令行操作数据库：系统命令+sql命令

创建数据库文件

```c
sqlite3 student.db
```

db=database

.help可以看到有哪些命令

命令分为系统命令和sql命令 sql命令不以 .开头 但以；结尾	系统命令 ， 都以'.'开头

系统命令 ， 都以'.'开头

```c
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

```c
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

student.c

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>

#define  DATABASE  "student.db"
#define  N  128
//实现增删改查的四个函数
int do_insert(sqlite3 *db)
{
	int id;
	char name[32] = {};
	char sex;
	int score;
	char sql[N] = {};
	char *errmsg;

	printf("Input id:");
	scanf("%d", &id);

	printf("Input name:");
	scanf("%s", name);
	getchar();

	printf("Input sex:");
	scanf("%c", &sex);

	printf("Input score:");
	scanf("%d", &score);

	sprintf(sql, "insert into stu values(%d, '%s', '%c', %d)", id, name, sex, score);

	if(sqlite3_exec(db, sql, NULL, NULL, &errmsg) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
	}
	else
	{
		printf("Insert done.\n");
	}

	return 0;
}
int do_delete(sqlite3 *db)
{
	int id;
	char sql[N] = {};
	char *errmsg;

	printf("Input id:");
	scanf("%d", &id);

	sprintf(sql, "delete from stu where id = %d", id);

	if(sqlite3_exec(db, sql, NULL, NULL, &errmsg) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
	}
	else
	{
		printf("Delete done.\n");
	}

	return 0;
}
int do_update(sqlite3 *db)
{
	int id;
	char sql[N] = {};
	char name[32] = "zhangsan";
	char *errmsg;

	printf("Input id:");
	scanf("%d", &id);

	sprintf(sql, "update stu set name='%s' where id=%d", name,id);

	if(sqlite3_exec(db, sql, NULL, NULL, &errmsg) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
	}
	else
	{
		printf("update done.\n");
	}

	return 0;
}


int callback(void *arg, int f_num, char ** f_value, char ** f_name)
{
	int i = 0;

	for(i = 0; i < f_num; i++)
	{
	//	printf("%-8s %s", f_value[i], f_name[i]);
		printf("%-8s", f_value[i]);
	}

	printf("++++++++++++++++++++++");
	putchar(10);

	return 0;
}

int do_query(sqlite3 *db)
{
	char *errmsg;
	char sql[N] = "select count(*) from stu where name='zhangsan';";//sql语句

	if(sqlite3_exec(db, sql, callback,NULL , &errmsg) != SQLITE_OK)
	{
		printf("%s", errmsg);
	}
	else
	{
		printf("select done.\n");
	}
}

int do_query1(sqlite3 *db)
{
	char *errmsg;
	char ** resultp;
	int nrow;
	int ncolumn;

	if(sqlite3_get_table(db, "select * from stu", &resultp, &nrow, &ncolumn, &errmsg) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
		return -1;
	}
	else
	{
		printf("query done.\n");
	}

	int i = 0;
	int j = 0;
	int index = ncolumn;

	for(j = 0; j < ncolumn; j++)
	{
		printf("%-10s ", resultp[j]);
	}
	putchar(10);

	for(i = 0; i < nrow; i++)
	{
		for(j = 0; j < ncolumn; j++)
		{
			printf("%-10s ", resultp[index++]);
		}
		putchar(10);
	}

return 0;
}

int main(int argc, const char *argv[])
{
	sqlite3 *db;
	char *errmsg;
	int n;//cmd
	
	if(sqlite3_open(DATABASE, &db) != SQLITE_OK)//打开数据库
	{
		printf("%s\n", sqlite3_errmsg(db));
		return -1;
	}
	else
	{
		printf("open DATABASE success.\n");//打开成功
	}
//打开数据库后对数据库进行增删改查
	if(sqlite3_exec(db, "create table if not exists stu(id int, name char , sex char , score int);",//执行sql语句
				NULL, NULL, &errmsg) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
	}
	else
	{
		printf("Create or open table success.\n");
	}

	while(1)
	{
		printf("********************************************\n");
		printf("1: insert  2:query  3:delete 4:update 5:quit\n");
		printf("********************************************\n");
		printf("Please select:");
		scanf("%d", &n);

		switch(n)
		{
			case 1:
				do_insert(db);
				break;
			case 2:
				do_query(db);
			//	do_query1(db);
				break;
			case 3:
				do_delete(db);
				break;
			case 4:
				do_update(db);
				break;
			case 5:
				printf("main exit.\n");
				sqlite3_close(db);
				exit(0);
				break;
			default :
				printf("Invalid data n.\n");
		}

	}
	return 0;
}
```

