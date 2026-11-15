# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal collection of LeetCode solutions, organized by NeetCode-style topic. There is no build system, package manager, test suite, or linter. Each solution is a standalone file written to be pasted into LeetCode's editor.

## Layout conventions

- `<topic>/<problem-number>.<Title-With-Dashes>/<kebab-case-title>.<ext>`, e.g. `2D-DP/62.Unique-Paths/unique-paths.py`.
- Topic directories are kebab-case (`sliding-window`, `heap-or-priority-queue`), except `1D-DP` and `2D-DP`.
- Most solutions are Python. Some problems also have Java or Go versions in the same folder, named the same way with a different extension.
- Solutions follow LeetCode's signature: a `class Solution` with the problem's method. Helper types such as `ListNode` and `TreeNode` are assumed to come from LeetCode and are not defined. Files have no `if __name__ == "__main__"` harness, so running one directly does nothing.

## Running a solution locally

Nothing is set up for this. To check a solution, add a temporary driver, or run it from the shell without changing the file:

```bash
python3 -c "import importlib.util as u; s=u.spec_from_file_location('m','2D-DP/62.Unique-Paths/unique-paths.py'); m=u.module_from_spec(s); s.loader.exec_module(m); print(m.Solution().uniquePaths(3,7))"
```

## README maintenance

`README.md` has a hand-written "Completed" list, followed by an auto-generated `## Updated Directory` section. Regenerate that section from the repo root with:

```bash
./update-directory
```

The script keeps everything above the `## Updated Directory` heading, then replaces everything below it with the output of `tree .`, so it needs `tree` installed (`brew install tree`). Never hand-edit content below that heading.

## Commits

Commit messages are short and imperative, one per problem, e.g. `Add unique paths` or `Fix koko eating bananas`.
