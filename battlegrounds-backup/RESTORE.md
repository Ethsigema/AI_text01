# Godot 酒馆战棋恢复与备份

这是工程备份分支，不是发布版。旧主分支及安装包不修改。每个 snapshots/<UTC时间>/ 目录是一个独立可恢复版本。

## 组成

1. 原始完整交接包：
   https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
2. 原包 SHA256：`33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65`
3. 某次快照的 `manifest.json`：恢复后完整工程逐文件大小与 SHA256。
4. 同一快照 `payload/`：相比原始交接包新增或变化的全部文件。未变素材/数据/运行证据直接从原包恢复，不重复存放。
5. `tools/snapshot.py`：仅使用 Python 标准库的构建与恢复工具。

**不能只下载 payload 当成完整游戏。必须保留原包和对应快照。** 恢复仅使用快照清单所列文件，因此原包中已被该版本移除的文件不会复活。排除 Godot 导入缓存、Git 元数据与 Python 缓存；不排除游戏运行所需 research 证明文件、源脚本文本和素材。

## 恢复

下载并保留原始 ZIP、下载本备份分支或某个固定提交，选择一个具体快照。将下面路径替换为实际位置：

```sh
python3 battlegrounds-backup/tools/snapshot.py restore \
  --base-zip /path/battlegrounds_new_scope_handoff_20261101.zip \
  --snapshot battlegrounds-backup/snapshots/YYYYMMDDTHHMMSSZ \
  --destination /path/new-empty-game-folder
```

目标目录必须尚不存在；工具不覆盖已有工程。工具会校验原包 SHA256、拒绝路径穿越/符号链接，并核对恢复后全部文件的大小与 SHA256。成功输出 `verified_files` 才表示该快照的文件恢复校验通过；这不等于游戏功能测试通过。

在 Godot 4.6.3 中导入恢复目录的 `游戏工程/project.godot`。具体实现和测试状态以该快照的 PROGRESS、进度台账及原始测试日志为准。2026-11-02 的历史 153/433 记录不能移植成重建代码的验收结论。

## 后续快照

停止对工程的写入后运行 build，成功后可立即恢复开发。构建工具会比较前后完整源清单；若源文件变化则报错，该不完整快照不得提交。

```sh
python3 battlegrounds-backup/tools/snapshot.py build \
  --root /path/酒馆战棋_新范围半成品交接包_20261101 \
  --base-zip /path/battlegrounds_new_scope_handoff_20261101.zip \
  --output battlegrounds-backup/snapshots/YYYYMMDDTHHMMSSZ \
  --created-utc YYYY-MM-DDTHH:MM:SSZ
```

提交前对新增 payload 做敏感信息检查，再在新的独立目录执行 restore。推送仅使用快进提交，不强推；保留历史快照。推送后以远端提交号和重新读取的 manifest/payload 哈希核验备份，而不是只检查本地文件。

## Godot 导入缓存

备份保留原始素材、源脚本、`.import` 元数据与运行证明文件；不保存可重建的 `.godot` 导入缓存。恢复后首次启动前需要用 Godot 4.6.3 重新导入资源。以下命令已在本恢复工程完成 3950 项资源导入，退出码 0，完整导入日志没有错误：

```sh
PROJECT='/path/new-empty-game-folder/游戏工程'
export HOME='/path/writable-home'
export XDG_CONFIG_HOME='/path/writable-config'
export XDG_DATA_HOME='/path/writable-data'
export XDG_CACHE_HOME='/path/writable-cache'
mkdir -p "$HOME" "$XDG_CONFIG_HOME" "$XDG_DATA_HOME" "$XDG_CACHE_HOME"
godot --headless --editor --path "$PROJECT" --import
```

也可在 Godot 项目管理器导入 `project.godot`，等待资源导入完成。资源导入成功不代表任意玩法组合验收通过。对当前 runtime 来源还可执行 `python3 "$PROJECT/tests/verify_recovery_source_integrity.py" --root "$PROJECT"`；这是辅助源码/证明完整性检查，不替代本备份全部文件校验，也不运行玩法。

## 低磁盘空间校验（后续切片）

后续切片可能使用 `stream_snapshot.py` 直接压缩捕获，并流式重建每个文件的字节来校验：新增/变化文件取自归档，未变文件取自固定SHA256的原始Release。完整清单决定最终文件集，不会复活已移除文件。此校验不创建新的完整目录，也不启动游戏；回执会明确标记 `streamed`，不可当作实际解包或可运行验收。正常恢复仍可用上面的安全解包和 `snapshot.py restore`。

`stream_snapshot.py verify --help` 显示所需原包、归档SHA、切片时间、运行清单相对路径和SHA参数。工具严格核验XZ结束、TAR结束和路径、全部文件大小/SHA、运行文件集。捕获时私密字符串扫描仅覆盖新增/变化文件，未变文件使用此前已公开的固定原包。
