<h1 align="center">FP</h1>

<p align="center"><strong>一份文件，四部分规范。</strong></p>
<p align="center">从调研复用开始，到文档同步和清理收尾。</p>

<p align="center">
  <a href="https://github.com/MiaoY0uShan/FP/stargazers"><img src="https://img.shields.io/github/stars/MiaoY0uShan/FP?style=social" alt="GitHub stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-22c55e.svg" alt="MIT license"></a>
</p>

<p align="center">
  <a href="fp/SKILL.md"><strong>完整规范</strong></a> ·
  <a href="#四部分规范">四部分规范</a> ·
  <a href="#使用">使用</a> ·
  <a href="#项目结构">项目结构</a>
</p>

---

FP 是面向编程任务的精简开发规范。它关注四件事：先研究已有方案、确定代码归属、同步当前文档，以及清理本轮开发留下的临时内容。

全部规则集中在 [fp/SKILL.md](fp/SKILL.md)，共四部分、24 条。README 用于介绍和导航，规则以该文件为准。

---

## 四部分规范

### 底层开发思维

坚决杜绝闭门造车、重复造轮子。

启动项目或制定较大方案前，优先在 GitHub 查找同类项目、文档和源码，比较多套开源方案。复用前评估许可证、维护状态、安全风险和适配成本；简单问题修复、明确小改动或离线任务可不强制调研。

### 模块边界

编程前先确认代码应该落在哪个模块、组件、服务、钩子、脚本或测试文件中。

已有大文件只做小范围、低风险修改；新增复杂能力先拆分到职责清晰的文件。拆分是开发前的设计动作，避免把新功能和临时验证逻辑继续堆进大文件。

### 文档同步

实现变化时，同步检查 README、开发规范、接口文档和当前状态文档。

优先更新当前执行入口和模块说明，让正文直接描述实际规则；历史说明留给归档文档或变更记录。文档检查属于交付收尾，内部细节调整若不影响使用方式和接口，可以说明无需更新。

### 临时残留代码清理

交付或提交前，检查并清理本轮产生的临时文件、调试输出、一次性脚本、模拟数据和无引用的验证代码。

保留正式业务代码、回归测试、测试夹具、正式文档和有意保留的诊断日志。明确的临时内容自动清理，无法确定的内容列出位置、用途和风险，由用户决定。

---

## 使用

让编程代理读取 [fp/SKILL.md](fp/SKILL.md)，例如：

```text
请先读取 fp/SKILL.md，并在接下来的编程任务中遵循其中的四部分规范。
```

支持技能目录的工具可加载 `fp` 文件夹；也可以将 `SKILL.md` 的正文加入项目现有的代理指令文件。

规范是 Markdown 文本，直接阅读和使用不需要安装运行依赖。

---

## 项目结构

```text
fpskill/
├── fp/
│   └── SKILL.md    # 完整规则与技能元信息
├── README.md       # 项目介绍与使用方式
└── LICENSE         # MIT 许可证
```

---

<p align="center"><strong>调研复用 · 模块边界 · 文档同步 · 临时清理</strong></p>
<p align="center"><a href="fp/SKILL.md">阅读完整规范</a> · <a href="LICENSE">MIT License</a></p>
