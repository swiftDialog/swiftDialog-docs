---
title: ICP合同差距分析
description: 对 swiftDialog 和 ignitecli 之间的 IPC 接口协议进行了差距分析，识别了已发现的不足之处、潜在风险，并提出了相应的协议条款，以确保这两个组件之间实现可靠的通信
translationSynced: 2026-11-25T05:38:40+00:00
---

**状态：** 待审核草稿。 **日期：** 2026年6月17日。 **范围：** 运行时进程间通信，涉及`swiftDialog`（检查模式，预设1-6）以及启动和控制它的`ignitecli`。 **代码仓库：**
- swiftDialog — `/Users/henry/Projects/GitHub/swiftDialog`
- ignitecli — `/Users/henry/Projects/GitHub/ignitecli-swift-private`

本文件记录了当前有效的IPC合同，并详细列出了双方在哪些方面仅出于巧合而达成一致，以及哪些方面虽然存在约定，但并未得到执行的情况。每个条款都与一个明确的依据相关联，以便可以进行重新验证。`file:line`

---

## 1. 交通概况

目前有三种传输方式在使用。合同涵盖所有这三种方式；一个可靠的实施方案不能假设任何一种方式是绝对可靠的。

| 交通运输。 | 方向。 | 通道 / 路径 | 有效载荷。 | 可靠性。 |
|---|---|---|---|---|
| 分布式通知（命令）。 | ignitecli → 对话框 | `com.swiftdialog.command` **和** `com.ignitecli.command` | `userInfo` 字典，字符串化。 | 尽力而为，不保证顺序，**如果在观察者注册之前发布，则可能丢失**。 |
| 分布式通知（事件）。 | dialog → ignitecli | `com.swiftdialog.event` | `userInfo` dict incl. `event`, `pid` | 尽力而为。 |
| 分布式通知（确认）。 | dialog → ignitecli | `com.swiftdialog.ack` | `userInfo` dict incl. `command`, `stepId`, `status`, `pid` | 尽力而为，**很少被使用**。 |
| 触发文件/命令文件。 | ignitecli → 对话框 | `--status-log-file` / 每个进程ID (PID) `.command` | 以换行符分隔，以冒号分隔。 | 耐用的，支持字节偏移量跟踪。 |
| 准备文件。 | dialog → ignitecli | `<trigger>.ready` 或者配置 `readinessFile`。 | JSON | 耐用，且具有良好的外观。 |
| 事件文件。 | dialog → ignitecli | 配置`eventFile`或由此派生的数据`.events`。 | JSONL 格式。 | 耐用，无尾巴。 |
| 结果文件。 | dialog → ignitecli | 配置 `resultFile` / 每个进程ID (PID) `.result.json`。 | JSON。 | 耐用的；坚固的。 |
| 已发布会话目录。 | 对话 → *(无人)* | `--published-sessions-dir` (默认设置 `/private/tmp/swiftdialog/sessions/<pid>.json`) | JSON。 | 耐用，**不可消耗**——参见第1条说明。 |
| ignitecli 的进程间通信 (IPC) 状态。 | ignitecli → ignitecli | `/private/tmp/.ignitecli-ipc-<pid>.json` | JSON。 | 耐用的；坚固的。 |

固定点。
- 频道：`dialog/Views/Inspect/Core Framework/DistributedNotifications.swift:36`；
  ignitecli `Sources/Dialog/ActionDispatcher.swift:9`.
- 双通道发布：使用 ignitecli 命令 `Sources/Commands/IpcCommand.swift:414`。
- 命令文件路由：`dialog/Views/Inspect/Core Framework/CommandRouter.swift:76`。
- 已发布的会话目录：`dialog/Command Line/CommandLineArguments.swift:167`。
  `dialog/Views/Inspect/Core Framework/PresetCommonHelpers.swift:1134`.
- ignitecli 的状态：`Sources/Dialog/IpcState.swift:11`。

---

## 2. 活动相关术语（关于合同的条款）

swiftDialog 会触发以下类型的事件（`DistributedNotifications.swift:36`，以及已锁定的原始值）。

| 事件类型。 | 原始数据。 | 当...发生时。 | 关键字段。 |
|---|---|---|---|
| `ready` | `ready` | 用户界面已准备好接收指令。 | `triggerFile`, `preset?`, `itemCount?`, `items?`, `ackChannel` |
| `exit` | `exit` | 即将终止。 | `triggerFile`, `exitCode?`, `completedCount?`, `failedCount?`, `resultFile?` |
| `deferred` | `defer` | 用户已延期。 | `duration`, `seconds`, `exitCode`, `resultFile` |
| `button` | `button` | 按钮点击。 | `stepId`, `button`, `action` |
| `step` | `step` | 过渡步骤。 | `stepId`, `action` (e.g. `completed`, `all_complete`) |
| `selection` | `selection` | 拣选/网格提交。 | `key`, `values` |

预设模式6确认会发出`step`、`button`、`selection`（对应参数为：`Preset6.swift:1251`、`:1116`、`:1638`）。

支持的命令（通过 ignitecli 界面），并按照以下顺序排列：`CommandRouter.swift:76–163`：`success`，`failure`，`warning`，`complete`，`navigate`/`goto`，`next`/`prev`/`back`，`reset`，`progress`，`update_guidance`，`update_message`，`batch_update`，`display_data`，`recheck`，`set`，`item`，`listitem`，`select`。 简写键（`userInfo`）会扩展为上述命令（`DistributedNotifications.swift:177`）。

---

## 3. 漏洞

按照严重程度排序。每个条目描述了**实际情况**、**潜在风险**以及**建议的合同条款**（用于未来共享规范的规范性语言）。

### 问题 1：已发布的会话目录只能写入，`ignitecli` 无法读取。 严重程度：**高**

**Observed.** swiftDialog writes a per-PID discovery file to `/private/tmp/swiftdialog/sessions/<pid>.json` (`PresetCommonHelpers.swift:1134`, CLI `CommandLineArguments.swift:167`). A grep of all of ignitecli `Sources/` finds **no reader** for that directory. ignitecli discovers sessions solely via its own `/private/tmp/.ignitecli-ipc-<pid>.json` (`IpcState.swift:11`), which it wrote at launch.

两个并行的数据记录系统描述的是同一事实（即哪个对话正在哪个触发文件上进行），并且它们永远不会进行同步。

| 注册登记。 | swiftDialog 编写。 | ignitecli 命令用于读取数据。 |
|---|---|---|
| `…/swiftdialog/sessions/<pid>.json` | ✅ | ❌ |
| `…/.ignitecli-ipc-<pid>.json` | ❌ | ✅ |

**风险：** `ignitecli` 只能连接到它自己启动的对话窗口。如果 `ignitecli` 丢失了自己的状态文件（例如，崩溃、重启或被单独调用），即使 `swiftDialog` 正在显示该对话窗口，也无法恢复正在运行的对话。最近推出的发现功能，对它的唯一内置使用者来说，没有任何价值。

**拟议条款。**
> swiftDialog 将会为每次直播会话发布一份记录。 ignitecli 将会...（此处缺少 ignitecli 的具体功能描述）。
> 将已发布的会话目录视为权威的发现来源，并且必须...（后续内容省略，因为原文不完整）。
> 能够采用在该处找到的会话设置（阅读`triggerFile`，`resultFile`）。
> `readinessFile`、`ackChannel`、`pid`），即使没有实际启动它。 ignitecli 的...
> 私有状态文件可能仍然作为启动时的缓存使用，但绝对不能是唯一的缓存文件。
> 权威信息来源。

**开放式决策 (所有者：ignitecli)。** “sessions” 目录是用于 ignitecli 的恢复，还是用于 *外部* 工具（监控/MDM）？ 这个选择将决定 ignitecli 是否会发展出“发现与采用”的功能，或者这个功能将故意保持在独立状态。

### 漏洞 2：事件文件路径由两种不同的规则推导得出。· **中等风险**

**Observed.** swiftDialog resolves the event path as `config.eventFile ?? readinessFile(.ready → .events)` (`Preset5.swift:4834`, identical in `Preset1.swift:460`, `Preset2.swift:533`, and Preset 6). ignitecli templates **always set `eventFile` explicitly** (`Sources/Resources/templates/*/config.json` → `/tmp/__WORKFLOW_NAME__.events`). They converge only because the config always sets the key.

**Risk.** A config that sets a custom `readinessFile` and omits `eventFile` makes swiftDialog derive a path ignitecli's `wait-step` is not watching. `wait-step` (`IpcCommand.swift` WaitStep, 2 s poll) then hangs to its timeout with no diagnostic naming the path mismatch.

**拟议条款。**
> 事件文件的路径必须由一个且只有一个规则确定，并且这个规则适用于双方。
> 如果两端都能从中获得所需的信息（而不需要明确的指示`eventFile`），那么……
> 推导算法的具体内容应在此处完整地列出，并应通过测试进行验证。
> 每个侧面。一个`wait-step`超时时间应包含已解决的事件文件路径。
> 它的错误。

### 漏洞 3：真正重要的服务不应该检查进程的存活状态。· **中等风险**

**观察结果：** `wait-exit` 检查 `kill(pid, 0)` (`IpcState.swift:58`) 时，发现一个无效的对话。 `wait-ready` 和 `wait-step` 正在等待通知或文件变更； `wait-step` 只能在早期检查成功的情况下捕获到无效的进程ID，否则它会等待整个超时时间（`IpcCommand.swift` WaitStep，`:376`）。

**风险：** 如果对话在执行过程中崩溃，原本应该快速且明确地显示失败，但现在会变成一个通用的超时错误，耗时2到600秒，且没有任何具体原因。

**拟议条款。**
> 每位服务员（`wait-ready`，`wait-step`，`wait-exit`）都必须进行调查 `kill(pid,0)`，内容是关于...
> 它的文件/通知检查与主循环同步进行，并且应该快速失败。
> `dialog PID <n> exited before <condition>` 而不是一个通用的超时设置。

### 问题 4：两端都存在确认（ACK）通道，但未将其用作隔离措施。· **中等**

**已观察到。** `swiftDialog` 会在每个路由命令（``CommandRouter.swift:351``）之后向 ``com.swiftdialog.ack`` 发送消息。 `ignitecli` 具有 ``waitAck()`` 功能（``Sources/Dialog/DialogOrchestrator.swift:151``），但大多数工作流程都不会调用它；默认的传输模式是“发送即忘”，依赖于最佳努力的传输方式。

**风险。** 一个被忽略的`navigate`通知，会导致后续预加载批处理出现同步错误，从而在静默状态下影响整个流程。 用户界面中的幂等操作可以容忍数据丢失，但对顺序至关重要的命令则不能。

**拟议条款。**
> 影响后续命令执行的指令（`navigate`、`goto`、`reset`，
> `batch_update` 在 "navigate" 命令之前发送的命令，必须启用确认等待功能。
> `ignitecli` 会在没有收到任何确认信息的情况下，重试该命令，或者报告错误。
> 在确认超时时间内，仍然允许使用“发送并忘记”的方式进行幂等性操作。
> (`progress`, `update_message`, `display_data`).

### 问题 5：触发文件回放可能存在的风险已修复两次，但未明确归属。**风险等级：低至中等**

**已观察到。** `ignitecli` 在启动前删除 IPC 文件 (`DialogLauncher.swift:199`)，以防止 swiftDialog 重新播放过时的 (`success:`) 数据行（即预设的快速闪烁）。 swiftDialog 独立记录初始字节偏移量，以便跳过已存在的内容 (`CommandRouter.swift:79`)。 两个独立的修复措施可以应对一种潜在的风险。

**风险：** 如果出现以下情况，该问题可能会再次出现：一是 swiftDialog 从偏移量 0 再次读取数据，二是 ignitecli 在新的路径中跳过清理操作。在这种情况下，该错误会悄无声息地再次发生。

**拟议条款。**
> swiftDialog 将忽略在它发布内容之前可能存在的任何触发文件内容。`ready`
> 此项保证将由 swiftDialog 负责，并进行相关测试；而 ignitecli 的...
> 发布前的清理工作是防御体系中的一个环节，但它并非主要的安全保障。

### 漏洞 6：所有传输均未进行身份验证（已接受，但未明确说明）。风险等级：**低**

**已观察到：** 分布式通知缺乏发送者验证（API没有提供相关功能）；命令/触发文件具有全球可写权限；会话目录具有全球可读和可枚举权限。 任何本地进程都可以控制或伪造对话，并且可以枚举正在运行的进程ID（PID）以及触发器路径。 新的会话目录*扩大了*这种信息泄露的范围。

**风险：** 在基于同一用户本地信任模型的环境中是可接受的；但如果该假设被打破（例如，共享主机环境或权限较低的共用租户），则存在风险。

**拟议条款。**
> IPC（进程间通信）的信任边界定义为“同一用户、同一主机、本地”。所有传输都基于此信任模型。
> 与当地发货商合作。这是一个经过明确、有记录的假设；没有。
> 传输过程提供身份验证或数据完整性保护。任何超出此范围的部署都...
> 边界超出了支持范围，不提供支持。

---

## 4. 严重程度总结与排序

| # | 盖普（Gap）品牌。 | 严重程度。 | 修复定位。 |
|---|---|---|---|
| 1 | 会话目录，只允许写入。 | 高。 | ignitecli (读取器) |
| 2 | 两个事件路径规则。 | 中等。 | 两者（共享规则）。 |
| 3 | 服务员忽略了顾客的活跃状态。 | 中等。 | ignitecli 命令。 |
| 4 | “Ack”未被用作隔离措施。 | 中等。 | ignitecli (策略) |
| 5 | 已两次修复了重播功能。 | 低至中等。 | swiftDialog (我们提供保证) |
| 6 | 无授权，未明确说明。 | 低。 | 仅限文档。 |

**建议的执行顺序：** 首先，完成第5-6个任务（这些任务仅涉及文档，并且可以立即完成）。然后，同时完成**第1个和第2个任务**——让 `ignitecli` 将已发布的会话目录作为权威的发现来源，并将事件路径推导简化为一条规则。这会将最近的 `swiftDialog` 进程间通信（IPC）相关的代码改造成 `ignitecli` 实际使用的形式。第3-4个任务是独立的 `ignitecli` 稳定性改进，可以在后续进行。

---

## 5. 验证日志

本文件中引用的信息已于2026年6月17日与原始资料进行核对。

- `ignitecli` 无法读取 "sessions" 目录 — 正在搜索 `Sources/`。
  `swiftdialog/sessions` / `publishedSessions`：没有消费者。
- 预设模式6 对应“步进/按钮/选择”功能。`Preset6.swift:1116,1152,1251,1638`
- 事件路径的双重推导 — `Preset1.swift:460`，`Preset2.swift:533`。
  `Preset5.swift:4834`; 使用 `ignitecli` 命令，并明确指定参数。`eventFile` 在 `Sources/Resources/templates/*/config.json` 中。
- 确认已收到，但非强制要求 — `CommandRouter.swift:351`。
  ignitecli `DialogOrchestrator.swift:151`.
- 仅在`wait-exit`和`IpcState.swift:58`中存在活性。
- 发布前清理与跳过字节偏移量 — `DialogLauncher.swift:199`。
  `CommandRouter.swift:79`.
