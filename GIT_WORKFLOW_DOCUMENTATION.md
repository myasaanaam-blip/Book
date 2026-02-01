# توثيق سير عمل Git لمشروع قائمة المهام

## المقدمة
يهدف هذا المستند إلى توضيح سير عمل Git المتكامل من خلال مشروع بسيط لقائمة المهام (To-Do List). سيتم تغطية الأوامر الأساسية لـ Git، إدارة الفروع، عمليات الدمج، وحل التعارضات، مع التركيز على توثيق كل خطوة والالتزامات (commits) التي تمت.

## 1. إعداد المشروع وتهيئة Git

بدأنا بإنشاء مجلد للمشروع وتهيئة مستودع Git داخله. تم تعيين اسم المستخدم والبريد الإلكتروني لضمان ظهور الالتزامات بشكل صحيح.

**الأوامر المنفذة:**
```bash
mkdir my_git_project
cd my_git_project
git init
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

بعد التهيئة، قمنا بتغيير اسم الفرع الافتراضي من `master` إلى `main` وأنشأنا أول ملف `README.md`.

**الأوامر المنفذة:**
```bash
git branch -m main
echo "# To-Do List Project" > README.md
git add README.md
git commit -m "Initial commit: Add README.md"
```

ثم أضفنا الملف الأساسي للتطبيق `todo.py`.

**الأوامر المنفذة:**
```bash
# محتوى ملف todo.py الأولي:
# def main():
#     print("Welcome to the To-Do List Application")
#     tasks = []
#     pass
# if __name__ == "__main__":
#     main()

git add todo.py
git commit -m "Add base structure for todo.py"
```

## 2. إنشاء فروع متعددة وتطوير الميزات وإصلاح الأخطاء

لإظهار سير عمل الفروع، أنشأنا فرعين: أحدهما لتطوير ميزة جديدة (`feature/add-task-functionality`) والآخر لإصلاح خطأ (`bugfix/fix-readme-title`).

### 2.1. تطوير ميزة إضافة المهام

انتقلنا إلى فرع جديد لتطوير ميزة إضافة المهام.

**الأوامر المنفذة:**
```bash
git checkout -b feature/add-task-functionality
```

تم تعديل ملف `todo.py` لإضافة وظيفة `add_task` وعرض المهام.

**الأوامر المنفذة:**
```bash
# محتوى ملف todo.py بعد التعديل:
# def add_task(tasks, task):
#     tasks.append(task)
#     print(f"Task added: {task}")
# def main():
#     print("Welcome to the To-Do List Application")
#     tasks = []
#     add_task(tasks, "Learn Git Commands")
#     add_task(tasks, "Create a project")
#     print("\nYour Tasks:")
#     for task in tasks:
#         print(f"- {task}")
# if __name__ == "__main__":
#     main()

git add todo.py
git commit -m "Feature: Implement add_task functionality and display tasks"
```

### 2.2. إصلاح خطأ في ملف README

عدنا إلى الفرع الرئيسي `main` لإنشاء فرع لإصلاح خطأ.

**الأوامر المنفذة:**
```bash
git checkout main
git checkout -b bugfix/fix-readme-title
```

تم تعديل ملف `README.md` لتحسين العنوان وإضافة قائمة بالأوامر المستخدمة.

**الأوامر المنفذة:**
```bash
# محتوى ملف README.md بعد التعديل:
# # Advanced To-Do List Project with Git Documentation
# This project demonstrates the use of Git commands, branching, and merging.
# ## Commands Used:
# - `git init`
# - `git branch`
# - `git checkout`
# - `git add`
# - `git commit`
# - `git merge`

git add README.md
git commit -m "Bugfix: Update README title and add command list"
```

## 3. تنفيذ عمليات الدمج (Merging)

بعد الانتهاء من تطوير الميزات وإصلاح الأخطاء في الفروع الخاصة بها، قمنا بدمجها في الفرع الرئيسي `main`.

### 3.1. دمج فرع إصلاح الأخطاء (Fast-forward Merge)

تم دمج فرع `bugfix/fix-readme-title` في `main`. نظرًا لعدم وجود تغييرات في `main` منذ إنشاء فرع الإصلاح، تم الدمج بنمط `Fast-forward`.

**الأوامر المنفذة:**
```bash
git checkout main
git merge bugfix/fix-readme-title
```

### 3.2. دمج فرع الميزات (Three-way Merge)

تم دمج فرع `feature/add-task-functionality` في `main`. نظرًا لوجود تغييرات في كلا الفرعين، تم الدمج بنمط `Three-way merge`، مما أدى إلى إنشاء التزام دمج جديد.

**الأوامر المنفذة:**
```bash
git merge feature/add-task-functionality -m "Merge feature/add-task-functionality into main"
```

## 4. حل التعارضات (Conflict Resolution)

لإظهار كيفية التعامل مع التعارضات، قمنا بإنشاء تعارض متعمد في ملف `README.md`.

**الأوامر المنفذة:**
```bash
git checkout -b conflict-test
echo "Conflict line from branch" >> README.md
git add README.md
git commit -m "Add line in conflict-test branch"
git checkout main
echo "Conflict line from main" >> README.md
git add README.md
git commit -m "Add line in main branch"
git merge conflict-test
```

بعد محاولة الدمج، ظهر تعارض في `README.md`. قمنا بقراءة الملف لرؤية علامات التعارض:

**محتوى README.md مع علامات التعارض:**
```
# Advanced To-Do List Project with Git Documentation
...
<<<<<<< HEAD
Conflict line from main
=======
Conflict line from branch
>>>>>>> conflict-test
```

تم حل التعارض يدويًا عن طريق تعديل الملف وإزالة علامات التعارض، ثم تم إضافة الملف المحدث وعمل التزام جديد.

**الأوامر المنفذة:**
```bash
# محتوى README.md بعد حل التعارض:
# # Advanced To-Do List Project with Git Documentation
# ...
# ## Conflict Resolution Example:
# This section shows how we resolved a merge conflict between the main branch and the conflict-test branch.

git add README.md
git commit -m "Resolve merge conflict between main and conflict-test"
```

## 5. رفع المشروع على GitHub (GitHub Integration)

لرفع المشروع إلى GitHub، ستحتاج إلى إنشاء مستودع جديد على GitHub (بدون تهيئة README أو .gitignore) ثم ربط المستودع المحلي به ورفع التغييرات.

**الأوامر المقترحة:**
```bash
git remote add origin <URL_of_your_github_repository>
git push -u origin main
```

## 6. سجل الالتزامات (Git Log)

يمكنك عرض سجل الالتزامات بالكامل باستخدام الأمر `git log`.

**الأمر:**
```bash
git log --oneline --graph --all
```

هذا الأمر سيعرض سجلًا موجزًا ومرئيًا لجميع الالتزامات والفروع.

## الخلاصة

يوضح هذا المشروع كيفية استخدام Git لإدارة التغييرات، العمل على ميزات مختلفة في فروع منفصلة، دمج هذه الفروع، وحل التعارضات التي قد تنشأ. هذه الممارسات أساسية لأي مشروع تطوير جماعي أو فردي لضمان سير عمل منظم وفعال.
