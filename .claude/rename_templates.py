
import os
import re

def rename_and_update():
    root_dir = ".claude/skills"
    # Files to process based on 'find' output
    # We will walk the directory to be dynamic
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip SKILL_TEMPLATE directory itself if we don't want to mess with it?
        # User said "No agents, hook, skill or SoT files or template should exist without a proper refernacce."
        # And "The only file that should have a _template in the file name is the readme_template.md and EPIC_template.md files."
        # So SKILL_TEMPLATE directory name might be okay, but files inside?
        # Ideally we rename files inside SKILL_TEMPLATE too if they violate.
        
        for filename in filenames:
            if "template" in filename.lower() and filename.endswith(".md"):
                # Handle exclusions
                if filename == "README_template.md" or filename == "EPIC_template.md":
                    continue
                
                # Construct old path
                old_path = os.path.join(dirpath, filename)
                
                # Determine new name
                # Remove -template or _template or template
                new_name = re.sub(r'[-_]?template', '', filename, flags=re.IGNORECASE)
                if new_name == ".md": # Edge case if file was just template.md
                     new_name = "structure.md" 
                
                new_path = os.path.join(dirpath, new_name)
                
                print(f"Renaming {old_path} -> {new_path}")
                os.rename(old_path, new_path)
                
                # Update reference in SKILL.md
                # SKILL.md is usually in the parent of 'assets' or 'references'
                # So if we are in .../assets/, SKILL.md is in .../
                
                # Check for SKILL.md in parent directory
                parent_dir = os.path.dirname(dirpath)
                skill_md_path = os.path.join(parent_dir, "SKILL.md")
                
                target_skill_md = None
                if os.path.exists(skill_md_path):
                    target_skill_md = skill_md_path
                else:
                    # Maybe we are deeper? or in SKILL_TEMPLATE root?
                    # If we are in .claude/skills/SKILL_TEMPLATE/assets, parent is .claude/skills/SKILL_TEMPLATE
                    # which has SKILL.md
                    pass
                
                if target_skill_md and os.path.exists(target_skill_md):
                    print(f"Updating reference in {target_skill_md}")
                    with open(target_skill_md, 'r') as f:
                        content = f.read()
                    
                    # specific replacement to avoid false positives?
                    # filename is unique enough usually
                    if filename in content:
                        new_content = content.replace(filename, new_name)
                        with open(target_skill_md, 'w') as f:
                            f.write(new_content)
                    else:
                        print(f"WARNING: Reference to {filename} not found in {target_skill_md}")

if __name__ == "__main__":
    rename_and_update()
