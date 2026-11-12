# 恢复此未验收开发快照

需要Python 3.12或更新、Godot 4.6.3；源工程约1.55GB。此包是原始基包＋第14批合并增量上的累积增量，不是独立全量。

1. 按DEPENDENCIES.json固定链接下载原始Release ZIP（324,041,102字节）以及全部base_package文件；逐个核对大小与SHA256。
2. 在base_package目录运行：python3 restore.py --base-zip ../original_release.zip --destination ../restored_base --report ../BASE_RESTORE.json。目标目录不得存在。
3. 在本包目录核对SHA256SUMS.txt，然后运行：python3 restore_increment.py --base-tree ../restored_base --base-map ../base_package/SOURCE_MAP.json.gz --destination ../restored_noon_snapshot --report ../SNAPSHOT_RESTORE.json。
4. 恢复器按MANIFEST的移除清单及变化内容构建最终集合，再逐文件从磁盘读取大小和SHA256；完整目标清单另附SOURCE_MAP.json.gz。不要将delta单独解压当工程，不需要叠加旧碎地者、骑手或暗潮候选。

此快照没有游戏功能验收，也不推广默认工程。原不可见工作树及未知修改不在此范围。旧备份必须全部保留。远端恢复结果将另附，只有本地包不表示上传成功。
