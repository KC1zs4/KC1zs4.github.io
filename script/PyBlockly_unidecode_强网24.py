import unidecode

"""代码逻辑

1. 转换和打印字符串：
    unidecode.unidecode("Κνωσός") 将希腊语字符串 "Κνωσός" 转换为 ASCII 字符串 "Knosos" 并打印。

2. 查找目标字符：
    遍历 unidecode 库中的数据文件，每个文件名格式为 unidecode.xXXX，其中 XXX 是从 000 到 1F0 的十六进制值。
    对于每个文件，检查目标字符 ( 是否存在于文件的数据中。
    如果找到目标字符，打印相关的信息并计算其 Unicode 编码

"""

print(unidecode.unidecode("Κνωσός"))
target = "("
for section in range(0x000, 0x1f1):
    try:
        mod = __import__('unidecode.x%03x'%(section), globals(), locals(),
        ['data'])
        if target in mod.data:
            print(mod.data)
            print(section)
            print(mod.data.index(target))
            print(chr((section << 8) + mod.data.index(target)))
            break
    except ImportError:
        pass