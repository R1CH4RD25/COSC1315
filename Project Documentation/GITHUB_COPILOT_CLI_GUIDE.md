# 🤖 GitHub Copilot CLI - Quick Reference Guide

**Installed:** October 30, 2025
**Version:** 1.1.1
**Status:** ✅ Active and Configured

---

## 🎯 What Is GitHub Copilot CLI?

GitHub Copilot CLI brings AI assistance directly to your terminal. It can:

- Explain terminal commands in plain English
- Suggest commands based on what you want to do
- Help debug errors and issues
- Generate complex command sequences
- Work with PowerShell, Bash, CMD, etc.

---

## 🚀 Quick Start Commands

### **1. Explain a Command**

Ask Copilot to explain what a command does:

```bash
gh copilot explain "git rebase -i HEAD~3"
```

### **2. Suggest Commands**

Describe what you want to do, get command suggestions:

```bash
gh copilot suggest "find all .py files modified in the last 7 days"
```

### **3. Interactive Mode**

Start an interactive chat session:

```bash
gh copilot
```

Then type your questions naturally!

---

## 💡 Common Use Cases

### **Git Operations**

```bash
gh copilot suggest "commit all changes and push to main branch"
gh copilot suggest "undo last commit but keep changes"
gh copilot explain "git cherry-pick abc123"
```

### **File Management**

```bash
gh copilot suggest "copy all .ipynb files to a backup folder"
gh copilot suggest "find large files over 100MB"
gh copilot suggest "compress all PDFs in current directory"
```

### **Python/Development**

```bash
gh copilot suggest "create a virtual environment and install requirements"
gh copilot suggest "run all tests in the tests folder"
gh copilot explain "python -m pytest -v --cov=src"
```

### **System Administration**

```bash
gh copilot suggest "check disk space and show largest folders"
gh copilot suggest "kill process using port 8080"
gh copilot explain "netstat -ano | findstr :8080"
```

---

## 🎨 Aliases (Optional Shortcuts)

Add these to your PowerShell profile for faster access:

**For PowerShell** (`$PROFILE`):

```powershell
# GitHub Copilot CLI Aliases
function ghcs { gh copilot suggest $args }
function ghce { gh copilot explain $args }
function ghc { gh copilot }
```

**For Bash** (`~/.bashrc` or `~/.bash_profile`):

```bash
alias ghcs='gh copilot suggest'
alias ghce='gh copilot explain'
alias ghc='gh copilot'
```

Then use:

```bash
ghcs "find all python files"
ghce "docker-compose up -d"
ghc  # Start interactive mode
```

---

## 🔧 Configuration

### **Check Status**

```bash
gh copilot --version
gh auth status
```

### **Re-authenticate (if needed)**

```bash
gh auth login --web
```

### **Update Extension**

```bash
gh extension upgrade gh-copilot
```

---

## 📚 Example Workflows

### **Professor Workflow: Lesson Management**

```bash
# Find all lesson files modified today
gh copilot suggest "show all .ipynb files modified today"

# Copy lessons to backup
gh copilot suggest "copy Lessons folder to backup with timestamp"

# Count total lines of Python code
gh copilot suggest "count lines in all .py files recursively"
```

### **Git Workflow: Push Lesson Changes**

```bash
# Interactive: Ask for help
gh copilot
> "I want to commit all changes in the Lessons folder and push to GitHub"

# Or direct command suggestion
gh copilot suggest "stage all changes in Lessons folder, commit with message, and push"
```

### **Debugging: Check Python Environment**

```bash
gh copilot suggest "show all installed Python packages and their versions"
gh copilot explain "pip list --outdated"
```

---

## 🌟 Pro Tips

1. **Be Specific**: More detail = better suggestions

   - ❌ "copy files"
   - ✅ "copy all .ipynb files from Lessons to Backup folder"

2. **Ask for Explanations**: Before running unfamiliar commands

   ```bash
   gh copilot explain "rm -rf node_modules"
   ```

3. **Use Natural Language**: No need for technical jargon

   ```bash
   gh copilot suggest "show me what's taking up space on my disk"
   ```

4. **Chain Commands**: Ask for complex workflows

   ```bash
   gh copilot suggest "create a new branch, copy lesson 8 files, commit, and push"
   ```

5. **Safety First**: Review commands before executing
   - Copilot suggests, YOU verify
   - Especially for destructive operations (rm, del, etc.)

---

## 🆚 Copilot CLI vs VS Code Copilot

| Feature                  | VS Code Copilot       | Copilot CLI    |
| ------------------------ | --------------------- | -------------- |
| **Code Completion**      | ✅ Inline suggestions | ❌ No          |
| **Terminal Commands**    | ⚠️ Limited            | ✅ Specialized |
| **Command Explanations** | ❌ No                 | ✅ Yes         |
| **File Editing**         | ✅ Yes                | ❌ No          |
| **System Operations**    | ⚠️ Via terminal       | ✅ Direct      |
| **Interactive Chat**     | ✅ In editor          | ✅ In terminal |

**Best Practice**: Use both together!

- VS Code Copilot: Write and edit code
- Copilot CLI: Execute commands, manage files, debug

---

## 🐛 Troubleshooting

### **Command Not Found: `gh`**

The terminal hasn't refreshed the PATH. Solutions:

1. **Close and reopen your terminal**
2. Or use full path: `"C:/Program Files/GitHub CLI/gh.exe" copilot`
3. Or refresh PATH in current session:
   ```powershell
   $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine")
   ```

### **"Not Authorized" Error**

Re-authenticate:

```bash
gh auth login --web
```

### **Extension Not Working**

Reinstall:

```bash
gh extension remove gh-copilot
gh extension install github/gh-copilot
```

---

## 📊 Usage Limits

**GitHub Copilot Pro Plan:**

- ✅ Unlimited CLI requests
- ✅ Works with your VS Code subscription
- ✅ No separate billing

**GitHub Copilot Free Plan:**

- ⚠️ Limited requests per month
- Check: `gh copilot --help`

---

## 🎓 Learning Resources

- **Official Docs**: https://docs.github.com/en/copilot/github-copilot-in-the-cli
- **GitHub CLI Docs**: https://cli.github.com/manual/
- **Video Tutorial**: Search "GitHub Copilot CLI tutorial" on YouTube

---

## 🔥 Advanced Examples

### **Batch Operations**

```bash
# Process multiple files
gh copilot suggest "convert all .md files in docs/ to PDF"

# Database operations
gh copilot suggest "export MySQL database to SQL file with timestamp"
```

### **Automation**

```bash
# Create backup script
gh copilot suggest "create a bash script that backs up Lessons folder daily"

# Schedule tasks
gh copilot suggest "schedule a task to run my Python script every Monday at 9am"
```

### **Network & Services**

```bash
# Check service status
gh copilot suggest "check if port 8080 is in use and show the process"

# Test connectivity
gh copilot suggest "test internet connection and show ping statistics"
```

---

## 🎉 You're All Set!

GitHub Copilot CLI is now installed and ready to use. Try it out:

```bash
gh copilot suggest "show me my largest files"
```

**Remember:** Close and reopen your terminal for the `gh` command to work without the full path!

---

**Installed on:** October 30, 2025
**Your GitHub Account:** R1CH4RD25
**CLI Version:** gh 2.81.0
**Copilot Extension:** 1.1.1
**Status:** ✅ Ready to use!
