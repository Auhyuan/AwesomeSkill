# AwesomeSkill

面向软件开发与职业成长的 AI Agent Skill 集合，帮助开发者评估项目价值、分析和交付需求，以及维护可接续的项目开发流程。

当前仓库收录 4 个 Skill，均位于 `skill/career/`。每个 Skill 以 `SKILL.md` 为入口，按需配套参考文档、模板及 Agent 界面配置。使用说明默认面向中文交流场景。

## Skill 索引

| Skill | 适用场景 | 主要能力 | 入口 |
| --- | --- | --- | --- |
| `project-evaluation` | 判断项目是否值得学习、参与、维护，或作为简历与面试素材 | 基于项目证据评估学习价值、求职相关性、技术深度与广度、业务价值和成长机会 | [项目价值评估](skill/career/project-evaluation/SKILL.md) |
| `requirement-helper` | 分析新需求、增强功能、修复缺陷、制定实现方案或审查改动 | 先只读分析价值、方案与风险，再按授权进入手动指导或自动实现，并验证结果 | [需求分析与交付助手](skill/career/requirement-helper/SKILL.md) |
| `p-sop` | 新项目启动、已有项目接入、日常接续与中断恢复 | 按需求、设计、任务、开发、验证与验收推进，维护当前状态和精简资料，按需生成进度页面 | [P-SOP 项目开发规范](skill/career/P-SOP/SKILL.md) |
| `p-sop-build-pp` | 独立生成或更新项目进度看板 | 读取现有资料，展示实际进度、可折叠的部分/模块/功能与高亮文件路径，无需接入完整 SOP | [项目进度看板](skill/career/p-sop-build-pp/SKILL.md) |

> `P-SOP` 是仓库目录名，`p-sop` 是该 Skill 在 `SKILL.md` 中声明的名称。

## 如何选择

- 想知道“这个项目值得投入吗、能学到什么、对求职有什么帮助”，使用 `project-evaluation`。
- 已有具体需求，想判断“要不要做、怎么做、怎么验证”，使用 `requirement-helper`。
- 希望知道“项目做到哪了、接下来做什么、如何接续或交接”，使用 `p-sop`。
- 只希望“用现有资料生成或更新进度看板”，使用 `p-sop-build-pp`。

这些能力可以独立使用，也可以配合：先评估项目，再由 P-SOP 管理项目流程，在具体需求上使用 requirement-helper 分析与交付。P-SOP 提供流程骨架，专项 Skill 负责对应的分析和实施工作。P-SOP 与独立看板共用一份维护源码，发布时各自携带完整的看板规则与模板。

## 快速开始

### 1. 获取仓库

```bash
git clone https://github.com/Auhyuan/AwesomeSkill.git
cd AwesomeSkill
```

### 2. 选择并加载 Skill

打开上方索引中的 `SKILL.md`，确认其适用场景和执行规则。若所用 Agent 支持安装 Skill，按该工具的约定放置所选 Skill 的完整目录；保留 `references/`、`assets/` 和 `agents/` 等已有配套文件，保证相对引用可用。

P-SOP 与看板推荐使用下方生成的完整安装包：解压 `p-sop-skill.zip` 后安装其中的 `p-sop/`，或解压 `p-sop-build-pp-skill.zip` 后安装其中的 `p-sop-build-pp/`。只安装 P-SOP 即可使用完整流程和看板；只安装看板即可独立生成页面，无需 P-SOP。两个包均不要求另一个 Skill 存在。

仓库中的 `P-SOP/` 是维护源码目录，看板资料在打包时从唯一源码带入；完整安装 P-SOP 使用安装包。独立看板源码目录本身已完整，也可直接安装。仓库内容更新不会自动更新已复制到个人 Skill 目录的旧版本。

也可以直接让 Agent 阅读仓库中的 Skill 文件，并按其中规则处理任务。例如，在本仓库中：

```text
请阅读 skill/career/project-evaluation/SKILL.md，
按其中规则评估我指定项目的学习价值与求职价值。
我的目标岗位是 Java 后端，参与方式是负责一个业务模块。
```

评估其他项目时，提供目标项目路径或资料入口，并确保 Agent 能访问相应内容。

### 3. 描述目标与执行范围

若 Skill 已被所用工具识别，可按其名称调用。以下是可参考的提示词：

**项目价值评估**

```text
使用 $project-evaluation 评估当前项目。
我希望提升后端开发能力，并积累可用于简历与面试的项目经历。
请基于仓库事实给出评分、证据置信度、成长机会和建议投入路线。
```

**需求分析与手动指导**

```text
使用 $requirement-helper 分析这个需求：为订单列表增加状态筛选。
先只读检查项目，给出验收条件、实现方案和风险。
分析后采用 Manual 模式，由我写代码，你逐步指导并检查结果。
```

**需求分析与自动实现**

```text
使用 $requirement-helper 处理这个需求：为订单列表增加状态筛选。
先完成只读分析，再采用 Automatic 模式。
我授权你修改该需求范围内的代码并执行适用验证。
```

**已有项目接入与流程维护**

```text
使用 $p-sop 将当前已有项目接入开发流程管理。
本次只读核对当前范围，并建立必要的状态与资料入口，不修改业务代码。
请复用已有需求、设计和任务文档，说明当前进度、验证缺口及下一步。
```

**独立构建项目进度看板**

```text
使用 $p-sop-build-pp 根据当前项目的 PRD、技术方案和任务记录，
生成或更新 psop/PROJECT-DASHBOARD.html。
只更新看板，展示已知进度、可折叠模块、验证缺口与高亮文件路径。
```

### 4. 构建完整安装包与插件包

从仓库根目录运行：

```bash
python3 skill/career/P-SOP/scripts/package_plugin.py
```

默认生成以下文件：

| 文件 | 包内入口 | 安装后可用能力 |
| --- | --- | --- |
| `tmp/p-sop-skill.zip` | `p-sop/SKILL.md` | 完整 P-SOP，包括内置看板能力 |
| `tmp/p-sop-build-pp-skill.zip` | `p-sop-build-pp/SKILL.md` | 独立看板，无需安装 P-SOP |
| `tmp/p-sop.zip` | 插件清单与 `skills/` | 在同一个插件中提供主流程与独立看板两个入口 |

只需要两份 Skill 安装包时使用 `--format skills`；只需要插件时使用 `--format plugin`。原有 `--output tmp/其他名称.zip` 可指定插件路径，独立 Skill ZIP 写到同一目录；输出仅允许位于仓库根目录 `tmp/`。

看板规则的唯一维护入口为 `skill/career/p-sop-build-pp/SKILL.md`，模板为其中的 `assets/dashboard-template.html`。打包工具将规则正文和模板带入 P-SOP 的 `references/dashboard-generation.md` 与 `assets/dashboard-template.html`，调整本包内引用；独立看板包携带原规则和模板。两个包解压后均可独立迁移，引用不会越出各自 Skill 目录。插件中的两个 Skill 同样各自完整。

脚本只封装维护源码，不读取业务项目、不解析文档、不生成看板，也不修改已安装的 Skill 或插件配置。生成目录中的规则和模板随源码重新打包更新，不作为第二份维护源码；打包物可随时删除或重新生成。

若选择插件安装，将 `p-sop.zip` 解压为插件目录，按所用 Agent 的插件来源登记、安装与启用流程加载；随后选择 `p-sop` 下的 `build-pp` 看板能力。支持命名空间斜杠入口的宿主可使用 `/p-sop:build-pp`；具体可见名称以安装后的菜单为准，打包成功不代表已安装或命令已注册。普通 Skill 安装分别使用 `$p-sop` 与 `$p-sop-build-pp`。可参考 [官方插件封装说明](https://developers.openai.com/plugins/build/plugins) 与 [技能调用说明](https://learn.chatgpt.com/docs/reference/slash-commands)。

该包不依赖 MCP、后台服务或自定义文件打开协议。已安装旧版主 Skill 时，选择一种安装方式，避免同时加载旧版、独立版和插件版造成入口或规则混淆。

## 各 Skill 的工作方式

### project-evaluation：基于证据判断项目价值

从目标岗位、个人阶段和实际参与方式出发，检查项目结构、代表性业务链路、工程质量与可承担的工作，按 1～5 分评估各维度，并给出证据置信度。

输出包括项目结论、评分依据、可学习内容、求职素材、成长机会和建议投入路线。只有项目描述、缺少仓库证据时，给出初步评估并说明缺失信息。

### requirement-helper：先分析，再按授权交付

采用 `Advisory → Delivery → Verification` 三阶段，并按需求复杂度选择 Light、Standard 或 Deep 分析深度。

- **Advisory**：只读检查上下文，明确目标、验收条件、价值、方案与风险。
- **Manual**：用户编写代码，Agent 提供逐步指导、结果检查与验证建议。
- **Automatic**：获得当前需求的明确修改授权后，Agent 在约定范围内实现与验证。
- **Review**：只读审查方案、补丁、差异或 PR，给出可执行的反馈。

详细规则见 [手动交付](skill/career/requirement-helper/references/manual-delivery.md)、[自动交付](skill/career/requirement-helper/references/automatic-delivery.md)、[审查协议](skill/career/requirement-helper/references/review-protocol.md) 与 [价值评估标准](skill/career/requirement-helper/references/value-rubric.md)。

### P-SOP：让项目状态与交付依据随时可读

支持 `NEW`、`ADOPT`、`CONTINUE`、`RESUME` 四种进入方式，分别对应新项目、已有项目接入、日常继续和中断恢复。

使用少量持续维护的文档记录当前目标、需求与验收条件、技术方案、任务、检查结果和剩余事项。默认以 `PROJECT-STATE.md` 保存当前快照，以 `psop/REQ`、`psop/DEV`、`psop/DEV/DATA`、`psop/OPS` 按需组织资料；已有项目可复用原来的文件名称、位置与格式。

用户需要进度页面时，使用安装包内置的看板规则与模板，生成自包含、可离线查看的 `psop/PROJECT-DASHBOARD.html`，无需额外安装独立看板 Skill。该页面展示当前项目事实、证据入口与状态，支持部分和模块折叠。本地文件使用可复制的高亮路径，页面内导航及已核对的网页来源可以保留链接。

详细规则见 [接入与恢复](skill/career/P-SOP/references/adoption-recovery.md)、[流程与门禁](skill/career/P-SOP/references/workflow.md)、[产物与维护](skill/career/P-SOP/references/artifacts.md) 和 [独立看板 Skill](skill/career/p-sop-build-pp/SKILL.md)。

### p-sop-build-pp：只从现有资料构建看板

不要求 `PROJECT-STATE.md`、固定 PRD / TECH / TASK 格式或先完成 SOP 接入。Agent 按模板理解和提炼资料，保留来源、范围与不确定性；信息缺失时展示缺口，不编造完成比例或检查结果。只生成或更新约定的 HTML，不创建配套状态、索引或中间数据文件，也不自动修改需求、任务和项目状态。

## 仓库结构

```text
AwesomeSkill/
├── README.md
└── skill/
    └── career/
        ├── project-evaluation/
        │   └── SKILL.md
        ├── requirement-helper/
        │   ├── SKILL.md
        │   ├── agents/openai.yaml
        │   └── references/
        │       ├── automatic-delivery.md
        │       ├── manual-delivery.md
        │       ├── review-protocol.md
        │       └── value-rubric.md
        ├── P-SOP/
        │   ├── SKILL.md
        │   ├── agents/openai.yaml
        │   ├── scripts/package_plugin.py
        │   ├── assets/
        │   │   ├── development-flow.drawio
        │   │   └── project-state-template.md
        │   └── references/
        │       ├── adoption-recovery.md
        │       ├── artifacts.md
        │       └── workflow.md
        └── p-sop-build-pp/
            ├── SKILL.md
            ├── agents/openai.yaml
            └── assets/dashboard-template.html
```

- `SKILL.md`：声明名称、适用场景、工作流程和执行边界。
- `references/`：按具体任务加载的详细规则与参考说明。
- `assets/`：可复用模板与流程图。
- `agents/openai.yaml`：Agent 界面配置，包含显示名称、简短说明与默认提示词。
- `scripts/package_plugin.py`：两份完整 Skill 安装包及可选插件的发行封装；生成的 ZIP 位于仓库根目录 `tmp/`，不作为第二份维护源码。

## 使用原则

- **事实与证据优先**：结论应能追溯到项目资料或实际检查，缺失信息明确标为未知。
- **授权与范围明确**：只读分析和审查保持只读；代码修改、Git 暂存与提交、推送、部署、SQL 执行及外部数据写入分别遵守实际授权。
- **验证结果如实记录**：区分通过、失败、未执行、未核实和不适用，完成结论须有覆盖当前范围的依据。
- **复用已有约定**：遵守适用的 `AGENTS.md` 和用户指令，保留用户修改，优先复用现有资料。
- **按需维护资料**：文档与模板按任务需要使用，临时产物放在目标项目根目录的 `tmp/` 中，并保持可随时删除。
