#!/bin/env python
# -*- coding: utf-8 -*-

""" 迁移 memcache 中的数据.

迁移方法:
1. 在源主机用 stats items 拿到每个 slab 的 key 的数量;
2. 用 stats cachedump slab号 最大key 数量, 把每个 slab 的
   key 都拿到; 
3. 对于每一个 key, 从源主机取出来, set 到新主机.

有三个问题:
1. 如果 key 特别多, 有风险;
2. 如果 value 是二进制, 从源主机 get key 会报反序列化的错;
3. 目前我还没找从源主机 get key 时 key 的剩余存活时间, 所以只能自定义一个值了.

所以我觉得还没找到一种合理迁移 memcache 数据的方法.

参考:
    http://stackoverflow.com/questions/19560150/get-all-keys-set-in-memcached

"""


import memcache


origin_host = "cache5.hy01"
new_host = "apps-memcached0-bgp0.hy01"
port = 11211

origin_mc = memcache.Client(['%s:%s' % (origin_host, port) ], debug=0)
new_mc = memcache.Client(['%s:%s' % (new_host, port) ], debug=0)


def stats_items():
    slab_number = list()
    data = origin_mc.get_stats(" items")[0][1]
    for i in data:
        if ":number" in i:
            _dict = {
                "slab" : i.split(":")[1],
                "number" : data[i]
            }
            slab_number.append(_dict)
            print _dict

    return slab_number


def stats_cachedump(slab, number):
    return origin_mc.get_stats(" cachedump %s %s" % (slab, number))[0][1].keys()


def main():
    for i in stats_items():
        slab = i["slab"]
        number = i["number"]
        keys = stats_cachedump(slab, number)
        for i in keys:
            _value = origin_mc.get(i)
            new_mc.set(i, _value, 3600)   # 自定义过期时间.


if __name__ == "__main__":
    main()
