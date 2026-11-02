import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('dsavd.db')

# 创建一个Cursor对象
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS exam")

# 创建考试题库表，包含选择题和判断题，以及所属章节
cursor.execute("""
CREATE TABLE IF NOT EXISTS exam (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    option4 TEXT,

    correct_answer TEXT NOT NULL,
    answer_analy TEXT,
    question_type TEXT NOT NULL CHECK(question_type IN ('0', '1')), -- 0: 选择题, 1: 判断题
    chapter TEXT NOT NULL,
    subchapter TEXT NOT NULL
)
""")

# 清空数据库

#  1.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 数据结构是指（ ）的集合以及它们之间的关系。 (2分)
', 'A. 数据元素', 'B. 计算方法', 'C. 逻辑存储', 'D. 数据映像',  'B', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 下列特性中，不是算法必须具备的特性是（ ）。 (2分)
', 'A. 有穷性', 'B. 确定性', 'C. 高效性', 'D. 可行性',  'C', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 算法应该具有确定性、可行性和有穷性，其中有穷性是指（ ）。 (2分)
', 'A. 算法在有穷的时间内终止', 'B. 输入是有穷的', 'C. 输出是有穷的', 'D. 描述步骤是有穷的',  'A', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 算法分析是对已设计的算法进行评价，其主要目的是（ ）。 (2分)
', 'A. 找出数据结构的合理性', 'B. 研究算法中输入和输出的关系', 'C. 分析算法的效率以求改进', 'D. 分析算法的易读性和文档性',  'C', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 算法分析的两个主要方面是（ ）。 (2分)
', 'A. 空间性能和时间性能', 'B. 正确性和简明性', 'C. 可读性和文档性', 'D. 数据复杂性和程序复杂性',  'A', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 某算法的时间复杂度是O(n^2)，表明该算法（ ）。 (2分)
', 'A.  问题规模是n^2', 'B. 执行时间等于n^2', 'C. 执行时间与n^2成正比', 'D. 问题规模与n^2成正比',  'C', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 对于数据结构的描述，下列说法中不正确的是（ ）。 (2分)
', 'A. 相同的逻辑结构对应的存储结构也必相同', 'B. 数据结构由逻辑结构、存储结构和基本操作三方面组成', 'C. 数据结构基本操作的实现与存储结构有关', 'D. 数据的存储结构是逻辑结构的机内实现',  'A', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 链接存储结构中数据元素之间的逻辑关系由（ ）表示。 (2分)
', 'A. 线性结构', 'B. 非线性结构', 'C. 存储位置', 'D. 指针',  'D', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 顺序存储结构中数据元素之间的逻辑关系由（ ）表示。 (2分)
', 'A. 线性结构', 'B. 计算方法', 'C. 逻辑存储', 'D. 数据映像',  'B', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在存储数据时，通常不仅要存储各数据元素的值，还要存储（ ）。 (2分)
', 'A. 数据的处理方法', 'B. 数据元素的类型', 'C. 数据元素之间的关系', 'D. 数据的存储方法',  'C', '无','0','1' ,'1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 链表是一个线性数据结构。 (2分)', 'A. 是', 'B. 否', 'A', '链表是一种线性数据结构，其元素通过指针连接。', '1', '1', '1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 堆排序的时间复杂度为O(n log n)。 (2分)', 'A. 是', 'B. 否', 'A', '堆排序的时间复杂度最坏情况下为O(n log n)。', '1', '1', '1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 在图的邻接矩阵表示法中，如果图是稀疏的，存储空间的浪费较大。 (2分)', 'A. 是', 'B. 否', 'A', '邻接矩阵占用O(n^2)的空间，对于稀疏图来说存储效率低。', '1', '1', '1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 快速排序的最坏时间复杂度为O(n^2)。 (2分)', 'A. 是', 'B. 否', 'A', '快速排序的最坏时间复杂度出现在输入数据已经有序的情况下，此时为O(n^2)。', '1', '1', '1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 在哈希表中，使用链地址法时每个桶的元素数量最多为1。 (2分)', 'A. 是', 'B. 否', 'B', '链地址法允许一个桶中有多个元素。', '1', '1', '1.1')
""")

# ----------------------111111111111111111111111111111111111111111----------------------------1.2
# ----------------------111111111111111111111111111111111111111111----------------------------1.2
# ----------------------111111111111111111111111111111111111111111----------------------------1.2

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 数据结构的基本概念是什么？ (2分)', 'A. 数据元素的集合及其关系', 'B. 数据的存储方式', 'C. 数据的运算规则', 'D. 数据的存储算法', 
'A', '数据结构是数据元素的集合及其关系，常常通过逻辑结构和存储结构进行表达。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 以下哪种数据结构属于线性结构？ (2分)', 'A. 栈', 'B. 堆', 'C. 图', 'D. 树', 'A', '线性结构是元素之间有且只有一个前驱和一个后继关系。栈属于线性结构。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 队列（Queue）遵循什么原则？ (2分)', 'A. 先进先出', 'B. 后进先出', 'C. 随机访问', 'D. 随机存储', 'A', '队列遵循先进先出（FIFO）原则。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 链表中的每个节点包含哪些部分？ (2分)', 'A. 数据和指针', 'B. 数据和两个指针', 'C. 数据和指针及状态', 'D. 数据和标志位', 'A', '链表节点包含数据部分和指向下一个节点的指针。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 在二叉树中，最大度为多少？ (2分)', 'A. 1', 'B. 2', 'C. 3', 'D. 4', 'B', '在二叉树中，每个节点最多有两个子节点，因此节点的最大度为2。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 图的深度优先遍历（DFS）的基本思想是什么？ (2分)', 'A. 从根节点出发，优先访问左子树', 'B. 从根节点出发，优先访问未被访问过的邻接节点', 'C. 从根节点出发，按层级访问所有节点', 'D. 从根节点出发，优先访问右子树', 'B', '深度优先遍历是从根节点出发，优先访问未被访问过的邻接节点，直到不能继续访问为止。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 树的高度是指什么？ (2分)', 'A. 树的深度', 'B. 根节点到叶节点的最长路径长度', 'C. 所有叶节点的深度最大值', 'D. 从根节点到任意一个节点的距离', 'B', '树的高度是根节点到叶节点的最长路径的长度。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 在哈希表中，冲突是指什么？ (2分)', 'A. 哈希值相同的元素', 'B. 元素的值相同', 'C. 哈希表的容量不足', 'D. 哈希函数不能有效分配元素', 'A', '哈希冲突是指不同的元素被映射到哈希表中的相同位置。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 在堆（Heap）中，父节点的值与子节点的关系是什么？ (2分)', 'A. 父节点值大于子节点值', 'B. 父节点值小于子节点值', 'C. 父节点值与子节点值相等', 'D. 父节点值与子节点值无关', 'A', '在堆中，父节点的值大于或等于子节点的值（大根堆）。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 以下哪项不是图的遍历方式？ (2分)', 'A. 广度优先遍历', 'B. 深度优先遍历', 'C. 最短路径遍历', 'D. 无', 'C', '最短路径遍历不是一种标准的图遍历方式。', '0', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 数据结构的存储结构可以分为顺序存储和链式存储。 (2分)', 'A. 是', 'B. 否', 'A', '数据结构的存储结构通常包括顺序存储和链式存储。', '1', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 树的深度优先遍历和广度优先遍历的区别是遍历的顺序不同。 (2分)', 'A. 是', 'B. 否', 'A', '树的深度优先遍历和广度优先遍历是通过不同的顺序进行节点访问的。', '1', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 图的邻接矩阵存储方式适用于稀疏图。 (2分)', 'A. 是', 'B. 否', 'B', '图的邻接矩阵存储方式适用于稠密图，因为稀疏图中大部分矩阵元素为零，浪费空间。', '1', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 哈希表的查找时间复杂度为O(1)。 (2分)', 'A. 是', 'B. 否', 'A', '哈希表的查找时间复杂度在理想情况下为O(1)，即常数时间复杂度。', '1', '1', '1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 二叉树的最小深度是从根节点到最近叶节点的路径长度。 (2分)', 'A. 是', 'B. 否', 'A', '二叉树的最小深度是从根节点到最近的叶节点的路径长度。', '1', '1', '1.2')
""")

# ----------------------111111111111111111111111111111111111111111----------------------------1.3
# ----------------------111111111111111111111111111111111111111111----------------------------1.3
# ----------------------111111111111111111111111111111111111111111----------------------------1.3
# ----------------------111111111111111111111111111111111111111111----------------------------1.3
# cursor.execute("""
# INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
# VALUES ('1. 数据结构是指（ ）的集合以及它们之间的关系。 (2分)
# ', 'A. 数据元素', 'B. 计算方法', 'C. 逻辑存储', 'D. 数据映像',  'B', '无','0','1' ,'1.1')
# """)
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 什么是算法的时间复杂度？ (2分)', 'A. 算法执行的总时间', 'B. 算法中最复杂操作的时间', 'C. 算法执行所需的输入大小与输出大小的关系', 'D. 算法执行过程中所涉及的所有数据量的和', 
'C', '时间复杂度是指算法的运行时间与问题规模之间的关系。', '0', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 以下哪个算法属于分治算法？ (2分)', 'A. 快速排序', 'B. 插入排序', 'C. 归并排序', 'D. 堆排序', 'C', '归并排序是一种典型的分治算法，将问题分解为子问题，递归解决并合并结果。', '0', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 哈希表中的冲突解决方法有哪几种？ (2分)', 'A. 开放地址法与链地址法', 'B. 线性探测法与二次探测法', 'C. 链式哈希与静态哈希', 'D. 顺序查找与二分查找', 'A', '哈希表的冲突解决方法主要包括开放地址法和链地址法。', '0', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 在堆排序中，堆的结构是什么？ (2分)', 'A. 完全二叉树', 'B. 有序二叉树', 'C. 二叉搜索树', 'D. 平衡二叉树', 'A', '堆排序基于完全二叉树的结构，通常使用大根堆或小根堆来进行排序。', '0', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 快速排序的最坏时间复杂度是多少？ (2分)', 'A. O(n log n)', 'B. O(n^2)', 'C. O(log n)', 'D. O(n)', 'B', '快速排序的最坏时间复杂度为O(n^2)，通常出现在数据已经有序或接近有序的情况下。', '0', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 什么是动态规划？ (2分)', 'A. 一种贪心算法', 'B. 通过递归的方式解决问题', 'C. 通过将问题分解成子问题并存储子问题的解来避免重复计算', 'D. 一种图的遍历方法', 'C', '动态规划通过将问题分解为子问题，并存储已解决子问题的结果，避免重复计算。', '0', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 以下哪种排序算法是稳定的？ (2分)', 'A. 快速排序', 'B. 堆排序', 'C. 冒泡排序', 'D. 选择排序', 'C', '冒泡排序是一种稳定的排序算法，即相同元素的相对顺序不会改变。', '0', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 在归并排序中，分治的“分”阶段如何进行？ (2分)', 'A. 将数组分为两半并递归排序', 'B. 将数组拆分为若干个子数组', 'C. 对数组进行排序后合并', 'D. 将数组元素顺序交换', 'A', '归并排序通过将数组分为两半递归排序，然后合并两个已排序的子数组。', '0', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 在图的深度优先遍历中，使用了什么数据结构？ (2分)', 'A. 队列', 'B. 栈', 'C. 哈希表', 'D. 堆', 'B', '深度优先遍历使用栈来追踪访问的节点。', '0', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 以下哪种数据结构适合用来实现优先队列？ (2分)', 'A. 数组', 'B. 链表', 'C. 堆', 'D. 栈', 'C', '堆是一种适合实现优先队列的数据结构，能够快速找到最大或最小元素。', '0', '1', '1.3')
""")
# cursor.execute("""
# INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
# VALUES ('15. 二叉树的最小深度是从根节点到最近叶节点的路径长度。 (2分)', 'A. 是', 'B. 否', 'A', '二叉树的最小深度是从根节点到最近的叶节点的路径长度。', '1', '1', '1.2')
# """)

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 算法的时间复杂度是指算法执行所需的时间与输入数据量之间的关系。 (2分)', 'A. 是', 'B. 否', 'A', '时间复杂度衡量的是算法执行时间与输入数据量之间的关系。', '1', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 所有的排序算法都是稳定的。 (2分)', 'A. 是', 'B. 否', 'B', '并不是所有排序算法都稳定，快速排序和选择排序是不稳定的。', '1', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 图的广度优先遍历可以通过递归实现。 (2分)', 'A. 是', 'B. 否', 'B', '广度优先遍历通常使用队列来实现，而非递归。', '1', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 动态规划只能应用于最优化问题。 (2分)', 'A. 是', 'B. 否', 'A', '动态规划主要应用于最优化问题，通过分解子问题来得到最优解。', '1', '1', '1.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 哈希表查找的平均时间复杂度为O(1)。 (2分)', 'A. 是', 'B. 否', 'A', '在理想情况下，哈希表的查找操作的平均时间复杂度为O(1)。', '1', '1', '1.3')
""")

# ----------------------222222222222222222222222----------------------------2.1
# ----------------------222222222222222222222222----------------------------2.1
# ----------------------222222222222222222222222----------------------------2.1
# ----------------------222222222222222222222222----------------------------2.1
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 线性表的逻辑结构中，元素之间的关系是怎样的？ (2分)', 'A. 元素之间没有关系', 'B. 元素之间有顺序关系', 'C. 元素之间有树形结构关系', 'D. 元素之间有图的关系', 'B', '线性表的逻辑结构中，元素之间有顺序关系。', '0', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 线性表包括哪些基本类型？ (2分)', 'A. 数组和链表', 'B. 队列和栈', 'C. 树和图', 'D. 数组、链表、队列和栈', 'D', '线性表包括数组、链表、队列和栈等基本类型。', '0', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 以下关于线性表的描述中，哪个是错误的？ (2分)', 'A. 线性表中的元素是有序的', 'B. 线性表可以是动态大小的', 'C. 线性表的元素之间没有顺序关系', 'D. 线性表可以用数组或链表实现', 'C', '线性表中的元素是有序的，因此元素之间有顺序关系。', '0', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 链表与数组在存储结构上的主要区别是什么？ (2分)', 'A. 数组是顺序存储，链表是链式存储', 'B. 链表是顺序存储，数组是链式存储', 'C. 数组比链表更灵活', 'D. 数组不需要额外的空间', 'A', '链表是链式存储，数组是顺序存储，两者的存储结构不同。', '0', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 下列哪种操作在线性表的数组实现中最为高效？ (2分)', 'A. 插入操作', 'B. 删除操作', 'C. 查找操作', 'D. 修改操作', 'C', '在数组实现的线性表中，查找操作效率最高，因为可以通过索引直接访问元素。', '0', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 在链表中，删除一个元素的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'A', '在链表中，删除操作的时间复杂度是O(1)，只需改变指针即可。', '0', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 队列的基本操作有哪些？ (2分)', 'A. 入栈、出栈', 'B. 入队、出队', 'C. 添加、删除', 'D. 查找、删除', 'B', '队列的基本操作是入队（enqueue）和出队（dequeue）。', '0', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 栈的插入和删除操作是在哪一端进行的？ (2分)', 'A. 任意端', 'B. 前端', 'C. 后端', 'D. 同一端', 'D', '栈的插入和删除操作都发生在栈的同一端，即栈顶。', '0', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 以下关于循环队列的描述哪个是正确的？ (2分)', 'A. 循环队列使用数组实现，但不允许队列末尾与队头重叠', 'B. 循环队列不使用数组实现', 'C. 循环队列的数组存储结构是线性结构', 'D. 循环队列允许队列末尾与队头重叠', 'D', '循环队列的特殊之处在于它允许队列末尾与队头重叠，形成环形结构。', '0', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 链表的优点是什么？ (2分)', 'A. 查找速度较快', 'B. 动态大小调整', 'C. 存储效率高', 'D. 支持随机访问', 'B', '链表的优点是它的动态大小调整，可以根据需要灵活地插入和删除元素。', '0', '2', '2.1')
""")

### 判断题：

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 线性表的元素之间必须具有顺序关系。 (2分)', 'A. 是', 'B. 否', 'A', '线性表中的元素之间必须具有顺序关系，这是线性表的定义特点。', '1', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 数组和链表都是线性表。 (2分)', 'A. 是', 'B. 否', 'A', '数组和链表都属于线性表，它们的元素具有顺序关系。', '1', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 栈和队列都属于线性表。 (2分)', 'A. 是', 'B. 否', 'A', '栈和队列都是线性表，但它们具有不同的操作方式（栈是后进先出，队列是先进先出）。', '1', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 链表的查找效率比数组低。 (2分)', 'A. 是', 'B. 否', 'A', '链表的查找效率较低，因为需要从头节点开始遍历。', '1', '2', '2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 循环队列的队列大小是固定的。 (2分)', 'A. 是', 'B. 否', 'A', '循环队列的大小在初始化时确定，并且是固定的。', '1', '2', '2.1')
""")

# ----------------------222222222222222222222222----------------------------2.2
# ----------------------222222222222222222222222----------------------------2.2
# ----------------------222222222222222222222222----------------------------2.2
# ----------------------222222222222222222222222----------------------------2.2
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 顺序表的存储方式是？ (2分)', 'A. 顺序存储', 'B. 链式存储', 'C. 数组存储', 'D. 动态存储', 'A', '顺序表是一种顺序存储结构，通常使用数组来实现。', '0', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 顺序表的元素在内存中是如何排列的？ (2分)', 'A. 按照元素的顺序排列', 'B. 按照元素的哈希值排列', 'C. 随机排列', 'D. 依据链表结构排列', 'A', '顺序表中的元素在内存中是连续排列的，按照元素的顺序依次存储。', '0', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 以下哪项是顺序表的优点？ (2分)', 'A. 支持动态扩展', 'B. 查找操作时间复杂度为O(1)', 'C. 插入和删除操作高效', 'D. 支持随机访问', 'B', '顺序表支持随机访问，通过索引可以直接访问任意元素，查找操作的时间复杂度为O(1)。', '0', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 顺序表在插入和删除元素时的主要缺点是什么？ (2分)', 'A. 时间复杂度为O(1)', 'B. 需要移动大量元素', 'C. 只能存储相同类型的元素', 'D. 插入和删除操作很容易', 'B', '在顺序表中，插入和删除元素时需要移动大量元素，时间复杂度为O(n)。', '0', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 顺序表中的元素如何进行查找？ (2分)', 'A. 通过元素的值查找', 'B. 通过索引查找', 'C. 通过指针查找', 'D. 通过链表查找', 'B', '顺序表中的元素可以通过索引直接查找，时间复杂度为O(1)。', '0', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 顺序表的动态扩展通常采用什么方法？ (2分)', 'A. 使用指针扩展', 'B. 按比例增加数组的大小', 'C. 使用链表连接', 'D. 分配更多内存', 'B', '顺序表的动态扩展通常是按比例增加数组的大小，常见的增长策略是将数组大小增加一倍。', '0', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 顺序表的空间利用率随着元素的增加而如何变化？ (2分)', 'A. 增加', 'B. 减少', 'C. 不变', 'D. 无法预测', 'B', '随着顺序表中元素的增加，未使用的空间减少，导致空间利用率降低。', '0', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 在顺序表中，如何快速访问第i个元素？ (2分)', 'A. 通过链表索引', 'B. 通过数组索引', 'C. 通过指针定位', 'D. 通过顺序查找', 'B', '顺序表中元素可以通过数组的索引直接访问，时间复杂度为O(1)。', '0', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 如果顺序表的容量满了，下一步应该做什么？ (2分)', 'A. 扩展容量', 'B. 丢弃新插入的数据', 'C. 重新排序元素', 'D. 合并多个顺序表', 'A', '如果顺序表的容量满了，应该扩展容量，通常是按比例增加数组大小。', '0', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 顺序表的空间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(n^2)', 'D. O(log n)', 'B', '顺序表的空间复杂度为O(n)，其中n为元素个数。', '0', '2', '2.2')
""")

### 判断题：
cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 顺序表的元素存储方式是连续的。 (2分)', 'A. 是', 'B. 否', 'A', '顺序表中的元素在内存中是连续存储的。', '1', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 顺序表支持随机访问。 (2分)', 'A. 是', 'B. 否', 'A', '顺序表支持随机访问，可以通过索引直接访问元素。', '1', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 顺序表在插入和删除操作时效率较高。 (2分)', 'A. 是', 'B. 否', 'B', '顺序表在插入和删除元素时需要移动大量元素，效率较低。', '1', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 顺序表的大小是固定的，不能动态扩展。 (2分)', 'A. 是', 'B. 否', 'B', '顺序表的大小是可以动态扩展的，通常通过重新分配数组实现。', '1', '2', '2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 顺序表的元素在内存中是按顺序存储的。 (2分)', 'A. 是', 'B. 否', 'A', '顺序表中的元素在内存中是顺序存储的，按照元素的顺序排列。', '1', '2', '2.2')
""")

# ----------------------222222222222222222222222----------------------------2.2.1
# ----------------------222222222222222222222222----------------------------2.2.1
# ----------------------222222222222222222222222----------------------------2.2.1
# cursor.execute("""
# INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
# VALUES ('1. 数据结构是指（ ）的集合以及它们之间的关系。 (2分)# ', 'A. 数据元素', 'B. 计算方法', 'C. 逻辑存储', 'D. 数据映像',  'B', '无','0','1' ,'1.1')
# """)
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 顺序存储结构是线性表的哪种存储方式？ (2分)', 'A. 线性链表', 'B. 数组存储', 'C. 哈希表存储', 'D. 树形存储', 'B', '顺序存储结构是通过数组来实现线性表的存储。', '0', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 顺序表中的元素是如何存储的？ (2分)', 'A. 按照元素的地址存储', 'B. 按顺序依次存储在连续的内存空间中', 'C. 按照元素的哈希值存储', 'D. 每个元素通过指针链接', 'B', '顺序表中的元素在内存中是按顺序依次存储在连续的内存空间中。', '0', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 顺序表的优点是什么？ (2分)', 'A. 支持随机访问', 'B. 支持动态扩展', 'C. 支持插入和删除操作', 'D. 操作简单且元素存储连续', 'A', '顺序表支持随机访问，可以通过下标直接访问任意元素。', '0', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 顺序表在插入和删除元素时的主要缺点是？ (2分)', 'A. 时间复杂度为O(1)', 'B. 需要移动大量元素', 'C. 只能存储相同类型元素', 'D. 空间复杂度过高', 'B', '顺序表在插入和删除元素时需要移动大量元素，特别是在数组中间插入或删除时。', '0', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 顺序表的存储空间利用率如何变化？ (2分)', 'A. 随着元素增加，利用率降低', 'B. 随着元素增加，利用率提高', 'C. 空间利用率保持不变', 'D. 无法确定', 'A', '随着顺序表中元素增加，未使用的空间减少，导致空间利用率降低。', '0', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 动态扩展顺序表时，通常采取什么策略？ (2分)', 'A. 增加容量到原来的两倍', 'B. 增加容量到原来的三倍', 'C. 使用链表扩展', 'D. 不支持动态扩展', 'A', '顺序表通常采用按比例扩展的策略，如将容量增加到原来的两倍。', '0', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 在顺序表中，如何实现随机访问？ (2分)', 'A. 通过数组下标', 'B. 通过指针访问', 'C. 通过链表索引', 'D. 通过哈希查找', 'A', '顺序表支持通过数组下标直接访问元素，时间复杂度为O(1)。', '0', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 顺序表的空间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '顺序表的空间复杂度为O(n)，其中n为元素的个数。', '0', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 在顺序表中，删除操作的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '在顺序表中，删除操作的时间复杂度为O(n)，因为删除元素后可能需要移动多个元素。', '0', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 顺序表适用于哪些应用场景？ (2分)', 'A. 元素需要频繁插入和删除', 'B. 需要快速随机访问', 'C. 需要动态调整大小', 'D. 数据量过大时', 'B', '顺序表适用于需要快速随机访问元素的场景，但插入和删除操作较慢。', '0', '2', '2.2.1')
""")

### 判断题：
# cursor.execute("""
# INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
# VALUES ('11. 数据对象就是一组任意数据元素的集合。 (2分)# ', 'A. 是', 'B. 否',  'B', '无','1','1' ,'1.1')
# """)

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 顺序表支持快速插入和删除操作。 (2分)', 'A. 是', 'B. 否', 'B', '顺序表在插入和删除操作时需要移动大量元素，效率较低。', '1', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 顺序表中的元素是按照元素的顺序依次存储在连续的内存空间中的。 (2分)', 'A. 是', 'B. 否', 'A', '顺序表中的元素在内存中是连续存储的，按照元素的顺序排列。', '1', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 顺序表的动态扩展不会影响原有元素的存储位置。 (2分)', 'A. 是', 'B. 否', 'B', '顺序表的动态扩展通常会分配一个新的更大的数组，因此原有元素需要被复制到新数组中。', '1', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 顺序表支持通过索引直接访问任何一个元素。 (2分)', 'A. 是', 'B. 否', 'A', '顺序表通过数组下标支持直接访问任何一个元素，时间复杂度为O(1)。', '1', '2', '2.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 顺序表的空间复杂度通常与元素个数无关。 (2分)', 'A. 是', 'B. 否', 'B', '顺序表的空间复杂度为O(n)，其中n为元素的个数。', '1', '2', '2.2.1')
""")

# ----------------------222222222222222222222222----------------------------2.2.2
# ----------------------222222222222222222222222----------------------------2.2.2
# ----------------------222222222222222222222222----------------------------2.2.2
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 顺序表的插入操作的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '在顺序表中，插入操作最坏情况下需要移动元素，时间复杂度为O(n)。', '0', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 顺序表中删除元素时，最坏情况下的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '在删除元素时，最坏情况下需要移动多个元素，因此时间复杂度为O(n)。', '0', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 顺序表在插入元素时，如果当前表满了，通常的处理方式是什么？ (2分)', 'A. 丢弃插入的元素', 'B. 增加容量并复制原有元素', 'C. 删除一个元素', 'D. 直接覆盖插入位置的元素', 'B', '当顺序表满时，通常通过增加容量并将原有元素复制到新的空间来扩展表的大小。', '0', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 顺序表的查找操作的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(log n)', 'C. O(n)', 'D. O(n^2)', 'C', '顺序表的查找操作通常需要遍历表中的所有元素，最坏情况下时间复杂度为O(n)。', '0', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 顺序表在查找操作中的效率通常受到什么因素的影响？ (2分)', 'A. 元素个数', 'B. 元素大小', 'C. 操作的类型', 'D. 操作次数', 'A', '顺序表的查找效率通常与元素个数相关，元素越多，查找时间越长。', '0', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 在顺序表中，删除一个元素的过程通常包括哪些步骤？ (2分)', 'A. 查找元素并将其删除', 'B. 直接删除元素并更新数组长度', 'C. 查找元素并移动后续元素', 'D. 直接删除元素并调整内存', 'C', '在顺序表中，删除元素时，需要先查找元素，然后将其后的元素前移。', '0', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 顺序表的扩展操作是如何进行的？ (2分)', 'A. 新增元素时直接扩展数组', 'B. 数组满时增加固定大小的空间', 'C. 数组满时增加原有数组大小的一倍', 'D. 数组不会扩展', 'C', '顺序表扩展时，通常将原有数组大小加倍，确保扩展后的数组足够存储新的元素。', '0', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 顺序表中查找操作的最坏时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '顺序表的查找操作最坏情况下需要遍历所有元素，因此时间复杂度为O(n)。', '0', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 顺序表支持的基本操作不包括哪项？ (2分)', 'A. 查找', 'B. 插入', 'C. 删除', 'D. 排序', 'D', '顺序表的基本操作通常包括查找、插入和删除，而排序操作需要借助其他算法实现。', '0', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 在顺序表中，如何实现插入操作？ (2分)', 'A. 直接将元素添加到末尾', 'B. 在指定位置插入元素并移动后续元素', 'C. 替换指定位置的元素', 'D. 插入元素并扩展内存', 'B', '顺序表的插入操作需要将新元素放入指定位置，并将该位置之后的元素后移。', '0', '2', '2.2.2')
""")

### 判断题：

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 顺序表的插入操作必须保证元素顺序不变。 (2分)', 'A. 是', 'B. 否', 'A', '在顺序表中，插入元素时需要保持元素的顺序，因此插入后需要移动元素。', '1', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 在顺序表中，删除元素时不需要移动其他元素。 (2分)', 'A. 是', 'B. 否', 'B', '删除元素时，通常需要将该元素后面的所有元素向前移动，以保证表的连续性。', '1', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 顺序表在扩展时会重新分配一块新的内存空间。 (2分)', 'A. 是', 'B. 否', 'A', '当顺序表扩展时，通常会重新分配一块更大的内存空间，并将原有数据复制过去。', '1', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 顺序表的查找操作是基于顺序访问的。 (2分)', 'A. 是', 'B. 否', 'A', '顺序表的查找操作是基于顺序访问的，通常需要从头到尾逐一检查元素。', '1', '2', '2.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 在顺序表中，插入操作的时间复杂度为O(1)。(2分)', 'A. 是', 'B. 否', 'B', '顺序表的插入操作最坏情况下时间复杂度为O(n)，因为需要移动元素。', '1', '2', '2.2.2')
""")

# ----------------------222222222222222222222222----------------------------2.2.3
# ----------------------222222222222222222222222----------------------------2.2.3
# ----------------------222222222222222222222222----------------------------2.2.3

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 单链表中插入元素的时间复杂度为多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '在单链表中插入元素时，最坏情况下需要遍历链表，时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 单链表的删除操作中，最坏情况下需要遍历多少次？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '删除操作最坏情况下需要找到指定元素，时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 单链表的查找操作最坏情况下的时间复杂度是？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '单链表的查找操作最坏情况下需要遍历整个链表，时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 在单链表中，删除一个元素通常需要进行什么操作？ (2分)', 'A. 查找元素并删除', 'B. 直接删除元素并更新链表头', 'C. 查找元素并调整链表指针', 'D. 直接删除元素并不需要更新链表', 'C', '删除元素时，需要查找元素并调整指针来删除目标元素。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 单链表相较于顺序表的一个主要优点是什么？ (2分)', 'A. 查找速度更快', 'B. 插入和删除速度更快', 'C. 占用更少内存', 'D. 实现更简单', 'B', '单链表的插入和删除操作无需移动其他元素，效率较高。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 单链表中的反转操作时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '单链表的反转操作需要遍历链表一次，时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 单链表的尾插法插入元素时，时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '尾插法插入元素时需要遍历整个链表，最坏情况下时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 如果单链表的头指针为空，表示什么情况？ (2分)', 'A. 链表为空', 'B. 链表已满', 'C. 链表正在扩展', 'D. 链表已排序', 'A', '当单链表的头指针为空时，表示链表为空，没有任何元素。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 在单链表中，如何实现删除链表尾部元素？ (2分)', 'A. 遍历链表找到尾部元素并删除', 'B. 直接删除尾部元素', 'C. 修改头指针', 'D. 修改尾指针并删除', 'A', '删除尾部元素通常需要遍历链表找到尾节点，然后调整指针。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 在单链表中，如何判断链表是否为空？ (2分)', 'A. 头指针为null', 'B. 头指针指向一个节点', 'C. 链表长度为0', 'D. 尾指针为null', 'A', '如果头指针为null，表示链表为空。', '0', '2', '2.3')
""")

### 判断题：
cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 单链表中的节点只能包含数据和指针。 (2分)', 'A. 是', 'B. 否', 'A', '单链表中的每个节点通常包含数据和指向下一个节点的指针。', '1', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 单链表的反转操作需要使用额外的内存空间。 (2分)', 'A. 是', 'B. 否', 'A', '反转单链表通常需要使用额外的指针来改变节点的链接，因此需要额外的空间。', '1', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 单链表的删除操作效率低于顺序表。 (2分)', 'A. 是', 'B. 否', 'B', '单链表的删除操作通常只需要修改指针，不需要移动其他元素，因此删除效率较高。', '1', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 在单链表中，插入元素时必须保持元素的顺序。 (2分)', 'A. 是', 'B. 否', 'A', '在单链表中插入元素时需要保持元素的顺序，插入操作通常不会改变已有元素的顺序。', '1', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 单链表中不能实现尾部插入操作。 (2分)', 'A. 是', 'B. 否', 'B', '单链表可以实现尾部插入操作，尽管尾插法需要遍历整个链表。', '1', '2', '2.3')
""")

# ----------------------222222222222222222222222----------------------------2.3
# ----------------------222222222222222222222222----------------------------2.3
# ----------------------222222222222222222222222----------------------------2.3

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 单链表中插入元素的时间复杂度为多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '在单链表中插入元素时，最坏情况下需要遍历链表，时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 单链表的删除操作中，最坏情况下需要遍历多少次？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '删除操作最坏情况下需要找到指定元素，时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 单链表的查找操作最坏情况下的时间复杂度是？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '单链表的查找操作最坏情况下需要遍历整个链表，时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 在单链表中，删除一个元素通常需要进行什么操作？ (2分)', 'A. 查找元素并删除', 'B. 直接删除元素并更新链表头', 'C. 查找元素并调整链表指针', 'D. 直接删除元素并不需要更新链表', 'C', '删除元素时，需要查找元素并调整指针来删除目标元素。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 单链表相较于顺序表的一个主要优点是什么？ (2分)', 'A. 查找速度更快', 'B. 插入和删除速度更快', 'C. 占用更少内存', 'D. 实现更简单', 'B', '单链表的插入和删除操作无需移动其他元素，效率较高。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 单链表中的反转操作时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '单链表的反转操作需要遍历链表一次，时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 单链表的尾插法插入元素时，时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '尾插法插入元素时需要遍历整个链表，最坏情况下时间复杂度为O(n)。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 如果单链表的头指针为空，表示什么情况？ (2分)', 'A. 链表为空', 'B. 链表已满', 'C. 链表正在扩展', 'D. 链表已排序', 'A', '当单链表的头指针为空时，表示链表为空，没有任何元素。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 在单链表中，如何实现删除链表尾部元素？ (2分)', 'A. 遍历链表找到尾部元素并删除', 'B. 直接删除尾部元素', 'C. 修改头指针', 'D. 修改尾指针并删除', 'A', '删除尾部元素通常需要遍历链表找到尾节点，然后调整指针。', '0', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 在单链表中，如何判断链表是否为空？ (2分)', 'A. 头指针为null', 'B. 头指针指向一个节点', 'C. 链表长度为0', 'D. 尾指针为null', 'A', '如果头指针为null，表示链表为空。', '0', '2', '2.3')
""")

### 判断题：
cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 单链表中的节点只能包含数据和指针。 (2分)', 'A. 是', 'B. 否', 'A', '单链表中的每个节点通常包含数据和指向下一个节点的指针。', '1', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 单链表的反转操作需要使用额外的内存空间。 (2分)', 'A. 是', 'B. 否', 'A', '反转单链表通常需要使用额外的指针来改变节点的链接，因此需要额外的空间。', '1', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 单链表的删除操作效率低于顺序表。 (2分)', 'A. 是', 'B. 否', 'B', '单链表的删除操作通常只需要修改指针，不需要移动其他元素，因此删除效率较高。', '1', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 在单链表中，插入元素时必须保持元素的顺序。 (2分)', 'A. 是', 'B. 否', 'A', '在单链表中插入元素时需要保持元素的顺序，插入操作通常不会改变已有元素的顺序。', '1', '2', '2.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 单链表中不能实现尾部插入操作。 (2分)', 'A. 是', 'B. 否', 'B', '单链表可以实现尾部插入操作，尽管尾插法需要遍历整个链表。', '1', '2', '2.3')
""")

# ----------------------222222222222222222222222----------------------------2.3.1
# ----------------------222222222222222222222222----------------------------2.3.1
# ----------------------222222222222222222222222----------------------------2.3.1
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 在链式存储结构中，节点包含哪些基本部分？ (2分)', 'A. 数据和前驱指针', 'B. 数据和后继指针', 'C. 数据和指向下一个节点的指针', 'D. 数据和键值对', 'C', '链式存储结构中的每个节点包含数据和指向下一个节点的指针。', '0', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 以下哪个是链表的优点？ (2分)', 'A. 存储空间利用率低', 'B. 插入和删除操作效率高', 'C. 随机访问效率高', 'D. 支持动态扩展', 'B', '链表的插入和删除操作效率较高，尤其在已知位置时。', '0', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 哪种链表可以从任意节点开始向前或向后遍历？ (2分)', 'A. 单链表', 'B. 双链表', 'C. 循环链表', 'D. 静态链表', 'B', '双链表的节点有两个指针，可以支持双向遍历。', '0', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 在单链表中，如何删除一个节点？ (2分)', 'A. 修改前后节点的指针', 'B. 直接删除节点', 'C. 先反转链表，再删除节点', 'D. 不需要任何操作', 'A', '在单链表中，删除一个节点需要修改前后节点的指针。', '0', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 下列哪种操作在链式存储结构中时间复杂度较高？ (2分)', 'A. 插入头部', 'B. 查找元素', 'C. 删除节点', 'D. 插入尾部', 'B', '链式存储结构中的查找操作需要遍历链表，因此时间复杂度为O(n)。', '0', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 什么情况下链表的查找操作可以达到O(1)的时间复杂度？ (2分)', 'A. 查找头节点', 'B. 查找尾节点', 'C. 查找中间节点', 'D. 所有情况下都无法达到O(1)', 'A', '在链表中，如果查找头节点，可以直接访问，因此时间复杂度为O(1)。', '0', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 循环链表的最大特点是什么？ (2分)', 'A. 链表不含头节点', 'B. 头尾相连，形成循环结构', 'C. 只能单向遍历', 'D. 节点存储顺序连续', 'B', '循环链表的最大特点是尾节点指向头节点，形成一个循环结构。', '0', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 对于双链表，每个节点的指针数量是多少？ (2分)', 'A. 1', 'B. 2', 'C. 3', 'D. 4', 'B', '双链表的每个节点包含两个指针，一个指向前一个节点，另一个指向后一个节点。', '0', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 以下哪个操作对链表来说是最耗时的？ (2分)', 'A. 查找尾部元素', 'B. 查找头部元素', 'C. 遍历整个链表', 'D. 插入头部', 'C', '遍历整个链表的时间复杂度是O(n)，是链表操作中最耗时的。', '0', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 如何避免链表中的内存浪费？ (2分)', 'A. 使用动态数组', 'B. 使用指针结构', 'C. 使用静态链表', 'D. 节点按顺序存储', 'B', '链表通过使用指针结构，避免了内存浪费，因为节点之间不需要连续存储。', '0', '2', '2.3.1')
""")

### 判断题：

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 在双链表中，每个节点都包含前驱指针和后继指针。 (2分)', 'A. 是', 'B. 否', 'A', '双链表的每个节点包含一个指向前一个节点的指针和一个指向下一个节点的指针。', '1', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 单链表中，删除尾节点的操作比删除头节点的操作复杂。 (2分)', 'A. 是', 'B. 否', 'A', '在单链表中，删除尾节点需要遍历整个链表找到前驱节点，因此操作比删除头节点复杂。', '1', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 循环链表中的头节点没有特殊作用。 (2分)', 'A. 是', 'B. 否', 'B', '循环链表的头节点起到重要作用，它作为链表的起点，连接尾节点形成循环。', '1', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 单链表比双链表的插入和删除操作更为复杂。 (2分)', 'A. 是', 'B. 否', 'B', '双链表需要修改前后节点的指针，因此插入和删除操作更为复杂。', '1', '2', '2.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 链式存储结构的元素必须按照顺序存储。 (2分)', 'A. 是', 'B. 否', 'B', '链式存储结构的节点之间不要求按顺序存储，它们通过指针连接。', '1', '2', '2.3.1')
""")

# ----------------------222222222222222222222222----------------------------2.3.2
# ----------------------222222222222222222222222----------------------------2.3.2
# ----------------------222222222222222222222222----------------------------2.3.2
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 在单链表中，插入一个节点到链表头部的操作时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'A', '插入操作只需要修改头节点的指针，时间复杂度为O(1)。', '0', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 单链表中，如何访问指定位置的节点？ (2分)', 'A. 通过指针直接访问', 'B. 通过数组下标访问', 'C. 需要遍历链表', 'D. 无法访问', 'C', '由于单链表是线性结构，访问节点需要从头节点开始遍历，直到指定位置。', '0', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 以下关于单链表的插入操作，哪个说法是正确的？ (2分)', 'A. 插入操作总是O(n)', 'B. 插入操作只需要O(1)', 'C. 插入操作不能插入尾部', 'D. 插入操作需要先遍历链表', 'D', '单链表插入操作时，如果插入到中间位置，需要遍历链表找到插入位置。', '0', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 删除单链表中指定节点的操作，最耗时的是哪个步骤？ (2分)', 'A. 查找节点', 'B. 修改前驱节点的指针', 'C. 修改后继节点的指针', 'D. 释放内存', 'A', '删除操作的最耗时步骤是查找指定节点，因为需要遍历链表。', '0', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 如果在单链表的尾部插入一个节点，最坏情况下需要遍历多少个节点？ (2分)', 'A. 0', 'B. 1', 'C. n-1', 'D. n', 'C', '尾部插入需要遍历链表找到最后一个节点，最坏情况下需要遍历n-1个节点。', '0', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 在单链表中，删除链表头节点的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'A', '删除链表头节点时，只需修改头指针，时间复杂度为O(1)。', '0', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 在单链表中，查找指定节点的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '查找指定节点需要遍历链表，时间复杂度为O(n)。', '0', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 在单链表的插入操作中，哪种位置的插入最简单？ (2分)', 'A. 头部', 'B. 中间', 'C. 尾部', 'D. 任意位置', 'A', '头部插入操作只需要修改头指针即可，时间复杂度为O(1)。', '0', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 如果链表中有n个节点，删除尾部节点需要遍历多少个节点？ (2分)', 'A. 0', 'B. 1', 'C. n-1', 'D. n', 'C', '删除尾部节点需要遍历链表找到倒数第二个节点，最坏情况下需要遍历n-1个节点。', '0', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 在单链表中，如何实现反转链表？ (2分)', 'A. 修改指针的方向', 'B. 交换数据', 'C. 创建新链表', 'D. 遍历链表删除节点', 'A', '反转链表的核心思想是修改每个节点的指针方向。', '0', '2', '2.3.2')
""")

### 判断题：
cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 在单链表中，删除尾节点时不需要遍历整个链表。 (2分)', 'A. 是', 'B. 否', 'B', '删除尾节点需要遍历链表找到尾节点的前驱节点，因此需要O(n)时间复杂度。', '1', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 单链表在头部插入节点比尾部插入节点效率高。 (2分)', 'A. 是', 'B. 否', 'A', '在单链表中，插入头部节点只需要修改头指针，时间复杂度为O(1)，而插入尾部需要遍历链表，时间复杂度为O(n)。', '1', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 单链表中插入和删除操作的时间复杂度都是O(n)。 (2分)', 'A. 是', 'B. 否', 'B', '单链表的插入和删除操作，头部操作的时间复杂度是O(1)，而尾部操作和删除指定节点需要遍历链表，时间复杂度为O(n)。', '1', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 单链表反转操作的时间复杂度为O(n)。 (2分)', 'A. 是', 'B. 否', 'A', '单链表反转操作需要遍历链表一次，修改指针方向，因此时间复杂度为O(n)。', '1', '2', '2.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 单链表的内存空间是连续分配的。 (2分)', 'A. 是', 'B. 否', 'B', '单链表的节点是分散存储的，节点通过指针连接，因此内存空间不是连续分配的。', '1', '2', '2.3.2')
""")

# ----------------------222222222222222222222222----------------------------2.3.3
# ----------------------222222222222222222222222----------------------------2.3.3
# ----------------------222222222222222222222222----------------------------2.3.3

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 循环链表的优点是什么？ (2分)', 'A. 支持双向遍历', 'B. 支持从任意节点开始遍历', 'C. 插入删除操作更高效', 'D. 空间复杂度更低', 'B', '循环链表通过将尾节点指向头节点，使得可以从任意节点开始遍历。', '0', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 双向链表比单链表的优势是什么？ (2分)', 'A. 支持从前向后和后向遍历', 'B. 更低的空间复杂度', 'C. 更高的时间复杂度', 'D. 插入删除操作不能在O(1)内完成', 'A', '双向链表每个节点有前后指针，支持双向遍历，相比单链表更加灵活。', '0', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 循环双向链表的主要特点是什么？ (2分)', 'A. 头指针指向尾节点', 'B. 具有两个指针指向前后节点且尾节点指向头节点', 'C. 每个节点只有一个指针', 'D. 不支持双向操作', 'B', '循环双向链表结合了双向链表和循环链表的特点，尾节点指向头节点形成闭环，且每个节点有前后指针。', '0', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 在单链表中，如何实现从尾部插入元素？ (2分)', 'A. 从头节点开始遍历到尾节点，插入新节点', 'B. 只需修改头节点的指针', 'C. 使用循环链表结构', 'D. 使用栈结构', 'A', '在单链表中，插入尾部元素需要从头节点开始遍历，找到尾节点后进行插入操作。', '0', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 双向链表的删除操作如何实现？ (2分)', 'A. 只需要修改头指针', 'B. 只需修改尾指针', 'C. 修改前后指针以连接剩余节点', 'D. 无法删除节点', 'C', '双向链表删除节点时需要修改前驱节点的指针和后继节点的指针，确保链表的连接性。', '0', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 循环链表中的头指针和尾指针有什么区别？ (2分)', 'A. 头指针指向最后一个节点', 'B. 尾指针指向第一个节点', 'C. 头指针指向尾节点，尾指针指向头节点', 'D. 头指针和尾指针无区别', 'C', '在循环链表中，头指针指向尾节点的后继节点，而尾指针指向头节点，形成循环结构。', '0', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 在双向链表中，插入节点的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'A', '在双向链表中，插入操作可以通过直接修改相邻节点的指针来完成，时间复杂度为O(1)。', '0', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 双向链表与循环链表相比，主要的区别是什么？ (2分)', 'A. 双向链表支持双向遍历，循环链表不支持', 'B. 循环链表的尾节点指向头节点，而双向链表没有此特性', 'C. 双向链表没有尾指针', 'D. 循环链表不能插入节点', 'B', '循环链表的尾节点指向头节点，而双向链表的尾节点没有类似关系。', '0', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 使用双向链表时，哪些操作可以在O(1)时间内完成？ (2分)', 'A. 插入和删除操作', 'B. 查找操作', 'C. 遍历操作', 'D. 查找和插入操作', 'A', '双向链表支持在O(1)时间内进行插入和删除操作，因为每个节点有前后指针。', '0', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 循环双向链表中的删除操作最坏情况下需要遍历多少个节点？ (2分)', 'A. 1', 'B. n', 'C. log n', 'D. 0', 'B', '循环双向链表需要遍历所有节点才能找到并删除指定节点，最坏情况下需要遍历n个节点。', '0', '2', '2.3.3')
""")

### 判断题：
cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 循环链表中的尾指针指向头节点，形成循环结构。 (2分)', 'A. 是', 'B. 否', 'A', '在循环链表中，尾节点的指针指向头节点，形成循环结构。', '1', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 双向链表的空间复杂度比单链表高，因为每个节点都需要额外存储一个前驱指针。 (2分)', 'A. 是', 'B. 否', 'A', '双向链表每个节点除了存储数据和后继指针外，还需要存储前驱指针，因此空间复杂度更高。', '1', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 循环链表适用于需要频繁访问尾节点的应用场景。 (2分)', 'A. 是', 'B. 否', 'A', '循环链表可以高效地访问尾节点，特别适用于需要频繁访问尾节点的场景。', '1', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 双向链表的插入和删除操作相比于单链表更加复杂。 (2分)', 'A. 是', 'B. 否', 'B', '无', '1', '2', '2.3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 链式存储结构的元素必须按照顺序存储。 (2分)', 'A. 是', 'B. 否', 'B', '链式存储结构的节点之间不要求按顺序存储，它们通过指针连接。', '1', '2', '2.3.1')
""")

# ----------------------222222222222222222222222----------------------------2.4
# ----------------------222222222222222222222222----------------------------2.4
# ----------------------222222222222222222222222----------------------------2.4
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 顺序表与链表的主要区别是什么？ (2分)', 'A. 顺序表是静态结构，链表是动态结构', 'B. 顺序表有头尾指针，链表没有', 'C. 链表中的元素在内存中是连续存储的', 'D. 顺序表的元素可以动态调整', 'A', '顺序表的大小固定，存储元素是连续的，因此是静态结构，而链表的大小可以动态调整，节点分散存储，属于动态结构。', '0', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 在顺序表中，插入操作的时间复杂度是？ (2分)', 'A. O(1)', 'B. O(log n)', 'C. O(n)', 'D. O(n^2)', 'C', '在顺序表中，插入操作需要移动元素以保持元素的顺序，因此时间复杂度是O(n)。', '0', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 链表中删除节点的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(log n)', 'C. O(n)', 'D. O(n^2)', 'A', '在链表中，删除操作只需要修改相邻节点的指针，因此时间复杂度为O(1)，前提是已知节点的前后指针。', '0', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 顺序表的查找操作时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(log n)', 'C. O(n)', 'D. O(n^2)', 'A', '顺序表的查找操作可以直接通过索引访问元素，时间复杂度为O(1)。', '0', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 顺序表适用于哪种类型的操作？ (2分)', 'A. 频繁的插入和删除', 'B. 频繁的查找操作', 'C. 大量的随机访问', 'D. 小规模的顺序遍历', 'B', '顺序表由于支持O(1)的查找操作，因此适合查找操作频繁的场景。', '0', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 链表中随机访问元素的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(log n)', 'C. O(n)', 'D. O(n^2)', 'C', '链表无法像顺序表一样通过索引直接访问元素，因此需要遍历链表，时间复杂度为O(n)。', '0', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 在顺序表中，删除操作的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(log n)', 'C. O(n)', 'D. O(n^2)', 'C', '在顺序表中，删除操作需要移动元素以填补空缺，时间复杂度为O(n)。', '0', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 下列哪项操作适用于链表？ (2分)', 'A. 动态调整大小', 'B. 随机访问', 'C. 常数时间内的删除和插入操作', 'D. 数据连续存储', 'C', '链表可以在常数时间内删除或插入节点，因为只需要修改相邻节点的指针。', '0', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 链表比顺序表的主要优点是什么？ (2分)', 'A. 顺序访问效率高', 'B. 插入删除操作高效', 'C. 随机访问时间短', 'D. 查找速度更快', 'B', '链表的插入和删除操作更高效，因为不需要移动其他元素。', '0', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 顺序表和链表相比，哪个在空间利用上更加高效？ (2分)', 'A. 顺序表', 'B. 链表', 'C. 两者一样', 'D. 取决于操作类型', 'A', '顺序表通过连续存储，可以高效利用内存，而链表需要为每个节点额外存储指针，导致空间利用率较低。', '0', '2', '2.4')
""")

### 判断题：
cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 链表可以有效避免顺序表中因频繁插入和删除而导致的内存移动。 (2分)', 'A. 是', 'B. 否', 'A', '链表在插入和删除操作时，不需要移动其他元素，因此在这些操作上比顺序表更加高效。', '1', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 顺序表适合用于需要频繁插入删除的场景。 (2分)', 'A. 是', 'B. 否', 'B', '顺序表插入和删除操作的时间复杂度是O(n)，因此不适合频繁插入删除的场景。', '1', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 链表可以在O(1)的时间复杂度内进行查找操作。 (2分)', 'A. 是', 'B. 否', 'B', '链表的查找操作需要从头遍历到指定节点，因此时间复杂度为O(n)。', '1', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 顺序表比链表更节省内存空间。 (2分)', 'A. 是', 'B. 否', 'A', '顺序表的元素是连续存储的，相比链表的分散存储和额外的指针，顺序表在内存使用上更为高效。', '1', '2', '2.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 链表的插入操作通常比顺序表的插入操作更加高效。 (2分)', 'A. 是', 'B. 否', 'A', '链表的插入操作只需修改相邻节点的指针，不需要移动其他元素，因此通常比顺序表更高效。', '1', '2', '2.4')
""")

# ----------------------222222222222222222222222----------------------------2.5
# ----------------------222222222222222222222222----------------------------2.5
# ----------------------222222222222222222222222----------------------------2.5

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 下列哪种存储方式适用于需要频繁插入和删除操作的线性表？ (2分)', 'A. 顺序表', 'B. 静态链表', 'C. 链表', 'D. 哈希表', 'C', '链表是动态存储结构，插入和删除操作效率较高，因此适合这种场景。', '0', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 静态链表与动态链表的主要区别是什么？ (2分)', 'A. 静态链表使用动态分配的内存', 'B. 动态链表中节点指针是预先定义好的', 'C. 静态链表的内存大小在创建时固定', 'D. 动态链表具有更高的内存利用率', 'C', '静态链表使用数组存储节点，内存大小在创建时固定；动态链表则是通过动态分配内存。', '0', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 下列哪种线性表存储方式需要额外的指针来连接元素？ (2分)', 'A. 顺序表', 'B. 静态链表', 'C. 动态链表', 'D. 数组', 'C', '动态链表每个节点包含一个指针，指向下一个节点，因此需要额外的指针来连接元素。', '0', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 静态链表的主要优点是什么？ (2分)', 'A. 内存使用高效', 'B. 支持高效的插入和删除', 'C. 存储空间不需要额外分配指针', 'D. 查找速度较快', 'C', '静态链表通过数组存储，减少了指针的额外开销，因此可以更高效地使用内存。', '0', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 线性表中使用链表存储方式的一个缺点是什么？ (2分)', 'A. 随机访问元素较慢', 'B. 空间利用率高', 'C. 插入删除操作效率低', 'D. 实现复杂', 'A', '链表无法像顺序表那样支持O(1)时间复杂度的随机访问，因此随机访问较慢。', '0', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 在链表中，节点间的连接方式是什么？ (2分)', 'A. 通过数组的下标连接', 'B. 通过指针连接', 'C. 通过静态内存块连接', 'D. 通过索引连接', 'B', '链表中的每个节点通过指针连接，指向下一个节点。', '0', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 下列哪种方式存储的线性表在插入操作时最为高效？ (2分)', 'A. 顺序表', 'B. 单向链表', 'C. 数组', 'D. 双向链表', 'B', '单向链表在插入操作时，只需要修改相邻节点的指针，操作效率较高。', '0', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 在静态链表中，如何表示一个元素的“下一个元素”？ (2分)', 'A. 通过指针', 'B. 通过数组的下标', 'C. 通过元素值', 'D. 通过栈指针', 'B', '静态链表中，通过数组下标来表示一个元素的“下一个元素”。', '0', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 动态链表比顺序表更适合用于哪些场景？ (2分)', 'A. 查找频繁', 'B. 插入删除频繁', 'C. 随机访问', 'D. 内存紧张', 'B', '动态链表在插入和删除操作中不需要移动元素，因此在这些场景中更高效。', '0', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 下列哪种存储方式不支持直接访问元素？ (2分)', 'A. 顺序表', 'B. 静态链表', 'C. 动态链表', 'D. 哈希表', 'C', '链表的元素存储不连续，需要遍历才能访问指定节点，因此不支持直接访问元素。', '0', '2', '2.5')
""")

### 判断题：
cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 静态链表和动态链表的区别在于是否使用动态内存分配。 (2分)', 'A. 是', 'B. 否', 'A', '静态链表在创建时固定大小，而动态链表使用动态内存分配。', '1', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 动态链表的元素在内存中是连续存储的。 (2分)', 'A. 是', 'B. 否', 'B', '动态链表的元素在内存中是分散存储的，每个节点通过指针连接。', '1', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 链表比顺序表更节省内存空间。 (2分)', 'A. 是', 'B. 否', 'B', '链表需要额外存储指针，因此相比顺序表，链表的内存开销更大。', '1', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 静态链表是动态链表的一种特殊形式，只有数组没有指针。 (2分)', 'A. 是', 'B. 否', 'B', '静态链表和动态链表一样，都需要指针来连接元素，只是静态链表通过数组来存储节点。', '1', '2', '2.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 动态链表比静态链表在插入和删除操作上更高效。 (2分)', 'A. 是', 'B. 否', 'B', '静态链表由于使用数组存储，避免了动态内存分配的开销，插入和删除效率不低于动态链表。', '1', '2', '2.5')
""")

# ----------------------222222222222222222222222----------------------------2.6
# ----------------------222222222222222222222222----------------------------2.6
# ----------------------222222222222222222222222----------------------------2.6
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 一元多项式的表示方式中，哪一种方式最适合稀疏多项式？ (2分)', 'A. 数组表示法', 'B. 链表表示法', 'C. 栈表示法', 'D. 矩阵表示法', 'B', '链表表示法适合稀疏多项式，因为它只存储非零项，节省空间。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 一元多项式的数组表示法中，数组的下标表示什么？ (2分)', 'A. 系数', 'B. 常数项', 'C. 指数', 'D. 指数和系数', 'C', '数组的下标代表多项式的指数，而数组的值代表对应的系数。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 在一元多项式的链表表示法中，链表的每个节点存储了什么信息？ (2分)', 'A. 只存储系数', 'B. 只存储指数', 'C. 系数和指数', 'D. 常数项和系数', 'C', '链表的每个节点通常包含一个多项式项的系数和对应的指数。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 多项式相加时，如果两个多项式有相同指数的项，如何处理？ (2分)', 'A. 忽略这些项', 'B. 相加系数，保留相同指数项', 'C. 删除这些项', 'D. 将系数减去', 'B', '在多项式加法中，指数相同的项系数应相加，结果保留该项。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 一元多项式加法中，如何处理没有相同指数的项？ (2分)', 'A. 系数为0', 'B. 该项被删除', 'C. 将该项加入结果多项式', 'D. 将该项指数归一', 'C', '没有相同指数的项会被直接加入结果多项式。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 在一元多项式加法中，如果一个多项式的指数比另一个多项式的最大指数大，如何处理？ (2分)', 'A. 忽略该项', 'B. 将其系数设为0', 'C. 直接加到结果中', 'D. 抛出异常', 'C', '即使某一项的指数比另一个多项式的最大指数大，该项仍会加到结果多项式中。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 如果两个多项式的常数项不同，那么加法后的常数项应该如何计算？ (2分)', 'A. 取较大的常数项', 'B. 常数项为0', 'C. 将常数项相加', 'D. 常数项为两者的差', 'C', '常数项在加法中需要相加。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 在链表表示法中，如果两个多项式有相同指数的项，如何处理？ (2分)', 'A. 删除其中一个项', 'B. 合并项的系数', 'C. 直接替换其中一项', 'D. 保留两个项', 'B', '链表表示法中，相同指数的项应该合并，系数相加。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 对于一元多项式加法，如果结果中有系数为0的项，如何处理？ (2分)', 'A. 保留该项', 'B. 删除该项', 'C. 将该项设为常数项', 'D. 系数设为1', 'B', '系数为0的项通常会被删除。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 如果两个多项式的次数相同，结果多项式的次数是多少？ (2分)', 'A. 等于其中一个多项式的次数', 'B. 一定为0', 'C. 可能小于两个多项式的次数', 'D. 结果多项式次数可能与两个多项式的最高次项相同', 'D', '如果两个多项式的次数相同，结果的次数通常保持不变，除非最高次项的系数相加后为0。', '0', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 在一元多项式相加时，如果有相同指数的项，它们的系数一定会相加。 (2分)', 'A. 是', 'B. 否', 'A', '在一元多项式相加时，系数相同指数的项需要相加。', '1', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 一元多项式加法时，常数项系数始终不会发生变化。 (2分)', 'A. 是', 'B. 否', 'B', '常数项的系数可能会变化，因为它会与其他多项式的常数项相加。', '1', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 在链表表示法中，如果多项式项的指数不连续，链表仍然能有效表示。 (2分)', 'A. 是', 'B. 否', 'A', '链表表示法能够处理不连续的指数，只需在相应位置插入新节点即可。', '1', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 数组表示法适合表示稀疏多项式，因为它占用的空间较少。 (2分)', 'A. 是', 'B. 否', 'B', '数组表示法适合密集多项式，稀疏多项式应使用链表等节省空间的数据结构。', '1', '2', '2.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 在多项式加法中，两个多项式的最高次项系数相加后，结果的最高次项系数可能为零。 (2分)', 'A. 是', 'B. 否', 'A', '如果两个多项式的最高次项系数相加后为零，结果的最高次项系数为零，可能会被删除。', '1', '2', '2.6')
""")

# --------------33333333333333333333333333333------------------3.1
# --------------33333333333333333333333333333------------------3.1
# --------------33333333333333333333333333333------------------3.1
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 栈是一种什么类型的数据结构？ (2分)', 'A. 线性表', 'B. 树形结构', 'C. 图结构', 'D. 无序集合', 'A', '栈是一种线性表，它遵循后进先出（LIFO）的原则。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 以下哪种操作是栈常见的操作？ (2分)', 'A. 入队', 'B. 出队', 'C. 入栈', 'D. 删除', 'C', '栈常见操作是入栈（push）和出栈（pop）。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 在栈中，哪种操作会导致栈顶元素被移除？ (2分)', 'A. 入栈', 'B. 出栈', 'C. 查询', 'D. 清空', 'B', '出栈操作会移除栈顶元素。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 栈的基本特性是什么？ (2分)', 'A. 先进先出（FIFO）', 'B. 后进先出（LIFO）', 'C. 支持随机访问', 'D. 按优先级出栈', 'B', '栈遵循后进先出（LIFO）原则，即最后入栈的元素最先出栈。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 在栈中，如果执行两次入栈操作并进行一次出栈操作，那么栈的大小将如何变化？ (2分)', 'A. 增加1', 'B. 增加2', 'C. 增加1后减少1', 'D. 不变', 'C', '执行两次入栈后栈增加2个元素，执行一次出栈后栈减少1个元素，最终栈增加1个元素。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 栈的实现通常使用哪两种数据结构？ (2分)', 'A. 数组和链表', 'B. 数组和栈结构', 'C. 链表和队列', 'D. 队列和树', 'A', '栈可以通过数组或链表实现。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 栈的空间复杂度是怎样的？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '栈的空间复杂度取决于栈中元素的个数，因此为O(n)。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 栈的出栈操作是否可以访问栈底元素？ (2分)', 'A. 可以', 'B. 不可以', 'C. 只有通过遍历栈才可以访问栈底元素', 'D. 只有栈空时才可以访问栈底元素', 'B', '栈的出栈操作只能访问栈顶元素，栈底元素无法直接访问。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 栈在程序中的应用通常包括哪些方面？ (2分)', 'A. 函数调用管理', 'B. 图的遍历', 'C. 队列的实现', 'D. 排序算法', 'A', '栈常用于管理函数调用（函数调用栈）等场景。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 在栈中进行操作时，如果栈为空，执行哪种操作会导致错误？ (2分)', 'A. 入栈', 'B. 出栈', 'C. 查询栈顶元素', 'D. 查询栈是否为空', 'B', '在栈为空时，执行出栈操作会导致栈下溢错误。', '0', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 栈的操作遵循先进先出（FIFO）的原则。 (2分)', 'A. 是', 'B. 否', 'B', '栈遵循的是后进先出（LIFO）的原则，而非先进先出（FIFO）。', '1', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 在栈的实现中，常见的操作有入栈（push）和出栈（pop）。 (2分)', 'A. 是', 'B. 否', 'A', '栈的常见操作就是入栈（push）和出栈（pop）。', '1', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 在栈中可以随时访问栈底元素。 (2分)', 'A. 是', 'B. 否', 'B', '栈只能访问栈顶元素，栈底元素不能直接访问。', '1', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 栈的空间复杂度是O(1)。 (2分)', 'A. 是', 'B. 否', 'B', '栈的空间复杂度取决于栈中元素的数量，因此是O(n)。', '1', '3', '3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 栈的出栈操作可以返回并删除栈顶元素。 (2分)', 'A. 是', 'B. 否', 'A', '出栈操作会返回并删除栈顶元素。', '1', '3', '3.1')
""")

# --------------33333333333333333333333333333------------------3.1.1
# --------------33333333333333333333333333333------------------3.1.1
# --------------33333333333333333333333333333------------------3.1.1
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 栈的数据结构遵循哪种访问规则？ (2分)', 'A. 先进先出（FIFO）', 'B. 后进先出（LIFO）', 'C. 随机访问', 'D. 优先级访问', 'B', '栈遵循后进先出（LIFO）规则，即最后入栈的元素最先出栈。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 在栈中，哪个操作可以插入一个元素？ (2分)', 'A. 出栈', 'B. 入栈', 'C. 查询', 'D. 清空栈', 'B', '插入元素的操作是入栈（push）。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 栈的典型应用包括哪一项？ (2分)', 'A. 队列管理', 'B. 深度优先搜索（DFS）', 'C. 图的遍历', 'D. 快速排序', 'B', '栈在深度优先搜索（DFS）中扮演重要角色。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 栈的最基本操作是？ (2分)', 'A. 入栈和出栈', 'B. 入栈和查询', 'C. 出栈和删除', 'D. 入栈和清空', 'A', '栈的最基本操作是入栈（push）和出栈（pop）。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 栈的“栈顶”指的是哪个位置？ (2分)', 'A. 最底部的元素', 'B. 最上面的元素', 'C. 插入的第一个元素', 'D. 被删除的最后一个元素', 'B', '栈顶是栈中最后一个插入的元素。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 如果栈为空，执行哪种操作会导致错误？ (2分)', 'A. 入栈', 'B. 出栈', 'C. 查询栈顶元素', 'D. 检查栈是否为空', 'B', '在栈为空时，执行出栈操作会导致栈下溢错误。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 以下哪种方式通常用于实现栈？ (2分)', 'A. 数组', 'B. 链表', 'C. 树', 'D. 数组或链表', 'D', '栈可以通过数组或链表实现。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 栈的空间复杂度通常为？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '栈的空间复杂度与栈中元素的个数有关，通常为O(n)。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 如果对栈执行两次入栈操作后，再执行一次出栈操作，栈的大小变化为？ (2分)', 'A. 增加1', 'B. 增加2', 'C. 增加1后减少1', 'D. 不变', 'C', '两次入栈操作使栈大小增加2，再执行一次出栈操作使栈大小减少1，最终增加1。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 栈中元素的插入和删除操作是如何进行的？ (2分)', 'A. 随机访问', 'B. 只能从栈顶进行插入和删除', 'C. 先进先出', 'D. 按照优先级插入和删除', 'B', '栈的元素只能从栈顶进行插入（push）和删除（pop）。', '0', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 栈遵循先进先出（FIFO）规则。 (2分)', 'A. 是', 'B. 否', 'B', '栈遵循的是后进先出（LIFO）规则，而非先进先出（FIFO）。', '1', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 栈的出栈操作会移除栈顶元素。 (2分)', 'A. 是', 'B. 否', 'A', '出栈操作会返回并移除栈顶元素。', '1', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 栈只能访问栈底元素。 (2分)', 'A. 是', 'B. 否', 'B', '栈只能访问栈顶元素，栈底元素不能直接访问。', '1', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 入栈操作会将元素添加到栈顶。 (2分)', 'A. 是', 'B. 否', 'A', '入栈操作会将新元素添加到栈顶。', '1', '3', '3.1.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 栈的空间复杂度总是O(1)。 (2分)', 'A. 是', 'B. 否', 'B', '栈的空间复杂度取决于栈中的元素数量，通常为O(n)。', '1', '3', '3.1.1')
""")

# --------------33333333333333333333333333333------------------3.1.2
# --------------33333333333333333333333333333------------------3.1.2
# --------------33333333333333333333333333333------------------3.1.2

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 栈的逻辑结构属于哪种类型的数据结构？ (2分)', 'A. 线性结构', 'B. 非线性结构', 'C. 图结构', 'D. 队列结构', 'A', '栈是线性数据结构，其元素按顺序排列。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 栈的实现可以通过哪种方式进行？ (2分)', 'A. 数组', 'B. 链表', 'C. 数组或链表', 'D. 树', 'C', '栈可以通过数组或链表实现，数组实现时栈顶是索引，链表实现时栈顶是节点。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 使用数组实现栈时，栈顶指针的作用是什么？ (2分)', 'A. 表示栈的大小', 'B. 指向栈底元素', 'C. 指向栈顶元素', 'D. 用于判断栈是否为空', 'C', '栈顶指针用于指向栈中最后一个插入的元素。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 用链表实现栈时，栈顶指针通常指向什么位置？ (2分)', 'A. 链表头', 'B. 链表尾', 'C. 链表的中间', 'D. 任意位置', 'A', '链表实现栈时，栈顶通常指向链表头部，即最后插入的节点。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 栈的“栈顶指针”用于标记栈顶元素的位置。在栈为空时，栈顶指针的值通常是多少？ (2分)', 'A. 0', 'B. -1', 'C. null', 'D. 1', 'B', '栈为空时，栈顶指针通常为-1，表示没有元素。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 栈的空间复杂度是如何计算的？ (2分)', 'A. O(1)', 'B. O(log n)', 'C. O(n)', 'D. O(n^2)', 'C', '栈的空间复杂度通常是O(n)，其中n是栈中元素的个数。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 使用数组实现栈时，栈的最大容量受到什么限制？ (2分)', 'A. 栈顶指针的大小', 'B. 数组的固定大小', 'C. 元素的类型', 'D. 栈操作的次数', 'B', '栈的最大容量通常受到数组大小的限制。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 栈的“出栈操作”需要哪些步骤？ (2分)', 'A. 先删除栈顶元素，再调整栈顶指针', 'B. 先调整栈顶指针，再删除栈顶元素', 'C. 直接删除栈顶元素', 'D. 先判断栈是否为空', 'A', '出栈操作先删除栈顶元素，然后调整栈顶指针指向上一个元素。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 如果栈在数组实现中达到最大容量，执行入栈操作时会发生什么？ (2分)', 'A. 程序会报错', 'B. 程序会自动增加数组大小', 'C. 栈会被清空', 'D. 栈会丢失元素', 'A', '栈在数组实现时，如果达到最大容量，执行入栈操作会导致栈溢出错误。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 使用链表实现栈时，栈操作的时间复杂度是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'A', '链表实现栈时，入栈和出栈操作的时间复杂度都是O(1)。', '0', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 栈的元素只能从栈顶访问。 (2分)', 'A. 是', 'B. 否', 'A', '栈只能从栈顶访问元素，栈底的元素无法直接访问。', '1', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 使用数组实现栈时，栈的大小是固定的，不能动态增长。 (2分)', 'A. 是', 'B. 否', 'A', '在数组实现栈时，栈的大小通常是固定的，除非重新分配更大的数组。', '1', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 链表实现栈时，栈的操作时间复杂度是O(n)。 (2分)', 'A. 是', 'B. 否', 'B', '链表实现栈时，入栈和出栈操作的时间复杂度为O(1)，而非O(n)。', '1', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 栈的空间复杂度与栈的元素数量成正比。 (2分)', 'A. 是', 'B. 否', 'A', '栈的空间复杂度与栈中的元素数量有关，通常为O(n)。', '1', '3', '3.1.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 栈可以使用链表实现，但在数组中栈的大小是固定的。 (2分)', 'A. 是', 'B. 否', 'A', '栈可以使用链表实现，且数组实现时栈的大小是固定的，除非动态调整。', '1', '3', '3.1.2')
""")

# --------------33333333333333333333333333333------------------3.2
# --------------33333333333333333333333333333------------------3.2
# --------------33333333333333333333333333333------------------3.2
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 栈的主要特点是什么？ (2分)', 'A. 后进先出（LIFO）', 'B. 先进先出（FIFO）', 'C. 随机访问', 'D. 队列式访问', 'A', '栈是一种后进先出（LIFO）数据结构，只能访问栈顶元素。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 在递归算法中，栈的作用是什么？ (2分)', 'A. 存储递归函数的返回地址和局部变量', 'B. 存储递归的参数', 'C. 存储递归的函数名', 'D. 存储递归的中间结果', 'A', '栈在递归算法中用于存储每一次递归调用的返回地址和局部变量。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 栈通常用来解决哪些问题？ (2分)', 'A. 树的遍历', 'B. 图的遍历', 'C. 括号匹配', 'D. 以上全部', 'D', '栈广泛应用于括号匹配、树的遍历、图的深度优先搜索等问题。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 如何使用栈检查一个字符串是否包含合法的括号？ (2分)', 'A. 利用栈存储左括号，遇到右括号时弹出栈顶元素', 'B. 直接检查括号的数量是否一致', 'C. 通过递归检查每对括号的匹配', 'D. 利用栈存储数字，检查数字的顺序', 'A', '栈可以通过存储左括号，遇到右括号时弹出栈顶元素来判断括号是否匹配。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 在深度优先搜索（DFS）中，栈的作用是什么？ (2分)', 'A. 存储当前节点路径，进行回溯', 'B. 存储图的所有节点', 'C. 存储已访问的节点', 'D. 存储图的边权值', 'A', '栈在深度优先搜索中用于存储当前节点路径，回溯时弹出栈顶元素。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 如何使用栈实现表达式的求值？ (2分)', 'A. 通过栈存储操作数，遇到运算符时出栈计算', 'B. 直接进行递归计算', 'C. 使用栈存储结果，不进行操作符处理', 'D. 利用栈存储运算符并推迟计算', 'A', '在栈实现的表达式求值过程中，操作数入栈，遇到运算符时从栈中弹出操作数进行计算。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 在浏览器的历史记录管理中，栈的应用是什么？ (2分)', 'A. 存储当前页面历史记录，支持前进和后退操作', 'B. 存储当前网页内容', 'C. 存储用户输入的信息', 'D. 存储书签', 'A', '浏览器的历史记录管理使用栈存储页面历史，通过栈的弹出和入栈操作支持前进和后退功能。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 栈的空间复杂度通常是多少？ (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '栈的空间复杂度通常为O(n)，其中n是栈中元素的数量。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 在运算符优先级转换中，栈的作用是什么？ (2分)', 'A. 存储操作数，按顺序输出', 'B. 存储运算符并根据优先级进行处理', 'C. 存储括号并处理括号内的表达式', 'D. 存储运算符和操作数，执行计算', 'B', '在运算符优先级转换中，栈用于存储运算符，并根据其优先级进行出栈。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 栈在表达式求值中的操作顺序是？ (2分)', 'A. 入栈操作数，遇到运算符时出栈计算', 'B. 先计算运算符，再入栈操作数', 'C. 先计算运算符，再出栈操作数', 'D. 直接跳过操作符', 'A', '栈在表达式求值中，操作数先入栈，遇到运算符时才出栈进行计算。', '0', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 栈是一种先进先出（FIFO）的数据结构。 (2分)', 'A. 是', 'B. 否', 'B', '栈是一种后进先出（LIFO）的数据结构，不是先进先出。', '1', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 使用栈可以有效地实现深度优先搜索（DFS）算法。 (2分)', 'A. 是', 'B. 否', 'A', '栈是实现深度优先搜索（DFS）算法的基础，栈用于存储访问路径和节点。', '1', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 栈只能存储整数类型的数据。 (2分)', 'A. 是', 'B. 否', 'B', '栈可以存储多种数据类型，如整数、字符、对象等。', '1', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 栈在解决括号匹配问题时，栈顶元素是最先被访问的。 (2分)', 'A. 是', 'B. 否', 'A', '栈是后进先出（LIFO）的数据结构，栈顶元素最先被访问。', '1', '3', '3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 使用栈可以帮助实现表达式的逆波兰表示法（后缀表达式）计算。 (2分)', 'A. 是', 'B. 否', 'A', '无', '1', '3', '3.2')
""")

# --------------33333333333333333333333333333------------------3.3
# --------------33333333333333333333333333333------------------3.3
# --------------33333333333333333333333333333------------------3.3
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 栈是一种什么类型的数据结构？ (2分)', 'A. 先进先出（FIFO）', 'B. 后进先出（LIFO）', 'C. 随机访问', 'D. 顺序访问', 'B', '栈是一种后进先出（LIFO）数据结构。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 在递归算法中，栈的主要作用是什么？ (2分)', 'A. 存储函数调用信息', 'B. 存储全局变量', 'C. 存储返回值', 'D. 存储循环信息', 'A', '栈在递归算法中用于存储每次函数调用的信息，包括返回地址和局部变量。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 栈在递归算法中如何发挥作用？ (2分)', 'A. 存储局部变量和函数返回地址', 'B. 存储递归函数的参数', 'C. 存储函数体', 'D. 存储计算结果', 'A', '栈通过存储局部变量和函数返回地址来实现递归调用。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 在栈中，哪个操作是最先进行的？ (2分)', 'A. 入栈', 'B. 出栈', 'C. 查询栈顶元素', 'D. 清空栈', 'A', '栈操作遵循后进先出（LIFO）原则，最先执行的是入栈操作。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 栈的主要应用之一是？ (2分)', 'A. 实现深度优先搜索（DFS）', 'B. 实现广度优先搜索（BFS）', 'C. 数组排序', 'D. 动态规划', 'A', '栈常用于深度优先搜索（DFS），用于存储当前路径和回溯。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 在递归函数调用时，栈的状态是什么？ (2分)', 'A. 不断增长', 'B. 一直保持不变', 'C. 不断减少', 'D. 往复波动', 'A', '在递归调用过程中，每一次递归调用都会将信息压入栈中，栈的状态不断增长。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 在栈的运算中，何时进行栈顶元素的删除？ (2分)', 'A. 只有在栈满时', 'B. 只有在栈为空时', 'C. 只有遇到特定条件时', 'D. 每次操作后自动删除', 'C', '栈顶元素的删除通常在满足特定条件下，例如弹出栈顶元素。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 以下哪项操作通常不会直接应用于栈？ (2分)', 'A. 括号匹配', 'B. 数值计算', 'C. 排序算法', 'D. 树的深度优先遍历', 'C', '栈通常不直接应用于排序算法，主要应用于括号匹配、数值计算等。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 在浏览器的前进和后退功能中，栈的作用是什么？ (2分)', 'A. 存储历史页面', 'B. 存储当前页面', 'C. 存储书签', 'D. 存储页面的HTML代码', 'A', '浏览器使用栈存储页面历史，通过栈进行页面的前进和后退。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 递归调用函数时，栈的大小通常受什么因素影响？ (2分)', 'A. 输入的大小和递归的深度', 'B. 计算复杂度', 'C. 递归函数的返回值', 'D. 操作系统的配置', 'A', '递归的深度和输入的大小会影响栈的大小，栈会随着递归层数增加而增加。', '0', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 栈是一种后进先出（LIFO）结构。 (2分)', 'A. 是', 'B. 否', 'A', '栈遵循后进先出（LIFO）的原则。', '1', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 在递归算法中，栈的大小与递归的深度成正比。 (2分)', 'A. 是', 'B. 否', 'A', '递归的深度会直接影响栈的大小，因为每次递归都会向栈中压入信息。', '1', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 栈只能存储整数类型的数据。 (2分)', 'A. 是', 'B. 否', 'B', '栈可以存储任何类型的数据，如整数、字符、对象等。', '1', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 深度优先搜索（DFS）可以通过队列实现，而不需要栈。 (2分)', 'A. 是', 'B. 否', 'B', '深度优先搜索（DFS）通常使用栈来存储节点和回溯路径。', '1', '3', '3.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 栈在递归调用时用于存储函数的返回地址和局部变量。 (2分)', 'A. 是', 'B. 否', 'A', '栈在递归调用中用于存储每次递归调用的返回地址和局部变量。', '1', '3', '3.3')
""")

# --------------33333333333333333333333333333------------------3.4.1
# --------------33333333333333333333333333333------------------3.4.1
# --------------33333333333333333333333333333------------------3.4.1
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 队列是一种什么类型的数据结构？ (2分)', 'A. 后进先出（LIFO）', 'B. 先进先出（FIFO）', 'C. 随机访问', 'D. 顺序访问', 'B', '队列是一种先进先出（FIFO）的数据结构，最先进入的数据最先出队。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 队列与栈的主要区别是什么？ (2分)', 'A. 队列是先进先出，栈是后进先出', 'B. 队列是后进先出，栈是先进先出', 'C. 队列只能存储整数，栈只能存储字符', 'D. 队列只能单向存储，栈只能双向存储', 'A', '队列遵循先进先出（FIFO）原则，而栈遵循后进先出（LIFO）原则。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 队列的基本操作包括以下哪些？ (2分)', 'A. 入队、出队、查询队头、查询队尾', 'B. 入栈、出栈、查询栈顶', 'C. 排序、查找', 'D. 插入、删除', 'A', '队列的基本操作包括入队、出队、查询队头和查询队尾。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 在循环队列中，当队列满时，通常采取什么措施？ (2分)', 'A. 扩展队列大小', 'B. 队列头指针不动', 'C. 队列尾指针不动', 'D. 使用空余空间循环复用', 'D', '循环队列通过复用空余空间来避免队列溢出。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 队列通常不用于以下哪项操作？ (2分)', 'A. 实现广度优先搜索（BFS）', 'B. 数据流处理', 'C. 排序算法', 'D. 实现打印任务调度', 'C', '队列不常用于排序算法，主要应用于广度优先搜索、数据流处理和任务调度等。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 在队列的实现中，什么是“队头”元素？ (2分)', 'A. 最先被插入的元素', 'B. 最后被插入的元素', 'C. 最先被删除的元素', 'D. 最后被删除的元素', 'C', '队头元素是最先进入队列并将最先被删除的元素。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 在队列中，什么是“入队”操作？ (2分)', 'A. 将一个元素插入到队列的末尾', 'B. 将一个元素插入到队列的开头', 'C. 将一个元素从队列中删除', 'D. 查询队列中的元素', 'A', '入队操作是将元素插入队列的末尾。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 队列常用在哪些场景？ (2分)', 'A. 打印任务调度', 'B. 网络数据包缓冲', 'C. CPU调度', 'D. 以上都是', 'D', '队列广泛应用于打印任务调度、网络数据包缓冲和CPU调度等场景。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 循环队列相较于线性队列的优势是什么？ (2分)', 'A. 不会出现“队列满”情况', 'B. 节省空间，避免浪费', 'C. 可以进行随机访问', 'D. 更易于实现', 'B', '循环队列避免了线性队列中由于空间浪费导致的队列满情况，节省空间。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 什么情况下队列的“队尾”指针会发生变化？ (2分)', 'A. 入队操作', 'B. 出队操作', 'C. 查询操作', 'D. 队列为空时', 'A', '队尾指针会在入队操作时发生变化。', '0', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 队列是一种先进先出（FIFO）结构。 (2分)', 'A. 是', 'B. 否', 'A', '队列遵循先进先出（FIFO）的原则。', '1', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 队列在入队时不会改变队尾指针的位置。 (2分)', 'A. 是', 'B. 否', 'B', '入队操作会将元素插入队列尾部，并改变队尾指针的位置。', '1', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 在队列的实现中，出队操作会改变队头指针的位置。 (2分)', 'A. 是', 'B. 否', 'A', '出队操作会删除队头元素，并改变队头指针的位置。', '1', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 循环队列可以有效解决线性队列在队列满时的问题。 (2分)', 'A. 是', 'B. 否', 'A', '循环队列通过循环复用空闲空间，避免了线性队列中队列满时无法继续入队的问题。', '1', '3', '3.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 队列通常不能用于实现广度优先搜索（BFS）算法。 (2分)', 'A. 是', 'B. 否', 'B', '队列广泛应用于广度优先搜索（BFS）算法，用于存储待访问的节点。', '1', '3', '3.4')
""")

# --------------33333333333333333333333333333------------------3.4.2
# --------------33333333333333333333333333333------------------3.4.2
# --------------33333333333333333333333333333------------------3.4.2
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 栈是一种什么类型的数据结构？ (2分)', 'A. 先进先出（FIFO）', 'B. 后进先出（LIFO）', 'C. 队列', 'D. 双向链表', 'B', '栈是一种后进先出（LIFO）数据结构，最后进入的元素最先出栈。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 以下哪种情况最适合使用栈？ (2分)', 'A. 树的遍历', 'B. 计算机程序的递归调用', 'C. 快速排序', 'D. 文件缓存', 'B', '栈常用于实现递归调用，存储函数的调用信息。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 栈的“压栈”操作是指什么？ (2分)', 'A. 从栈中删除元素', 'B. 将元素插入栈顶', 'C. 从栈底插入元素', 'D. 查找栈中的元素', 'B', '压栈操作是将元素添加到栈顶。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 在栈中，哪项操作会改变栈顶指针的位置？ (2分)', 'A. 入栈', 'B. 出栈', 'C. 查看栈顶元素', 'D. 清空栈', 'B', '出栈操作会删除栈顶元素，并改变栈顶指针的位置。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 以下哪项是栈的特点？ (2分)', 'A. 支持随机访问', 'B. 支持先入先出', 'C. 支持后进先出', 'D. 支持队列操作', 'C', '栈遵循后进先出（LIFO）的原则，最后进入的元素最先出栈。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 栈常常用于哪种算法的实现？ (2分)', 'A. 深度优先搜索（DFS）', 'B. 广度优先搜索（BFS）', 'C. Dijkstra算法', 'D. 归并排序', 'A', '栈常用于实现深度优先搜索（DFS）算法，保存遍历路径。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 以下关于栈的描述，哪一项是错误的？ (2分)', 'A. 栈的访问方式是先进先出', 'B. 栈可以通过数组或链表实现', 'C. 栈用于函数调用管理', 'D. 栈在表达式求值中有广泛应用', 'A', '栈是一种后进先出（LIFO）的数据结构，而不是先进先出（FIFO）。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 以下哪种实现方式适用于栈？ (2分)', 'A. 顺序存储', 'B. 链式存储', 'C. 以上都可以', 'D. 双向链表', 'C', '栈可以通过顺序存储（数组）或链式存储（链表）实现。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 栈的“出栈”操作是什么？ (2分)', 'A. 从栈底删除元素', 'B. 从栈顶删除元素', 'C. 从栈底插入元素', 'D. 查看栈底元素', 'B', '出栈操作是将栈顶元素删除，并返回该元素。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 在栈的实现中，如何检测栈是否为空？ (2分)', 'A. 判断栈顶指针是否为0', 'B. 判断栈底指针是否为最大容量', 'C. 判断栈顶指针是否为-1', 'D. 判断栈中元素个数是否为负', 'C', '栈为空时，栈顶指针通常为-1，表示没有元素。', '0', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 栈是一种后进先出（LIFO）数据结构。 (2分)', 'A. 是', 'B. 否', 'A', '栈遵循后进先出（LIFO）的原则，最后进入的元素最先出栈。', '1', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 栈只能通过链表来实现。 (2分)', 'A. 是', 'B. 否', 'B', '栈可以通过数组或链表来实现，数组和链表都有各自的优势。', '1', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 栈常用于实现广度优先搜索（BFS）算法。 (2分)', 'A. 是', 'B. 否', 'B', '栈常用于深度优先搜索（DFS）算法，而广度优先搜索（BFS）通常使用队列。', '1', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 在栈的实现中，“压栈”操作会改变栈顶指针的位置。 (2分)', 'A. 是', 'B. 否', 'A', '压栈操作会将元素加入栈顶，并改变栈顶指针的位置。', '1', '3', '3.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 栈可以实现回溯算法。 (2分)', 'A. 是', 'B. 否', 'A', '栈可以通过保存函数调用的状态来实现回溯算法，逐步恢复到上一步。', '1', '3', '3.4.2')
""")

# --------------33333333333333333333333333333------------------3.5
# --------------33333333333333333333333333333------------------3.5
# --------------33333333333333333333333333333------------------3.5
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 数据结构中，哪种结构用于存储线性元素并允许随机访问？ (2分)', 'A. 栈', 'B. 队列', 'C. 数组', 'D. 链表', 'C', '数组是一种存储线性元素的数据结构，支持随机访问，索引元素的时间复杂度为O(1)。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 下列哪种数据结构适合用于实现操作系统中的任务调度？ (2分)', 'A. 栈', 'B. 队列', 'C. 哈希表', 'D. 图', 'B', '队列遵循先进先出（FIFO）规则，适用于任务调度等按顺序处理的场景。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 哈希表的关键特性是什么？ (2分)', 'A. 支持随机访问', 'B. 不支持重复元素', 'C. 允许通过键直接查找值', 'D. 需要排序', 'C', '哈希表通过哈希函数将键映射到特定位置，实现快速查找，插入和删除操作。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 以下哪种数据结构不支持随机访问？ (2分)', 'A. 数组', 'B. 链表', 'C. 哈希表', 'D. 堆', 'B', '链表是线性结构，不能通过索引随机访问其元素，访问是顺序进行的。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 二叉树的最大深度是指什么？ (2分)', 'A. 树的最深层节点的层数', 'B. 从根节点到最远叶子节点的路径长度', 'C. 树的叶子节点数量', 'D. 每层节点的平均数量', 'B', '二叉树的最大深度是指从根节点到最远叶子节点的路径长度。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 什么是图的邻接矩阵？ (2分)', 'A. 存储图中节点之间的关系，使用二维数组表示', 'B. 存储图的节点值，使用一维数组表示', 'C. 存储每个节点的度数，使用二维数组表示', 'D. 存储图的边权值，使用一维数组表示', 'A', '邻接矩阵是图的常见表示方式，使用二维数组存储节点间的连接关系。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 下列哪种数据结构通常用于实现图的广度优先遍历（BFS）？ (2分)', 'A. 栈', 'B. 队列', 'C. 链表', 'D. 哈希表', 'B', '广度优先搜索（BFS）通常使用队列进行实现，因为队列符合先进先出（FIFO）的原则。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 动态数组和链表相比，哪个数据结构在随机访问时更高效？ (2分)', 'A. 动态数组', 'B. 链表', 'C. 都一样', 'D. 取决于数据大小', 'A', '动态数组支持通过索引进行随机访问，时间复杂度为O(1)，而链表需要顺序遍历。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 以下哪种数据结构通常用于实现递归算法的调用栈？ (2分)', 'A. 数组', 'B. 栈', 'C. 队列', 'D. 链表', 'B', '栈是一种后进先出（LIFO）的数据结构，非常适合用于存储递归调用的信息。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 线性数据结构中，哪一项数据结构支持对头部进行高效的插入和删除操作？ (2分)', 'A. 数组', 'B. 栈', 'C. 链表', 'D. 队列', 'C', '链表在头部插入和删除元素的时间复杂度为O(1)，非常高效。', '0', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('11. 二叉树的每个节点最多可以有两个子节点。 (2分)', 'A. 是', 'B. 否', 'A', '二叉树的每个节点最多有两个子节点，即左子节点和右子节点。', '1', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('12. 在哈希表中，冲突是指两个不同的键被哈希到同一个位置。 (2分)', 'A. 是', 'B. 否', 'A', '哈希冲突是指两个不同的键被哈希到相同的索引位置，这时需要采取冲突解决策略。', '1', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('13. 图的邻接矩阵表示法是一种稀疏图的高效存储方式。 (2分)', 'A. 是', 'B. 否', 'B', '邻接矩阵适用于稠密图，对于稀疏图来说，邻接表更加高效。', '1', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('14. 队列是一种先进先出（FIFO）的数据结构。 (2分)', 'A. 是', 'B. 否', 'A', '队列遵循先进先出（FIFO）原则，首先进入队列的元素最先被移除。', '1', '3', '3.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('15. 链表的插入和删除操作的时间复杂度总是O(1)，无论插入位置在哪里。 (2分)', 'A. 是', 'B. 否', 'B', '链表在头部插入和删除元素的时间复杂度为O(1)，但在其他位置插入或删除需要遍历，时间复杂度为O(n)。', '1', '3', '3.5')
""")

#  4.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在数据结构中，串是指（ ）。 (2分)', 'A. 有序字符的集合', 'B. 线性表的一种变形', 'C. 二叉树的一种类型', 'D. 一种非线性结构',  'A', '串是字符组成的线性表，具有有序性和可变性','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 下列关于串的长度的描述中，正确的是（ ）。 (2分)', 'A. 包括串的终止符', 'B. 等于串中字符的个数', 'C. 总是一个偶数', 'D. 等于串的编码长度',  'B', '串的长度定义为其字符个数，不包括终止符','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 以下操作中，哪一项不属于串的基本操作？ (2分)', 'A. 求子串', 'B. 串的合并', 'C. 查找子串', 'D. 删除非字符数据',  'D', '串操作包括子串处理、拼接和定位等，与非字符数据无关','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 在串的存储结构中，采用定长存储的优点是（ ）。 (2分)', 'A. 节省存储空间', 'B. 操作灵活', 'C. 存储地址容易计算', 'D. 避免碎片',  'C', '定长存储的特点是存储位置可以通过简单的计算得出','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. KMP算法的核心思想是（ ）。 (2分)', 'A. 构造一个指向下标的表', 'B. 利用部分匹配表避免回溯', 'C. 提高匹配的空间复杂度', 'D. 以暴力匹配方式提高效率',  'B', 'KMP算法利用部分匹配表避免了字符重复匹配','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 串的顺序存储结构的特点是（ ）。 (2分)', 'A. 数据随机存储', 'B. 数据按存储顺序排列', 'C. 支持快速查找子串', 'D. 不需要额外存储空间',  'B', '顺序存储要求字符按线性顺序存储','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 在KMP算法中，next数组的作用是（ ）。 (2分)', 'A. 记录字符串的位置', 'B. 记录匹配失败时的回溯点', 'C. 记录匹配成功的长度', 'D. 存储字符的ASCII值',  'B', 'next数组的目的是在匹配失败时提供回溯点','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 假设有两个串S1和S2，若S1大于S2的含义是（ ）。 (2分)', 'A. S1中字符的ASCII值总和大于S2', 'B. S1的长度大于S2', 'C. S1的字符在字典序中大于S2', 'D. S1的存储空间大于S2',  'C', '串比较基于字典序','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 若串S包含子串T，以下哪个操作可以实现子串的定位？ (2分)', 'A. index(S,T)', 'B. concat(S,T)', 'C. replace(S,T)', 'D. length(S)',  'A', 'index是定位子串的标准操作','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 串的存储形式包括以下哪种？ (2分)', 'A. 顺序存储', 'B. 链式存储', 'C. 索引存储', 'D. A和B',  'D', '串可以顺序或链式存储','0','4' ,'4.1') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 串是一种线性数据结构。 (2分)', 'A. 是', 'B. 否',  'A', '串是由字符组成的线性表','1','4' ,'4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 串的存储结构可以采用链表表示。 (2分)', 'A. 是', 'B. 否',  'A', '链表是串存储的一种方式','1','4' ,'4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. KMP算法的时间复杂度是O(n)。 (2分)', 'A. 是', 'B. 否',  'A', 'KMP算法通过next数组优化了匹配过程','1','4' ,'4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 顺序存储的串可以动态扩展存储空间。 (2分)', 'A. 是', 'B. 否',  'B', '顺序存储需要固定存储空间，无法动态扩展','1','4' ,'4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 计算两个串的拼接结果的时间复杂度为O(n)。 (2分)', 'A. 是', 'B. 否',  'A', '串拼接需要逐字符复制，时间复杂度为O(n)','1','4' ,'4.1')
""")

#  4.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 串的顺序存储结构的优点是（ ）。 (2分)', 'A. 存储密度高', 'B. 动态存储灵活', 'C. 便于插入和删除操作', 'D. 不需要预分配存储空间',  'A', '顺序存储结构紧凑，存储密度高','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 串的链式存储结构的一个显著特点是（ ）。 (2分)', 'A. 每个结点存储一个字符', 'B. 需要额外的指针域', 'C. 只能用于存储字符串', 'D. 顺序存储在内存中',  'B', '链式存储需要指针域来表示结点间的关系','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 在顺序存储的串中，访问某个字符的时间复杂度为（ ）。 (2分)', 'A. O(1)', 'B. O(logn)', 'C. O(n)', 'D. O(n^2)',  'A', '顺序存储支持随机访问，时间复杂度为O(1)','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 在链式存储的串中，查找第k个字符的时间复杂度为（ ）。 (2分)', 'A. O(1)', 'B. O(k)', 'C. O(logk)', 'D. O(k^2)',  'B', '链式存储需要依次遍历，时间复杂度为O(k)','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 若串S采用顺序存储结构，下列哪项操作的效率最高？ (2分)', 'A. 求长度', 'B. 插入字符', 'C. 删除字符', 'D. 查找子串',  'A', '长度存储为属性，读取时间为O(1)','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 下列关于顺序存储结构和链式存储结构的描述，错误的是（ ）。 (2分)', 'A. 顺序存储效率高但灵活性低', 'B. 链式存储插入效率高但空间利用率低', 'C. 链式存储在内存中是连续存储', 'D. 顺序存储适合固定长度的串',  'C', '链式存储的结点通常在内存中不连续','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 在顺序存储中，串的拼接操作的时间复杂度是（ ）。 (2分)', 'A. O(1)', 'B. O(n)', 'C. O(logn)', 'D. O(n^2)',  'B', '拼接需要复制字符，时间复杂度为O(n)','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 链式存储的串适合于以下哪种情况？ (2分)', 'A. 串的长度变化较频繁', 'B. 串中字符的访问频率高', 'C. 串的内容固定不变', 'D. 串的存储密度要求高',  'A', '链式存储适合长度变化较频繁的场景','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在链式存储的串中，每个结点一般包含（ ）。 (2分)', 'A. 数据域和前驱指针', 'B. 数据域和后继指针', 'C. 数据域和两个指针域', 'D. 数据域和长度域',  'B', '链式存储的每个结点包含数据域和后继指针','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 顺序存储和链式存储的主要区别是（ ）。 (2分)', 'A. 存储密度不同', 'B. 存储是否连续', 'C. 操作效率不同', 'D. B和C',  'D', '链式存储不连续，插入删除效率较高','0','4' ,'4.2') 
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 顺序存储的串占用的空间大小可以动态调整。 (2分)', 'A. 是', 'B. 否',  'B', '顺序存储需要固定分配空间','1','4' ,'4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 链式存储的串的存储密度低于顺序存储的串。 (2分)', 'A. 是', 'B. 否',  'A', '链式存储需要额外的指针域','1','4' ,'4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 顺序存储的串可以通过计算下标直接访问字符。 (2分)', 'A. 是', 'B. 否',  'A', '顺序存储支持随机访问','1','4' ,'4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 链式存储的串适合处理非常长的串。 (2分)', 'A. 是', 'B. 否',  'A', '链式存储更灵活，适合长串','1','4' ,'4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 顺序存储的串和链式存储的串的时间复杂度完全相同。 (2分)', 'A. 是', 'B. 否',  'B', '不同操作的复杂度不同','1','4' ,'4.2')
""")

#  4.3.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在BF算法中，若主串长度为n，模式串长度为m，则该算法的最坏时间复杂度是（ ）。 (2分)', 'A. O(m)', 'B. O(n)', 'C. O(m*n)', 'D. O(m^2)', 'C', 'BF算法在最坏情况下需要进行O(m*n)次比较','0','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. BF算法的主要特点是（ ）。 (2分)', 'A. 从后向前匹配', 'B. 从前向后逐位匹配', 'C. 双向匹配', 'D. 递归匹配', 'B', 'BF算法通过逐位比较来进行模式匹配','0','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 在BF算法中，当匹配失败时，主串的指针应移动到（ ）。 (2分)', 'A. 主串当前位置的下一位', 'B. 模式串起始位置', 'C. 上一次匹配的下一位', 'D. 模式串当前位置的下一位', 'A', 'BF算法每次匹配失败时，主串指针后移一位','0','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 对于一个主串长度为10，模式串长度为3的匹配问题，BF算法最多需要进行（ ）次比较。 (2分)', 'A. 7', 'B. 10', 'C. 28', 'D. 21', 'C', '最坏情况下，BF算法需比较(n - m + 1) * m 次','0','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. BF算法是一种（ ）的匹配算法。 (2分)', 'A. 高效', 'B. 复杂', 'C. 低效', 'D. 动态规划', 'C', '由于其逐字符匹配的性质，BF算法相对低效','0','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. BF算法最适用于（ ）的场景。 (2分)', 'A. 模式串较短的情况', 'B. 主串较短的情况', 'C. 模式串较长的情况', 'D. 任意情况', 'A', 'BF算法适合于较短的模式串或匹配次数较少的情况','0','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 若模式串为“abc”，主串为“abcabcabc”，在BF算法中，匹配次数为（ ）。 (2分)', 'A. 3', 'B. 9', 'C. 6', 'D. 4', 'A', 'BF算法会依次匹配每个位置，共3次匹配成功','0','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. BF算法的优点是（ ）。 (2分)', 'A. 结构复杂', 'B. 实现简单', 'C. 效率高', 'D. 需要额外的存储空间', 'B', 'BF算法的实现非常简单','0','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在BF算法中，若主串和模式串长度相同，则匹配复杂度为（ ）。 (2分)', 'A. O(n)', 'B. O(n^2)', 'C. O(log n)', 'D. O(1)', 'A', '当主串和模式串长度相同时，BF算法的复杂度为O(n)','0','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在字符串匹配算法中，BF算法的主要缺点是（ ）。 (2分)', 'A. 空间复杂度高', 'B. 时间复杂度高', 'C. 无法处理特殊字符', 'D. 匹配准确度低', 'B', 'BF算法逐位匹配，时间复杂度较高','0','4' ,'4.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. BF算法需要逐个字符进行匹配，因此效率较低。 (2分)', 'A. 是', 'B. 否',  'A', 'BF算法逐字符比较，效率较低','1','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 在BF算法中，如果匹配失败，主串指针会回退到初始位置。 (2分)', 'A. 是', 'B. 否',  'B', '匹配失败时主串指针只需前进一位','1','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. BF算法的最坏时间复杂度是O(m*n)。 (2分)', 'A. 是', 'B. 否',  'A', 'BF算法最坏情况下需O(m*n)次匹配','1','4' ,'4.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. BF算法的匹配过程不需要额外的存储空间。 (2分)', 'A. 是', 'B. 否',  'A', 'BF算法不需额外存储空间','1','4' ,'4.3.1')
""")

#  4.3.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. KMP算法的核心思想是（ ）。 (2分)', 'A. 从头逐位匹配', 'B. 根据部分匹配信息跳过部分字符', 'C. 使用递归方式匹配', 'D. 匹配失败后主串指针回退', 'B', 'KMP算法利用部分匹配表跳过重复比较的字符，提高匹配效率','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. KMP算法引入的部分匹配表称为（ ）。 (2分)', 'A. 散列表', 'B. 前缀表', 'C. next数组', 'D. 主串表', 'C', 'KMP算法通过next数组来存储部分匹配信息','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. KMP算法的最坏时间复杂度是（ ）。 (2分)', 'A. O(m*n)', 'B. O(m)', 'C. O(n)', 'D. O(n + m)', 'D', '在最坏情况下，KMP算法的时间复杂度为O(n + m)','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 在构造next数组时，next数组的值主要反映了（ ）。 (2分)', 'A. 后缀与前缀的匹配情况', 'B. 字符重复情况', 'C. 主串字符位置', 'D. 匹配成功次数', 'A', 'next数组记录了前缀与后缀的匹配情况，用于跳过不必要的比较','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在KMP算法中，如果next[j] = -1，则表示（ ）。 (2分)', 'A. 模式串已匹配成功', 'B. 无法匹配，需移到主串下一位', 'C. 匹配到模式串的第一个字符', 'D. 匹配失败，需重新开始', 'C', 'next[j] = -1表示匹配到了模式串的起始位置','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 假设模式串的next数组为[0, 1, 0, 2, 3]，则模式串的长度是（ ）。 (2分)', 'A. 3', 'B. 4', 'C. 5', 'D. 6', 'C', 'next数组的长度与模式串长度相同','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 假设主串长度为15，模式串长度为5，则KMP算法在最坏情况下的时间复杂度为（ ）。 (2分)', 'A. O(5)', 'B. O(10)', 'C. O(15)', 'D. O(20)', 'C', 'KMP算法的时间复杂度取决于主串和模式串的长度，最坏情况为O(n + m)','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. KMP算法在模式串匹配失败时，依赖next数组的作用是（ ）。 (2分)', 'A. 减少主串和模式串的比较次数', 'B. 提前退出匹配', 'C. 固定跳过字符', 'D. 重置主串指针', 'A', 'next数组可以减少不必要的比较，从而加速匹配过程','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. KMP算法中，若next数组中某个位置的值为3，则表示模式串此位置的最长前后缀长度为（ ）。 (2分)', 'A. 1', 'B. 2', 'C. 3', 'D. 4', 'C', 'next数组的值表示前后缀的长度','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. KMP算法相较于BF算法的优势在于（ ）。 (2分)', 'A. 减少空间开销', 'B. 增加空间开销', 'C. 减少不必要的匹配', 'D. 减少模式串长度', 'C', 'KMP算法通过next数组减少不必要的匹配，提高效率','0','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. KMP算法主要通过利用前缀表来加快匹配过程。 (2分)', 'A. 是', 'B. 否',  'A', 'KMP算法依赖next数组加速匹配','1','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. KMP算法的时间复杂度与主串和模式串的长度无关。 (2分)', 'A. 是', 'B. 否',  'B', 'KMP算法时间复杂度取决于主串和模式串长度','1','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 在KMP算法中，next数组的构造是为了减少匹配次数。 (2分)', 'A. 是', 'B. 否',  'A', 'next数组通过记录部分匹配信息来减少匹配次数','1','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 在KMP算法中，若模式串与主串前缀匹配成功后，不需要重新匹配。 (2分)', 'A. 是', 'B. 否',  'A', 'KMP算法通过next数组减少重复匹配','1','4' ,'4.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. KMP算法相比BF算法，不适合处理大规模文本匹配问题。 (2分)', 'A. 是', 'B. 否',  'B', 'KMP算法适用于大规模文本匹配问题','1','4' ,'4.3.2')
""")

#  4.4 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在数组中，元素的存储地址通过下标计算得到，因此数组支持的时间复杂度为O(1)的操作是（ ）。 (2分)', 'A. 插入元素', 'B. 删除元素', 'C. 随机访问', 'D. 修改大小', 'C', '数组支持随机访问，因此访问时间复杂度为O(1)','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 假设一个一维数组A有10个元素，其存储类型是int（占用4个字节），则数组的总占用空间为（ ）。 (2分)', 'A. 20字节', 'B. 30字节', 'C. 40字节', 'D. 50字节', 'C', '数组A的元素数量为10，每个元素占4字节，因此总占用空间为40字节','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 在C语言中，假设int数组a的首地址为1000，a[4]的地址为（ ）。 (2分)', 'A. 1004', 'B. 1016', 'C. 1020', 'D. 1032', 'C', 'a[4]的地址为首地址加上4*4=16字节，因此为1020','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 在插入操作中，若要在数组的第一个位置插入一个新元素，最坏情况下的时间复杂度是（ ）。 (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '数组在第一个位置插入元素时，需将所有元素后移，时间复杂度为O(n)','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在多维数组中，二维数组的下标为A[i][j]，通常用于表示（ ）。 (2分)', 'A. 一维数组', 'B. 二维矩阵', 'C. 三维矩阵', 'D. 树形结构', 'B', 'A[i][j]用于表示二维矩阵中的元素','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 若一个数组的大小为10，在访问数组时若访问索引为11的元素，将会导致（ ）。 (2分)', 'A. 元素覆盖', 'B. 越界访问错误', 'C. 自动扩展数组', 'D. 无任何影响', 'B', '访问越界索引会导致越界访问错误','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 数组作为一种线性表，其特点不包括（ ）。 (2分)', 'A. 随机访问', 'B. 插入删除灵活', 'C. 占用连续存储空间', 'D. 元素类型相同', 'B', '数组的特点是随机访问快，但插入删除不灵活','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 在数组中，假设数组元素按行优先存储，下标为A[3][2]的元素，其地址计算公式为（ ）。 (2分)', 'A. Base + (i * col + j) * w', 'B. Base + (j * col + i) * w', 'C. Base + (i + j) * w', 'D. Base + (i * row + j) * w', 'A', '按行优先存储的地址公式为Base + (i * col + j) * w','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在数组操作中，若按元素值查找特定元素，通常采用的最优算法为（ ）。 (2分)', 'A. 线性查找', 'B. 二分查找', 'C. 插值查找', 'D. 哈希查找', 'B', '若数组有序，二分查找可提高查找效率','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 二维数组A[3][3]存储在一维数组中，假设按行优先存储，第3行第2列的元素在一维数组中的下标为（ ）。 (2分)', 'A. 5', 'B. 6', 'C. 7', 'D. 8', 'D', '按行优先存储，位置为3*3+2=8','0','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 数组是一种线性结构，具有随机访问的特点。 (2分)', 'A. 是', 'B. 否',  'A', '数组是线性结构并支持随机访问','1','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 数组的内存地址必须是连续的，因此不支持动态扩展。 (2分)', 'A. 是', 'B. 否',  'A', '数组内存地址连续，导致不支持动态扩展','1','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 在数组中删除元素需要移动元素，时间复杂度为O(n)。 (2分)', 'A. 是', 'B. 否',  'A', '删除操作需移动其他元素，时间复杂度为O(n)','1','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 数组是同类型元素的集合。 (2分)', 'A. 是', 'B. 否',  'B', '无','1','4' ,'4.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 数组可看成线性表的一种推广，因此与线性表一样，其基本运算有插入和删除等。 (2分)', 'A. 是', 'B. 否',  'B', '无','1','4' ,'4.4')
""")

#  4.5.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('1. 对于对称矩阵的压缩存储，通常只存储（ ）。 (2分)', 'A. 主对角线上的元素', 'B. 主对角线以下的元素', 'C. 主对角线及其以上的元素', 'D. 所有元素', 'C', '对称矩阵中，只需存储主对角线及其上或其下的元素以节省空间','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('2. 在压缩存储上三角矩阵时，存储元素的个数为（ ）。 (2分)', 'A. n', 'B. n*(n+1)/2', 'C. n^2', 'D. 2n-1', 'B', '上三角矩阵的元素数为n*(n+1)/2','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('3. 在n阶三对角矩阵中，总共需要存储的元素数量为（ ）。 (2分)', 'A. 3n-2', 'B. n^2', 'C. n', 'D. 2n', 'A', '三对角矩阵只存储主对角线及相邻两条对角线，共3n-2个元素','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('4. 对于稀疏矩阵的压缩存储，通常采用的存储方法是（ ）。 (2分)', 'A. 顺序存储', 'B. 链式存储', 'C. 三元组表', 'D. 栈存储', 'C', '稀疏矩阵通常使用三元组表来仅存储非零元素','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('5. 下列哪种矩阵适合用压缩存储以节省空间？（ ）。 (2分)', 'A. 稠密矩阵', 'B. 稀疏矩阵', 'C. 上下三角矩阵', 'D. 对称矩阵', 'B', '稀疏矩阵中零元素较多，适合压缩存储','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('6. 在压缩存储三对角矩阵时，存储下标i行j列的元素a[i][j]的方式是（ ）。 (2分)', 'A. 通过偏移量计算', 'B. 按顺序存储', 'C. 链表存储', 'D. 二维数组存储', 'A', '三对角矩阵通常用偏移量计算元素在存储数组中的位置','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('7. 下列哪种压缩方法最适合于下三角矩阵的存储？（ ）。 (2分)', 'A. 只存储对角线以上元素', 'B. 只存储对角线及对角线以下的元素', 'C. 按列优先顺序存储', 'D. 三元组表', 'B', '下三角矩阵只需存储对角线及以下元素以节省空间','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('8. 在n阶稀疏矩阵的压缩存储中，若矩阵的非零元素个数为m，则空间复杂度为（ ）。 (2分)', 'A. O(m)', 'B. O(n)', 'C. O(n^2)', 'D. O(log n)', 'A', '稀疏矩阵存储的空间复杂度通常与非零元素个数m成正比','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('9. 用压缩存储法存储对称矩阵A[4][4]，只需存储的元素数为（ ）。 (2分)', 'A. 6', 'B. 8', 'C. 10', 'D. 16', 'C', '4阶对称矩阵需要存储4*(4+1)/2=10个元素','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy, question_type, chapter, subchapter)
VALUES ('10. 稀疏矩阵中用链表表示法存储的优点是（ ）。 (2分)', 'A. 能够快速进行算术运算', 'B. 存储密集数据', 'C. 节省存储空间', 'D. 易于数据排序', 'C', '稀疏矩阵用链表表示法节省了存储零元素的空间','0','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 稀疏矩阵的压缩存储仅存储非零元素，节省存储空间。 (2分)', 'A. 是', 'B. 否',  'A', '稀疏矩阵的压缩存储方法仅存储非零元素','1','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 对称矩阵的压缩存储可以只存储主对角线及其以下元素。 (2分)', 'A. 是', 'B. 否',  'A', '对称矩阵只需存储一半的元素','1','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 三对角矩阵的压缩存储只需要存储主对角线及相邻的两条对角线。 (2分)', 'A. 是', 'B. 否',  'A', '三对角矩阵只需存储三条对角线上的元素','1','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 在上三角矩阵的压缩存储中，主对角线以上的元素不会被存储。 (2分)', 'A. 是', 'B. 否',  'B', '上三角矩阵存储主对角线及其上元素','1','4' ,'4.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 稀疏矩阵的链表存储法不支持高效的矩阵转置操作。 (2分)', 'A. 是', 'B. 否',  'A', '链表存储法在矩阵转置时较低效','1','4' ,'4.5.1')
""")

#  4.5.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 稀疏矩阵通常的压缩存储方法是（ ）。 (2分)', 'A. 顺序存储', 'B. 三元组表', 'C. 散列表存储', 'D. 链式存储', 'B', '三元组表是一种常用的稀疏矩阵压缩存储方法，记录行、列和非零值','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 稀疏矩阵的三元组表存储中，每个非零元素需要存储的信息包括（ ）。 (2分)', 'A. 行号和列号', 'B. 行号、列号和值', 'C. 列号和值', 'D. 行号和值', 'B', '三元组表存储行号、列号和值三部分信息','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 如果稀疏矩阵的行数为m，列数为n，非零元素数为t，三元组表所需的存储空间为（ ）。 (2分)', 'A. O(m)', 'B. O(n)', 'C. O(t)', 'D. O(m+n+t)', 'C', '三元组表只存储非零元素，因此其存储复杂度为O(t)','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 稀疏矩阵中零元素的比例通常（ ）。 (2分)', 'A. 小于50%', 'B. 大于50%', 'C. 等于50%', 'D. 无法确定', 'B', '稀疏矩阵的零元素比例通常大于50%，因此采用压缩存储','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 稀疏矩阵的压缩存储方法不包括（ ）。 (2分)', 'A. 三元组表', 'B. 压缩行存储', 'C. 链表存储', 'D. 栈存储', 'D', '稀疏矩阵的压缩存储常用三元组表、压缩行存储和链表存储，但不采用栈存储','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 三元组表法中，稀疏矩阵转置的时间复杂度是（ ）。 (2分)', 'A. O(t)', 'B. O(m+n)', 'C. O(t^2)', 'D. O(1)', 'A', '稀疏矩阵转置时，依次调整三元组表中列号和行号，时间复杂度为O(t)','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 使用压缩行存储（CRS）方法，存储的数组不包括（ ）。 (2分)', 'A. 值数组', 'B. 行指针数组', 'C. 列索引数组', 'D. 对角线数组', 'D', 'CRS方法存储值数组、行指针数组和列索引数组，但不包括对角线数组','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 如果稀疏矩阵为对称矩阵，则压缩存储的特点是（ ）。 (2分)', 'A. 存储所有元素', 'B. 只存储主对角线及以上或以下元素', 'C. 按行存储非零元素', 'D. 转换为稠密矩阵存储', 'B', '对称稀疏矩阵只需存储主对角线及以上或以下元素以节省空间','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 稀疏矩阵的列压缩存储（CCS）方法的优点是（ ）。 (2分)', 'A. 支持快速行访问', 'B. 支持快速列访问', 'C. 支持快速查找对角元素', 'D. 支持快速转置操作', 'B', 'CCS方法按列存储数据，因此支持快速列访问','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 稀疏矩阵在实际应用中的优点是（ ）。 (2分)', 'A. 节省存储空间', 'B. 提高运算效率', 'C. 简化矩阵操作', 'D. 以上都是', 'D', '稀疏矩阵在节省空间和优化运算方面具有显著优势','0','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 稀疏矩阵的三元组表法可以通过交换行号和列号实现矩阵转置。 (2分)', 'A. 是', 'B. 否',  'A', '三元组表法通过调整行号和列号可实现转置操作','1','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 稀疏矩阵的稠密部分不适合压缩存储。 (2分)', 'A. 是', 'B. 否',  'A', '稀疏矩阵中稠密部分不适合压缩存储，因为没有明显的零元素分布','1','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 稀疏矩阵的压缩行存储方法支持快速行访问。 (2分)', 'A. 是', 'B. 否',  'A', 'CRS方法中行指针数组用于快速访问指定行','1','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 稀疏矩阵中零元素的比例小于50%。 (2分)', 'A. 是', 'B. 否',  'B', '稀疏矩阵零元素比例大于50%，因此适合压缩存储','1','4' ,'4.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 稀疏矩阵的压缩存储一定能够减少时间复杂度。 (2分)', 'A. 是', 'B. 否',  'B', '稀疏矩阵压缩存储减少的是空间复杂度，但不一定减少时间复杂度','1','4' ,'4.5.2')
""")

#  4.6.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 列序递增法是矩阵转置的一种算法，其中对矩阵的元素按（ ）。 (2分)', 'A. 行序递增', 'B. 列序递增', 'C. 元素值递增', 'D. 随机顺序', 'B', '列序递增法的核心在于按列顺序遍历矩阵的元素','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在列序递增法中，矩阵的转置操作是通过交换（ ）。 (2分)', 'A. 行和列的索引', 'B. 列的值和行的值', 'C. 行和列的元素', 'D. 行和列的位置', 'A', '列序递增法通过交换行列索引来实现转置','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 列序递增法的时间复杂度为（ ）。 (2分)', 'A. O(m)', 'B. O(n)', 'C. O(mn)', 'D. O(log n)', 'C', '列序递增法需要遍历整个矩阵的每个元素，因此时间复杂度为O(mn)','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 列序递增法主要适用于（ ）。 (2分)', 'A. 小矩阵', 'B. 大矩阵', 'C. 对称矩阵', 'D. 非稀疏矩阵', 'B', '列序递增法对于大矩阵的转置具有较好的效果','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 列序递增法的主要优点是（ ）。 (2分)', 'A. 转置过程简单', 'B. 适合小矩阵', 'C. 时间复杂度低', 'D. 空间复杂度低', 'A', '列序递增法转置过程简单，按列顺序处理','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 在列序递增法中，转置后的矩阵的元素存放位置为（ ）。 (2分)', 'A. 仅交换行和列的顺序', 'B. 保持原位置不变', 'C. 原矩阵的行变成新矩阵的列', 'D. 原矩阵的列变成新矩阵的行', 'D', '列序递增法将原矩阵的列转置为新矩阵的行','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 列序递增法相比其他矩阵转置算法的优势是（ ）。 (2分)', 'A. 较低的内存占用', 'B. 实现更复杂', 'C. 操作更多的元素', 'D. 可以在原地转置', 'A', '列序递增法占用内存较低，适用于大规模数据处理','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 列序递增法的缺点是（ ）。 (2分)', 'A. 不适合大矩阵', 'B. 时间复杂度较高', 'C. 无法进行并行处理', 'D. 对内存要求较高', 'C', '列序递增法通常是顺序处理，不适合并行处理','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在列序递增法中，转置矩阵的元素位置交换是通过（ ）。 (2分)', 'A. 临时存储区', 'B. 直接交换内存地址', 'C. 使用栈实现', 'D. 在数组中实现', 'D', '列序递增法直接在数组中交换位置','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 使用列序递增法进行矩阵转置时，转置后的矩阵的维度是（ ）。 (2分)', 'A. 与原矩阵相同', 'B. 行列数互换', 'C. 不变', 'D. 仅行数改变', 'B', '列序递增法会将矩阵的行列互换','0','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 列序递增法是一种矩阵转置算法，其主要通过行索引递增来实现转置。 (2分)', 'A. 是', 'B. 否', 'B', '列序递增法按列索引递增，而不是行索引递增','1','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 列序递增法的时间复杂度与矩阵的维度无关。 (2分)', 'A. 是', 'B. 否', 'B', '列序递增法的时间复杂度是O(mn)，与矩阵的维度有关','1','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 列序递增法通过交换矩阵的行和列来实现转置。 (2分)', 'A. 是', 'B. 否', 'A', '列序递增法是通过交换矩阵的行和列的索引来完成转置的','1','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 列序递增法是一种高效的矩阵转置算法，适合用于小型矩阵。 (2分)', 'A. 是', 'B. 否', 'B', '列序递增法适合处理大型矩阵，对于小型矩阵的优势不明显','1','4' ,'4.6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 列序递增法通过直接修改矩阵的元素位置实现转置，无需额外的存储空间。 (2分)', 'A. 是', 'B. 否', 'A', '列序递增法可以在原地修改矩阵的元素位置，无需额外空间','1','4' ,'4.6.1')
""")

#  4.6.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 快速转置法主要用于（ ）。 (2分)', 'A. 对角线矩阵', 'B. 矩阵转置', 'C. 二维数组转置', 'D. 稀疏矩阵转置', 'D', '快速转置法主要用于转置稀疏矩阵，减少时间复杂度','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 快速转置法在矩阵转置时，主要优化了（ ）。 (2分)', 'A. 内存占用', 'B. 时间复杂度', 'C. 稳定性', 'D. 并行处理', 'B', '快速转置法通过减少冗余计算来降低时间复杂度','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 快速转置法的时间复杂度为（ ）。 (2分)', 'A. O(m)', 'B. O(n)', 'C. O(mn)', 'D. O(log n)', 'C', '快速转置法的时间复杂度仍然是O(mn)，但减少了计算量','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 快速转置法在处理稀疏矩阵时的优点是（ ）。 (2分)', 'A. 提高了内存的使用效率', 'B. 避免了冗余元素的处理', 'C. 保证了结果的正确性', 'D. 增加了计算复杂度', 'B', '快速转置法减少了冗余元素的计算，适用于稀疏矩阵','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 快速转置法最适合用在（ ）。 (2分)', 'A. 对称矩阵', 'B. 稠密矩阵', 'C. 稀疏矩阵', 'D. 单位矩阵', 'C', '对于稀疏矩阵，快速转置法能显著提高性能','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 快速转置法相比于普通转置法的优势是（ ）。 (2分)', 'A. 占用更少的内存', 'B. 更少的计算量', 'C. 更低的时间复杂度', 'D. 支持并行计算', 'B', '通过避免重复计算，快速转置法提高了效率','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 快速转置法通过（ ）。 (2分)', 'A. 转置矩阵的行列索引', 'B. 只处理稀疏矩阵中的非零元素', 'C. 重新排列矩阵的元素顺序', 'D. 动态调整矩阵的内存结构', 'B', '快速转置法处理稀疏矩阵时，仅考虑非零元素','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 在快速转置法中，矩阵转置后元素的位置是通过（ ）。 (2分)', 'A. 行列交换', 'B. 元素的值交换', 'C. 指针交换', 'D. 内存位置交换', 'A', '快速转置法通过交换行和列的索引来实现转置','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 使用快速转置法时，稀疏矩阵的转置可以在（ ）。 (2分)', 'A. 不改变内存结构的情况下进行', 'B. 利用递归方式实现', 'C. 在原地进行', 'D. 利用栈实现', 'C', '快速转置法可以在原地转置稀疏矩阵，无需额外的存储空间','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 快速转置法相比列序递增法的优势是（ ）。 (2分)', 'A. 处理稠密矩阵更高效', 'B. 适合并行处理', 'C. 更适合稀疏矩阵', 'D. 更易实现', 'C', '快速转置法适用于稀疏矩阵，可以减少计算量','0','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 快速转置法适用于处理稀疏矩阵。 (2分)', 'A. 是', 'B. 否', 'A', '快速转置法在处理稀疏矩阵时能够减少计算量','1','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 快速转置法比普通转置法有更高的内存占用。 (2分)', 'A. 是', 'B. 否', 'B', '快速转置法相对于普通转置法，在稀疏矩阵的情况下能减少内存占用','1','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 快速转置法可以通过直接修改矩阵的内存位置来转置矩阵。 (2分)', 'A. 是', 'B. 否', 'A', '快速转置法通过交换行和列的索引来修改矩阵的内存位置','1','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 快速转置法的主要优势在于优化了矩阵的空间复杂度。 (2分)', 'A. 是', 'B. 否', 'B', '快速转置法主要优化的是时间复杂度，而非空间复杂度','1','4' ,'4.6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 快速转置法可以通过避免冗余计算来提高稀疏矩阵的转置效率。 (2分)', 'A. 是', 'B. 否', 'A', '快速转置法通过减少冗余计算，能够提高稀疏矩阵转置的效率','1','4' ,'4.6.2')
""")

#  5.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在树结构中，根节点是（ ）。 (2分)', 'A. 树中深度最小的节点', 'B. 没有子节点的节点', 'C. 树中最左的节点', 'D. 树中度最大的节点', 'A', '根节点是深度最小的节点，即深度为0的节点','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在树中，节点的度是指（ ）。 (2分)', 'A. 节点的子树数目', 'B. 节点的深度', 'C. 节点的兄弟节点数', 'D. 节点的父节点数', 'A', '节点的度是指直接连接到该节点的子节点数','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 二叉树中，叶子节点的特点是（ ）。 (2分)', 'A. 没有父节点', 'B. 度为1', 'C. 度为0', 'D. 是树的根节点', 'C', '叶子节点的度为0，即没有子节点','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 满二叉树是指（ ）。 (2分)', 'A. 所有非叶节点都有两个子节点', 'B. 所有节点的度均为2', 'C. 所有叶子节点都在同一层', 'D. 每层节点数等于层数的平方', 'A', '满二叉树的非叶节点都正好有两个子节点','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在树中，路径的长度是指（ ）。 (2分)', 'A. 节点到根节点的距离', 'B. 两个节点之间边的数目', 'C. 根节点到叶子节点的距离', 'D. 树的高度', 'B', '路径长度是指两个节点之间边的数量','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 树的深度是指（ ）。 (2分)', 'A. 树的根节点的深度', 'B. 树中所有节点深度的和', 'C. 树中节点的最大层次值', 'D. 树的叶子节点的个数', 'C', '树的深度是树中节点的最大层次值','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 二叉树的性质是（ ）。 (2分)', 'A. 任意一个节点的子节点最多有2个', 'B. 每层节点的数量是固定的', 'C. 所有叶子节点都在同一层', 'D. 所有节点的度都相同', 'A', '二叉树中每个节点最多有两个子节点','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 对树的遍历不包括（ ）。 (2分)', 'A. 先序遍历', 'B. 中序遍历', 'C. 后序遍历', 'D. 层次遍历', 'D', '树的遍历方式通常包括先序、中序和后序遍历','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 如果树的高度为h，则最多有（ ）个节点。 (2分)', 'A. 2^h - 1', 'B. 2^h', 'C. h^2', 'D. 2h', 'A', '树的高度为h时最多有2^h - 1个节点','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在二叉树中，节点总数为n时，叶子节点数为（ ）。 (2分)', 'A. n/2', 'B. n/2 + 1', 'C. n - 1', 'D. n + 1', 'B', '在二叉树中，叶子节点数为(n/2 + 1)','0','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 二叉树中每个节点的度数最多为2。 (2分)', 'A. 是', 'B. 否', 'A', '二叉树中每个节点的度数确实最多为2','1','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 满二叉树的所有节点都必须有两个子节点。 (2分)', 'A. 是', 'B. 否', 'A', '满二叉树的所有非叶节点都有两个子节点','1','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 树的高度和树的深度是相同的概念。 (2分)', 'A. 是', 'B. 否', 'A', '树的高度和深度在概念上是等价的','1','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 所有二叉树都是二叉搜索树。 (2分)', 'A. 是', 'B. 否', 'B', '只有满足特定排序规则的二叉树才是二叉搜索树','1','5' ,'5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 一棵树可以有多个根节点。 (2分)', 'A. 是', 'B. 否', 'B', '一棵树只能有一个根节点','1','5' ,'5.1')
""")

#  5.2.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 满二叉树的特点是（ ）。 (2分)', 'A. 每个非叶节点都有两个子节点', 'B. 每个叶节点深度相同', 'C. 每层节点数均达到最大值', 'D. 以上都是', 'D', '满二叉树的定义包括以上所有特点','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 二叉树的最大高度为n时，最多有多少个节点？ (2分)', 'A. 2^(n-1)', 'B. 2^n', 'C. 2^n - 1', 'D. n^2', 'C', '二叉树的节点数最多为2^n - 1','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 在二叉树中，先序遍历的顺序是（ ）。 (2分)', 'A. 根-左-右', 'B. 左-根-右', 'C. 左-右-根', 'D. 根-右-左', 'A', '先序遍历按照根节点、左子树、右子树的顺序','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 如果一棵二叉树的节点总数为n，叶子节点数为l，则度为2的节点数是（ ）。 (2分)', 'A. l - 1', 'B. n - l - 1', 'C. n - l', 'D. l - n', 'B', '根据二叉树性质，度为2的节点数等于总节点数减去叶节点数再减1','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 对于完全二叉树，其节点编号的特点是（ ）。 (2分)', 'A. 所有节点按从上到下、从左到右连续编号', 'B. 只有叶节点需要编号', 'C. 所有节点按从左到右编号', 'D. 节点编号是随机分配的', 'A', '完全二叉树的节点编号规则是从上到下、从左到右连续编号','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 对一棵完全二叉树进行层次遍历时，节点访问顺序是（ ）。 (2分)', 'A. 从左到右、从上到下', 'B. 从右到左、从上到下', 'C. 从左到右、从下到上', 'D. 从右到左、从下到上', 'A', '层次遍历按照从左到右、从上到下的顺序','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 二叉搜索树的特点是（ ）。 (2分)', 'A. 所有左子节点值小于根节点值，右子节点值大于根节点值', 'B. 每个节点的左右子树高度相同', 'C. 所有叶子节点都在同一层', 'D. 节点的度数必须为2', 'A', '二叉搜索树的定义是左子树小于根，右子树大于根','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 完全二叉树的定义是（ ）。 (2分)', 'A. 每个节点的左右子树高度相差不超过1', 'B. 除最后一层外，所有层的节点数达到最大值', 'C. 所有叶子节点都在同一层', 'D. 节点的左右子树节点数相等', 'B', '完全二叉树的定义是除最后一层外，所有层都满，最后一层从左到右填充','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 二叉树的中序遍历顺序是（ ）。 (2分)', 'A. 根-左-右', 'B. 左-根-右', 'C. 左-右-根', 'D. 根-右-左', 'B', '中序遍历按照左子树、根节点、右子树的顺序','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 二叉树的后序遍历顺序是（ ）。 (2分)', 'A. 根-左-右', 'B. 左-根-右', 'C. 左-右-根', 'D. 根-右-左', 'C', '后序遍历按照左子树、右子树、根节点的顺序','0','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 一棵二叉树的所有节点度数之和等于节点总数减1。 (2分)', 'A. 是', 'B. 否', 'A', '树的度数之和等于总边数，总边数等于节点数减1','1','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 对于任意二叉树，层次遍历的顺序与中序遍历相同。 (2分)', 'A. 是', 'B. 否', 'B', '层次遍历是按层访问，中序遍历是按照左-根-右的顺序','1','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 所有二叉树都可以唯一地用先序遍历和中序遍历结果重建。 (2分)', 'A. 是', 'B. 否', 'A', '先序遍历和中序遍历结果可以唯一确定二叉树结构','1','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 所有满二叉树都是完全二叉树，但并非所有完全二叉树都是满二叉树。 (2分)', 'A. 是', 'B. 否', 'A', '满二叉树符合完全二叉树的定义，但完全二叉树不一定是满二叉树','1','5' ,'5.2.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 对于二叉搜索树，中序遍历结果一定是一个递增的有序序列。 (2分)', 'A. 是', 'B. 否', 'A', '二叉搜索树中序遍历结果是递增序列','1','5' ,'5.2.1')
""")

#  5.2.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 一棵深度为k的满二叉树的节点总数是（ ）。 (2分)', 'A. 2^k - 1', 'B. 2^(k-1)', 'C. k^2 - 1', 'D. 2k - 1', 'A', '满二叉树的节点总数公式为2^k - 1','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 一棵完全二叉树中，编号为i的节点，其父节点编号是（ ）。 (2分)', 'A. i/2', 'B. i-1', 'C. floor(i/2)', 'D. i+1', 'C', '完全二叉树中，父节点编号为floor(i/2)','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 一棵深度为d的二叉树最多有多少个叶子节点？ (2分)', 'A. d^2', 'B. 2^(d-1)', 'C. 2^d', 'D. d!', 'B', '二叉树的最大叶子节点数是2^(d-1)','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 在一棵二叉树中，如果度为1的节点数为m，叶子节点数为n，则二叉树的总节点数是（ ）。 (2分)', 'A. m + 2n', 'B. 2m + n', 'C. m + n', 'D. m + n + 1', 'D', '根据二叉树的性质，节点总数等于度为1节点和叶子节点之和加1','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在二叉树中，每个节点的子节点个数最多是（ ）。 (2分)', 'A. 1', 'B. 2', 'C. 3', 'D. 无限制', 'B', '二叉树的定义规定每个节点最多有两个子节点','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 二叉树中，非叶子节点数等于（ ）。 (2分)', 'A. 总节点数减去叶子节点数', 'B. 叶子节点数减1', 'C. 总节点数减去根节点数', 'D. 叶子节点数加1', 'A', '非叶子节点数等于总节点数减去叶子节点数','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 一棵完全二叉树中，最后一层的节点个数最多是（ ）。 (2分)', 'A. 2^(h-1)', 'B. 2^h', 'C. 2^(h-1) - 1', 'D. h^2', 'A', '完全二叉树最后一层的节点数最多为2^(h-1)','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 二叉树中，一个节点的兄弟节点一定是（ ）。 (2分)', 'A. 父节点的左孩子', 'B. 父节点的右孩子', 'C. 同一父节点的另一个孩子', 'D. 无法确定', 'C', '兄弟节点定义为同一父节点的另一个孩子','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在一棵满二叉树中，度为2的节点个数等于（ ）。 (2分)', 'A. 总节点数减1', 'B. 总节点数除以2', 'C. 总节点数的一半', 'D. 总节点数减去叶子节点数', 'D', '满二叉树中度为2的节点数等于总节点数减去叶子节点数','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在二叉树中，根节点一定（ ）。 (2分)', 'A. 没有父节点', 'B. 没有兄弟节点', 'C. 没有子节点', 'D. 位于最后一层', 'A', '根节点是二叉树的唯一没有父节点的节点','0','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 二叉树中每个非叶子节点的子节点个数可以为0。 (2分)', 'A. 是', 'B. 否', 'B', '非叶子节点至少有一个子节点','1','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 一棵深度为h的完全二叉树，其节点总数最多为2^h - 1。 (2分)', 'A. 是', 'B. 否', 'A', '完全二叉树在每层节点满时，节点总数等于2^h - 1','1','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 二叉树中最多有一个节点的度数为2。 (2分)', 'A. 是', 'B. 否', 'B', '二叉树允许多个节点的度数为2','1','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 每棵满二叉树都是完全二叉树。 (2分)', 'A. 是', 'B. 否', 'A', '满二叉树符合完全二叉树的定义','1','5' ,'5.2.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 二叉树中，所有节点的度数之和等于总节点数减1。 (2分)', 'A. 是', 'B. 否', 'A', '节点度数之和等于树的总边数，总边数等于节点数减1','1','5' ,'5.2.2')
""")

#  5.2.3 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 二叉树的链式存储结构中，每个节点至少需要存储（ ）。 (2分)', 'A. 一个数据域', 'B. 一个左孩子指针和一个右孩子指针', 'C. 一个数据域和两个指针域', 'D. 三个指针域', 'C', '链式存储结构中，每个节点需要一个数据域和两个指针域','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 顺序存储的二叉树通常适用于（ ）。 (2分)', 'A. 稀疏的二叉树', 'B. 满二叉树', 'C. 非完全二叉树', 'D. 所有二叉树', 'B', '顺序存储适合节点分布紧凑的满二叉树','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 顺序存储的二叉树中，若节点的数组下标为i，其右孩子的下标是（ ）。 (2分)', 'A. 2i', 'B. 2i+1', 'C. i/2', 'D. i-1', 'B', '右孩子下标公式为2i+1','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 链式存储的二叉树，存储效率较低的原因是（ ）。 (2分)', 'A. 需要额外存储指针域', 'B. 数据域占用空间大', 'C. 需要按层遍历节点', 'D. 二叉树不易平衡', 'A', '链式存储增加了指针域的存储开销','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在二叉树的链式存储中，根节点的父节点指针应指向（ ）。 (2分)', 'A. NULL', 'B. 自身地址', 'C. 右孩子地址', 'D. 左孩子地址', 'A', '根节点没有父节点，其父节点指针指向NULL','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 在二叉树的顺序存储中，左孩子下标大于n时，表示（ ）。 (2分)', 'A. 没有左孩子', 'B. 左孩子超出范围', 'C. 树为稀疏结构', 'D. 遍历出错', 'A', '左孩子下标超出范围说明不存在左孩子','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 二叉树的链式存储中，若一个节点只有左孩子，则右孩子指针（ ）。 (2分)', 'A. 指向父节点', 'B. 指向NULL', 'C. 指向根节点', 'D. 指向左孩子', 'B', '没有右孩子时，右孩子指针为NULL','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 二叉树的顺序存储和链式存储相比，优点是（ ）。 (2分)', 'A. 占用空间小', 'B. 节点存取快', 'C. 适用于稀疏树', 'D. 遍历效率高', 'B', '顺序存储直接通过数组下标定位节点，存取快','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在二叉树的顺序存储中，最后一个非叶子节点的数组下标是（ ）。 (2分)', 'A. n/2', 'B. n-1', 'C. floor(n/2)', 'D. n/2 + 1', 'C', '最后一个非叶子节点下标为floor(n/2)','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 顺序存储的二叉树，若下标为1的节点为空，则（ ）。 (2分)', 'A. 整棵树为空', 'B. 树结构不合法', 'C. 仅该节点为空', 'D. 只有右子树', 'A', '下标为1表示根节点为空，整棵树为空','0','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 链式存储适合存储稀疏的二叉树。 (2分)', 'A. 是', 'B. 否', 'A', '稀疏二叉树链式存储节省空间','1','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 顺序存储的二叉树可以高效存取节点，适合稀疏树。 (2分)', 'A. 是', 'B. 否', 'B', '稀疏树顺序存储会浪费空间，不适合','1','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 链式存储的二叉树中，每个叶子节点左右指针均指向NULL。 (2分)', 'A. 是', 'B. 否', 'A', '叶子节点没有子节点，左右指针均为NULL','1','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 顺序存储的二叉树无法表示深度很大的树。 (2分)', 'A. 是', 'B. 否', 'A', '深度大的树顺序存储可能需要非常大的数组','1','5' ,'5.2.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 链式存储的二叉树可以动态添加节点而不影响已有结构。 (2分)', 'A. 是', 'B. 否', 'A', '链式存储可自由动态添加节点','1','5' ,'5.2.3')
""")

#  5.3.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在二叉树的递归遍历中，前序遍历的访问顺序是（ ）。 (2分)', 'A. 根节点 -> 左子树 -> 右子树', 'B. 左子树 -> 根节点 -> 右子树', 'C. 左子树 -> 右子树 -> 根节点', 'D. 根节点 -> 右子树 -> 左子树', 'A', '前序遍历的顺序是根节点、左子树、右子树','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在递归遍历中，中序遍历的特点是（ ）。 (2分)', 'A. 先访问左子树，后访问右子树', 'B. 节点访问顺序为左-根-右', 'C. 根节点总是最后被访问', 'D. 适用于计算树高度', 'B', '中序遍历的顺序是左节点、根节点、右节点','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 若采用后序遍历访问二叉树，则根节点的访问时机是（ ）。 (2分)', 'A. 最后', 'B. 最先', 'C. 左子树和右子树之间', 'D. 不确定', 'A', '后序遍历是左子树、右子树、根节点的顺序','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 以下关于递归遍历的说法正确的是（ ）。 (2分)', 'A. 前序遍历和后序遍历的递归代码完全相同', 'B. 中序遍历和层次遍历可以统一用递归实现', 'C. 每种遍历方式递归代码都不同', 'D. 遍历方式与递归结构无关', 'C', '每种遍历的递归代码访问顺序不同，因此实现不同','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 递归遍历的时间复杂度主要取决于（ ）。 (2分)', 'A. 树的深度', 'B. 树的节点数量', 'C. 遍历方式', 'D. 节点的存储结构', 'B', '每个节点只被访问一次，时间复杂度与节点数目相关','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 在二叉树的递归遍历中，如果左右子树为空，根节点的递归操作（ ）。 (2分)', 'A. 停止递归', 'B. 返回父节点', 'C. 继续递归', 'D. 报错', 'A', '递归遍历中，遇到空节点递归终止','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 使用递归遍历时，函数调用栈的最大深度与（ ）。 (2分)', 'A. 树的高度有关', 'B. 树的宽度有关', 'C. 节点总数有关', 'D. 遍历顺序有关', 'A', '递归深度与树的高度直接相关','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 在递归遍历中，栈空间的开销主要体现在（ ）。 (2分)', 'A. 函数的调用次数', 'B. 树的节点总数', 'C. 每次递归的局部变量', 'D. 栈的深度', 'D', '栈空间与递归深度密切相关','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在递归实现中，最核心的操作是（ ）。 (2分)', 'A. 判断节点是否为空', 'B. 记录遍历路径', 'C. 动态分配内存', 'D. 树的层次遍历', 'A', '递归中要不断判断节点是否为空以决定递归的方向','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 递归遍历二叉树的关键是（ ）。 (2分)', 'A. 确定访问顺序', 'B. 动态分配节点存储', 'C. 确保所有节点有父节点', 'D. 遍历过程中计算树高', 'A', '递归遍历的关键是根据不同遍历方式确定访问顺序','0','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 递归遍历的实现中，左子树必须在右子树之前被访问。 (2分)', 'A. 是', 'B. 否', 'A', '递归遍历中，左子树优先于右子树被访问','1','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 二叉树的递归遍历和非递归遍历本质上等价。 (2分)', 'A. 是', 'B. 否', 'A', '两种遍历的逻辑实现可以相互等价','1','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 后序遍历递归实现中，根节点是最先被访问的。 (2分)', 'A. 是', 'B. 否', 'B', '后序遍历中，根节点最后被访问','1','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 递归遍历需要额外空间来存储函数调用栈信息。 (2分)', 'A. 是', 'B. 否', 'A', '递归调用时，每次函数调用需要额外栈空间','1','5' ,'5.3.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 递归遍历的时间复杂度通常为O(n)。 (2分)', 'A. 是', 'B. 否', 'A', '每个节点被访问一次，时间复杂度为O(n)','1','5' ,'5.3.1')
""")

#  5.3.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在二叉树的应用中，使用前序遍历可以直接用于（ ）。 (2分)', 'A. 表达式树的求值', 'B. 二叉树的拷贝', 'C. 树的高度计算', 'D. 按层次打印二叉树', 'B', '前序遍历访问根节点时可以直接拷贝数据','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 中序遍历通常用于（ ）。 (2分)', 'A. 实现表达式求值', 'B. 判断二叉搜索树的合法性', 'C. 计算树的叶子节点', 'D. 统计二叉树的宽度', 'B', '中序遍历二叉搜索树可以获得递增的序列','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 后序遍历在二叉树应用中通常用于（ ）。 (2分)', 'A. 打印节点数据', 'B. 统计二叉树的节点数量', 'C. 释放二叉树的动态存储空间', 'D. 进行路径搜索', 'C', '后序遍历在释放动态分配的树时非常有效','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 使用层次遍历可以直接完成的操作是（ ）。 (2分)', 'A. 生成二叉树的镜像', 'B. 判断完全二叉树', 'C. 按照深度优先方式遍历', 'D. 将树的结构存储到数组中', 'B', '层次遍历从根节点逐层判断，可以验证完全二叉树','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 下面关于遍历的描述正确的是（ ）。 (2分)', 'A. 前序遍历不能唯一确定二叉树', 'B. 后序遍历和层次遍历结合可唯一确定二叉树', 'C. 中序遍历和层次遍历无法唯一确定二叉树', 'D. 层次遍历和前序遍历无法唯一确定二叉树', 'B', '后序和层次遍历结合可唯一重建二叉树','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 表达式树中后序遍历的结果通常表示（ ）。 (2分)', 'A. 中缀表达式', 'B. 后缀表达式', 'C. 前缀表达式', 'D. 语法树', 'B', '后序遍历的顺序与后缀表达式一致','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 对于一个完全二叉树，层次遍历后可以（ ）。 (2分)', 'A. 重建唯一二叉树', 'B. 计算所有节点的深度', 'C. 直接转换为数组表示', 'D. 生成中序遍历序列', 'C', '完全二叉树的层次遍历可以直接映射到数组','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 对表达式树进行中序遍历时，可以得到（ ）。 (2分)', 'A. 后缀表达式', 'B. 中缀表达式', 'C. 前缀表达式', 'D. 语法树', 'B', '中序遍历表达式树会按照中缀表达式的顺序访问节点','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在构建哈夫曼树的过程中，树的遍历可以用于（ ）。 (2分)', 'A. 判断是否为完全二叉树', 'B. 确定节点权重', 'C. 打印编码表', 'D. 验证树的最优性', 'C', '遍历哈夫曼树可以生成对应的编码表','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在二叉搜索树中，中序遍历的应用主要在于（ ）。 (2分)', 'A. 输出节点的层次', 'B. 按升序输出所有节点', 'C. 统计节点的深度', 'D. 按后缀表达式排序', 'B', '中序遍历二叉搜索树时节点按升序访问','0','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 对表达式树的后序遍历可以得到对应的中缀表达式。 (2分)', 'A. 是', 'B. 否', 'B', '后序遍历对应后缀表达式','1','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 层次遍历的结果可以用于构建二叉树的镜像。 (2分)', 'A. 是', 'B. 否', 'A', '层次遍历可以结合递归生成镜像树','1','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 中序遍历的结果对于二叉搜索树是一个有序序列。 (2分)', 'A. 是', 'B. 否', 'A', '二叉搜索树的中序遍历是有序的','1','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 后序遍历二叉树时，根节点是第一个访问的节点。 (2分)', 'A. 是', 'B. 否', 'B', '后序遍历根节点是最后一个访问的','1','5' ,'5.3.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 中序遍历适合用于表达式树的生成。 (2分)', 'A. 是', 'B. 否', 'A', '中序遍历表达式树有助于解析中缀表达式','1','5' ,'5.3.2')
""")

#  5.3.3 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 二叉树的非递归前序遍历通常使用的数据结构是（ ）。 (2分)', 'A. 队列', 'B. 栈', 'C. 链表', 'D. 优先队列', 'B', '前序遍历的非递归实现依赖栈来存储未访问的右子树','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在二叉树的非递归中序遍历中，访问节点的顺序是（ ）。 (2分)', 'A. 先左后根再右', 'B. 先右后根再左', 'C. 先根后左再右', 'D. 按层次顺序', 'A', '中序遍历按照左-根-右的顺序进行访问','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 二叉树的非递归后序遍历比中序遍历更复杂，其主要难点在于（ ）。 (2分)', 'A. 如何确定当前节点是否可以访问', 'B. 如何存储所有节点', 'C. 如何计算树的深度', 'D. 如何判断完全二叉树', 'A', '后序遍历需要在访问子节点后确认是否可以访问父节点','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 非递归层次遍历通常使用的数据结构是（ ）。 (2分)', 'A. 栈', 'B. 队列', 'C. 链表', 'D. 哈希表', 'B', '层次遍历需要先进先出的顺序，适合使用队列','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 非递归前序遍历中栈中保存的节点通常是（ ）。 (2分)', 'A. 已访问的节点', 'B. 尚未访问的右子树节点', 'C. 尚未访问的左子树节点', 'D. 树的根节点', 'B', '栈保存的是当前节点的右子树，以便稍后访问','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 在非递归遍历中，访问一个节点后需要（ ）。 (2分)', 'A. 删除其左右子树', 'B. 记录其父节点', 'C. 标记已访问', 'D. 压入栈中', 'C', '标记访问节点以防止重复访问','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 在非递归后序遍历中，第二次访问的节点通常是（ ）。 (2分)', 'A. 左子树根节点', 'B. 右子树根节点', 'C. 当前节点', 'D. 父节点', 'C', '后序遍历会在第二次访问时处理当前节点','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 在非递归中序遍历中，从栈中弹出一个节点后应（ ）。 (2分)', 'A. 打印该节点并停止操作', 'B. 访问该节点并转向其右子树', 'C. 访问该节点并转向其左子树', 'D. 直接将其左右子树压入栈', 'B', '中序遍历在弹出节点后需要转向右子树','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在非递归层次遍历中，每次从队列中弹出的节点通常是（ ）。 (2分)', 'A. 当前层的最后一个节点', 'B. 当前层的第一个节点', 'C. 所有左子节点', 'D. 所有右子节点', 'B', '层次遍历按层从左到右访问，队列弹出的是当前层的第一个节点','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在非递归遍历算法中，需要提前终止遍历的情况通常是（ ）。 (2分)', 'A. 栈为空', 'B. 队列为空', 'C. 遇到目标节点', 'D. 树为空', 'C', '目标节点找到后可以提前终止遍历以节省时间','0','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 非递归前序遍历的核心是维护一个栈来保存未访问的右子树。 (2分)', 'A. 是', 'B. 否', 'A', '前序遍历需要栈来存储右子树以保证顺序','1','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 非递归中序遍历必须先访问右子树后访问左子树。 (2分)', 'A. 是', 'B. 否', 'B', '中序遍历按左-根-右的顺序进行访问','1','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 在非递归后序遍历中需要一个额外的标记来记录节点的访问状态。 (2分)', 'A. 是', 'B. 否', 'A', '后序遍历为了避免重复访问需要标记节点的访问状态','1','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 非递归层次遍历依赖于栈结构来保证顺序。 (2分)', 'A. 是', 'B. 否', 'B', '层次遍历依赖队列而非栈来实现','1','5' ,'5.3.3')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 在非递归遍历中，无需检查节点是否已经访问过。 (2分)', 'A. 是', 'B. 否', 'B', '非递归遍历中需要标记节点避免重复访问','1','5' ,'5.3.3')
""")

#  5.3.4 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 二叉树的线索化主要是为了（ ）。 (2分)', 'A. 增加二叉树的存储效率', 'B. 方便查找节点的父节点', 'C. 遍历过程中避免递归', 'D. 增加二叉树的层次', 'C', '线索化二叉树主要用于提高遍历的效率，避免递归调用','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 二叉树的线索化是通过填充节点的空左或空右指针来指向（ ）。 (2分)', 'A. 树的根节点', 'B. 该节点的子节点', 'C. 该节点的直接后继或前驱节点', 'D. 树的深度', 'C', '线索化会填充空指针指向中序遍历下的直接前驱或后继节点','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 在中序线索二叉树中，如果一个节点的右指针为空，则右指针将指向该节点的（ ）。 (2分)', 'A. 根节点', 'B. 父节点', 'C. 直接前驱节点', 'D. 直接后继节点', 'D', '中序线索二叉树的右线索指向直接后继节点','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 中序线索二叉树的节点中，只有一个子节点的节点数目最多为（ ）。 (2分)', 'A. 1', 'B. n-1', 'C. n-2', 'D. n', 'C', '二叉树中至多有 n-2 个节点有 2 个子节点','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在线索二叉树中添加一个头节点的目的是（ ）。 (2分)', 'A. 提高树的平衡性', 'B. 方便遍历控制', 'C. 提高树的高度', 'D. 增加树的存储空间', 'B', '头节点用于方便访问起点和终点，便于遍历控制','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 后序线索二叉树的一个特点是（ ）。 (2分)', 'A. 左指针指向直接前驱', 'B. 右指针指向直接前驱', 'C. 左指针指向直接后继', 'D. 右指针指向直接后继', 'A', '在后序线索二叉树中，左指针会指向直接前驱','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 在线索二叉树的定义中，“线索”是指（ ）。 (2分)', 'A. 节点的数据值', 'B. 左右指针的状态', 'C. 节点的高度', 'D. 节点的层次', 'B', '线索是指节点的空左或右指针，用于指向遍历顺序的前驱或后继','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 在一个节点的右指针指向直接后继的线索二叉树中，该节点被称为（ ）。 (2分)', 'A. 左线索节点', 'B. 右线索节点', 'C. 中序节点', 'D. 后序节点', 'B', '右指针指向后继的节点称为右线索节点','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 如果线索二叉树的所有节点都有右线索，则可以将该树理解为（ ）。 (2分)', 'A. 空树', 'B. 平衡二叉树', 'C. 单链表', 'D. 二叉查找树', 'C', '当所有右指针都指向直接后继时，整个树等效为单链表','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在中序线索二叉树中，如果一个节点没有左子树，那么其左指针将指向（ ）。 (2分)', 'A. 树的根节点', 'B. 树的最左节点', 'C. 该节点的直接前驱', 'D. 该节点的父节点', 'C', '无左子树时，左指针指向该节点的直接前驱','0','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 中序线索二叉树中，右指针为线索时指向直接后继节点。 (2分)', 'A. 是', 'B. 否', 'A', '中序线索二叉树中，右线索指向直接后继','1','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 线索二叉树比普通二叉树更适合查找操作。 (2分)', 'A. 是', 'B. 否', 'B', '线索化二叉树主要优化遍历，不适合快速查找','1','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 中序线索二叉树的所有右指针都指向空节点。 (2分)', 'A. 是', 'B. 否', 'B', '中序线索二叉树中的右指针指向直接后继或为空','1','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 在任何线索二叉树中，左指针总指向左子节点。 (2分)', 'A. 是', 'B. 否', 'B', '线索二叉树中的左指针可能指向直接前驱节点','1','5' ,'5.3.4')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 线索二叉树通过线索指针可以有效减少空指针的使用。 (2分)', 'A. 是', 'B. 否', 'A', '线索化的目的是利用空指针指向遍历的前驱或后继','1','5' ,'5.3.4')
""")

#  5.4.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 一棵具有 n 个节点的树，最多有多少条边？ (2分)', 'A. n-1', 'B. n', 'C. n+1', 'D. 2n-1', 'A', '树的边数为节点数减1，即 n-1','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在树中，度为 0 的节点被称为（ ）。 (2分)', 'A. 内部节点', 'B. 根节点', 'C. 叶节点', 'D. 子节点', 'C', '度为0的节点没有子节点，因此是叶节点','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 一棵完全二叉树中，第 i 层最多有多少个节点？ (2分)', 'A. i', 'B. 2^i', 'C. 2^(i-1)', 'D. 2^(i+1)-1', 'C', '完全二叉树第i层最多有2^(i-1)个节点','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 将一棵树转换为对应的森林的方法是（ ）。 (2分)', 'A. 删除根节点', 'B. 删除所有边', 'C. 删除树的根节点并将其子树分开', 'D. 转换为二叉树', 'C', '删除树的根节点并分离其子树即可得到对应的森林','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 森林中有 m 棵树，节点总数为 n，则该森林中的边数为（ ）。 (2分)', 'A. n-m', 'B. n', 'C. n+m-1', 'D. m', 'A', '每棵树有节点数减1的边，总数为 n-m','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 在树的遍历中，访问顺序是“先访问根节点，然后访问左右子树”的方式是（ ）。 (2分)', 'A. 中序遍历', 'B. 先序遍历', 'C. 后序遍历', 'D. 层次遍历', 'B', '先序遍历的顺序为根-左-右','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 在森林转二叉树的过程中，下一步处理子树的方法是将其（ ）。 (2分)', 'A. 转换为叶节点', 'B. 转换为右子树', 'C. 转换为左子树', 'D. 删除', 'C', '在森林转二叉树中，子树递归处理为左子树','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 树中节点的深度是指（ ）。 (2分)', 'A. 根到该节点的路径长度', 'B. 节点到叶节点的路径长度', 'C. 节点的子树个数', 'D. 节点的层次数', 'A', '深度是从根到节点路径的长度','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 树的高度是指（ ）。 (2分)', 'A. 树中最长路径的长度', 'B. 树的节点总数', 'C. 树的边数', 'D. 树中叶节点的数量', 'A', '高度是树中最长路径的长度','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在树中，若节点的左子树高度和右子树高度之差不超过 1，则称该树为（ ）。 (2分)', 'A. 满二叉树', 'B. 平衡二叉树', 'C. 二叉查找树', 'D. 完全二叉树', 'B', '平衡二叉树的左右子树高度差不超过1','0','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 树中的每个节点只能有一个父节点。 (2分)', 'A. 是', 'B. 否', 'A', '树的每个节点唯一的父节点是其结构特征','1','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 森林是互不相交的若干棵树的集合。 (2分)', 'A. 是', 'B. 否', 'A', '森林是树的集合，且各树互不相交','1','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 树中路径的长度等于路径上的节点数。 (2分)', 'A. 是', 'B. 否', 'B', '路径长度是路径上边的数目，与节点数不同','1','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 完全二叉树一定是满二叉树。 (2分)', 'A. 是', 'B. 否', 'B', '完全二叉树的定义比满二叉树宽松','1','5' ,'5.4.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 满二叉树的所有非叶节点都有两个子节点。 (2分)', 'A. 是', 'B. 否', 'A', '满二叉树的非叶节点都具有两个子节点','1','5' ,'5.4.1')
""")

#  5.4.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在将森林转换为二叉树时，处理每棵树的第一步是（ ）。 (2分)', 'A. 保留原树结构', 'B. 选取根节点作为二叉树根', 'C. 转化为链表形式', 'D. 删除树的根节点', 'B', '森林中每棵树的根节点将作为二叉树的主要根节点','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在将森林转换为二叉树时，非根节点之间的关系变为（ ）。 (2分)', 'A. 左子树与右子树', 'B. 父节点与子节点', 'C. 兄弟节点', 'D. 兄弟节点转为右子树', 'D', '森林中兄弟节点在二叉树中作为右子树处理','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 二叉树转换为森林的步骤之一是（ ）。 (2分)', 'A. 删除所有右子树', 'B. 删除所有左子树', 'C. 将右子树转为兄弟节点', 'D. 保留叶节点', 'C', '在二叉树转森林时，将右子树视为兄弟节点','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 树转换为二叉树的过程主要依赖（ ）。 (2分)', 'A. 树的高度', 'B. 节点的度', 'C. 节点的兄弟关系', 'D. 节点的深度', 'C', '兄弟关系决定了二叉树的右子树结构','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在森林到二叉树的转换中，兄弟节点的连接方向是（ ）。 (2分)', 'A. 左侧', 'B. 右侧', 'C. 双向', 'D. 无方向', 'B', '兄弟节点在二叉树中作为右子树连接','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 树到二叉树转换时，左子树的构造方式是（ ）。 (2分)', 'A. 保留树的左子节点', 'B. 将左子节点转为根', 'C. 将左子节点转为叶节点', 'D. 删除左子节点', 'A', '左子树在二叉树中保持不变','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 一棵树转为二叉树后，二叉树的节点总数与原树相比（ ）。 (2分)', 'A. 增加', 'B. 减少', 'C. 不变', 'D. 取决于树的深度', 'C', '转换过程不影响节点总数','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 如果一个森林有 m 棵树，转为二叉树后二叉树的根节点数量是（ ）。 (2分)', 'A. 1', 'B. m', 'C. 2m', 'D. m-1', 'B', '森林中每棵树的根节点会保留','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 如果一棵树有 n 个节点，转为二叉树后节点总数为（ ）。 (2分)', 'A. n', 'B. n+1', 'C. 2n', 'D. n-1', 'A', '节点总数不随转换改变','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 二叉树转换为森林后，原二叉树的右子树会变成（ ）。 (2分)', 'A. 新树', 'B. 兄弟节点', 'C. 父节点', 'D. 左子节点', 'B', '右子树在森林中转为兄弟节点','0','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 森林可以通过添加虚拟根节点直接转换为二叉树。 (2分)', 'A. 是', 'B. 否', 'A', '添加虚拟根节点后，森林可以转为二叉树','1','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 树与二叉树之间的节点关系在转换过程中会被改变。 (2分)', 'A. 是', 'B. 否', 'B', '树与二叉树的节点关系保留其层次结构','1','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 森林中每棵树的根节点在二叉树中会变成右子节点。 (2分)', 'A. 是', 'B. 否', 'B', '根节点在转换过程中不会变成右子节点','1','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 二叉树转换为森林后，左子树仍表示该节点的子节点关系。 (2分)', 'A. 是', 'B. 否', 'A', '左子树的子节点关系在转换为森林后保留','1','5' ,'5.4.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 一棵树可以直接作为森林中的一部分，不需要修改。 (2分)', 'A. 是', 'B. 否', 'A', '树本身就是森林的组成部分','1','5' ,'5.4.2')
""")

#  5.5.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 哈夫曼树的构建过程首先需要（ ）。 (2分)', 'A. 按照字符的出现频率构建优先队列', 'B. 按照字符的字母顺序构建二叉树', 'C. 将所有字符存储到哈希表中', 'D. 按照字符的长度构建树结构', 'A', '哈夫曼树的构建过程从优先队列开始，优先队列按字符的出现频率进行排序','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在哈夫曼树的构建过程中，使用的是哪种数据结构？（ ）。 (2分)', 'A. 堆', 'B. 树', 'C. 队列', 'D. 栈', 'A', '哈夫曼树使用的是堆这种数据结构来保持最小频率节点','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 构建哈夫曼树时，如果有两个字符频率相同，应如何处理？（ ）。 (2分)', 'A. 按照字母顺序处理', 'B. 随机选择其中一个字符', 'C. 将它们组合成一个父节点', 'D. 优先选择出现次数较少的字符', 'A', '当频率相同，可以按照字母顺序或其他规则进行处理','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 在哈夫曼树的构建过程中，每次合并的节点的频率是（ ）。 (2分)', 'A. 当前队列中频率最小的两个节点', 'B. 当前队列中频率最大的两个节点', 'C. 当前队列中频率最小的一个节点', 'D. 所有节点的频率之和', 'A', '每次选择队列中频率最小的两个节点进行合并','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在哈夫曼树的构建过程中，最终得到的树是（ ）。 (2分)', 'A. 二叉树', 'B. 树状图', 'C. 多叉树', 'D. 堆树', 'A', '哈夫曼树是一个二叉树，每个节点最多有两个子节点','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 哈夫曼树的编码是通过（ ）。 (2分)', 'A. 对树中的每个路径赋予一个二进制值', 'B. 给每个叶子节点分配一个固定的编码', 'C. 按照字符频率从大到小排序', 'D. 给每个节点分配一个固定的编码', 'A', '哈夫曼编码是通过树的路径（从根到叶子）赋予每个字符一个二进制编码','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 哈夫曼树构建完成后，树的根节点包含的信息是（ ）。 (2分)', 'A. 所有字符的编码', 'B. 所有字符的频率', 'C. 所有字符的出现次数和编码', 'D. 所有节点的编码', 'B', '哈夫曼树的根节点包含所有字符的频率信息','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 哈夫曼树的编码效率的一个重要特点是（ ）。 (2分)', 'A. 更常出现的字符编码较短', 'B. 更常出现的字符编码较长', 'C. 所有字符编码长度相同', 'D. 编码长度固定', 'A', '哈夫曼编码的特点是更常出现的字符编码较短','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在构建哈夫曼树时，最终合并后的根节点代表（ ）。 (2分)', 'A. 所有字符的编码', 'B. 所有字符的频率', 'C. 所有字符的路径', 'D. 所有字符的字符集', 'B', '根节点代表所有字符的总频率，而每个叶子节点代表一个字符的频率','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 如果一个字符的频率远大于其他字符，在哈夫曼树中该字符将会（ ）。 (2分)', 'A. 作为根节点', 'B. 被频繁合并', 'C. 编码较短', 'D. 被单独存储', 'C', '频率较大的字符在哈夫曼树中会有较短的编码','0','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 在哈夫曼树中，节点的频率越大，编码越长。 (2分)', 'A. 是', 'B. 否', 'B', '在哈夫曼树中，频率越大的字符，编码越短','1','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 哈夫曼树的构建过程使用的是贪心算法。 (2分)', 'A. 是', 'B. 否', 'A', '哈夫曼树是通过贪心算法逐步合并频率最小的节点来构建的','1','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 哈夫曼树的构建过程是自底向上的。 (2分)', 'A. 是', 'B. 否', 'A', '哈夫曼树的构建过程通过自底向上的方式逐步合并节点','1','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 哈夫曼树的根节点一定包含所有字符的信息。 (2分)', 'A. 是', 'B. 否', 'A', '哈夫曼树的根节点包含所有字符的频率信息','1','5' ,'5.5.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 在哈夫曼树的构建过程中，如果有两个节点的频率相同，合并顺序是唯一的。 (2分)', 'A. 是', 'B. 否', 'B', '如果有多个节点频率相同，合并顺序可能会有所不同','1','5' ,'5.5.1')
""")

#  5.5.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 哈夫曼树构建过程中的每一步都依赖于（ ）。 (2分)', 'A. 最大频率节点', 'B. 最小频率节点', 'C. 随机节点', 'D. 中间频率节点', 'B', '哈夫曼树的构建依赖于每次合并最小频率的两个节点','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 哈夫曼编码的一个重要特性是（ ）。 (2分)', 'A. 编码长度与字符的出现频率无关', 'B. 每个字符的编码长度固定', 'C. 频率越高的字符编码越短', 'D. 编码长度是固定的', 'C', '哈夫曼编码的特性是出现频率较高的字符会有较短的编码','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 在哈夫曼树的构建过程中，每次从队列中选择的两个节点的频率是（ ）。 (2分)', 'A. 最大频率', 'B. 随机频率', 'C. 最小频率', 'D. 中等频率', 'C', '哈夫曼树的构建总是选择频率最小的两个节点进行合并','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 哈夫曼编码在数据压缩中的应用主要是（ ）。 (2分)', 'A. 提高文件的传输速度', 'B. 节省存储空间', 'C. 提高处理速度', 'D. 提高安全性', 'B', '哈夫曼编码在数据压缩中主要通过减少冗余来节省存储空间','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 哈夫曼树构建过程中，合并的节点会（ ）。 (2分)', 'A. 生成新的节点，且新的节点频率为两个节点的和', 'B. 直接删除原节点', 'C. 不会影响节点的顺序', 'D. 频率会减小', 'A', '在哈夫曼树构建过程中，每次合并的节点会生成一个新节点，频率是合并节点的频率之和','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 哈夫曼编码的效率主要取决于（ ）。 (2分)', 'A. 编码表的长度', 'B. 字符的出现频率', 'C. 字符的种类', 'D. 字符的编码顺序', 'B', '哈夫曼编码的效率主要取决于字符的出现频率，频率高的字符会得到短的编码','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 在哈夫曼编码中，编码的总长度（ ）。 (2分)', 'A. 与字符频率无关', 'B. 与字符的频率成反比', 'C. 是固定的', 'D. 根据字符频率动态变化', 'D', '哈夫曼编码的总长度是动态变化的，依据字符的频率分布生成编码','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 以下关于哈夫曼树的描述，错误的是（ ）。 (2分)', 'A. 哈夫曼树可以生成唯一的编码表', 'B. 哈夫曼树的构建过程是自上而下的', 'C. 哈夫曼树是一种二叉树', 'D. 哈夫曼树的根节点表示所有字符的合并结果', 'B', '哈夫曼树的构建是自底向上的，逐步合并最小频率的节点','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 对于给定的字符集，哈夫曼编码的生成（ ）。 (2分)', 'A. 是唯一的', 'B. 可能不是唯一的', 'C. 完全随机', 'D. 不受字符频率影响', 'B', '哈夫曼编码在频率相同的情况下，生成的编码可能不是唯一的','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 下列哪项不属于哈夫曼树的特征？（ ）。 (2分)', 'A. 每个叶子节点表示一个字符', 'B. 内部节点有两个子节点', 'C. 所有路径长度相同', 'D. 路径长度与字符频率成反比', 'C', '哈夫曼树的路径长度与字符的频率有关，频率大的字符路径较短','0','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 哈夫曼树的构建过程是自上而下的。 (2分)', 'A. 是', 'B. 否', 'B', '哈夫曼树的构建过程是自底向上的','1','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 哈夫曼编码是一种无损压缩算法。 (2分)', 'A. 是', 'B. 否', 'A', '哈夫曼编码可以实现无损压缩','1','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 哈夫曼编码总是生成固定长度的编码。 (2分)', 'A. 是', 'B. 否', 'B', '哈夫曼编码的长度是可变的，频率高的字符编码较短','1','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 哈夫曼树的构建算法是一种贪心算法。 (2分)', 'A. 是', 'B. 否', 'A', '哈夫曼树的构建算法是一种贪心算法，通过每次选择最小频率的节点来构建树','1','5' ,'5.5.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 哈夫曼树可以用于字符的加密。 (2分)', 'A. 是', 'B. 否', 'B', '哈夫曼树用于编码压缩，不用于加密','1','5' ,'5.5.2')
""")

#  6.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 图的定义中，顶点和边分别表示（ ）。 (2分)', 'A. 数据和关系', 'B. 数据和节点', 'C. 关系和链接', 'D. 节点和连接', 'A', '图是由顶点和边组成的，其中顶点表示数据，边表示节点之间的关系','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 无向图中，一条边的两个端点是（ ）。 (2分)', 'A. 不可区分的', 'B. 可以区分的', 'C. 只有一个端点', 'D. 没有端点', 'A', '无向图中，边没有方向，两个端点是不可区分的','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 下列哪种类型的图可以表示层次关系？（ ）。 (2分)', 'A. 无向图', 'B. 有向图', 'C. 完全图', 'D. 交错图', 'B', '有向图可以通过顶点之间的方向表示层次关系','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 图的度数指的是（ ）。 (2分)', 'A. 每个顶点的入度和出度之和', 'B. 每个顶点的出度', 'C. 每个顶点的入度', 'D. 图中边的数量', 'A', '图的度数是指每个顶点的入度和出度之和','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 一个图是否连通的判断依据是（ ）。 (2分)', 'A. 图中是否包含环路', 'B. 图中是否每个顶点都有边相连', 'C. 图的度数是否大于1', 'D. 图的顶点数是否大于2', 'B', '图是连通的，当且仅当每个顶点都有边相连','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 有向图中的边表示的是（ ）。 (2分)', 'A. 从一个顶点到另一个顶点的关系', 'B. 从一个节点到另一个节点的关系', 'C. 不存在关系', 'D. 从一个顶点到一个节点的关系', 'A', '有向图中的边表示从一个顶点到另一个顶点的方向性关系','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 完全图中的每一对不同的顶点之间都有（ ）。 (2分)', 'A. 无边', 'B. 一条边', 'C. 两条边', 'D. 三条边', 'B', '完全图中的每一对不同的顶点之间都有一条边','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 以下哪项描述正确地反映了图的深度优先遍历（DFS）？（ ）。 (2分)', 'A. 没有回溯过程', 'B. 从一个顶点出发，先访问它的所有邻接点，再回溯到上一个顶点', 'C. 只访问一个邻接点', 'D. 只访问深度最浅的顶点', 'B', 'DFS从一个顶点开始，访问其所有邻接点，然后回溯到上一个顶点','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 以下哪项描述了图的广度优先遍历（BFS）？（ ）。 (2分)', 'A. 从一个顶点开始，逐层访问邻接顶点', 'B. 只访问深度最深的顶点', 'C. 只访问深度最浅的顶点', 'D. 无法访问到所有顶点', 'A', 'BFS从一个顶点开始，逐层访问它的邻接顶点','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 下列哪个不属于图的特征？（ ）。 (2分)', 'A. 顶点数', 'B. 边数', 'C. 每个顶点的度', 'D. 顶点的总权值', 'D', '图的特征通常包括顶点数、边数和顶点的度数，不包括顶点的总权值','0','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 图的定义是由一组顶点和边组成的。 (2分)', 'A. 是', 'B. 否', 'A', '图是由一组顶点和边组成的，边表示顶点之间的关系','1','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 有向图中的每条边都有方向。 (2分)', 'A. 是', 'B. 否', 'A', '有向图中的每条边都有明确的方向，从一个顶点指向另一个顶点','1','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 图的深度优先遍历会回溯到上一层。 (2分)', 'A. 是', 'B. 否', 'A', '深度优先遍历在到达某一节点的所有邻接节点后，会回溯到上一层继续遍历','1','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 完全图中，任意两个不同的顶点之间都有且只有一条边。 (2分)', 'A. 是', 'B. 否', 'A', '完全图中的每一对不同的顶点之间都有且只有一条边','1','6' ,'6.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 图的广度优先遍历是从一个顶点开始，访问深度最小的邻接顶点。 (2分)', 'A. 是', 'B. 否', 'A', '广度优先遍历从一个顶点开始，逐层访问邻接顶点','1','6' ,'6.1')
""")

#  6.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 下列哪种图的存储结构适用于稀疏图？（ ）。 (2分)', 'A. 邻接矩阵', 'B. 邻接表', 'C. 十字链表', 'D. 邻接多重表', 'B', '邻接表是一种适用于稀疏图的存储方式','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 对于一个无向图，邻接矩阵是（ ）。 (2分)', 'A. 对称的', 'B. 不对称的', 'C. 只有上三角', 'D. 只有下三角', 'A', '无向图的邻接矩阵是对称的，因为边没有方向','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 在邻接表存储结构中，图的每个顶点都对应一个（ ）。 (2分)', 'A. 数组', 'B. 链表', 'C. 栈', 'D. 队列', 'B', '在邻接表中，每个顶点有一个链表存储它的邻接点','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 下列哪个存储结构不适合表示稠密图？（ ）。 (2分)', 'A. 邻接矩阵', 'B. 邻接表', 'C. 十字链表', 'D. 邻接多重表', 'B', '邻接表更适合稀疏图，稠密图使用邻接矩阵较为高效','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 十字链表存储结构适用于（ ）。 (2分)', 'A. 无向图', 'B. 有向图', 'C. 完全图', 'D. 树', 'B', '十字链表适合用于表示有向图，因为它能够有效存储每条边的反向边信息','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 在邻接矩阵中，边的存储方式是（ ）。 (2分)', 'A. 使用0和1表示是否有边', 'B. 存储每条边的权重', 'C. 存储边的方向', 'D. 存储顶点的编号', 'A', '邻接矩阵通过0和1表示顶点之间是否有边','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 对于图的存储结构，邻接矩阵的空间复杂度为（ ）。 (2分)', 'A. O(V)', 'B. O(E)', 'C. O(V^2)', 'D. O(E^2)', 'C', '邻接矩阵需要V^2的空间，其中V是图的顶点数','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 下列哪种存储结构需要更多的存储空间来表示图的结构？（ ）。 (2分)', 'A. 邻接矩阵', 'B. 邻接表', 'C. 十字链表', 'D. 邻接多重表', 'A', '邻接矩阵需要O(V^2)的空间，而邻接表只需要O(E+V)的空间','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 如果一个图的边的权重不固定且较大，可以使用（ ）。 (2分)', 'A. 邻接矩阵', 'B. 邻接表', 'C. 十字链表', 'D. 邻接多重表', 'B', '邻接表可以高效存储图的边权，尤其在权重不固定且较大时','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 下列存储结构适用于表示图的带权边？（ ）。 (2分)', 'A. 邻接矩阵', 'B. 邻接表', 'C. 十字链表', 'D. 邻接多重表', 'A', '邻接矩阵可以直接存储带权边，适用于边权固定的图','0','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 邻接矩阵适合用于稀疏图的存储。 (2分)', 'A. 是', 'B. 否', 'B', '邻接矩阵不适合稀疏图，因为它需要O(V^2)的空间，浪费存储空间','1','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 邻接表存储结构适合存储稠密图。 (2分)', 'A. 是', 'B. 否', 'B', '邻接表适合存储稀疏图，稠密图通常使用邻接矩阵存储','1','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 十字链表是一种针对有向图的存储结构。 (2分)', 'A. 是', 'B. 否', 'A', '十字链表适用于存储有向图，它能够有效表示边的反向边信息','1','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 邻接矩阵适合用于图的加权边。 (2分)', 'A. 是', 'B. 否', 'A', '邻接矩阵适合用于图的加权边，可以直接在矩阵中存储权重值','1','6' ,'6.2')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 邻接表需要更多的存储空间来表示图。 (2分)', 'A. 是', 'B. 否', 'B', '邻接表比邻接矩阵更加节省空间，特别是对于稀疏图','1','6' ,'6.2')
""")

#  6.3 题目    和6.2标题相同，都是图的存储结构，是不是标错了？这里先不找了


#  6.4 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 若对n个顶点、e条弧的有向图采用邻接表存储，则拓扑排序算法的时间复杂度是（ ）。 (2分)
', 'A. O(n)', 'B. O(n+e)', 'C. O(n^2)', 'D. O(ne)',  'B', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 以下关于拓扑排序的说法中，错误的是（ ）。 (2分) <br>
① 若某有向图存在环路，则该有向图一定不存在拓扑排序<br>
② 在拓扑排序算法中为暂存入度为零的顶点，可以使用栈，也可以使用队列<br>
③ 若有向图的拓扑有序序列唯一，则图中每个顶点的入度和出度最多为1
', 'A. ①、③', 'B. ②、③', 'C. ②', 'D. ③',  'D', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 若用邻接矩阵存储有向图，矩阵中主对角线以下的元素均为零，则关于该图拓扑序列的结论是（ ）。 (2分)', 'A. 存在，且唯一', 'B. 存在，且不唯一', 'C. 存在，可能不唯一', 'D. 无法确定是否存在',  'D', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 若有向图的全部顶点不能形成一个拓扑序列，则可断定该有向图（ ）。 (2分)', 'A. 是个有根有向图', 'B. 是个强连通图', 'C. 含有多个入度为0的顶点', 'D. 含有顶点数大于1的强连通分量', 'D', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4, correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在有向图G的拓扑序列中，若顶点vi出现在顶点vj之前，则下列情形不可能出现的是（ ）。 (2分)', 'A. 图G中有弧<vi，vj>', 'B. 图G中有一条从vi到vj的路径', 'C. 图G中没有弧<vi, vj>', 'D. 图G中有一条从vj到vi的路径',  'D', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 下面的（ ）方法可以判断出一个有向图是否有环（回路）。 (2分)<br>
I. 深度优先遍历<br>
II. 拓扑排序<br>
III. 求最短路径<br>
IV. 求关键路径
', 'A. I、II、IV', 'B. I、III、IV', 'C. I、II、III', 'D. 全部可以', 'A', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 若一个有向图的顶点不能排在一个拓扑序列中，则可判定该有向图（ ）。 (2分)', 'A. 是一个有根的有向图', 'B. 是一个强连通图', 'C. 含有多个入度为0的顶点', 'D. 含有顶点数目大于1的强连通分量',  'D', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 用DFS遍历一个无环有向图，并在DFS算法退栈返回时打印相应的顶点，则输出的顶点序列是（ ）。 (2分)', 'A. 逆拓扑有序', 'B. 拓扑有序', 'C. 无序的', 'D. 无法确定',  'A', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 已知带权连通无向图G=(V，E)，{v1，v2，v3，v4，v5，v6，v7}，E= {(v1，v2)10，(v1，v3)2，(v3，v4)2，(v3，v6)11，(v2，v5)1，(v4，v5)4，(v4，v6)6，(v5， v7)7，(v6，v7)3}，（注：顶点偶对括号外的数据表示边上的权值），从源点v1到顶点v7的最短路径上经过的顶点序列是（ ）。 (2分)', 
'A. v1，v2，v5，v7，V7', 'B. v1，v3，v4，v6，v7', 'C. v1，v3，v4，v5，v7', 'D. v1，v2，v5，v4，v6，v7',  'B', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在有向图的拓扑序列中，若顶点vi在顶点vj之前，则下列情形不可能出现的是（ ）。 (2分)', 'A. G中有弧<vi，vj>', 'B. G中有一条从vi到vj的路径', 'C. G中没有弧<vi，vj>', 'D. G中有一条从vj到vi的路径',  'D', '无','0','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 若一个有向图具有有序的拓扑排序序列，则它的邻接矩阵必定为三角。 (2分)
', 'A. 是', 'B. 否',  'A', '注意为有序的拓扑序列','1','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 若一个有向图的顶点不能排成一个拓扑序列，则判定该有向图含有顶点数大于1的强连通分量。 (2分)
', 'A. 是', 'B. 否',  'A', '不能排成拓扑序列表示有环','1','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 拓扑排序方法可以判断一个有向图是否存在回路。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 对n个顶点的连通图G来说，如果其中的某个子图有n个顶点、n-1条边，则该子图一定是G的生成树。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. n个顶点的无向图至多有n(n-1)条边。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.4')
""")

# 6.5 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在AOE网中，关键路径是（ ）。 (2分)
', 'A. 从源点到终点的最长路径', 'B. 从源点到终点的最短路径', 'C. 从源点到终点的边数最多的路径', 'D. 从源点到终点的边数最少的路径',  'A', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 关于工程计划的AOE网，下列说法中不正确的是（ ）。 (2分)
', 'A. 关键活动不按期完成就会影响整个工程的完成时间', 'B. 任何一个关键活动提前完成，整个工程将会提前完成', 'C. 所有的关键活动都提前完成，整个工程将会提前完成', 'D. 某些关键活动若提前完成，整个工程将会提前完成',  'B', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 在关键路径上，路径中的活动都具有以下哪种特点?。（ ） (2分)
', 'A. 最短执行时间', 'B. 最长等待时间', 'C. 无法被并行执行', 'D. 最高执行优先级',  'C', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 下列关于关键路径的说法中，正确的是（ ）。 (2分)<br>
I. 改变网上某一关键路径的任一关键活动后，必将产生不同的关键路径<br>
II. AOE图中，关键路径上活动的时间延长多少，整个工程的时间也就随之延长多少<br>
III. 缩短关键路径上任意一个关键活动的持续时间可缩短关键路径长度<br>
IV. 缩短所有关键路径上共有的任意一个关键活动的持续时间可缩短关键路径长度<br>
V. 缩短多条关键路径上共有的任意一个关键活动的持续时间可缩短关键路径长度
', 'A. II和V', 'B. I、II和V', 'C. II和IV', 'D. I和IV',  'C', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 对于AOE网的关键路径，以下叙述(    )是正确的。 (2分)
', 'A. 任何一个关键活动提前完成，则整个工程一定会提前完成', 'B. 完成整个工程的最短时间是从源点到汇点的最短路径长度', 'C. 一个AOE网的关键路径一定是唯一的', 'D. 任何一个活动持续时间的改变可能会影响关键路径的改变',  'D', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 一个表示工程的AOE网中的关键路径  ( ）。 (2分)
', 'A. 必须是唯一的', 'B. 可以有多条', 'C. 可以没有', 'D. 以上都不对',  'B', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 若某带权图为G=(V，E)，其中V={v1，v2，v3，v4，v5，v6，v7，v8，v9，v10)，E={<v1, V2>5，<v1，v3>6，<v2,v5>3,<v3，v5>6,<v3，v4>3,<v4,v5>3,<v4,v7>1,<v4,v8>4,<v5，v6>4,<v5,v7>2,<v6,v10>4, <v7，v9>5，<v8, v9>2, <v9, v10>2} （注．边括号外的数据表示边上的权值）的关键路径的长度为（ ）。 (2分)
', 'A. 19', 'B. 20', 'C. 21', 'D. 22', 'C', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 在关键路径分析中，关键路径上的活动具有什么特征？（ ）。 (2分)
', 'A. 活动的开始和结束时间可以任意调整', 'B. 活动的开始和结束时间固定，不可调整', 'C. 活动的完成时间早于预定时间', 'D. 活动的开始时间可以延后',  'B', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 以下哪种方法可以用于关键路径的计算？（ ）。 (2分)
', 'A. 深度优先搜索', 'B. 广度优先搜索', 'C. 最短路径算法', 'D. 拓扑排序',  'D', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 关键路径方法主要用于以下哪个方面？（ ）。 (2分)
', 'A. 数据的排序', 'B. 优化内存使用', 'C. 任务调度与进度控制', 'D. 数据压缩',  'C', '无','0','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 项目管理中，关键路径是为了优化成本而设计的。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 在关键路径方法中，任何活动的延迟都可能导致项目整体延迟。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 在所有的网络图中，关键路径是唯一的。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 在关键路径中，所有活动的总时差都为零。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 如果某条关键路径上的某个活动缩短了时间，整个项目的工期将一定缩短。 (2分)
', 'A. 是', 'B. 否',  'B', '关键路径可能不只一条','1','6' ,'6.5')
""")

# 6.6 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 设无向连通图G含有n个顶点，下列说法中正确的是（ ）。 (2分)
', 'A. 只要图G中没有权值相同的边，其最小生成树一定惟一', 'B. 只要图G中有权值相同的边，其最小生成树一定不惟一', 'C. 从图G中选取n-1条权值最小的边，即可构成最小生成树', 'D. 含有n个顶点n-1条边的子图一定是图G的生成树',  'A', '无','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 设无向图G=(V, E)和G2=(V2, E2)，如果G2是G的生成树，下列说法中错误的是（ ）。 (2分)
', 'A. G2为G的极小连通子图', 'B. G2为G的连通分量', 'C. |V2|=|V|且|E2|≤|E|', 'D. G2为G的无环子图',  'B', '无','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 对于有n个顶点的带权连通图，它的最小生成树是指图中任意一个（ ）。 (2分)
', 'A. 由n-1条权值最小的边构成的子图', 'B. 由n-l条权值之和最小的边构成的子图', 'C. 由n个顶点构成的极大连通子图', 'D. 由n个顶点构成的极小连通子图，且边的权值之和最小',  'D', '无','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. Kruskal算法适合于求（ ）的最小生成树。 (2分)
', 'A. 稀疏图', 'B. 稠密图', 'C. 连通图', 'D. 有向图',  'A', '无','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 下面(    )算法适合用于构造一个稠密图的最小生成树。 (2分)
', 'A. Dijkstra算法', 'B. Prim算法', 'C. Floyd算法', 'D. Kruskal算法',  'B', '无','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 用Prim算法求一个连通的带权图的最小生成树，在算法执行的某时刻，已选取的顶点集合U＝{1，2，3}，边的集合TE＝{(1，2)，(2，3)}，要选取下一条权值最小的边，不可能从  (    )  组中选取。 (2分)
', 'A. {(1，4)，(3，4)，(3，5)，(2，5)}', 'B. {(1，5)，(2，4)，(3，5)}', 'C. {(1，2)，(2，3)，(3，1)}', 'D. {(1，4)，(3，5)，(2，5)，(3，4)}',  'C', '无','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 下列关于最小生成树的说法中，正确的是（ ）。 (2分)<br>
I．最小生成树的代价唯一<br>
II．所有权值最小的边一定会出现在所有的最小生成树中<br>
III．使用普里姆（Prim）算法从不同顶点开始得到的最小生成树一定相同<br>
IV．使用普里姆算法和克鲁斯卡尔（Kruskal）算法得到的最小生成树总不相同
', 'A. 仅Ⅰ', 'B. 仅Ⅱ', 'C. 仅Ⅰ、 Ⅲ', 'D. 仅Ⅱ、 Ⅳ',  'A', '无','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 任何一个无向连通图的最小生成树（ ）。 (2分)
', 'A. 有一棵或多棵', 'B. 只有一棵树', 'C. 一定有多裸', 'D. 可能不存在',  'A', '当无向连通图存在权值相同的多条边时，生成树可能是不唯一的','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. Prim法和Kruskal算法构造图的最小生成树，所得到的最小生成树（ ）。 (2分)
', 'A. 相同', 'B. 不相同', 'C. 无法比较', 'D. 可能相同，可能不同',  'D', '当生成树不唯一时，不同算法构造的最小生成树可能不同','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 下列关于图的说法中，正确的是（ ）。 (2分)<br>
I. 有向图中顶点V的度等于其邻接矩阵中第V行中1的个数<br>
II. 无向图的邻接矩阵一定是对称矩阵，有向图的邻接矩阵一定是非对称矩阵<br>
III. 在图G的最小生成树G1中，某条边的权值可能会超过未选边的权值<br>
IV. 若有向无环图的拓扑序列唯一，则可以唯一确定该图
', 'A. I、II和III', 'B. III和IV', 'C. III', 'D. IV',  'C', '邻接矩阵中第V行中1的个数是顶点V的出度，有向图全链接时是邻接矩阵','0','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 最小生成树在图中可以包含回路。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 最小生成树中的边数一定是顶点数减一。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 最小生成树是指一个连通无向图中包含所有顶点且总权值最小的树。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 如果在最小生成树中添加一条新的边，则它仍然是最小生成树。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.6')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. Kruskal算法适用于稠密图，而Prim算法更适合稀疏图。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.6')
""")

# 6.7.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 设图采用邻接矩阵存储，Dijkstra算法的时间复杂度为（ ）。 (2分)
', 'A. O(n^3)', 'B. O(n+e)', 'C. O(n^2)', 'D. O(ne)',  'C', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 下列说法中正确的是（ ）。 (2分)
', 'A. 最短路径一定是简单路径', 'B. Dijkstra算法不适用于有回路的网图', 'C. Dijkstra算法不适用于求任意两顶点间的最短路径', 'D. 在Floyd算法的求解过程中，Pathk-1[i][j]一定是Pathk[i][j]的子集',  'A', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 用Dijkstra算法求一个带权有向图G中从顶点0出发的最短路径，在算法执行的某时刻，S={0，2，3，4}，下一步选取的目标顶点可能是（ ）。 (2分)
', 'A. 顶点2', 'B. 顶点3', 'C. 顶点4', 'D. 顶点7',  'D', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. Dijkstra算法适用于以下哪类图？（ ）。 (2分)
', 'A. 有向图和无向图，但不能有负权边', 'B. 仅适用于无向图', 'C. 仅适用于无权图', 'D. 适用于带负权边的图',  'A', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. Dijkstra算法的核心思想是（ ）。 (2分)
', 'A. 深度优先搜索', 'B. 贪心算法', 'C. 动态规划', 'D. 回溯法',  'B', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. Dijkstra算法中，初始状态下源点的距离为（ ）。 (2分)
', 'A. 正无穷', 'B. 负无穷', 'C. 0', 'D. 随机数',  'C', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 在无向连通图中，Dijkstra算法可以用于求解（ ）。 (2分)
', 'A. 最小生成树', 'B. 单源最短路径', 'C. 所有顶点对之间的最短路径', 'D. 最长路径',  'B', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 在Dijkstra算法中，从起点到终点的最短路径是通过以下哪种方式找到的？（ ）。 (2分)
', 'A. 遍历所有路径', 'B. 按权值递增选择边', 'C. 按路径长度递减选择路径', 'D. 逐步更新各顶点的最短距离',  'D', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在Dijkstra算法中，当从起点到一个顶点的距离发生更新时，意味着（ ）。 (2分)
', 'A. 找到了到该顶点的更短路径', 'B. 路径不一定是最短的', 'C. 起点和终点距离减小', 'D. 其他顶点的距离需要更新',  'A', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 如果一个有向图中所有边的权值都为正整数，则Dijkstra算法在求解单源最短路径时的计算结果是（ ）。 (2分)
', 'A. 不唯一', 'B. 唯一的最短路径', 'C. 路径长度不确定', 'D. 与顶点数无关',  'B', '无','0','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 在Dijkstra算法执行过程中，每个顶点最多被访问一次。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 在Dijkstra算法中，距离最短的顶点优先被处理。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. Dijkstra算法的时间复杂度在稠密图上较高。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 在Dijkstra算法的求解过程中，已处理过的节点不会再次被更新。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.7.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. Dijkstra算法可以用于带负权边的图。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.7.1')
""")

# 6.7.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 有一个顶点编号为0～4的带权有向图G，现用Floyd算法求任意两个顶点之间的最短路径，在算法执行的某时刻，已考虑了0～2的顶点，现考虑顶点3，则以下叙述中正确的是（ ）。 (2分)
', 'A. 只可能修改从顶点0～2到顶点3的最短路径', 'B. 只可能修改从顶点3到顶点0～2的最短路径', 'C. 只可能修改从顶点0～2到顶点4的最短路径', 'D. 其他所有两个顶点之间的路径都可能被修改',  'D', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. Floyd算法主要用于解决以下哪类问题？（ ）。 (2分)
', 'A. 单源最短路径', 'B. 最小生成树', 'C. 全源最短路径', 'D. 拓扑排序',  'C', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. Floyd算法的时间复杂度为（ ）。 (2分)
', 'A. O(n)', 'B. O(n^2)', 'C. O(n^3)', 'D. O(nlogn)',  'C', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. Floyd算法适用于以下哪类图？（ ）。 (2分)
', 'A. 有向图和无向图，无负权边', 'B. 无向图且无负权边', 'C. 有向图和无向图，允许负权边但无负权回路', 'D. 仅适用于无权图',  'C', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在执行Floyd算法的过程中，更新距离矩阵的核心思想是（ ）。 (2分)
', 'A. 考虑当前路径是否经过新顶点会变短', 'B. 逐个删除边', 'C. 计算每条边的平方', 'D. 遍历所有的最短路径',  'A', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. Floyd算法在更新路径矩阵时，判断一个路径是否更优的条件是（ ）。 (2分)
', 'A. 起点和终点的距离相等', 'B. 起点到中间点加中间点到终点的距离小于起点到终点的当前距离', 'C. 两点之间没有边', 'D. 起点的值大于终点的值',  'B', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 在Floyd算法初始化时，两个顶点之间没有直接边的距离通常设为（ ）。 (2分)
', 'A. 0', 'B. 正无穷', 'C. 负无穷', 'D. 随机值',  'B', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 在Floyd算法的实现中，如果路径矩阵显示了顶点间的最短路径为正无穷，则表示（ ）。 (2分)
', 'A. 路径长度最大', 'B. 两顶点不可达', 'C. 路径长度为零', 'D. 路径中有负权边',  'B', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在Floyd算法执行的过程中，每次更新的路径长度会（ ）。 (2分)
', 'A. 保持不变', 'B. 逐步减小或保持不变', 'C. 随机变化 ', 'D. 逐步增加',  'B', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. Floyd算法的主要优点在于（ ）。 (2分)
', 'A. 时间复杂度低', 'B. 可处理所有顶点对之间的最短路径', 'C. 适用于稀疏图', 'D. 不需要动态规划',  'B', '无','0','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. Floyd算法用于求解图中所有顶点对之间的最短路径。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 若图中包含负权回路，Floyd算法的结果仍然有效。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. Floyd算法的时间复杂度较高，不适合处理大量顶点的图。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. Floyd算法适用于稠密图。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','6' ,'6.7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 在Floyd算法的初始化阶段，不相邻的顶点距离被设为0。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'6.7.2')
""")

# 7.1 题目
# 7.1节是查找的基本概念，一道题也找不到。。。
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在查找问题中，查找效率取决于（ ）。 (2分)', 'A. 数据存储结构', 'B. 数据规模', 'C. 查找方法', 'D. 以上都是', 'D', '查找效率受数据存储结构、数据规模及具体查找方法的综合影响','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 线性表的顺序查找的时间复杂度是（ ）。 (2分)', 'A. O(1)', 'B. O(n)', 'C. O(log n)', 'D. O(n^2)', 'B', '顺序查找需要逐个比较，最坏情况下需遍历整个表，时间复杂度为O(n)','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 对于一个有序表，最常用的查找方法是（ ）。 (2分)', 'A. 顺序查找', 'B. 二分查找', 'C. 哈希查找', 'D. 插值查找', 'B', '二分查找适用于有序表，效率较高，时间复杂度为O(log n)','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 在哈希查找中，为了避免冲突，常用的方法是（ ）。 (2分)', 'A. 开放地址法', 'B. 链地址法', 'C. 再哈希法', 'D. 以上都是', 'D', '以上方法均可用于解决哈希冲突，不同方法有不同特点','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 若查找表存储在主存中，则采用的主要查找方法是（ ）。 (2分)', 'A. 二分查找', 'B. 顺序查找', 'C. 哈希查找', 'D. B树查找', 'C', '哈希查找适合主存查找，具有常数级的时间复杂度','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 二分查找的适用条件是（ ）。 (2分)', 'A. 表无序', 'B. 表有序', 'C. 数据分布均匀', 'D. 数据规模小', 'B', '二分查找要求查找表必须是有序表','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 哈希函数的设计原则是（ ）。 (2分)', 'A. 复杂性高', 'B. 计算速度快', 'C. 产生冲突少', 'D. B和C', 'D', '哈希函数需保证计算快速，且尽量减少冲突','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 插值查找的特点是（ ）。 (2分)', 'A. 适用于均匀分布的数据', 'B. 适用于稀疏分布的数据', 'C. 不适用有序表', 'D. 时间复杂度为O(n)', 'A', '插值查找通过计算插值位置进行查找，适用于均匀分布的数据','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. B树查找的主要应用场景是（ ）。 (2分)', 'A. 内存中的小规模数据', 'B. 外存中的大规模数据', 'C. 网络中的数据传输', 'D. 哈希查找的替代方案', 'B', 'B树主要用于外存查找，支持大规模数据的动态查找和维护','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在顺序查找中，为了优化效率，可以采用的措施是（ ）。 (2分)', 'A. 提前终止', 'B. 添加哨兵', 'C. 使用索引', 'D. 以上都是', 'D', '哨兵和索引可以减少比较次数，提前终止则避免无效查找','0','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 顺序查找适用于有序表和无序表。 (2分)', 'A. 是', 'B. 否', 'A', '顺序查找不依赖数据的有序性，适用于有序和无序表','1','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 二分查找的时间复杂度始终是O(log n)。 (2分)', 'A. 是', 'B. 否', 'B', '在最坏情况下，二分查找的时间复杂度为O(log n)','1','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 哈希查找需要维护数据的有序性。 (2分)', 'A. 是', 'B. 否', 'B', '哈希查找不需要数据有序性，仅依赖于哈希函数','1','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 插值查找对分布不均的数据查找效率较低。 (2分)', 'A. 是', 'B. 否', 'A', '插值查找适合均匀分布的数据，分布不均时效率会下降','1','7','7.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. B树的高度一般较低，因此查找效率高。 (2分)', 'A. 是', 'B. 否', 'A', 'B树的高度较低，保证了查找路径的长度和效率','1','7','7.1')
""")

# 7.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 对有序表A[1]~A[17]进行折半查找，查找长度为5的元素下标是（ ）。 (2分)
', 'A. 8, 17', 'B. 5, 10, 12', 'C. 9, 16', 'D. 9, 17',  'A', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 对含有100个元素的有序表进行折半查找，在查找成功的情况下，比较次数最多是（ ）次。 (2分)
', 'A. 25', 'B. 50', 'C. 10', 'D. 7',  'D', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 假定查找成功与不成功的可能性相同，在查找成功的情况下每个记录的查找概率相同，则顺序查找的平均查找长度为（ ）。 (2分)
', 'A. 0.5(n+1)', 'B. 0.25(n+1)', 'C. 0.5(n-1)', 'D. 0.75n+0.25',  'D', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 适合于折半查找的数据组织方式是（ ）。 (2分)
', 'A. 以链表存储的线性表', 'B. 以顺序表存储的任意线性表', 'C. 以链表存储的有序线性表', 'D. 以顺序表存储的有序线性表',  'D', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 对含有n个元素的顺序表采用顺序查找方法，不成功时的比较次数是（ ）。 (2分)
', 'A. 1', 'B. n', 'C. n-1', 'D. n+1',  'B', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 当采用分块查找时，数据的组织方式为（ ）。 (2分)
', 'A. 数据分成若干块，每块内数据有序', 'B. 数据分成若干块，每块内数据不必有序，但块间必须有序，每块内最大（或最小）的关键字组成索引块', 'C. 数据分成若干块，每块内数据有序，每块内最大（或最小）的关键字组成索引块', 'D. 数据分成若干块，每块中的数据个数必须相同',  'B', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 设有序表的关键字序列为（1，4，6，10，18，35，42，53，67，71，78，84，92，99），当用二分查找法查找35的结点时，经（ ）次比较后查找成功。 (2分)
', 'A. 2', 'B. 3', 'C. 4', 'D. 6',  'C', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 对长度为3的顺序表进行查找，若查找第一个元素的概率为1/2，查找第二个元素的概率1/3，查找第三个元素的概率为1/6，则查找任一元素的平均查找长度为（ ）。 (2分)
', 'A. 5/3', 'B. 2', 'C. 7/3', 'D. 4/3',  'A', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 设折半查找过程所对应的判定树是一棵（ ）。 (2分)
', 'A. 最小生成树', 'B. 平衡二叉树', 'C. 完全二叉树 ', 'D. 满二叉树',  'B', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 已知一个长度为 16 的顺序表，其元素按关键字有序排列，若采用折半查找算法查找一个不存在的元素，则比较的次数至少是（ ），至多是（ ）。 (2分)
', 'A. 4', 'B. 5', 'C. 6', 'D. 7',  'A、B', '无','0','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 顺序查找既可以用于有序表，也可以用于无序表。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 折半查找的最坏情况时间复杂度为O(log n)，而顺序查找为O(n)。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 在顺序查找中，无论表是否有序，查找效率均为O(log n)。 (2分)
', 'A. 是', 'B. 否',  'B', '顺序查找的时间复杂度为O(n)','1','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 对于线性表来说，顺序查找总是比折半查找效率高。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','7' ,'7.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 在折半查找过程中，每次比较都会将查找区间缩小一半。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.2')
""")

# 7.3 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 折半查找和二又排序树的时间性能（ ）。 (2分)
', 'A. 相同', 'B. 有时不相同', 'C. 完全不同', 'D. 无法比较',  'B', '二叉排序数最坏情况即形成单支树时，其查找长度为O(n)','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 下列选项中，不能构成折半查找中关键字比较序列的是（ ）。 (2分)
', 'A. 500, 200, 450, 180', 'B.500, 450, 200, 180', 'C. 180, 500, 200, 450 ', 'D. 180, 200, 500, 450 ',  'A', '因为折半查找的判定树是一颗二叉排序树，因此画出图看其是否满足二叉排序树的要求','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 在二叉排序树中，左子树的所有节点值（ ）。 (2分)
', 'A. 必须小于右子树的所有节点值', 'B. 必须大于根节点值', 'C. 必须小于根节点值', 'D. 必须等于根节点值',  'C', '无','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 二叉排序树的查找操作在最理想情况下的时间复杂度为（ ）。 (2分)
', 'A. O(1)', 'B. O(logn)', 'C. O(n)', 'D. O(nlogn)',  'B', '无','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 若向一棵二叉排序树中插入节点，插入新节点的位置在（ ）。 (2分)
', 'A. 根节点', 'B. 左子树的任意位置', 'C. 一定是叶子节点的位置', 'D. 一定是右子树的最下层',  'C', '无','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 如果在一棵二叉排序树中删除一个节点且该节点有两个子节点，通常的做法是（ ）。 (2分)
', 'A. 直接删除该节点', 'B. 找到该节点的直接前驱或直接后继替换该节点', 'C. 删除该节点的子节点', 'D. 重构整棵树',  'B', '无','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 二叉排序树的中序遍历结果是（ ）。 (2分)
', 'A. 倒序排列', 'B. 有序递增排列', 'C. 无序排列', 'D. 随机排列',  'B', '无','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 在二叉排序树中，叶节点的度数为（ ）。 (2分)
', 'A. 0', 'B. 1', 'C. 2', 'D. 以上选项均有可能',  'A', '无','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 若向一棵高度为3的二叉排序树中插入一个新节点，最坏情况下查找插入位置需要比较的次数为（ ）。 (2分)
', 'A. 3', 'B. 4', 'C. 5', 'D. 6',  'B', '无','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在二叉排序树中，某节点的左子树最右侧的节点称为该节点的（ ）。 (2分)
', 'A. 直接前驱', 'B. 直接后继', 'C. 根节点', 'D. 兄弟节点',  'A', '无','0','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 二叉排序树的中序遍历序列一定是从小到大的有序序列。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 在二叉排序树中，删除一个节点时，不需要对其子树进行任何调整。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 对于二叉排序树，删除节点后中序遍历的结果仍然是有序序列。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 二叉排序树的根节点总是整个树中最小的元素。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.3')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 在二叉排序树中，查找一个节点的时间复杂度与树的高度有关。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.3')
""")

# 7.4 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 按{12, 24, 36, 90, 52, 30}的顺序构建平衡二叉树，根结点是（ ）。 (2分)
', 'A. 24', 'B. 36', 'C. 52', 'D. 30',  'B', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在平衡二叉树中插入一个结点后造成了不平衡，设最低的不平衡结点为A，并已知A的左孩子的平衡因子为0右孩子的平衡因子为1，则应作（ ）型调整以使其平衡。 (2分)
', 'A. LL', 'B. LR', 'C. RL', 'D. RR',  'C', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 以下数据结构中（ ）属非线性结构。 (2分)
', 'A. 栈', 'B. 串', 'C. 队列', 'D. 平衡二叉树',  'D', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 一棵高度为h的非空平衡二叉树，其每个非叶子结点的平衡因子均为0，则该树共有（ ）个结点。 (2分)
', 'A. 2^(h-1)-1', 'B. 2^(h-1)', 'C. 2^(h-1)+1', 'D. 2^(h)-1',  'D', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 高度为4的平衡二叉树含有的最少结点数为（ ）。 (2分)
', 'A. 9', 'B. 8', 'C. 7', 'D. 6',  'C', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 关于二叉排序树描述不正确的是（ ）。 (2分)
', 'A. 二叉排序树的查找效率取决于树的形态', 'B. 从二叉排序树中删去一个结点后再重新插入，一定是作为叶子结点插入的', 'C. 在最坏情况下，利用插入操作构造一棵二叉排序树的时间为O(nlog2n)', 'D. 在含有n个结点的平衡二叉排序树中，查找失败时最坏时间为O(log2n)',  'C', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 平衡二叉树的基本特性是（ ）。 (2分)
', 'A. 每个节点的左右子树高度相差不超过1', 'B. 树的高度不超过logn', 'C. 每个节点都有两个子节点', 'D. 只有叶子节点可以无子节点',  'A', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 平衡二叉树的最坏情况时间复杂度为（ ）。 (2分)
', 'A. O(n)', 'B. O(logn)', 'C. O(nlogn)', 'D. O(1)',  'B', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在AVL树中，插入新节点后需要进行调整的情况发生在（ ）。 (2分)
', 'A. 根节点', 'B. 任意两个相邻节点之间', 'C. 不平衡节点的父节点', 'D. 不平衡节点所在的子树',  'D', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 若在平衡二叉树中插入节点后出现左右不平衡（LR型），应进行的调整为（ ）。 (2分)
', 'A. 先左旋后右旋', 'B. 先右旋后左旋', 'C. 只进行右旋', 'D. 只进行左旋',  'A', '无','0','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 平衡二叉树的所有节点必须保证左右子树高度相差不超过1。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 平衡二叉树的插入和删除操作都可能会导致不平衡，并需要通过旋转来恢复平衡。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 在AVL树中，左旋或右旋操作会影响中序遍历的顺序。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 在AVL树中，左旋或右旋操作会影响中序遍历的顺序。 (2分)
', 'A. 是', 'B. 否',  'B', 'AVL树的高度与节点数量成对数关系','1','7' ,'7.4')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 平衡二叉树中的平衡因子通常定义为左子树高度减去右子树高度。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.4')
""")

# 7.5 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 适合动态查找的查找技术是（ ）。 (2分)
', 'A. 顺序查找', 'B. 折半查找', 'C. 散列查找', 'D. 随机查找',  'C', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 关于散列查找，下列说法中正确的是（ ）。 (2分)
', 'A. 再散列法处理冲突不会产生聚集', 'B. 散列表的装填因子越大说明空间利用率越高，因此应使装填因子尽可能大', 'C. 散列函数选择的好可以减少冲突现象', 'D. 对任何关键码集合都无法找到不产生冲突的散列函数',  'C', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 为一组关键码{87, 73, 25, 55, 90, 28, 17, 22, 3, 62}构造散列表，设散列函数为H(key)=key mod 11，用拉链法处理冲突，位于同一链表中的是（ ）。 (2分)
', 'A. 87, 90', 'B. 22, 62', 'C. 73, 17', 'D. 73, 62',  'D', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 散列查找一般适用于（ ）的情况下的查找。 (2分)
', 'A. 查找表为链表', 'B. 查找表为有序表', 'C. 关键字集合比地址集合大得多', 'D. 关键字集合与地址集合之间存在对应关系',  'D', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 下列关于散列表的说法中，正确的是（ ）。 (2分)<br>
I. 若散列表的填装因子a<1，则可避免碰撞的产生<br>
II. 散列查找中不需要任何关键字的比较<br>
III. 散列表在查找成功时平均查找长度与表长有关<br>
IV. 若在散列表中删除一个元素，不能简单地将该元素删除
', 'A. I和IV', 'B. II和III', 'C. III', 'D. IV',  'D', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 在开放定址法中散列到同一个地址而引起的“堆积”问题是由于（ ）引起的。 (2分)
', 'A. 同义词之间发生冲突', 'B. 非同义词之间发生冲突', 'C. 同义词之间或非同义词之间发生冲突', 'D. 散列表“溢出”',  'C', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 设有一个含有200个表项的散列表，用线性探测法解决冲突，按关键字查询时找到一个表项的平均探测次数不超过1.5 ，则散列表项应能够容纳（ ）个表项（设查找成功的平均查找长度为ASL=[1+1/(1/a)]/2，其中a为装填因子）（ ）。 (2分)
', 'A. 400', 'B. 526', 'C. 624', 'D. 676',  'A', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 假定有K个关键字互为同义坷，若用线性探测法把这K个关键字填入散列表，至少要进行（ ）次探测。 (2分)
', 'A. K-1', 'B. K', 'C. K+1', 'D. K(K+1)/2',  'D', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 对包含n个元素的散列表进行查找，平均查找长度为（ ）。 (2分)
', 'A. O(1)', 'B. O(logn)', 'C. 不直接依赖于n', 'D. 直接依赖于表长',  'C', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 为提高散列表的查找效率，可以采取的正确措施是（ ）。 (2分)<br>
I. 增大装填（载）因子<br>
II. 设计冲突（碰撞）少的散列函数<br>
III. 处理冲突（碰撞） 避免产生聚集（堆积）现象
', 'A. I', 'B. II', 'C. I、II', 'D. II、III',  'D', '无','0','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 在散列表中，装填因子越大，查找的效率通常越低。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 链地址法的散列表需要重新计算每个元素的位置来解决冲突。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 线性探测法的特点是冲突时探测位置具有线性递增关系。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 散列查找的平均时间复杂度一般为O(n)。 (2分)
', 'A. 是', 'B. 否',  'B', '一般为O(1)','1','7' ,'7.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 双散列法通常采用两个不同的散列函数来处理冲突。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','7' ,'7.5')
""")

# 8.1节是排序的基本概念
# 8.1题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 排序算法的稳定性是指（ ）。 (2分)', 'A. 算法在所有情况下的效率一致性', 'B. 相同关键字的记录在排序前后的相对位置不变', 'C. 算法的时间复杂度恒定', 'D. 算法的空间复杂度恒定', 'B', '稳定性指排序后相等关键字的记录仍保持原有次序','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 快速排序的平均时间复杂度是（ ）。 (2分)', 'A. O(n)', 'B. O(n log n)', 'C. O(n^2)', 'D. O(log n)', 'B', '快速排序的平均时间复杂度为O(n log n)','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 堆排序的主要思想是利用（ ）。 (2分)', 'A. 二叉查找树', 'B. 完全二叉树', 'C. 平衡二叉树', 'D. 红黑树', 'B', '堆排序通过构建最大堆或最小堆来实现排序，依赖完全二叉树的性质','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 归并排序是一种（ ）。 (2分)', 'A. 递归和分治的算法', 'B. 基于堆的排序算法', 'C. 非稳定的排序算法', 'D. 原地排序算法', 'A', '归并排序采用分治法进行递归排序，稳定性强','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 插入排序适合的应用场景是（ ）。 (2分)', 'A. 数据基本有序', 'B. 数据随机分布', 'C. 数据分布不均匀', 'D. 数据量非常大', 'A', '插入排序对少量或基本有序数据效率较高','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 希尔排序的时间复杂度与增量序列的选择有关，其最坏时间复杂度是（ ）。 (2分)', 'A. O(n^2)', 'B. O(n log n)', 'C. O(n^(3/2))', 'D. O(log n)', 'A', '最坏情况下，希尔排序的时间复杂度可达O(n^2)','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 桶排序的主要优点是（ ）。 (2分)', 'A. 时间复杂度低', 'B. 空间复杂度低', 'C. 适合大量数据的外部排序', 'D. 易于实现稳定性', 'A', '桶排序在适合的场景下时间复杂度为O(n)','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 冒泡排序在最优情况下的时间复杂度是（ ）。 (2分)', 'A. O(n)', 'B. O(n log n)', 'C. O(n^2)', 'D. O(log n)', 'A', '冒泡排序在数据已经有序时仅需一次遍历，时间复杂度为O(n)','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 以下排序算法中，属于不稳定排序的是（ ）。 (2分)', 'A. 冒泡排序', 'B. 插入排序', 'C. 选择排序', 'D. 归并排序', 'C', '选择排序可能改变相等关键字的相对位置，不稳定','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 外部排序的典型方法是（ ）。 (2分)', 'A. 归并排序', 'B. 快速排序', 'C. 插入排序', 'D. 冒泡排序', 'A', '归并排序常用于处理内存无法容纳的大量数据，适合外部排序','0','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 快速排序在最坏情况下的时间复杂度是O(n^2)。 (2分)', 'A. 是', 'B. 否', 'A', '当每次划分极不平衡时，快速排序的时间复杂度为O(n^2)','1','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 堆排序是一种不稳定的排序算法。 (2分)', 'A. 是', 'B. 否', 'A', '堆排序在调整堆时可能改变相等关键字的相对位置，因此是不稳定排序','1','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 希尔排序是一种改进的选择排序。 (2分)', 'A. 是', 'B. 否', 'B', '希尔排序是对插入排序的改进，不属于选择排序的范畴','1','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 冒泡排序总是需要n^2次比较。 (2分)', 'A. 是', 'B. 否', 'B', '冒泡排序在最优情况下（已有序列）仅需n次比较','1','8','8.1')
""")
cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 外部排序通常需要多次读写磁盘文件。 (2分)', 'A. 是', 'B. 否', 'A', '外部排序处理大规模数据，需频繁与外存交换数据','1','8','8.1')
""")

# 8.2.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 数据序列{8, 9, 10, 4, 5, 6, 20, 1, 2}只能是（ ）的两趟排序后的结果。 (2分)
', 'A. 选择排序', 'B. 起泡排序', 'C. 插入排序', 'D. 堆排序',  'C', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 下列排序算法中，（ ）可能会出现下面情况：在最后一趟排序开始之前，所有记录都不在最终位置。 (2分)
', 'A. 起泡排序', 'B. 直接插入排序', 'C. 快速排序', 'D. 堆排序',  'B', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 对有n个元素的排序表进行直接插入排序，在最好情况下需比较（ ）次关键字。 (2分)
', 'A. n-1', 'B. n+1', 'C. n/2', 'D. n(n-1)/2',  'A', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 以下排序方法中，（ ）在初始序列已基本有序的情况下，排序效率最高。 (2分)
', 'A. 二路归并排序', 'B. 快速排序', 'C. 直接插入排序', 'D. 堆排序',  'C', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 如果在一个排序算法的执行过程中，没有同一对元素被比较过两次或以上，则称该排序算法为节俭排序算法，以下算法中是节俭排序算法的有（ ）。 (2分)
', 'A. 直接插入排序', 'B. 简单选择排序', 'C. 堆排序', 'D. 以上选项都不对',  'A', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 若数据元素序列（11，12，13，7，8，9，23，4，5）是采用下列排序方法之一得到的第二趟排序后的结果，则该排序算法只能是（ ）。 (2分)
', 'A. 冒泡排序', 'B. 直接插入排序', 'C. 简单选择排序', 'D. 二路归并排序',  'B', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 插入排序的平均时间复杂度是（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'C', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 插入排序的最坏时间复杂度是（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'C', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 插入排序在处理下列哪种情况时，效率最低（ ）。 (2分)
', 'A. 数组已按降序排列', 'B. 数组已按升序排列', 'C. 数组部分有序', 'D. 数组中有重复元素',  'A', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 插入排序的稳定性是（ ）。 (2分)
', 'A. 不稳定', 'B. 稳定', 'C. 与数据有关', 'D. 无法确定',  'B', '无','0','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 插入排序的最优时间复杂度是O(nlogn)。 (2分)
', 'A. 是', 'B. 否',  'B', '最优时间复杂度是O(n)','1','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 插入排序的每一次插入操作会将数据进行分块处理。 (2分)
', 'A. 是', 'B. 否',  'B', '插入排序将元素插入到已有序的部分中','1','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 插入排序是一种基于比较的排序算法。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 插入排序需要辅助存储空间，因此它不是就地排序算法。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.2.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 插入排序一般比冒泡排序效率更高，尤其是当数据量较小或接近有序时。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.2.1')
""")

# 8.2.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 下列排序算法中，（ ）不能保证每趟至少将一个记录放到最终位置。 (2分)
', 'A. 快速排序', 'B. 希尔排序', 'C. 起泡排序', 'D. 堆排序',  'B', '无','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 希尔排序属于（ ）。 (2分)
', 'A. 插入排序', 'B. 交换排序', 'C. 选择排序', 'D. 归并排序',  'A', '无','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 对序列{15,9,7,8,20,-1,4}用希尔排序方法排序，经一趟后序列变为{15,-1,4,8,20,9,7}，则该次采用的增量是（ ）。 (2分)
', 'A. 1', 'B. 4', 'C. 3', 'D. 2',  'B', '无','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 用希尔排序方法对一个数据序列进行排序时，若第1趟排序结果为9,1,4,13,7,8,20,23,15,则该趟排序采用的增量（间隔）可能是（ ）。 (2分)
', 'A. 2', 'B. 3', 'C. 4', 'D. 5',  'B', '第二个元素为1，说明该希尔排序为从小到大排序','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在希尔排序中，增量的选择通常是（ ）。 (2分)
', 'A. 任意选择', 'B. 固定为2的幂', 'C. 任意的递减序列', 'D. 特殊的递减序列',  'D', '无','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 希尔排序在最坏情况下的时间复杂度是（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. 取决于增量序列',  'D', '无','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 希尔排序的平均时间复杂度通常被估计为（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(nlog2n)',  'D', '无','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 希尔排序的主要优点是（ ）。 (2分)
', 'A. 稳定性高', 'B. 适合大规模数据排序', 'C. 对部分有序的数据排序效率高', 'D. 不需要增量序列',  'C', '无','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 希尔排序是一种（ ）。 (2分)
', 'A. 内部排序算法', 'B. 外部排序算法', 'C. 交换排序算法', 'D. 选择排序算法',  'A', '无','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 希尔排序的稳定性是（ ）。 (2分)
', 'A. 稳定的', 'B. 不稳定的', 'C. 取决于数据分布', 'D. 取决于增量序列',  'B', '无','0','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 希尔排序的时间复杂度与选择的增量序列有关。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 希尔排序的主要目标是减少数据的移动次数，从而提高排序效率。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 希尔排序是一种交换排序算法。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 希尔排序适合小数据量的排序，但不适合大数据量排序。 (2分)
', 'A. 是', 'B. 否',  'B', '希尔排序适合较大数据量，尤其是部分有序数据','1','8' ,'8.2.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 使用希尔排序对数据进行分组排序后，不需要对组内进行插入排序。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.2.2')
""")

# 8.3.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 若初始数据基本正序，则选用的最好的排序方法是（ ）。 (2分)<br>
I. 直接插入排序
II. 冒泡排序
III. 快速排序
IV. 二路归并排序
', 'A. I', 'B. I、II', 'C. I、III', 'D. II、IV',  'B', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 某程序需要从10000个无序的整数中找出前10个最小的整数，在以下排序方法中最好采用（ ）。 (2分)
', 'A. 直接插入排序', 'B. 冒泡排序', 'C. 二路归并排序', 'D. 希尔排序',  'B', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 冒泡排序的基本思想是（ ）。 (2分)
', 'A. 将最小元素直接移动到起始位置', 'B. 每次找到最小的元素放到末尾', 'C. 通过相邻元素交换，将较大元素逐步移到数组末尾', 'D. 使用分治策略进行排序',  'D', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 冒泡排序的时间复杂度为（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'C', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 冒泡排序在以下（ ）情况下的时间复杂度为O(n)。 (2分)
', 'A. 数据完全无序', 'B. 数据完全有序', 'C. 数据部分有序', 'D. 数据逆序',  'B', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 冒泡排序属于以下哪一类排序算法（ ）。 (2分)
', 'A. 插入排序', 'B. 选择排序', 'C. 交换排序', 'D. 基数排序',  'C', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 冒泡排序的稳定性是（ ）。 (2分)
', 'A. 稳定', 'B. 不稳定', 'C. 随机', 'D. 不确定',  'A', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 冒泡排序适合以下哪种情况的排序？（ ）。 (2分)
', 'A. 大量无序数据', 'B. 数据量小且接近有序', 'C. 数据完全逆序', 'D. 数据有很多重复元素',  'B', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 在n个元素的数组中，冒泡排序在最坏情况下需要的比较次数是（ ）。 (2分)
', 'A. n', 'B. n-1', 'C. n^2', 'D. n(n-1)/2',  'D', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在冒泡排序的过程中，经过k次遍历后，数组中的哪些元素已处于最终位置（ ）。 (2分)
', 'A. 前k个元素', 'B. 后k个元素', 'C. 所有元素', 'D. 无法确定',  'B', '无','0','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 冒泡排序是一种内部排序算法。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 在冒泡排序中，元素交换的次数等于比较次数。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 在冒泡排序中，最大值会逐步“冒泡”到末尾。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 冒泡排序需要使用递归才能完成排序。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.3.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 冒泡排序只能用于整数类型的数据排序。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.3.1')
""")

# 8.3.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 下列序列中，（ ）是执行第一趟快速排序的结果。 (2分)
', 'A. [da，ax，eb，de，bb] ff [ha，gc]', 'B. [cd，eb，ax，da] ff [ha，gc，bb]', 'C. [gc，ax，eb，cd，bb] ff [da，ha]', 'D. [ax，bb，cd，da] ff [eb，gc，ha]',  'A', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 快速排序在（ ）情况下最不利于发挥其长处。 (2分)
', 'A. 待排序的数据量太大', 'B. 待排序的数据含有多个相同值', 'C. 待排序的数据基本有序', 'D. 待排序的数据数量为奇数',  'C', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 对下面的数据序列采用快速排序进行排序，速度最快的是（ ）。 (2分)
', 'A. {21, 25, 5, 17, 9, 23, 30}', 'B. {25, 23, 30, 17, 21, 5, 9}', 'C. {21, 9, 17, 30, 25, 23, 5}', 'D. {5, 9, 17, 21, 23, 25, 30}',  'A', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 用某种排序方法对数据序列（24，88，21，48，15，27，69，35，20）进行递增排序，元素序列的变化情况如下：<br>
①（24，88，21，48，15，27，69，35，20）<br>
②（20，15，21，24，48，27，69，35，88）<br>
③（15，20，21，24，35，27，48，69，88）<br>
④（15，20，21，24，27，35，48，69，88）<br>
则所采用的排序方法是（ ）。 (2分)
', 'A. 快速排序', 'B. 简单选择排序', 'C. 直接插入排序', 'D. 二路归并排序',  'A', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 采用递归方式对顺序表进行快速排序，下列关于递归次数的叙述中，正确的是。 (2分)
', 'A. 递归次数与初始数据的排列次序无关', 'B. 每次划分后，先处理较长的分区可以减少递归次数', 'C. 每次划分后，先处理较短的分区可以减少递归次数', 'D. 递归次数与每次划分后得到的分区处理顺序无关',  'D', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 快速排序的基本思想是（ ）。 (2分)
', 'A. 逐步将数组分成两半', 'B. 使用递归分治，将数组划分为两个子数组', 'C. 按照固定步长逐步交换相邻元素', 'D. 每次都找到最大元素放到末尾',  'B', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 快速排序在最坏情况下的时间复杂度是（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'C', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 快速排序在最优情况下的时间复杂度是（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'B', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 快速排序的平均时间复杂度是（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'B', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 快速排序属于以下哪种排序算法（ ）。 (2分)
', 'A. 交换排序', 'B. 插入排序', 'C. 选择排序', 'D. 合并排序',  'A', '无','0','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 快速排序是一种稳定的排序算法。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 快速排序通常适用于大规模、随机分布的数据集。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 快速排序的空间复杂度始终为O(n)。 (2分)
', 'A. 是', 'B. 否',  'A', '快速排序的空间复杂度平均为O(log n)，最坏情况为O(n)','1','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 快速排序在排序过程中会确定一个元素的最终位置。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.3.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 快速排序不适合用于部分有序的数据。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.3.2')
""")

# 8.4.1 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 有以下4种排序方法，在排序过程中所需的关键字比较总次数与初始序列顺序无关的是（ ）。 (2分)
', 'A. 直接插入排序', 'B. 简单选择排序', 'C. 快速排序', 'D. 二路归并排序',  'B', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 设线性表中每个元素有两个数据项k1和k2，现对线性表按以下规则进行排序：先看数据项k1，k1值小的在前，大的在后；在k1值相同的情况下，再看k2，k2值小的在前，大的在后。满足这种要求的排序方法是（ ）。 (2分)
', 'A. 先按k1值进行直接插入排序，再按k2值进行简单选择排序', 'B. 先按k2值进行直接插入排序，再按k1值进行简单选择排序', 'C. 先按k1值进行简单选择排序，再按k2值进行直接插入排序', 'D. 先按k2值进行简单选择排序，再按k1值进行直接插入排序',  'D', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 简单选择排序的主要思想是（ ）。 (2分)
', 'A. 每次找到最小元素并将其放在数组起始位置', 'B. 每次找到最大元素并将其放在数组末尾', 'C. 每次将相邻元素互换位置', 'D. 使用递归分治将数组分割成两部分',  'A', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 简单选择排序的平均时间复杂度为（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'C', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 在以下（ ）情况下，简单选择排序的效率最高。 (2分)
', 'A. 数据已完全有序', 'B. 数据完全逆序', 'C. 数据部分有序', 'D. 数据随机分布',  'A', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 简单选择排序的最优时间复杂度是（ ）。 (2分)
', 'A. 交换排序', 'B. 插入排序', 'C. 选择排序', 'D. 合并排序',  'A', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 简单选择排序是一种（ ）。 (2分)
', 'A. 稳定的排序', 'B. 不稳定的排序', 'C. 动态排序', 'D. 双向排序',  'B', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 简单选择排序的最坏时间复杂度是（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'C', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 简单选择排序的交换次数在最坏情况下为（ ）。 (2分)
', 'A. n', 'B. n-1', 'C. n^2', 'D. n(n-1)/2',  'B', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 简单选择排序适用于以下哪种情况（ ）。 (2分)
', 'A. 大量无序数据', 'B. 小规模数据且基本无序', 'C. 部分有序数据', 'D. 数据随机分布',  'B', '无','0','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 快速排序、简单选择排序和堆排序都与初始序列次序无关。 (2分)
', 'A. 是', 'B. 否',  'B', '只有快速排序无关','1','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 直接插入排序、冒泡排序和简单选择排序在最好情况下的时间复杂度均为O(n)。 (2分)
', 'A. 是', 'B. 否',  'B', '直接插入排序和冒泡排序在最好情况下的时间复杂度均为O(n)。','1','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 简单选择排序的交换次数始终等于比较次数。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 简单选择排序适合用于数据量非常大的场景。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.4.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 在简单选择排序中，比较次数在最坏情况下为n(n-1)/2。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.4.1')
""")

# 8.4.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 下面的记录序列中，（ ）是堆。 (2分)
', 'A. {1, 2, 8, 4, 3, 9, 10, 5}', 'B. {1, 5, 10, 6, 7, 8, 9, 2}', 'C. {9, 8, 7, 6, 4, 8, 2, 1}', 'D. {9, 8, 7, 6, 5, 4, 3, 7}',  'A', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 堆的形状是一棵（ ）。 (2分)
', 'A. 二叉查找树', 'B. 满二叉树', 'C. 完全二叉树', 'D. 判定树',  'C', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 对于序列{35, 25, 55, 15, 30, 20, 10, 40}，采用筛选法初始构建小根堆，元素之间的比较次数是（ ）。 (2分)
', 'A. 7', 'B. 8', 'C. 9', 'D. 10',  'D', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 对于小根堆{8, 17, 23, 52, 25, 72, 68, 71, 60}，输出两个最小关键码后的剩余堆是（ ）。 (2分)
', 'A. {23, 72, 60, 25, 68, 71, 52}', 'B. {23, 25, 52, 60, 71, 72, 68}', 'C. {71, 25, 23, 52, 60, 72, 68}', 'D. {23, 25, 68, 52, 60, 72, 71}',  'D', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 设有5000个元素，希望用最快的速度找出前10个最大的元素，采用（ ）方法最好。 (2分)
', 'A. 堆排序', 'B. 希尔排序', 'C. 快速排序', 'D. 二路归并排序',  'A', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 下列排序方法中，若将顺序存储更换为链接存储，则算法的时间效率会降低的是（ ）。 (2分)<br>
I．插入排序  II．选择排序  III．起泡排序  IV．希尔排序  V．堆排序
', 'A. I、II', 'B. II、III', 'C. III、IV', 'D. IV、V',  'D', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 下述二叉树中满足“从根结点到任意结点的路径上所经过的结点序列按其关键字有序”性质的是（ ）。 (2分)
', 'A. 二叉排序树', 'B. 哈夫曼树', 'C. B+树', 'D. 堆',  'D', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 将一个从大到小的数组，用以下排序方法排序成从小到大的，（ ）最快。 (2分)
', 'A. 堆排序', 'B. 冒泡排序', 'C. 快速排序', 'D. 直接插入排序',  'A', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 以下序列不是堆的是（ ）。 (2分)
', 'A. （100，85，98，77，80，60，82，40，20，10，66）', 'B. （100，98，85，82，80，77，66，60，40，20，10）', 'C. （10，20，40，60，66，77，80，82，85，98，100）', 'D. （100，85，40，77，80，60，66，98，82，10，20）',  'D', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 在含有n个关键字的小根堆R[1..n]中，关键字最大的元素有可能存储在（ ）位置上。 (2分)
', 'A. n/2', 'B. n/2-1', 'C. 1', 'D. n/2+2',  'D', '无','0','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 堆排序的平均时间复杂度为O(nlogn)。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 堆排序是一种稳定的排序算法。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 堆排序通常适用于小数据量的排序。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 堆排序的空间复杂度为O(1)，无需额外的存储空间。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.4.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 堆排序构建大根堆或小根堆时，必须遍历所有节点。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.4.2')
""")

# 8.5 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 若需在O(nlog2n)的时间内完成对数组的排序，且要求排序是稳定的，则可选择的排序方法是（ ）。 (2分)
', 'A. 快速排序', 'B. 堆排序', 'C. 归并排序', 'D. 希尔排序',  'C', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 下列排序方法中，时间性能与待排序记录的初始状态无关的是（ ）。 (2分)
', 'A. 插入排序和快速排序', 'B. 归并排序和快速排序', 'C. 选择排序和归并排序', 'D. 插入排序和归并排序',  'C', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 某文件经过内排序后得到100个初始归并段，若使用多路归并排序算法，并要求三趟归并完成排序，则归并路数最少是（ ）。 (2分)
', 'A. 3', 'B. 4', 'C. 5', 'D. 6',  'C', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 假设k路归并排序采用败者树，则败者树的结点个数是（ ）。 (2分)
', 'A. k', 'B. 2k', 'C. 2k+1', 'D. 2k-1',  'D', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 当内存工作区可容纳的记录个数w=2时，记录序列（5, 4, 3, 2, 1）采用置换-选择排序将产生（ ）个初始归并段。 (2分)
', 'A. 2', 'B. 3', 'C. 4', 'D. 5',  'B', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 外部归并排序是把外存文件调入内存，再利用内部排序的方法进行排序，因此外部归并排序所花费时间取决于（ ）。 (2分)
', 'A. 内部排序', 'B. 归并的趟数', 'C. 初始序列', 'D. 无法确定',  'B', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 将两个各有n个元素的有序表归并成一个有序表，其最少的比较次数是（ ）。 (2分)
', 'A. n', 'B. 2n-1', 'C. 2n', 'D. n-1',  'A', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 一个关键字序列为（12，38，35，25，74，50，63，90），按二路归并排序方法对序列进行一趟归并后的结果为（ ）。 (2分)
', 'A. 12，38，35，25，74，50，63，90', 'B. 12，38，25，35，50，74，63，90', 'C. 12，25，35，38，50，74，63，90', 'D. 12，35，38，25，63，50，74，90',  'B', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 时间复杂度恒为O(nlog2n)且不受数据初始状态影响的排序算法是（ ）。 (2分)
', 'A. 二路归并排序', 'B. 希尔排序', 'C. 快速排序', 'D. 简单选择排序',  'A', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 全国有1000000人参加竞赛，录取成绩优异的前20名作为获奖者，并将获奖者的成绩按照分数从高到低的顺序输出，若不排出非获奖者的名次，则选择（ ）方法速度最快。 (2分)
', 'A. 快速排序', 'B. 堆排序', 'C. 二路归并排序', 'D. 冒泡排序',  'B', '无','0','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 归并排序是一种稳定的排序算法。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 归并排序不适合处理大规模数据。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 归并排序的递归实现不需要任何辅助空间。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 归并排序的最差时间复杂度与平均时间复杂度相同。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.5')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 归并排序的时间复杂度为O(nlogn)。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.5')
""")

# 8.6.1 题目      8.6.1是桶排序，题目很少
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 桶排序的平均时间复杂度是（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'A', '无','0','8' ,'8.6.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在桶排序中，桶的数量通常取决于（ ）。 (2分)
', 'A. 数据分布范围', 'B. 数据长度', 'C. 数据类型', 'D. 数据有序性',  'A', '无','0','8' ,'8.6.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 桶排序的最佳时间复杂度为（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(n^2)', 'D. O(logn)',  'A', '无','0','8' ,'8.6.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 桶排序在以下哪种情况下效率最差（ ）。 (2分)
', 'A. 数据均匀分布', 'B. 数据有序', 'C. 数据集中于少数桶', 'D. 数据随机分布',  'C', '无','0','8' ,'8.6.1')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 桶排序是一种稳定的排序算法。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.6.1')
""")

# 8.6.2 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 已知关键码序列{78, 19, 63, 30, 89, 84, 55, 69, 28, 83}采用基数排序，第一趟排序后的关键码序列为（ ）。 (2分)
', 'A. {19, 28, 30, 55, 63, 69, 78, 83, 84, 89}', 'B. {28, 78, 19, 69, 89, 63, 83, 30, 84, 55}', 'C. {30, 63, 83, 84, 55, 78, 28, 19, 89, 69}', 'D. {30, 63, 83, 84, 55, 28, 78, 19, 69, 89}',  'C', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 有n个十进制整数进行基数排序，其中最大的整数为5位，则基数排序过程中临时建立的队数个数是（ ）。 (2分)
', 'A. 10', 'B. n', 'C. 5', 'D. 2',  'A', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 对给定的关键字序列（110，119，007，911，114，120，122）进行基数排序，则第二趟分配收集后得到的关键字序列是（ ）。 (2分)
', 'A. 007，110，119，114，911，120，122', 'B. 007，110，119，114，911，122，120', 'C. 007，110，911，114，119，120，122', 'D. 110，120，911，122，114，007，119',  'C', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 设有一组关键字序列为（345，253，674，924，627，310，56），对其采用基数排序方法递增排序，需要分配和收集（ ）趟。 (2分)
', 'A. 3', 'B. 4', 'C. 5', 'D. 6',  'A', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 以下4个线性表中，最适合采用基数排序的是（ ）。 (2分)
', 'A. 10000个实数', 'B. 1000个由字母、数字和其他字符组成的字符串', 'C. 1000个int类型的整数', 'D. 10000个100以内的正整数',  'D', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 基数排序通常适合用于（ ）。 (2分)
', 'A. 小规模数据', 'B. 负数数据集', 'C. 大量整数或字符串数据', 'D. 非均匀分布数据',  'C', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 基数排序的时间复杂度在最佳情况下为（ ）。 (2分)
', 'A. O(n)', 'B. O(nlogn)', 'C. O(d*(n + k))', 'D. O(n^2)',  'C', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 基数排序的空间复杂度为（ ）。 (2分)
', 'A. O(n)', 'B. O(logn)', 'C. O(n+k)', 'D. O(n^2)',  'C', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 基数排序在以下（ ）情况下效率更高。 (2分)
', 'A. 数据范围较小', 'B. 数据均匀分布', 'C. 数据包含负数', 'D. 数据位数较少且较多数据',  'D', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 基数排序的核心思想是通过（ ）。 (2分)
', 'A. 比较每个元素', 'B. 排序每个位数', 'C. 将数据划分成桶', 'D. 合并多个子序列',  'B', '无','0','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 基数排序与初始数据的次序无关。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 基数排序与初始数据中关键字的大小无关。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 基数排序只适用于以数字为关键字的情况，不适用以字符串为关键字的情况。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 基数排序是一种稳定的排序算法。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.6.2')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 基数排序对负数排序效果较差。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.6.2')
""")

# 8.7 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 在排序算法中，以下（ ）属于不稳定排序。 (2分)
', 'A. 冒泡排序', 'B. 插入排序', 'C. 选择排序', 'D. 归并排序',  'C', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 以下（ ）排序算法的平均时间复杂度为O(n²)。 (2分)
', 'A. 冒泡排序', 'B. 快速排序', 'C. 堆排序', 'D. 归并排序',  'A', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 以下（ ）排序算法不基于比较来进行排序。 (2分)
', 'A. 基数排序', 'B. 快速排序', 'C. 归并排序', 'D. 插入排序',  'A', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 以下（ ）排序算法在最坏情况下的时间复杂度是O(nlogn)。 (2分)
', 'A. 快速排序', 'B. 选择排序', 'C. 冒泡排序', 'D. 归并排序',  'D', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 以下（ ）排序算法通常在数组已经接近有序时效率较高。 (2分)
', 'A. 插入排序', 'B. 归并排序', 'C. 基数排序', 'D. 堆排序',  'A', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 如果不考虑空间复杂度，以下（ ）排序算法在大型数据集上效率最高。 (2分)
', 'A. 冒泡排序', 'B. 插入排序', 'C. 快速排序', 'D. 选择排序',  'C', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 以下（ ）排序算法在最坏情况下的时间复杂度为O(n^2)。 (2分)
', 'A. 快速排序', 'B. 归并排序', 'C. 堆排序', 'D. 希尔排序',  'A', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 以下（ ）排序算法的空间复杂度最高。 (2分)
', 'A. 冒泡排序', 'B. 插入排序', 'C. 归并排序', 'D. 选择排序',  'C', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 以下（ ）排序算法不适合大量数据排序。 (2分)
', 'A. 选择排序', 'B. 归并排序', 'C. 基数排序', 'D. 快速排序',  'A', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 如果数据需要频繁插入和删除，应优先选择以下（ ）排序算法。 (2分)
', 'A. 插入排序', 'B. 冒泡排序', 'C. 堆排序', 'D. 归并排序',  'A', '无','0','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 归并排序是一种稳定的排序算法。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 快速排序在最坏情况下的时间复杂度为O(nlogn)。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 基数排序是一种基于比较的排序算法。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','6' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 插入排序在数据接近有序时的效率较高。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.7')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 快速排序是一种不稳定的排序算法。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','8' ,'8.7')
""")

# 期末考试
# 9 题目
cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('1. 以下算法的时间复杂度为（ ）。<br>
void fun(int n)<br>
{int i=0;<br>
while (i<=n)<br>
i+=2;<br>
} (2分)
', 'A. O(n)', 'B. O(n^0.5)', 'C. O(nlog2(n))', 'D. O((log(n))^2)',  'A', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('2. 在一个带头结点的非空循环双链表L中删除尾结点的时间复杂度为（ ）。 (2分)
', 'A. O(n)', 'B. O(n^0.5)', 'C. O(1)', 'D. O(n^2)',  'C', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('3. 若一个栈采用数组s[0..n-1]存放其元素，初始时栈顶指针top为n，则以下元素x进栈的正确操作是（ ）。 (2分)
', 'A. top+=1; s[top]=x;', 'B. s[top]=x; top+=1', 'C. top-=1; s[top]=x;', 'D. s[top]=x; top-=1',  'C', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('4. 若用一个大小为6的数组来实现循环队列，队头指针front指向队列中队头元素的前一个位置，队尾指针rear指向队尾元素的位置。若当前rear和front的值分别为0和3，当从队列中删除一个元素，再加入两个元素后，rear和front的值分别为（ ）。 (2分)
', 'A. 1和5', 'B. 2和4', 'C. 4和2', 'D. 5和1',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('5. 假设以行序为主序存储二维数组a[1..20，1..100]，设每个数据元素占2个存储单元，基地址为10，则a[5，5]的地址是（ ）。 (2分)
', 'A. 808', 'B. 818', 'C. 1010', 'D. 1020',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('6. 若一棵二叉树的总结点数为98，只有一个孩子的结点数为48，则该树的叶子结点个数是（ ）。 (2分)
', 'A. 25', 'B. 50', 'C. 该二叉树不存在', 'D. 不确定',  'C', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('7. 下述二叉树中满足“从根结点到任意结点的路径上所经过的结点序列按其关键字有序”性质的是（ ）。 (2分)
', 'A. 二叉排序树', 'B. 哈夫曼树', 'C. B+树', 'D. 堆',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('8. 设一棵哈夫曼树中有1999个结点，该哈夫曼树用于对（ ）个字符进行编码。 (2分)
', 'A. 999', 'B. 998', 'C. 1000', 'D. 1001',  'C', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('9. 一个含有n（n>0）个顶点的连通图采用邻接矩阵存储，则该矩阵一定是（ ）。 (2分)
', 'A. 对称矩阵', 'B. 非对称矩阵', 'C. 稀疏矩阵', 'D. 稠密矩阵',  'A', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('10. 对于AOE网的关键路径，以下叙述（ ）是正确的。 (2分)
', 'A. 任何一个关键活动提前完成，则整个工程一定会提前完成', 'B. 完成整个工程的最短时间是从源点到汇点的最短路径长度', 'C. 一个AOE网的关键路径一定是唯一的', 'D. 任何一个活动持续时间的改变可能会影响关键路径的改变',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('11. 设有100个元素的有序表，用折半查找时，不成功时最大的比较次数是（ ）。 (2分)
', 'A. 25', 'B. 50', 'C. 10', 'D. 7',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('12. 在一棵m阶B树中删除一个关键字会引起合并，则该结点原有（ ）个关键字。 (2分)
', 'A. 1', 'B. m/2', 'C. m/2-1', 'D. m/2+1',  'C', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('13. 设有n个关键字具有相同的哈希函数值，则用线性探测法把这n个关键字映射到哈希表中需要做（ ）次探测。 (2分)
', 'A. n^2', 'B. n(n+1)', 'C. n(n+1)/2', 'D. n(n-1)/2',  'C', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('14. 用某种排序方法对数据序列（24，88，21，48，15，27，69，35，20）进行递增排序，元素序列的变化情况如下：<br>
①（24，88，21，48，15，27，69，35，20）<br>
②（20，15，21，24，48，27，69，35，88）<br>
③（15，20，21，24，35，27，48，69，88）<br>
④（15，20，21，24，27，35，48，69，88）<br>
则所采用的排序方法是（ ）。 (2分)
', 'A. 快速排序', 'B. 简单选择排序', 'C. 直接插入排序', 'D. 二路归并排序',  'A', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('15. 有以下4种排序方法，在排序过程中所需的关键字比较总次数与初始序列顺序无关的是（ ）。 (2分)
', 'A. 直接插入排序', 'B. 简单选择排序', 'C. 快速排序', 'D. 二路归并排序',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('16. 某算法的空间复杂度为O(1)，则（ ）。 (2分)
', 'A. 该算法执行不需要任何辅助空间', 'B. 该算法执行所需辅助空间大小与问题规模n无关', 'C. 该算法执行不需要任何空间', 'D. 该算法执行所需全部空间大小与问题规模n无关',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('17. 将两个各有n个元素的有序表归并成一个有序表，其最少的比较次数是（ ）。 (2分)
', 'A. n', 'B. 2n-1', 'C. 2n', 'D. n-1',  'A', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('18. 设线性表中有n个元素，以下运算中（ ）在单链表上实现要比在顺序表上实现效率更高。 (2分)
', 'A. 删除指定地址（位置）元素的后一个元素', 'B. 在最后一个元素的后面插入一个新元素', 'C. 顺序输出前k个元素', 'D. 交换第i个元素和第n-i+1个元素的值（i=1，2，…，n）',  'A', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('19. 以下数据结构中元素之间为非线性关系的是（ ）。 (2分)
', 'A. 栈', 'B. 队列', 'C. 线性表', 'D. 以上都不是',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('20. 若一个栈用数组data[1..n]存储，初始栈顶指针top为1，则以下元素x进栈的正确操作是（ ）。 (2分)
', 'A. top+=1; data[top]=x', 'B. data[top]=x; top+=1', 'C. top-=1; data[top]=x', 'D. data[top]=x; top-=1',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('21. 若某循环队列有队头指针front和队尾指针rear，在队不满时进队操作仅会改变（ ）。 (2分)
', 'A. front', 'B. rear', 'C. front和rear', 'D. 以上都不对',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('22. 一个链队中，由front和rear分别指向队头和队尾结点，它不具有的功能是（ ）。 (2分)
', 'A. 808', 'B. 818', 'C. 1010', 'D. 1020',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('23. 顺序表和链表相比存储密度较大，这是因为（ ）。 (2分)
', 'A. 顺序表的存储空间是预先分配的', 'B. 顺序表不需要增加指针来表示元素之间的逻辑关系', 'C. 链表中所有结点的地址是连续的', 'D. 顺序表中所有元素的存储地址是不连续的',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('24. 设树T的度为4，其中度为1、2、3、4的结点个数分别为4、2、1、1，则T中的叶子结点个数是（ ）。 (2分)
', 'A. 5', 'B. 6', 'C. 7', 'D. 8',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('25. 一棵哈夫曼树用于100个字符的编码，则其中的结点个数是（ ）。 (2分)
', 'A. 99', 'B. 100', 'C. 101', 'D. 199',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('26. 设森林F中有4棵树，第1、2、3、4棵树的结点个数分别为a、b、c、d，将森林F转换为一颗二叉树B，则二叉树B中根结点的左子树上的结点个数是（ ）。 (2分)
', 'A. a-1', 'B. a', 'C. a+b+c', 'D. b+c+d',  'A', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('27. 下列关于图的叙述中，正确的是。 (2分)<br>
I.回路是简单路径<br>
II.存储稀疏图，用邻接矩阵比邻接表更省空间<br>
III.若有向图中存在拓扑序列，则该图不存在回路
', 'A. 仅II', 'B. 仅I、II', 'C. 仅III', 'D. 仅I、III',  'C', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('28. 以下关于有向图的说法中，正确的是（ ）。 (2分)
', 'A. 强连通图中任何顶点到其他所有顶点都有边', 'B. 完全有向图一定是强连通图', 'C. 有向图中任一顶点的入度等于出度', 'D. 有向图边集的子集和顶点集的子集可构成原有向图的子图',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('29. 如果从无向图的某个顶点出发进行一次广度优先遍历即可访问所有顶点，则该图一定是（ ）。 (2分)
', 'A. 完全图', 'B. 连通图', 'C. 有回路', 'D. 一棵树',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('30. 用Dijkstra算法求一个带权有向图G中从顶点0出发的最短路径，在算法执行的某时刻，S={0，2，3，4}，下一步选取的目标顶点可能是（ ）。 (2分)
', 'A. 顶点2', 'B. 顶点3', 'C. 顶点4', 'D. 顶点7',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('31. 若用邻接矩阵存储有向图，矩阵中主对角线以下的元素均为零，则关于该图拓扑序列的结论是（ ）。 (2分)
', 'A. 存在，且唯一', 'B. 存在、且不唯一', 'C. 存在，可能不唯一', 'D. 无法确定是否存在',  'C', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('32. 哈希表中出现的哈希冲突是指（ ）。 (2分)
', 'A. 两个元素具有相同的序号', 'B. 两个元素的关键字不同，而其他属性相同', 'C. 数据元素过多', 'D. 两个元素的关键字不同，而对应的哈希函数值相同',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('33. 适合于折半查找的数据组织方式是（ ）。 (2分)
', 'A. 以链表存储的线性表', 'B. 以顺序表存储的任意线性表', 'C. 以链表存储的有序线性表', 'D. 以顺序表存储的有序线性表',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('34. 对有n个元素的排序表进行直接插入排序，在最好情况下需比较（ ）次关键字。 (2分)
', 'A. n-1', 'B. n+1', 'C. n/2', 'D. n(n-1)/2',  'A', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('35. 若数据元素序列（11，12，15，7，8，9，23，1，5）是采用下列排序方法之一得到的第二趟排序后的结果，则该排序算法只能是（ ）。 (2分)
', 'A. 冒泡排序', 'B. 直接插入排序', 'C. 简单选择排序', 'D. 二路归并排序',  'B', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2, option3, option4,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('36. 快速排序在（ ）情况下最不利于发挥其长处。 (2分)
', 'A. 排序的数据量太大', 'B. 排序的数据中含有多个相同值', 'C. 排序的数据个数为奇数', 'D. 排序的数据已基本有序',  'D', '无','0','9','9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('37. 在长度为n（n≥1）的循环双链表L中，在尾结点之后插入一个新结点的时间复杂度为O(1)。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('38. 设n个元素的进栈序列是p1、p2、p3、…、pn，其输出序列是1、2、3、…、n，若pn=1，则pi（1≤i≤n-1）的值是n-i。 (2分)
', 'A. 是', 'B. 否',  'B', '应为n-i+1','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('39. 一个循环队列中元素的排列顺序由元素进队的先后顺序确定。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('40. 将10阶对称矩阵A压缩存储到一维数组B中，则数组B的长度最少为40。 (2分)
', 'A. 是', 'B. 否',  'B', 'n阶对称矩阵压缩存储时需要存储的元素个数=n(n+1)/2，n=10时结果为55','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('41. 设目标串为s，模式串为t，在KMP模式匹配中，next[4]=2的含义是表示t4字符前面最多有2个字符和开头的2个字符相同。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('42. 由权值分别为9、2、7、5的4个叶子结点构造一棵哈夫曼树，该树的带权路径长度为37。 (2分)
', 'A. 是', 'B. 否',  'B', 'WPL=(2+5)×3+7×2+9×1=44','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('43. 对于不带权无向图的邻接矩阵来说，第i行上的非零元素个数和第i列的非零元素个数一定相等。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('44. 有一个顶点编号为0～4的带权有向图G，现用Floyd算法求任意两个顶点之间的最短路径，在算法执行的某时刻，已考虑了0～2的顶点，现考虑顶点3，则只可能修改从顶点0～2到顶点4的最短路径。 (2分)
', 'A. 是', 'B. 否',  'B', '无','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('45. 若一个有向图中的顶点不能排成一个拓扑序列，则可断定该有向图含有顶点数目大于1的强连通分量。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('46. 对含有n个元素的顺序表采用顺序查找方法，不成功时的比较次数是n-1。 (2分)
', 'A. 是', 'B. 否',  'B', '应为n','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('47. 含有20个结点的AVL树的最大高度是7。 (2分)
', 'A. 是', 'B. 否',  'B', '设Nh表示高度为h的平衡二叉树中含有的最少结点数，有N1=1，N2=2，Nh=Nh-1+Nh-2+1，求出N6=20','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('48. 在一棵m阶B树中插入一个关键字会引起分裂，则该结点原有m个关键字。 (2分)
', 'A. 是', 'B. 否',  'B', '在一棵m阶B树中每个内部结点的关键字个数为m/2-1～m-1，插入一个关键字会引起分裂，则该结点中关键字个数一定是最多的情况','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('49. 哈希表的装填因子等于表中填入的元素个数除以哈希表的长度。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','9' ,'9')
""")

cursor.execute("""
INSERT INTO exam (question, option1, option2,correct_answer, answer_analy,question_type, chapter,subchapter)
VALUES ('50. 某程序需要从10000个无序的整数中找出前10个最小的整数，最好采用冒泡排序。 (2分)
', 'A. 是', 'B. 否',  'A', '无','1','9' ,'9')
""")

# 查询数据
cursor.execute("SELECT * FROM exam")
print(cursor.fetchall())
#   根据chapter 和 subchapter 查询数据
# 清空表
# cursor.execute("DELETE FROM exam")
#   执行后提交事务
conn.commit()
# 关闭Cursor和Connection
cursor.close()
conn.close()
