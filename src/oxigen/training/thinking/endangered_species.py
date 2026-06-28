"""Animais brasileiros ameacados usados como sementes de tarefas de raciocinio."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EndangeredSpecies:
    """Registro pequeno, auditavel e sem pretensao de dataset final."""

    common_name: str
    scientific_name: str
    biome: str
    icmbio_status: str
    iucn_status: str
    threats: tuple[str, ...]
    reasoning_fact: str


ENDANGERED_SPECIES: tuple[EndangeredSpecies, ...] = (
    EndangeredSpecies(
        common_name="Mico-leao-dourado",
        scientific_name="Leontopithecus rosalia",
        biome="Mata Atlantica",
        icmbio_status="Em perigo",
        iucn_status="Endangered",
        threats=("fragmentacao florestal", "perda de habitat", "isolamento genetico"),
        reasoning_fact="Conservacao depende de corredores florestais e manejo populacional.",
    ),
    EndangeredSpecies(
        common_name="Ararinha-azul",
        scientific_name="Cyanopsitta spixii",
        biome="Caatinga",
        icmbio_status="Extinta na natureza",
        iucn_status="Critically Endangered",
        threats=("trafico de fauna", "perda de habitat", "baixa variabilidade genetica"),
        reasoning_fact="Reintroducao exige habitat restaurado, monitoramento e protecao local.",
    ),
    EndangeredSpecies(
        common_name="Onca-pintada",
        scientific_name="Panthera onca",
        biome="Amazonia, Cerrado, Pantanal, Mata Atlantica",
        icmbio_status="Vulneravel",
        iucn_status="Near Threatened",
        threats=("conflito com pecuaria", "desmatamento", "caca retaliatoria"),
        reasoning_fact="Predador de topo indica conectividade e integridade ecologica.",
    ),
    EndangeredSpecies(
        common_name="Tamandua-bandeira",
        scientific_name="Myrmecophaga tridactyla",
        biome="Cerrado, Pantanal, Mata Atlantica",
        icmbio_status="Vulneravel",
        iucn_status="Vulnerable",
        threats=("atropelamento", "queimadas", "perda de habitat"),
        reasoning_fact="Ameacas combinam infraestrutura, fogo e conversao de paisagem.",
    ),
    EndangeredSpecies(
        common_name="Tatu-bola",
        scientific_name="Tolypeutes tricinctus",
        biome="Caatinga, Cerrado",
        icmbio_status="Em perigo",
        iucn_status="Vulnerable",
        threats=("caca", "perda de habitat", "agropecuaria"),
        reasoning_fact="Especie simbolica para conectar conservacao, Caatinga e educacao publica.",
    ),
    EndangeredSpecies(
        common_name="Lobo-guara",
        scientific_name="Chrysocyon brachyurus",
        biome="Cerrado",
        icmbio_status="Vulneravel",
        iucn_status="Near Threatened",
        threats=("perda de habitat", "atropelamento", "doencas de caes domesticos"),
        reasoning_fact="Conservacao passa por paisagem produtiva, rodovias e saude unica.",
    ),
    EndangeredSpecies(
        common_name="Boto-cor-de-rosa",
        scientific_name="Inia geoffrensis",
        biome="Amazonia",
        icmbio_status="Em perigo",
        iucn_status="Endangered",
        threats=("pesca incidental", "mercurio", "barragens", "trafego fluvial"),
        reasoning_fact="Rios conectam biodiversidade, saude humana, energia e economia local.",
    ),
    EndangeredSpecies(
        common_name="Peixe-boi-marinho",
        scientific_name="Trichechus manatus",
        biome="Costa Atlantica",
        icmbio_status="Em perigo",
        iucn_status="Vulnerable",
        threats=("captura acidental", "colisao com embarcacoes", "degradacao costeira"),
        reasoning_fact="Protecao costeira precisa alinhar pesca, turismo e reproducao.",
    ),
    EndangeredSpecies(
        common_name="Muriqui-do-norte",
        scientific_name="Brachyteles hypoxanthus",
        biome="Mata Atlantica",
        icmbio_status="Criticamente em perigo",
        iucn_status="Critically Endangered",
        threats=("fragmentacao", "caca historica", "baixa populacao"),
        reasoning_fact="Primata depende de fragmentos florestais conectados e protegidos.",
    ),
    EndangeredSpecies(
        common_name="Soldadinho-do-araripe",
        scientific_name="Antilophia bokermanni",
        biome="Caatinga",
        icmbio_status="Criticamente em perigo",
        iucn_status="Critically Endangered",
        threats=("perda de nascentes", "urbanizacao", "uso de agua"),
        reasoning_fact="Mostra como agua, microhabitat e conservacao local se conectam.",
    ),
    EndangeredSpecies(
        common_name="Arara-azul-de-lear",
        scientific_name="Anodorhynchus leari",
        biome="Caatinga",
        icmbio_status="Em perigo",
        iucn_status="Endangered",
        threats=("trafico", "perda de licuri", "conflito agricola"),
        reasoning_fact="Dieta e reproducao ligam a especie a palmeiras e manejo comunitario.",
    ),
    EndangeredSpecies(
        common_name="Papagaio-de-cara-roxa",
        scientific_name="Amazona brasiliensis",
        biome="Mata Atlantica costeira",
        icmbio_status="Vulneravel",
        iucn_status="Near Threatened",
        threats=("perda de restingas", "trafico", "pressao urbana"),
        reasoning_fact="Conservacao depende de ilhas, manguezais, restingas e fiscalizacao.",
    ),
    EndangeredSpecies(
        common_name="Gato-maracaja",
        scientific_name="Leopardus wiedii",
        biome="Amazonia, Cerrado, Mata Atlantica",
        icmbio_status="Vulneravel",
        iucn_status="Near Threatened",
        threats=("desmatamento", "fragmentacao", "atropelamento"),
        reasoning_fact="Felino pequeno exige conectividade fina entre fragmentos.",
    ),
    EndangeredSpecies(
        common_name="Cervo-do-pantanal",
        scientific_name="Blastocerus dichotomus",
        biome="Pantanal, Cerrado",
        icmbio_status="Vulneravel",
        iucn_status="Vulnerable",
        threats=("drenagem de areas umidas", "doencas", "perda de habitat"),
        reasoning_fact="Areas umidas conectam biodiversidade, agua e regulacao climatica.",
    ),
    EndangeredSpecies(
        common_name="Jacutinga",
        scientific_name="Aburria jacutinga",
        biome="Mata Atlantica",
        icmbio_status="Em perigo",
        iucn_status="Endangered",
        threats=("caca", "perda de habitat", "fragmentacao"),
        reasoning_fact="Ave dispersora de sementes ajuda a medir regeneracao florestal.",
    ),
    EndangeredSpecies(
        common_name="Tartaruga-de-pente",
        scientific_name="Eretmochelys imbricata",
        biome="Costa Atlantica",
        icmbio_status="Criticamente em perigo",
        iucn_status="Critically Endangered",
        threats=("captura incidental", "plastico", "aquecimento de praias", "comercio ilegal"),
        reasoning_fact="Conservacao exige mar, praia, pesca, turismo e clima no mesmo mapa.",
    ),
)


def find_species(common_name: str) -> EndangeredSpecies | None:
    """Busca simples por nome comum, sem normalizacao linguistica pesada."""

    normalized = common_name.casefold().strip()
    return next(
        (species for species in ENDANGERED_SPECIES if species.common_name.casefold() == normalized),
        None,
    )
