### 1. bloom filter/布隆过滤器     
（1） 哈希表    
布隆过滤器类似于哈希表，哈希表的结构： HashTable + 拉链存储      
输入元素通过哈希函数获取index后，存入相应的位置；位置冲突时，会在index处开一个链表，来存储后续相同index的值           

两者对比：   
- 哈希表是一个没有误差的数据结构，所有的元素所需的位置和内存大小，哈希表都会进行存储   
- 布隆过滤器是一种为了更高效的工业级数据结构，负责判断元素是否存在     

（2）布隆过滤器     
由一个很长的二进制向量和一系列随机映射函数组成，用于检索一个元素是否在一个集合中        
优点：空间效率、查询时间 远远超过一般的算法   
缺点：有一定的误识别率和删除困难     

（3）使用案例  
- 比特币网络
- 分布式系统
- Redis缓存
- 垃圾邮件、评论等过滤  