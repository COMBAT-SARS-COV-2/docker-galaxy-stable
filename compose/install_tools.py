import click

@click.command()
@click.option('--illumina-version', default='latest', help='Illumina (SARS-COV-2) release version')
@click.option('--nanopore-version', default='latest', help='Nanopore (SARS-COV-2) release version')
def download_wf(illumina_version, nanopore_version):
    print(f('illumina: {illumina_version}'))
    print(f('Nanopore: {nanopore_version}'))
    pass

@click.command()
def generate_wf_yml():
    pass

@click.command()
def generate_tools_yml():
    pass

@click.command()
def create_yml():
    pass

@click.command()
def extract_plugins():
    pass

@click.command()
def misc():
    pass

if __name__ == '__main__':
   download_wf()