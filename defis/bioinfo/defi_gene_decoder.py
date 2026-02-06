import time
from collections import deque, Counter
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text



CODON_TABLE = {
    "AUG": "START",
    "ACG": "START",
    "AAA": "LYS",
    "AAC": "ASN",
    "AAU": "ASN",
    "GGU": "GLY",
    "GGC": "GLY",
    "GGA": "GLY",
    "GGG": "GLY",
    "UUU": "PHE",
    "UUC": "PHE",
    "CCC": "PRO",
    "CCU": "PRO",
    "CCA": "PRO",
    "CCG": "PRO",
    "GAA": "GLU",
    "GAG": "GLU",
    "CAA": "GLN",
    "CAG": "GLN",

    # codons STOP
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
    "UUA": "STOP",
}



class GeneStatistics:
    def __init__(self):
        self.total_bases = 0
        self.total_codons = 0
        self.total_genes = 0
        self.gc_content = 0.0
        self.invalid_bases = 0

    def get_avg_gene_length(self):
        return 0.0

    def get_quality_score(self):
        return 0.0



class StreamingGenomeDecoder:
    """
    RÈGLES :
    - lecture base par base (streaming)
    - groupement par codons (3 bases)
    - START = début d’un gène
    - STOP = fin d’un gène
    - PAS de retour en arrière
    """

    def __init__(self, validate=True):
        self.validate = validate
        self.stats = GeneStatistics()

    def is_valid_base(self, base):
        # do it
        return True

    def process_base(self, base):
        #do it ;)
        return []



# RENDERING (NE PAS MODIFIER!!!)

def render_stats_panel(stats):

    text = Text()
    text.append(f" Bases: {stats.total_bases}   ", style="cyan")
    text.append(f" Codons: {stats.total_codons}   ", style="green")
    text.append(f" Gènes: {stats.total_genes}\n", style="yellow")
    text.append(f" GC Content: {stats.gc_content:.1f}%   ", style="magenta")
    text.append(f" Longueur moy: {stats.get_avg_gene_length():.1f}\n", style="blue")
    text.append(f" Score qualité: {stats.get_quality_score():.1f}/100", style="bold green")

    if stats.invalid_bases > 0:
        text.append(f"\n/!\\  Bases invalides: {stats.invalid_bases}", style="red")

    return Panel(text, title="[bold]Statistiques en temps réel[/bold]", border_style="blue")


def render_gene_panel(current_gene):
    gene_str = ""
    for token in current_gene:
        if token == "START":
            gene_str += "[bold green]START[/bold green] -> "
        elif token == "STOP":
            gene_str += "[bold red]STOP[/bold red]"
        elif token == "UNKNOWN":
            gene_str += "[yellow]?[/yellow] -> "
        else:
            gene_str += f"[cyan]{token}[/cyan] -> "

    if not gene_str:
        gene_str = "[dim]Aucun gène actif...[/dim]"

    return Panel(gene_str, title="[bold]Gène en construction[/bold]", border_style="green")


def render_table(genome_tape, event_log, decoder):

    table = Table(
        title="[bold magenta]DÉCODEUR DE GÉNOME[/bold magenta]",
        show_lines=True,
        border_style="bright_blue"
    )

    table.add_column("ARN Entrant", width=35)
    table.add_column("Événements récents", width=35)

    genome_display = []
    for base in genome_tape:
        if decoder.is_valid_base(base):
            if base in ("G", "C"):
                genome_display.append(f"[green]{base}[/green]")
            else:
                genome_display.append(f"[yellow]{base}[/yellow]")
        else:
            genome_display.append(f"[bold red]{base}[/bold red]")

    genome_str = " ".join(genome_display)
    events_str = "\n".join(event_log) if event_log else "[dim]En attente...[/dim]"

    table.add_row(genome_str, events_str)
    return table


# MAIN (NE PAS MODIFIER NON PLUS !!!!!!)

if __name__ == "__main__":

    console = Console()
    console.print("[bold cyan]|    DÉCODEUR DE GÉNOME AMÉLIORÉ    |[/bold cyan]")
    console.print("[bold cyan]------------------------------------[/bold cyan]\n")

    genome = (
        "GCUAAGGCCUUGAACCGGAUACCCGUGAAGUUAACCGGGUAACCUAGGCUAAC"
        "GGAUUGCCAAUGGCCUAAXXGAUGGCUAACCGGAUUGCAAGGCUAAC"
    )

    console.print(f"séquence: [italic white]{genome}[/italic white]")
    console.print(f"Longueur: {len(genome)} bases\n")

    decoder = StreamingGenomeDecoder(validate=True)

    genome_tape = []
    event_log = deque(maxlen=8)
    current_gene = []

    with Live(console=console, refresh_per_second=10) as live:
        for base in genome:

            genome_tape.append(base)
            events = decoder.process_base(base)

            for event in events:
                event_type = event[0]

                if event_type == "CODON":
                    codon, token = event[1], event[2]

                    if token == "START":
                        event_log.append(f"[bold green] % {codon} => START[/bold green]")
                    elif token == "STOP":
                        event_log.append(f"[bold red] = {codon} => STOP[/bold red]")
                    elif token == "UNKNOWN":
                        event_log.append(f"[yellow]? {codon} => INCONNU[/yellow]")
                    else:
                        event_log.append(f"[cyan]* {codon} => {token}[/cyan]")

                elif event_type == "START":
                    event_log.append("[bold green]___ DÉBUT DE GÈNE ___[/bold green]")
                    current_gene = []

                elif event_type == "STOP":
                    current_gene = event[1]
                    event_log.append(
                        f"[bold red]___ FIN DE GÈNE ({len(current_gene)} codons) ___[/bold red]"
                    )

                elif event_type == "ERROR":
                    base_err = event[1]
                    event_log.append(f"[bold red]/!\\  ERREUR: '{base_err}' invalide[/bold red]")

            layout = Layout()
            layout.split_column(
                Layout(render_table(genome_tape, list(event_log), decoder), size=12),
                Layout(render_gene_panel(current_gene), size=5),
                Layout(render_stats_panel(decoder.stats), size=7),
            )

            live.update(layout)
            time.sleep(0.25)

    console.print("\n[bold green]Lecture terminée[/bold green]\n")
    console.print(
        Panel(
            f"Bases totales: {decoder.stats.total_bases}\n"
            f"Codons décodés: {decoder.stats.total_codons}\n"
            f"Gènes détectés: {decoder.stats.total_genes}\n"
            f"Score qualité: {decoder.stats.get_quality_score():.1f}/100",
            title="[bold]Résumé[/bold]",
            border_style="yellow"
        )
    )
