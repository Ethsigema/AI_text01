# 极紫外实例成长显示增量恢复

本包依赖固定提交3628b54a0ca04a2b56f5916ca9d4a565ae9f3be7的紫外成长增量及此前完整链，不是独立全量包。所有旧备份保留，未知中断线程未上传成果不在本范围。

1. 下载本包全部16文件，保留6个FULL_MANIFEST分卷，核对SHA256SUMS.txt。MANIFEST.json内remote_verified=false为冻结打包时状态，上传后实际结果由单独核验回执记录，不改写本包。
2. 运行 `python3 download_inputs.py --destination /绝对路径/全新inputs` 下载DEPENDENCIES.json全部93个固定版本依赖并逐个验证SHA256；不可省略任一分卷。
3. 运行 `python3 restore.py --inputs /绝对路径/inputs --workspace /绝对路径/全新workspace`。禁止使用已有目录。
4. 恢复顺序为原始Release→batch14基线→累计源码→六文件台账→船难增量→紫外成长→本显示增量。递归恢复器逐阶段验证完整文件集合；本包先核对28,024文件前序全量清单，再应用新增/修改/移除，最后验证28,029文件所有路径、大小和SHA256。
5. 工程入口 `workspace/project/project.godot`；恢复回执 `workspace/RESULT.json`。要求Python3.12+、Godot4.6.3；定向测试环境Linux headless，可重建.godot缓存不在包内。

本期新增5、修改3、移除0，core字节未改。不应把新建恢复目录或79项定向测试当成完整游戏、完整卡牌、像素布局或原生窗口交互验收。已知退出资源泄漏及其余限制见TEST_REPORT.md。凭据、私聊、缓存和无关文件排除；不删除、轮换旧备份，不强推。
