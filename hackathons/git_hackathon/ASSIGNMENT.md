# Assignment Instructions (Individual Git Challenges)

## Your Task
- For your git hackathon, the only challenge you are required to complete is challenge 1.
- However!  If you want some extra credit, you can complete the remaining challenges.
- You will get +5 extra credit points PER CHALLENGE added to your assignment 2 grade. 
- That means you can get up to +15 extra points on your assignment 2!
- You will **clone this repo**, then create **your own remote repo** (e.g., on GitHub),
  and push your progress there.
- Make multiple, meaningful commits as you go (not one giant commit).

## Suggested Workflow
1. Clone:
   ```bash
   git clone <URL-to-class-starter>
   cd git_hackathon
   ```
2. Configure Git (once on your machine):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
3. Create your own empty GitHub repo and connect it:
   ```bash
   git remote remove origin   # if this repo already has an origin you cannot write to
   git remote add origin <your-GitHub-URL>
   git push -u origin main    # or 'master', depending on your default
   ```
4. Open your assigned challenge folder and follow `problem.md`.
5. Commit frequently:
   ```bash
   git add -A
   git commit -m "Implement X / fix Y / add tests"
   git push
   ```

## What to Submit
- The URL of your **own** remote repository with your solutions to canvas.


## Pro Tips
- Use `git status` often.
- Commit when you finish a *small* logical change.
- Write messages that complete the sentence “This commit will…”. 
