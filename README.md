# Student Portfolio Site Skill

为正在求职或寻找实习的大学生创建、优化、导出或发布个人作品集网站。它强调真实材料、个人辨识度、隐私边界、可访问性与可验证的项目表达，不预设专业、视觉风格或技术栈。

## 安装到 WorkBuddy

### WorkBuddy 桌面端（推荐）

1. 下载 [v1.0.0 安装包](https://github.com/singerliu226/student-portfolio-site/releases/download/v1.0.0/student-portfolio-site-workbuddy-skill.zip)。
2. 在 WorkBuddy 打开「专家 → Skills → Connectors → Skills → 添加 Skill」。
3. 上传原始 ZIP，不要解压或重新打包。

安装包的根目录直接包含 `SKILL.md`，不需要连接器、密钥或联网权限。

### 支持 `gh skill` 的兼容宿主

```bash
gh skill install singerliu226/student-portfolio-site skills/student-portfolio-site --dir ~/.workbuddy/skills --pin v1.0.0
```

`gh skill` 仍处于预览阶段；请仅在宿主明确支持该命令时使用。WorkBuddy 桌面端请使用上方 ZIP 导入方式。

## 使用

```text
使用 $student-portfolio-site 为我的秋招方向创建或优化个人作品集网站。
```

## 内容与隐私

- 以用户提供的简历、项目材料和已确认事实为准，不虚构角色、数据、成果或链接。
- 默认不公开未经授权的联系方式、未发布项目、雇主机密和私人链接。
- 仅提供流程指导，不包含脚本、外部 API、连接器或自动发布行为。

## 版本

当前版本：`v1.0.0`

本仓库暂未附加开源许可证；使用、分发或二次改造前请联系维护者取得授权。
