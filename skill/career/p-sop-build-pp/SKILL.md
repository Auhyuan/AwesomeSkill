---
name: p-sop-build-pp
description: 根据项目现有需求、设计、任务与验证资料，独立生成或更新可离线查看的项目进度看板。用于仅查看项目进度、梳理部分/模块/功能、展示当前工作与证据入口；兼容任意文档格式，无需先接入 P-SOP，支持部分与模块折叠。
---

# 项目进度看板

这是 P-SOP 内置看板能力的独立快捷入口，可单独安装和使用，无需安装 P-SOP。

生成或更新页面时，读取本目录的 [看板规则](references/dashboard-generation.md)，按其中引用的 [HTML 模板](assets/dashboard-template.html) 理解现有项目资料并填写页面。默认覆盖更新 `psop/PROJECT-DASHBOARD.html`。

只执行看板展示任务，不启动项目接入、状态初始化或开发门禁；资料格式不固定，缺失信息明确标注，不改写来源文档。
