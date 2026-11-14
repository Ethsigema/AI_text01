# 紫外成长增量恢复

本增量依赖固定提交5a1cd70bc1f818d5abde913d6482fb6573a15401的船难海盗增量及它的完整依赖链。不是独立全量包。旧备份全部保留，无删除或强推。未知中断线程未上传内容不在本范围。

1. 下载本包全部文件，包括6个FULL_MANIFEST分卷，校验SHA256SUMS.txt。
2. 按DEPENDENCIES.json下载78个固定版本依赖，保留filename指定路径，逐个核对size与SHA256。可运行 `python3 download_inputs.py --destination /绝对路径/新的inputs`。
3. 运行 `python3 restore.py --inputs /绝对路径/inputs --workspace /绝对路径/全新目录`。
4. 恢复器先从原始基包恢复完整前序链、旧源码台账及船难海盗增量，核验28,011文件基线全量SHA256，再应用本次新增、修改和移除清单；最后逐文件重读比对全部路径、大小、SHA256。工程入口为workspace/project/project.godot，结果为workspace/RESULT.json。

运行要求：Godot4.6.3，Linuxheadless已定向测试；Python3.12+用于恢复。可重建的.godot缓存不备份，首次打开可重新生成。凭据、私聊、无关文件不纳入。

本包生成并不等于远端核验通过。应在上传后重新实际下载本包与78个依赖，以新目录重建或逐文件重建核验全部字节再发布成功回执。完整恢复也不等于游戏全功能验收。测试和规则来源限制详见TEST_REPORT.md。
