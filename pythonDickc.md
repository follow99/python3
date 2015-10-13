python 字典操作详解(创建,访问,删除)

python的列表只能是以索引数字开头并且顺序递增的序列。字典则可以是以字母为key的序列。

字典内置方法
<ul>
<li>dict.clear()	删除字典中所有元素</li>
<li>dict.copy()	返回字典(浅复制)的一个副本</li>
<li>dict.fromkeysc(seq,val=None)	创建并返回一个新字典，以seq 中的元素做该字典的键，val 做该字典中所有键对应的初始值(如果不提供此值，则默认为None)</li>
<li>dict.get(key,default=None)	对字典dict 中的键key,返回它对应的值value，如果字典中不存在此键，则返回default 的值(注意，参数default 的默认值为None)</li>
<li>dict.has_key(key)	如果键(key)在字典中存在，返回True，否则返回False. 在Python2.2版本引入in 和not in 后，此方法几乎已废弃不用了，但仍提供一个 可工作的接口。</li>
<li>dict.items()	返回一个包含字典中(键, 值)对元组的列表</li>
<li>dict.keys()	返回一个包含字典中键的列表</li>
<li>dict.values()	返回一个包含字典中所有值的列表</li>
<li>dict.iter()	方法iteritems(), iterkeys(), itervalues()与它们对应的非迭代方法一样，不同的是它们返回一个迭代子，而不是一个列表。</li>
<li>dict.pop(key[, default])	和方法get()相似，如果字典中key 键存在，删除并返回dict[key]，如果key 键不存在，且没有给出default 的值，引发KeyError 异常。
<li>dict.setdefault(key,default=None)	和方法set()相似，如果字典中不存在key 键，由dict[key]=default 为它赋值。</li>
</ul>