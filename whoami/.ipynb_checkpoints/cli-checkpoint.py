import click

@click.group()
def cli():
    """Gogo'yu tanıtan küçük bir CLI uygulaması"""
    pass

@cli.command()
def intro():
    """Kendini tanıt"""
    click.echo("👋 Merhaba, ben gogo - PhD Öğrencisi")

@cli.command()
def skills():
    """Yeteneklerini göster"""
    click.echo("🛠️ Python, Veri Analizi, Makine Öğrenmesi, QML")

@cli.command()
def vision():
    """Vizyonunu paylaş"""
    click.echo("🚀 Akademik dünyada ileri görüşlü, disiplinler arası çalışmalar yapıyorum!")

if __name__ == "__main__":
    cli()
