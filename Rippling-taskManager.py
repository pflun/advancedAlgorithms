# -*- coding: utf-8 -*-
# https://www.1point3acres.com/interview/problems/company/rippling/task-manager-filter-sort-dedupe
# Pipeline: Dedupe -> Filter -> Sort -> Format & Print

def process_tasks(tasks):
    # Dedupe: 按 description + due_date，保留第一次出现
    seen = set()
    deduped = []
    for task in tasks:
        key = (task.get('description'), task.get('due_date'))
        if key not in seen:
            seen.add(key)
            deduped.append(task)

    # Filter: 无 assignee 且未完成
    filtered = [
        task for task in deduped
        if task.get('assignee') is None and not task.get('is_done', False)
    ]

    # Sort: earliest due_date -> high priority first -> oldest created_at
    # 技巧：(0, value) 排前，(1, '') 代表 None 排最后
    def sort_key(task):
        due = task.get('due_date')
        due_key = (0, due) if due is not None else (1, '')
        priority_key = 0 if task.get('is_high_priority', False) else 1
        created = task.get('created_at')
        created_key = (0, created) if created is not None else (1, '')
        return (due_key, priority_key, created_key)

    sorted_tasks = sorted(filtered, key=sort_key)

    # Format & Print: 如果有父任务，追加 parent 信息
    result = []
    for task in sorted_tasks:
        line = "Task ID: {0}, Description: {1}".format(
            task.get('id'), task.get('description'))
        parent = task.get('parent_task_description')
        if parent:
            line += ", parent: {0}".format(parent)
        print line
        result.append(line)

    return result


# ==================== 测试用例 ====================
tasks = [
    {
        'id': 1,
        'description': 'Fix login bug',
        'due_date': '2026-08-15',
        'created_at': '2026-08-01',
        'is_high_priority': True,
        'assignee': None,
        'is_done': False,
    },
    {
        'id': 2,
        'description': 'Write tests',
        'due_date': '2026-08-10',
        'created_at': '2026-08-02',
        'is_high_priority': False,
        'assignee': None,
        'is_done': False,
    },
    {
        'id': 3,
        'description': 'Fix login bug',   # duplicate of id=1 (same desc + due_date)
        'due_date': '2026-08-15',
        'created_at': '2026-08-03',
        'is_high_priority': False,
        'assignee': None,
        'is_done': False,
    },
    {
        'id': 4,
        'description': 'Deploy to prod',
        'due_date': '2026-08-10',
        'created_at': '2026-08-01',
        'is_high_priority': True,
        'assignee': 'Alice',              # assigned, filtered out
        'is_done': False,
    },
    {
        'id': 5,
        'description': 'Update docs',
        'due_date': '2026-08-10',
        'created_at': '2026-08-01',
        'is_high_priority': False,
        'assignee': None,
        'is_done': True,                  # done, filtered out
    },
    {
        'id': 6,
        'description': 'Code review',
        'due_date': None,                 # None due_date, sorts last
        'created_at': '2026-07-30',
        'is_high_priority': True,
        'assignee': None,
        'is_done': False,
        'parent_task_description': 'Fix login bug',
    },
]

process_tasks(tasks)
# Expected output:
# Task ID: 2, Description: Write tests
# Task ID: 1, Description: Fix login bug
# Task ID: 6, Description: Code review, parent: Fix login bug
