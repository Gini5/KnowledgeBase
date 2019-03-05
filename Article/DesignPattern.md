* 面试题：
	* https://blog.csdn.net/coolwriter/article/details/79794309
	
* ACID:
	* Atomicity: 原子性体现在对于一个事务来讲，要么一起执行成功要么一起失败，执行的过程中是不能被打断或者执行其他操作的。
	*  Consistency: 一致性表现为事务进行过后和执行前，整体系统都是稳定的，事务必须始终保持系统处于一致的状态，不管在任何给定的时间并发事务有多少。比如对于入账出账操作是不会有总资金的变化的。
	*  Isolation: 隔离性表示各个事务之间不会互相影响，数据库一般会提供多种级别的隔离。实际上多个事务是并发执行的，但是他们之间不会互相影响。
	*  Durability: 持久性表示一旦一个事务成功了，那么他的改变是永久性的被记录和操作。
	
* Database Normalization：
	* Normalization is a systematic approach of decomposing tables, to eliminate data redundancy, insert/update/delete anomalies, ensure data dependencies make sense.
	* Update anomaly: when updating employee address, update is partially successful, will cause data inconsistence

	* Insertion anomaly: can't insert a new member has not been assigned to teach course, except by setting course code to NULL

	* Deletion anomaly: delete teach course entry will delete that faculty member information

	
* Normalization:

	* 第一范式：属性是不可分割的
	* 第二范式：非主键属性，完全依赖于主键属性
	例如：订单号，联系人号，联系人名在一张表里，主键是订单号和联系人号，联系人名非完全依赖主键，就应该拆分
	* 第三范式：非主键属性无传递依赖，非主键属性依赖其他非主键属性而不是主键。
	 Trasitive dependency: When a non-prime attribute depends on other non-prime attributes rather than depending upon the prime attributes or primary key
		
		比如Student表（学号，姓名，年龄，性别，所在院校，院校地址，院校电话）
		这样一个表结构，就存在上述关系。 学号--> 所在院校 --> (院校地址，院校电话)
		这样的表结构，我们应该拆开来，如下。（学号，姓名，年龄，性别，所在院校）--（所在院校，院校地址，院校电话）
		
	• 超键：能唯一标识组的属性
	• 候选键：不含多余属性的超键
	• 主键：用户选作元组标识的候选键
	• 外键：一张表的某个属性是另一张表的主键
	
	
* 建索引原则:
	1. 在经常用作过滤器的字段上建立索引； 
	2. 索引的选择性（Selectivity），是指不重复的索引值（也叫基数，Cardinality）与表记录数（#T）的比值比较高的
	3. 在SQL语句中经常进行GROUP BY、ORDER BY的字段上建立索引； 
	4. 在不同值较少的字段上不必要建立索引，如性别字段； 
	5. 对于经常存取的列避免建立索引； 
	6. 用于联接的列（主健/外健）上建立索引； 
	7. 在经常存取的多个列上建立复合索引，但要注意复合索引的建立顺序要按照使用的频度来确定； 
	8. 缺省情况下建立的是非簇集索引，但在以下情况下最好考虑簇集索引，如：含有有限数目（不是很少）唯一的列；进行大范围的查询；充分的利用索引可以减少表扫描I/0的次数，有效的避免对整表的搜索。当然合理的索引要建立在对各种查询的分析和预测中，也取决于DBA的所设计的数据库结构。 
	• https://blog.csdn.net/u013412790/article/details/51612304
	
* SQL related:
	* Where vs having: 
	where、聚合函数、having 在from后面的执行顺序：where>聚合函数(sum,min,max,avg,count)>having 
	即where在分组之前过滤行数据，having在分组之后过滤。 
	Where后不能接聚合函数，having可以。
	having不能对没有select的字段过滤，where可以。
	From <https://blog.csdn.net/jdjh1024/article/details/76647866> 
	From <https://blog.csdn.net/yexudengzhidao/article/details/54924471> 
	* 聚集索引和非聚集索引：https://www.cnblogs.com/hyd1213126/p/5828937.html
		• https://jingyan.baidu.com/article/e73e26c0f1e82d24acb6a75d.html
		• 聚集索引是索引逻辑顺序和数据物理顺序一致（一个表只包含一个聚集索引）
		• 非聚集索引是索引的逻辑顺序和数据内容的物理顺序不一致的
		• 在数据库中以二叉树形式表现，聚集索引的叶节点即数据，非聚集索引叶节点会指向数据
		
* 数据库查询语句速度优化：
	* 建索引 
	* 减少表之间的关联 
	* 优化sql，尽量让sql很快定位数据，不要让sql做全表查询，应该走索引 
	* 简化查询字段，没用的字段不要，已经对返回结果的控制，尽量返回少量数据 
	From <https://www.2cto.com/database/201710/688377.html> 
		* Use join instead of sub statement
		* Avoid like '%test%'，通配符出现在开头，无法使用索引
		* Avoid using calculation in where statement
		* Avoid using != or <> in where statement
		* 应注意在 where 子句中使用 or 来连接条件，如果一个字段有索引，一个字段没有索引，将导致引擎放弃使用索引而进行全表扫描
		* 应尽量避免在where子句中对字段进行函数操作，这将导致引擎放弃使用索引而进行全表扫描。如：	
	select id from t where substring(name,1,3)='abc'--name以abc开头的id	
	应改为:	
	select id from t where name like 'abc%'	
		From <https://blog.csdn.net/jie_liang/article/details/77340905> 
		From <https://blog.csdn.net/wuhuagu_wuhuaguo/article/details/72875054> 
		
* UNION vs UNION ALL:
	* UNION selects distinct values while UNION ALL allows duplicate values
* Condition:
	* CASE WHEN a='1' THEN 'ok' ELSE 'not ok' END
* SELECT * FROM table LIMIT 1 OFFSET 10
* MySQL:
	1. Search engine:
		| a. InnoDB                      | MyISAM                             |  |  |
| ------------------------------ | ---------------------------------- |  |  |
| B+Tree                         | B+Tree                             |  |  |
| 聚集索引，数据文件本身是主索引 | 非聚集索引，索引文件和数据文件分离 |  |  |
| 叶节点data域保存完整数据记录 | 叶节点data域存放数据记录的地址 |  |  |

	2. 索引匹配：在联合索引（列ABC）中
		a. 全列匹配：where A='xx' and B = 'xx' and C='xx' （顺序可以颠倒, MySQL查询优化器会调整）
		b. 最左前缀匹配：
			where A='xx'，只用到索引的A列
			where A = 'xx' and C = 'xx', 只用到索引中的A列
				解决：可考虑 A='xx' and B IN(全部值) and C='xx'，如果B列值较少
			Where A<'xx' and B='xx'，只用到A列索引，索引可以用到范围列(必须是最左前缀)，但范围列后的列无法用索引
		c. 没用索引: where C = 'xx' 当不指定第一列时不用索引
	3. 前缀索引：用列的前缀代替整个列作为索引key, 通过索引选择性值来判断优化程度。Select count(distinct(left(A,3))/count(*）计算索引选择性
