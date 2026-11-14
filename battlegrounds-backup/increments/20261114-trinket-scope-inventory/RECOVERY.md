# 饰品范围研究增量恢复
基线94800ef59fba786027d49290c92163d4ac5f0c1c，回执ea707b2b9030fbd2ebd7c7784d61e182e7225ce2。不是独立全量包。
Python3.12+，Godot4.6.3，恢复验证环境Linux。
下载本目录全部文件，sha256sum -c SHA256SUMS.txt。运行 python download_inputs.py --destination /不存在的目录/inputs 下载125件固定依赖。再运行 python restore.py --inputs /绝对路径/inputs --workspace /不存在的新目录。
顺序：原Release→batch14→累积源码→6文件台账overlay→船难→极紫外成长→极紫外显示→空气投球手成长→本次5个research文件。
所有固定URL/大小/SHA在DEPENDENCIES.json；MANIFEST.json列出新增修改移除和全量清单分卷顺序。restore.py重新解包完整链，不覆盖既有工程，逐文件比较全量大小和SHA，project/project.godot为入口。
263只是候选，不是完成数/分母。旧备份全部保留，未知未上传工作未捕获。
