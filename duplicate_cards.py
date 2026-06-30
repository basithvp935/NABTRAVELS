import re

file_path = 'c:/NAB TRAVELS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the content inside advance-grid
pattern = r'(<div class="advance-grid">)(.*?)(</div>\s*</div>\s*</section>)'

def replace_func(match):
    prefix = match.group(1)
    cards = match.group(2)
    suffix = match.group(3)
    # Append the original cards again
    return prefix + cards + '\n\n                <!-- Duplicated Cards for Sliding Animation -->\n' + cards + suffix

new_content = re.sub(pattern, replace_func, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully duplicated cards in index.html for slider!")
