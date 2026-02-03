alias cls='clear'

function add_commit_push() {
    if [ $# -eq 0 ]; then
        echo "Usage: add_commit_push <commit_message>"
        return 1
    fi
    git add .
    git commit -m "$*"
    git push
}
