# EJU 预览站

这个仓库只用来放四个 EJU 课程站的 **PR 预览**，由各课程仓库的 GitHub Actions 推送到 `<科目>/pr-<编号>/`。

- 预览地址：<https://feather0000.github.io/eju-preview/>
- 正式站：<https://eju.feather0.com/>（物理）、<https://chemistry.eju.feather0.com/>、<https://biology.eju.feather0.com/>、<https://math.eju.feather0.com/>

请不要在这个仓库里加入 `CNAME`，也不要绑定自定义域名。正式站仍然由原来的四个仓库各自的 GitHub Pages 发布。

预览页带「测试版」横幅、`noindex`，并且 `robots.txt` 禁止收录。PR 关闭后，对应目录会自动删掉。
