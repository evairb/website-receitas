from django.db import models

# Create your models here.


class CategoriaProfissional(models.Model):
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.categoria


class CoordenadoriaHospitalMunicipal(models.Model):
    coordenadoria_hospital = models.CharField(max_length=255)

    def __str__(self):
        return self.coordenadoria_hospital


class SupervisaoTecnica(models.Model):
    supervisao_tecnica = models.CharField(max_length=255)

    def __str__(self):
        return self.supervisao_tecnica


class LocalTrabalho(models.Model):
    local_coordenadoria_hospital = models.ForeignKey(
        'CoordenadoriaHospitalMunicipal',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    local_supervisao_tecnica = models.ForeignKey(
        'SupervisaoTecnica', on_delete=models.SET_NULL, blank=True, null=True)
    local_trabalho = models.CharField(max_length=255)

    def __str__(self):
        return self.local_trabalho


class InformacoePessoal(models.Model):
    cpf = models.CharField(
        max_length=11, null=False, blank=False, verbose_name='CPF'
    )
    email = models.EmailField(verbose_name='E-mail', null=False, blank=False)
    nome = models.CharField(
        max_length=50, null=False, blank=False, verbose_name='Nome'
    )
    sobrenome = models.CharField(
        max_length=80, null=False, blank=False, verbose_name='Sobrenome'
    )
    cidade = models.CharField(
        max_length=80, null=True, blank=True, verbose_name='Cidade'
    )
    pais = models.CharField(
        max_length=70, null=True, blank=True, verbose_name='Pais'
    )
    fone = models.CharField(max_length=14, null=False, blank=False)
    choice_sexo = (
        ('Feminino', 'feminino'),
        ('Masculino', 'masculino'),
        ('Intersexo', 'Intersexo'),
        ('Não-binárion', 'nao-binario'),
        ('Prefiro não declararar', 'nao-declarado'),
    )
    sexo = models.CharField(
        max_length=22, default=None, choices=choice_sexo, verbose_name='Gênero'
    )
    color = (
        ('Branca', 'branca'),
        ('Parda', 'parda'),
        ('Preta', 'preta'),
        ('Amarela', 'amarela'),
        ('Indigena', 'indigena'),
    )
    cor = models.CharField(
        max_length=10, default=None, choices=color, verbose_name='Raça/Cor'
    )
    rg = models.CharField(
        max_length=9, null=False, blank=False
    )
    nome_social = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Nome Social'
    )
    grau_escolaridade = (
        ('Ensino Fundamental', 'fundamental'),
        ('Ensino Médio', 'medio'),
        ('Superior', 'superior'),
        ('Mestrado', 'mestrado'),
        ('Doutorado', 'doutorado'),
    )
    escolaridade = models.CharField(
        max_length=18, default=None, choices=grau_escolaridade
    )
    vinculo_empregaticio = (
        ('Direta PMSP', 'direta-pmsp'),
        ('Organizações Sociais', 'organizacao-social'),
        ('Admitido', 'admitido'),
        ('CLT', 'clt'),
        ('Lei 500', 'lei-500'),
        ('Prestador Externo', 'prestador-externo'),
        ('PJ', 'pj'),
    )
    vinculo = models.CharField(
        max_length=20, default=None, choices=vinculo_empregaticio,
        verbose_name='Vínculo Empregatício'
    )
    registro_funciona = models.CharField(
        max_length=11, null=True, blank=True,
        verbose_name='RF Registro Funcional'
    )
    categoria_profissiona = models.ForeignKey(
        'CategoriaProfissional', on_delete=models.SET_NULL, null=True
    )
    grupos_relatorios = (
        ('ATI T2023 R2', 'ati-t2023-r2'),
        ('BMF T2023 R2', 'bmf-t2023-r2'),
        ('NEO T2023 R2', 'neo-t2023-r2'),
        ('UE T2023 R2', 'ue-t2023-r2'),
        ('PICS T2023 R2', 'pics-t2023-r2'),
        ('ATI T2024 R1', 'ati-t2024-r1'),
        ('BMF T2024 R1', 'bmf-t2024-r1'),
        ('NEO T2024 R1', 'neo-t2024-r1'),
        ('UE T2024 R1', 'ue-t2024-r1'),
        ('PICS T2024 R1', 'pics-t2024-r1'),
        ('BMF T2022 R3', 'bmf-t2022-r3'),
    )
    grupo_relatorio = models.CharField(
        max_length=15, default=None,
        choices=grupos_relatorios,
        verbose_name='Grupo Relatorio'
    )
    ramal = models.CharField(max_length=14, null=False, blank=False)
    local_trabalho = models.ForeignKey(
        'LocalTrabalho', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.cpf
