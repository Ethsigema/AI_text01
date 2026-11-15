# 13点研究部分成果增量恢复
不是独立全量包。完整已发布基线c256a6300c1aacc3155cd5fa9b4742fbd8110060，回执ce1b0ebeaca98ca3f002d3b65c0f307eea5b9ea1。
Python3.12+、Godot4.6.3，Linux恢复。下载本目录所有文件并sha256sum -c SHA256SUMS.txt。
python download_inputs.py --destination /不存在的新inputs目录 下载DEPENDENCIES.json中153件固定URL/大小/SHA依赖。
python restore.py --inputs /绝对路径/inputs --workspace /不存在的新恢复目录。
原Release→batch14→累积源码→6文件台账overlay→船难→极紫外成长→极紫外显示→空气投球手成长→饰品候选→饰品REVIEW→本次四文件研究。
MANIFEST.json列出新增修改移除及全量清单分卷顺序。restore.py解包完整已发布链再应用本包，逐文件核对大小SHA；project/project.godot为入口。
重要缺口：两项后续独立测试weapons_forge及weighted_gauntlet未获取，不在本包或本次全量清单中。恢复已捕获工程不等于所有最新工作均已捕获，也不等于游戏功能验收。旧备份全部保留。
