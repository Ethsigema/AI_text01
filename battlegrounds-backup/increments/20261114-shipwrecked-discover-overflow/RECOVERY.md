# 机智的船难海盗满手发现增量恢复

本包是已发布恢复工程＋六文件台账 overlay 之上的源码增量，不是独立游戏，不代表所有功能已验收。基线源码提交 32a8b33abe2bfb980c5ec890e7950f6b5a9f1346，台账 f2296d9db1209f4b8c0068fb2edb51f5f7df2f0b；原始基包、batch14 与累积源码的固定链接及逐包 SHA256 全部列于 DEPENDENCIES.json。源目录没有捕获旧中断线程未知未上传成果，不能保证未知内容已备份。

## 恢复顺序
1. 下载本目录所有文件（全部 FULL_MANIFEST.json.gz.part 分卷不可缺少），校验 SHA256SUMS.txt。
2. 按 DEPENDENCIES.json 原样下载每个 URL，保存到 inputs/ 下指定 filename。不得替换成最新版分支 URL，所有依赖均固定提交或原始 Release 固定 SHA256。
   可运行：python3 download_inputs.py --destination /绝对路径/不存在的inputs
3. 使用 Python 3.12+ 执行：
   python3 restore.py --inputs /绝对路径/inputs --workspace /绝对路径/新的不存在目录
4. 恢复器逐包核验后，从原始 ZIP 新建 batch14，再应用累积源码、台账 overlay、本次增量；移除列表按 MANIFEST.json 精确应用。最后重新读取目标工程每个文件，对比完整路径集合、大小与 SHA256。成功结果位于 workspace/RESULT.json，游戏入口为 workspace/project/project.godot。

Godot 4.6.3；定向测试在 Linux headless 执行。首次打开游戏可重建 .godot 缓存，缓存不是源码。全量清单涵盖本次开发树所有应备份文件，排除 .godot、__pycache__、.git。没有删除任何旧备份、依赖或未知成果，不强推。

本次 TEST_REPORT.md 说明实际规则改动与定向测试。恢复完整性通过不等于默认卡池、所有组合、完整对局、GUI 或旧存档验收。发布后重新下载与全链恢复回执另行发布；在该回执成功前不能声称远端核验成功。
