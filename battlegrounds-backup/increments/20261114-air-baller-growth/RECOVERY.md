# 空气投篮手成长增量恢复
本包不是独立全量包。基线固定8150b6e0be811636cfd3b8f29be3479aed595264，完整依赖的固定URL、大小、SHA256均在DEPENDENCIES.json。
Python 3.12+；Godot 4.6.3；本次恢复环境Linux。
下载本目录全部文件，sha256sum -c SHA256SUMS.txt。用python download_inputs.py --help查看参数，再下载109项依赖；python restore.py --inputs /绝对路径/inputs --workspace /不存在的新目录。
顺序：原Release→batch14→累积源码→6文件台账overlay→船难→极紫外成长→极紫外显示→本增量。
restore.py验证全部依赖和本包SHA，逐级新建工程，应用新增修改和移除，再逐文件核全量清单。全量清单压缩分卷按MANIFEST.json顺序拼接后gzip解压。
游戏运行入口新目录/project/project.godot。恢复通过不等于全游戏功能验收；本批113项定向测试不算整卡完成。保留全部旧备份、失败测试与限制说明。仅捕获指定冻结开发目录，不保证未知未上传工作。
