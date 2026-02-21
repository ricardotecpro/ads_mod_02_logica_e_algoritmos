
import os
import re

def fix_slides():
    slides_dir = 'docs/slides/src'
    for filename in os.listdir(slides_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(slides_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Substituir { .fragment } por <!-- .element: class="fragment" -->
            # Lidando com possíveis variações de espaços
            new_content = re.sub(r'\{\s*\.fragment\s*\}', '<!-- .element: class="fragment" -->', content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✓ Corrigida sintaxe em {filename}")
            else:
                print(f"- Nenhuma mudança necessária em {filename}")

if __name__ == "__main__":
    fix_slides()
