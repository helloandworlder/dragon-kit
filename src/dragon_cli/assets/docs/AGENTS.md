# Dragon Kit · 通用编码代理规范（AGENTS）

本文件面向所有对接 Dragon Kit 的 AI 编码代理，用于统一交互语言、信息粒度以及实现流程。除非任务另有说明，必须遵循以下约束。

## 一、核心强制要求（Core Mandatory Rules）

1. **所有面对用户的输出必须采用专业、易懂的简体中文**（All user-facing responses must be in professional, easy-to-read Simplified Chinese）。
2. **推进开发、决策或规划时须提供充分细节，严禁空泛概述**（When making decisions or plans, provide comprehensive details—no vague summaries）。
3. **读写代码或文档时优先使用 `Read`/`ApplyPatch`/`EditFile` 等专用工具；若缺权限需暂停并请求**（Use repository tools such as Read/ApplyPatch/EditFile; stop and request access if denied）。
4. **实现核心或复杂能力时优先采用 TDD；简单需求避免无谓测试**（Prefer TDD for core/complex features; skip only when the task is trivially simple）。
5. **保持架构高内聚、低耦合，职责边界清晰，避免过度封装**（Architectural changes must enforce high cohesion & low coupling; no over-engineering）。
6. **执行重要命令前需说明意图与理由，确保可追溯**（Explain intent & reasoning before running critical commands to guarantee traceability）。

## 二、通用开发流程（参考 `/templates/commands`）

| 阶段 | 对应命令 | 核心动作 |
|------|-----------|----------|
| 需求澄清 | `/speckit.clarify` | 发现风险、补齐需求空白；所有问题一次性给足上下文 |
| 规格输出 | `/speckit.specify` | 产出基线规格，列出业务目标/约束、评价指标 |
| 实施规划 | `/speckit.plan` | 结合 `plan-template.md` 生成可执行架构与技术栈决策 |
| 任务拆解 | `/speckit.tasks` | 依据 `tasks-template.md` 切分阶段、串并行规则与验证点 |
| 研发执行 | `/speckit.implement` | 严格按照任务顺序 + TDD，保持日志、状态追踪 |

在实现阶段，若发现规格/任务缺失，必须先补齐（运行 clarify/plan/tasks）再继续编码，避免直接“想当然”修改。

## 三、执行守则

1. **读文件**：使用 `Read`/`grep` 等只读工具定位上下文；复制大段内容时需注明来源文件与行号。
2. **改文件**：使用 `ApplyPatch` 等工具保持最小差异；必要时解释修改范围、潜在影响与回滚方式。
3. **命令执行**：先向用户说明命令目的，再运行；若命令可能失败或耗时，提供预期输出与风险提示。
4. **验证**：所有变更须运行约定的 lint/test/build（至少 `uv run pytest` 及脚本中列出的校验）；失败时要修复或说明无法通过的原因。
5. **进度跟踪**：复杂任务应维护 Todo（pending → in_progress → completed），并在完成/阻塞时即时更新。
6. **安全与合规**：
   - 严禁在日志或提交中泄露凭证、密钥、token；
   - `.factory/commands`、`.specify/memory` 等目录如含敏感内容，应提示用户加入 `.gitignore`。

## 四、文档与命令（Droid/Dragon 扩展）

1. **.factory/commands**：对接 Droid CLI 的命令文件由 Dragon Kit 自动生成，命令体内已注入「使用说明（中文）」；代理在补充说明时应保持同样语气与排版。
2. **AGENTS/CLAUDE 覆盖**：`dragon init` 支持从 `~/.specify/<DOC>.md` 覆盖项目文档；若任务涉及这些文档需优先读取本地覆盖版本并注明来源层级（全局 vs 项目）。
3. **安装与版本**：默认依赖 `uv tool install dragon-cli --from git+https://github.com/helloandworlder/dragon-kit.git`；如需 CLI/IDE 额外扩展请在方案中列明并给出官方链接。

## 五、质量基线

- **提交前 checklist**：
  1. 是否完全遵循 6 条核心强制要求？
  2. 代码是否通过全部 linters/tests？
  3. 是否解释了复杂命令、变更动机与风险？
  4. 架构/模块边界是否仍清晰？
  5. 如需文档/命令覆盖，是否记录来源并同步至 Todo/说明？

- **回退策略**：所有重要操作（尤其是多文件修改、脚本执行）须提供回滚思路，例如“恢复为 commit X”或“重新运行命令 Y 并附带 --force 标记”。

遵循以上指南，Dragon Kit 即可在多代理/多团队协作中保持统一、可靠的开发体验。若新增规则或命令模板，请同步更新本文件以确保信息一致。
