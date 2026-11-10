# 恢复本次组合依赖审查包

从固定GitHub提交下载MANIFEST.json、SHA256SUMS.txt、verify_package.py和.part000至.part005六份分片。按编号拼接后应为1,384,084字节，SHA256 d684f9e5bde5193f95e8fecb242a7d49cc17adb7f796dc380c81d91b89174e40。

可用可信Python 3执行 python3 verify_package.py <下载目录> --write-archive --report verification.json。脚本只读取分片，在内存验证130项成员及内外哈希白名单，再写入不存在的新归档；不覆盖已有归档，不联网、不下载依赖、不执行包内代码、不运行回归或Game。

核验后仅在新的独立目录解包查看，不覆盖现有游戏树或安装候选。包内回归/图分析脚本有各自来源依赖，备份校验器不会自动调用它们。

843文件preload闭包和2070源码范围仅静态审查，完整模块、Game和旧存档未验收。候选仍未安装、345缺口不变，不能承诺旧存档指纹兼容。本包不是完整游戏备份。旧依赖未复核，已取消的第14批依赖下载不属于本任务。
