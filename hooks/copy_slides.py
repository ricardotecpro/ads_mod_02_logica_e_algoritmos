"""
Hook para copiar slides HTML gerados para o site após build
"""
import shutil
import pathlib
from rich import print


def copy_slides(config, **kwargs):
    """
    Copia slides HTML e Markdown do diretório docs/slides/ para site/slides/
    após o build do MkDocs
    
    Args:
        config: Configuração do MkDocs
        **kwargs: Argumentos adicionais
    """
    site_dir = config['site_dir']
    slides_dest = pathlib.Path(site_dir) / 'slides'
    slides_dest.mkdir(exist_ok=True)
    
    # Diretório fonte dos slides
    slides_source = pathlib.Path('docs/slides')
    slides_src_source = slides_source / 'src'
    
    if not slides_source.exists():
        print("[yellow]WARN: Pasta docs/slides/ não encontrada[/yellow]")
        return
    
    # Copiar todos os slides HTML
    html_copied = 0
    print("[cyan]Copiando slides HTML...[/cyan]")
    for slide in slides_source.glob('slide-*.html'):
        dest_file = slides_dest / slide.name
        shutil.copy(slide.resolve(), dest_file.resolve())
        html_copied += 1
    
    # Copiar Markdown da pasta src
    md_copied = 0
    if slides_src_source.exists():
        print("[cyan]Copiando slides Markdown de src...[/cyan]")
        slides_src_dest = slides_dest / 'src'
        slides_src_dest.mkdir(exist_ok=True)
        
        for slide in slides_src_source.glob('slide-*.md'):
            dest_file = slides_src_dest / slide.name
            shutil.copy(slide.resolve(), dest_file.resolve())
            md_copied += 1
    
    if html_copied > 0:
        print(f"[green]OK: {html_copied} slide(s) HTML copiados[/green]")
    if md_copied > 0:
        print(f"[green]OK: {md_copied} slide(s) Markdown copiados[/green]")
    
    if html_copied == 0 and md_copied == 0:
        print("[yellow]WARN: Nenhum slide encontrado em docs/slides/[/yellow]")


def on_post_build(config):
    """Hook chamado após o build do MkDocs"""
    copy_slides(config)
