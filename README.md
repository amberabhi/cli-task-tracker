# 🧠 CLI Task Tracker

A simple command-line-based Task Tracker written in Python.  
You can **add**, **list**, **mark as done**, **update**, **delete**, and **search** your tasks easily — all from your terminal!

---

## 🚀 Features

- 📌 Add tasks with descriptions
- 📋 List tasks (all, pending, or done)
- ✅ Mark tasks as done
- 📝 Update task descriptions
- ❌ Delete tasks
- 🔍 Search tasks by keyword
- 💾 All data is saved locally in a JSON file

---

## 🛠️ Setup Instructions

Follow these steps to set up and use the project on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cli-task-tracker.git
cd cli-task-tracker


## 🛠️ How It Works

All tasks are stored in a local file called `task.json`.  
Each task has the following structure:

```json
{
  "id": 1,
  "description": "Finish the report",
  "status": "pending",
  "created-at": "2025-08-07T14:32:17",
  "updated-at": "2025-08-07T15:01:12"
}
