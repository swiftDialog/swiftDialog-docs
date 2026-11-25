---
title: 项目列表
description: 创建带有状态指示器和图标的动态有序列表
translationSynced: 2026-11-25T05:26:37+00:00
---

项目列表功能允许您以有序的方式展示一定数量的项目。如果列表内容超出可见区域，列表将变为可滚动显示。

列表可以在任何已有的自定义选项的对话框中显示，但图像除外，因为图像会占用整个消息显示区域。

<hr />
创建物品列表有三种方法：

### 1) 命令行

将一个或多个`--listitem <text>`条目指定为命令行参数。列表将按照给定的顺序构建。

列表项的图标可以通过命令行参数进行设置 `--listitem "<text>,icon=<image>"`，但是，如果您需要更高级的选项，则必须使用 JSON 格式。

### 2) JSON 格式

当使用 JSON 作为配置源时，请将各项配置以一维数组的形式指定。

#### 基础

最基本的方法是一种简单的方式，用于创建一份清单，其中每个条目最初都没有设置任何状态。

```json
{
  "listitem" : ["Item 1", "Item 2", "Item 3"]
}
```

#### 高级

“高级”功能允许您初始化一个列表，并可以选择设置图标、状态和状态文本。

```json
{
  "listitem" : [
    {"title" : "Item One", "icon" : "/path/to/image", "status" : "pending", "statustext" : "Pending"},
    {"title" : "Item Two", "icon" : "/path/to/SomeApp.app", "status" : "wait", "statustext" : "Waiting"},
    {"title" : "Item Three", "icon" : "https://some.url/image", "status" : "success", "statustext" : "Winning"}
  ]
}
```

##### 状态选项

列表项的状态可以是 `wait`、`success`、`fail`、`error`、`pending` 或 `progress` 中的一种，并且状态区域会显示相应的图标。

当使用 `progress` 作为状态时，会显示一个圆形进度指示器作为状态图标。 添加一个数字，例如 `progress: 20`，会将指示器动画到适当的位置，以表示需要填充的百分比。 进度指示器可以接受介于 `0` 和 `100` 之间的任何值。

<img width="599" alt="image" src="https://user-images.githubusercontent.com/3598965/182604151-3eabe9b5-3f77-4949-9b88-c522676e3314.png">

#### 每个论点的 JSON 配置

从版本 3.1.1 开始，列表项也可以通过 `--listitem` 以 JSON 对象的形式进行配置（而不是使用整个配置文件的 JSON）。 这样可以提供更直接的控制，尤其适用于具有嵌套图标对象的复杂配置。

**语法：**
```bash
dialog --listitem '{"title":"Download","status":"wait","statustext":"Working…"}'
```

**特性：**
- `title` - 列表项的标签文本。
- `status` - 状态指示器：`wait`、`success`、`fail`、`error`、`pending`、`progress` 或 `progress:<value>` (0-100)。
- `statustext` - 显示在状态指示器旁边的状态文本。
- `icon` - 图标路径、URL，或者**嵌套的 JSON 格式的图标对象**。

**嵌套的图标对象：**

该字段可以接受 JSON 格式的图标对象，用于进行高级的图标配置。`icon`

```bash
# Basic list item with SF Symbol
dialog --listitem '{"title":"Processing","status":"wait","icon":{"sf":"gear","colour":"blue"}}'

# List item with animated icon
dialog --listitem '{"title":"Downloading","status":"progress:50","icon":{"sf":"arrow.triangle.turn","colour":"green","animation":"variable"}}'

# List item with gradient icon
dialog --listitem '{"title":"Installing","status":"wait","icon":{"sf":"arrow.down.circle","colour":"pink","colour2":"purple"}}'

# List item with application icon
dialog --listitem '{"title":"App Installation","status":"success","icon":{"path":"/Applications/MyApp.app"}}'
```

**多项商品：**

```bash
dialog --listitem '{"title":"Step 1","status":"success","statustext":"Complete"}' \
       --listitem '{"title":"Step 2","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}' \
       --listitem '{"title":"Step 3","status":"pending"}'
```

**注意：** 当使用针对每个参数的 JSON 格式时，每个 `--listitem` 都是独立的。 仍然支持整体配置的 JSON 格式，用于批量初始化。


### 3) 作为发送到命令文件的指令

以逗号分隔的值发送各项信息。

`echo "list: Item 1, Item 2, Item 3" >> /var/tmp/dialog.log`


## 更新现有列表

已显示在列表中的条目可以通过向命令文件发送指令进行更新，从而修改其状态。


#### 基础

所需的语法结构如下：

`echo listitem: <list item title>: <status text> >> /var/tmp/dialog.log`

 - `<list item title>` 必须与列表项的名称/标题完全匹配，并且区分大小写。
 - `<status text>` 可以是任何 Unicode 文本字符串。
   - 如果发送了任何支持的状态关键词，则会显示相应的指示符，而不是文本。

#### 高级

高级语法允许您更新状态文本和状态指示器，以及通过索引引用列表项。关键词以逗号分隔的列表形式排列（这意味着 `title` 和 `statustext` 中的内容不能包含逗号）。

`listitem: [title: <title>|index: <index>], status: <status>, statustext: <text>`

`<index>` 从 0 开始。

e.g.

`listitem: index: 0, status: complete, statustext: Item 1 on the list has completed`

可以使用 ``add:`` 命令将新条目添加到现有列表的末尾，可以使用 ``delete:`` 命令删除条目。 添加行时，“状态”和“状态文本”是可选的。

示例：

`echo "listitem: add, title: <title>, statustext: <text>, status: <status>" >> /var/tmp/dialog.log`

按索引删除：`echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log`

按标题引用删除。`echo "listitem: title: Some Row Title, delete:" >> /var/tmp/dialog.log`

即使当前没有显示任何列表，也可以对列表中的项目进行添加或删除操作。

## 显示或隐藏列表

列表可以被命令隐藏或显示，而不会影响列表的内容。

显示 `echo "list: show`

隐藏 `echo "list: hide`

## 删除列表

可以通过向命令文件中发送命令 `list: clear` 来删除现有的列表。

清除一个列表会删除该列表中的所有条目及其相关的状态。

## 例子


`echo "list: Test item 1, Test item 2, Test item 3" >> /var/tmp/dialog.log`

![图片](https://user-images.githubusercontent.com/3598965/151488006-ba027af7-0736-47b2-abdd-ba847491f086.png)

然后，执行以下命令将更新列表状态。

`echo "listitem: Test item 1: Complete ✅" >> /var/tmp/dialog.log`

`echo "listitem: Test item 2: There was an error processing this item ❌" >> /var/tmp/dialog.log`

`echo "listitem: Test item 3: wait" >> /var/tmp/dialog.log`

![图片](https://user-images.githubusercontent.com/3598965/151486051-967e760e-f164-467f-8bd6-dcccba3c7504.png)

#### 高级JSON格式

![图片](https://user-images.githubusercontent.com/3598965/163742836-22fd32e8-8010-467f-a518-b4d348619698.png)