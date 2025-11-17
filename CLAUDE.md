# Dragon Kit · Claude Code 使用说明

本文件为 Claude Code/Claude Desktop 适配的 Dragon Kit 项目指令集。除非另有说明，所有对 Claude 的交互必须遵循以下约束。

## 1. 交互准则

1. **全程使用专业、易懂的简体中文回复用户**；如需使用其它语言，必须由用户明确指示。
2. **遵循 AGENTS.md 的 6 条核心强制要求**，特别是：充分论证决策、关键步骤前说明意图、复杂改动优先 TDD。
3. 使用 Claude 的多轮能力时，务必在单条消息中给足上下文，避免碎片化请求；引用文件片段时注明路径与行号。
4. 修改文件必须借助 `Read`/`ApplyPatch`/`EditFile` 等工具，保持最小 diff 并说明影响范围与回滚策略。
5. 在对用户输出命令前，先解释执行目的、预期结果及可能风险，待用户确认或无风险时再执行。
6. 如遇权限/网络/依赖问题需立刻声明阻塞，并给出可行的手动补救或重新运行方案。

## 2. Dragon Kit 开发流程

Claude 在此项目中的标准工作流：

1. `/speckit.constitution`：建立或更新项目宪章，澄清团队原则、质量红线、禁用事项。
2. `/speckit.specify`：围绕需求“做什么/为什么”输出结构化规格，禁止提前做技术实现假设。
3. `/speckit.plan`：结合规格与约束，列出技术架构、关键依赖、边界条件与验证策略。
4. `/speckit.tasks`：把计划拆分为可执行任务（串/并行），标注 owner、验收标准与阻塞条件。
5. `/speckit.implement`：严格按任务顺序推进，记录执行状态，确保每一步可回放。

发现规格缺陷或任务遗漏时，必须先运行 `/speckit.clarify`/`/speckit.plan`/`/speckit.tasks` 进行更新后再继续实现。

## 3. Claude 常用命令与目录

| 类型 | 位置 | 说明 |
|------|------|------|
| Slash Commands | `.claude/commands/*.md` | Dragon Kit 自动生成的命令文件；请勿手动覆盖，必要时重新运行 `dragon init` |
| 计划/任务 | `.specify/memory/plan.md`、`tasks.md` | 读取或更新前必须先 `Read` 获取最新内容 |
| 模板脚本 | `.specify/scripts/` | 包含 Bash/PowerShell 脚本，修改后需同步另一个平台版本 |
| 自定义指令 | 当前文件 `CLAUDE.md` | 如需扩展，请新增章节并保持中文描述 |

## 4. 输出与质量要求

- 编写代码前先列出计划：包含目标文件、接口、验证方式；复杂功能先写测试。
- 提交补丁时，引用 `ApplyPatch` 语句，确保 diff 最小化且带必要上下文。
- 所有命令输出使用 fenced code block，并在代码块前后注明上下文或预期影响。
- 发现潜在风险（安全、性能、兼容性）必须主动提示并给出缓解方案。
- 在总结阶段，按“变更概览 / 验证情况 / 风险与后续”格式反馈，保持短句但信息完整。

保持该文件与 `src/dragon_cli/assets/docs/CLAUDE.md` 内容同步，确保 CLI 在复制覆盖时获得相同指令。
