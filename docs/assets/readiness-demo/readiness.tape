# VHS tape for the README motion proof — "a repo that scores its own readiness".
# Render: brew install vhs && vhs docs/assets/readiness-demo/readiness.tape
# Storyboard + fixture: docs/v2/V2_GO_LIVE_POLISH_PLAN.md §10.3
Output docs/assets/readiness-demo.gif
Set Shell bash
Set FontSize 16
Set Width 1200
Set Height 720
Set Padding 24
Set Theme "Catppuccin Latte"
Set TypingSpeed 40ms

Hide
Type "bash docs/assets/readiness-demo/make-demo.sh prepare && clear"
Enter
Sleep 1s
Show

Type "# PRD-Led Context Engineering — a repo that scores its own readiness"
Enter
Sleep 2s
Type "python3 scripts/readiness.py run --repo /tmp/prd-ce-demo"
Enter
Sleep 6s

Type "# the gate says what to fix first — draft the API contracts it asked for"
Enter
Type "bash docs/assets/readiness-demo/make-demo.sh fix"
Enter
Sleep 1.5s

Type "clear && python3 scripts/readiness.py run --repo /tmp/prd-ce-demo"
Enter
Sleep 6s

Type "# github.com/mattgierhart/PRD-driven-context-engineering — Memory as Infrastructure"
Enter
Sleep 3s

Hide
Type "bash docs/assets/readiness-demo/make-demo.sh clean"
Enter
