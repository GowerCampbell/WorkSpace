# My Code Snippet Collection 🚀

Welcome to **My-Code-Snippet.md**! This document serves as a collection of useful code snippets for open-source contributions. Whether you're debugging, optimizing, or adding new features, these snippets will help streamline development. 📌

## 1. Git Basics 🛠️

### **Clone a Repository**
Cloning a repository allows you to download a copy of a project to your local machine.
```sh
git clone https://github.com/user/repository.git
```

### **Create a New Branch**
Branches help manage different versions of a project without affecting the main codebase.
```sh
git checkout -b feature-branch
```

### **Stage and Commit Changes**
Before committing, you must stage the changes to include them in your next commit.
```sh
git add .
git commit -m "Your meaningful commit message"
```

### **Push to Remote Repository**
Push your committed changes to the remote repository to share your work.
```sh
git push origin feature-branch
```

## 2. Working with Pull Requests 🤝

### **Fetch and Merge Latest Changes**
Ensure your local branch is up to date with the latest changes from the main repository.
```sh
git fetch upstream
git merge upstream/main
```

### **Rebase Your Branch**
Rebasing helps keep your branch history clean by applying your changes on top of the latest main branch.
```sh
git rebase main
```

## 3. Code Formatting & Linting 🎨

### **Prettier (JavaScript/TypeScript)**
Automatically formats your code according to a consistent style.
```sh
npx prettier --write "src/**/*.js"
```

### **ESLint (JavaScript)**
Lint your JavaScript files to find and fix problems.
```sh
npx eslint "src/**/*.js"
```

## 4. Debugging Tips 🐞

### **Check Logs in Terminal**
Logs provide insight into application behavior and help diagnose issues.
```sh
tail -f /var/log/app.log
```

### **Debug JavaScript in Browser**
Use `console.log` for basic debugging and `debugger` to pause script execution.
```js
console.log("Debugging message");
debugger;
```

## 5. Useful Git Commands 🏆

### **Undo the Last Commit (Soft Reset)**
This removes the last commit while keeping the changes staged.
```sh
git reset --soft HEAD~1
```

### **Remove a File from Staging**
Unstage a file without deleting the changes.
```sh
git reset HEAD filename
```

### **Squash Commits**
Squashing combines multiple commits into one, making history cleaner.
```sh
git rebase -i HEAD~3
```

### **Amend Last Commit**
Modify the last commit message or add new changes to it.
```sh
git commit --amend
```

### **Stash Changes**
Save changes temporarily without committing them.
```sh
git stash
```

### **Apply Stashed Changes**
Retrieve previously stashed changes.
```sh
git stash pop
```

### **View Commit History**
Check a log of all previous commits.
```sh
git log --oneline --graph --decorate --all
```

---
📌 Keep this document updated with new snippets! Happy coding! 🚀
