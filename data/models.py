from django.db import models

# Create your models here.


class Cancer(models.Model):
    cancer_name_cn = models.CharField(verbose_name='肿瘤中文名', max_length=10)
    cancer_name_en = models.CharField(verbose_name='肿瘤英文名', max_length=20)
    category_level_1 = models.CharField(verbose_name='等级分类1级', max_length=10)
    category_level_2 = models.CharField(verbose_name='等级分类2级', max_length=10)
    category_level_3 = models.CharField(verbose_name='等级分类3级', max_length=10)
    category_level_4 = models.CharField(verbose_name='等级分类4级', max_length=10)
    category_level_5 = models.CharField(verbose_name='等级分类5级', max_length=10)
    category_level_6 = models.CharField(verbose_name='等级分类6级', max_length=10)
    heredity_model = models.CharField(verbose_name='遗传模型', max_length=20)
    incidence = models.FloatField(verbose_name='发病率')
    mortality = models.FloatField(verbose_name='致死率')
    population_description = models.CharField(
        verbose_name='易患病人群', max_length=100)
    age_choice = models.CharField(verbose_name='年龄偏好', max_length=100)
    gender_choice = models.CharField(verbose_name='性别偏好', max_length=100)
    symptom = models.TextField(verbose_name='症状')
    cancer_descritpion = models.TextField(verbose_name='其它描述')

    class Meta:
        verbose_name = '肿瘤疾病信息'
        verbose_name_plural = '肿瘤疾病信息'


class Panel(models.Model):
    panel_id = models.CharField(verbose_name='Panel编号', max_length=10)
    panel_class = models.CharField(verbose_name='Panel分类', max_length=20)
    panel_abbr = models.CharField(verbose_name='项目简称', max_length=10)
    panel_abbr_pre = models.CharField(verbose_name='项目简称-旧', max_length=4)
    panel_name = models.CharField(verbose_name='项目名称', max_length=100)
    panel_report_index_name = models.CharField(
        verbose_name='Panel在报告封面的名称', max_length=50)
    panel_report_pageheader_name = models.CharField(
        verbose_name='Panel在报告页眉的名称', max_length=50)
    panel_report_type = models.CharField(
        verbose_name='Panel的报告类型', max_length=10, default='ngs')
    panel_library_method = models.CharField(verbose_name='建库方法', max_length=10)
    target_therapy_genes = models.TextField(verbose_name='靶向基因')
    chemo_therapy_genes = models.TextField(verbose_name='化疗基因')
    genetic_counseling_gene = models.TextField(verbose_name='遗传基因')
    immunity_therapy_gene = models.TextField(verbose_name='免疫基因')
    mutation_short_gene = models.TextField(verbose_name='SNP/Indel基因')
    mutation_cnv_gene = models.TextField(verbose_name='CNV基因')
    mutation_fusion_gene = models.TextField(verbose_name='融合基因')
    other_gene = models.TextField(verbose_name='其他基因')
    pharmgkb_sites = models.TextField(verbose_name='pharmGKB特有位点')

    class Meta:
        verbose_name = 'Panel信息'
        verbose_name_plural = 'Panel信息'


class Gene(models.Model):
    gene_name = models.CharField(verbose_name='基因名', max_length=20)
    transcript_id = models.CharField(verbose_name='转录本ID', max_length=20)
    transcript_version = models.PositiveSmallIntegerField(
        verbose_name='转录本版本号')
    lrg_number = models.CharField(verbose_name='LRG编号', max_length=20)
    gene_alias = models.CharField(verbose_name='基因别名', max_length=50)
    gene_description_cn = models.TextField(verbose_name='基因中文描述')
    gene_description_en = models.TextField(verbose_name='基因英文描述')
    driver_tag = models.BooleanField(
        verbose_name='是否Driver Gene', default=False)
    target_therapy_tag = models.BooleanField(
        verbose_name='是否靶向相关', default=False)
    chemo_therapy_tag = models.BooleanField(
        verbose_name='是否化疗相关', default=False)
    genetic_counseling_tag = models.BooleanField(
        verbose_name='是否遗传相关', default=False)
    immunity_therapy_tag = models.BooleanField(
        verbose_name='是否免疫相关', default=False)

    class Meta:
        verbose_name = 'Gene信息'
        verbose_name_plural = 'Gene信息'


class RefGeneFlat(models.Model):
    gene_name = models.CharField(verbose_name='基因名称', max_length=20)
    transcript_id = models.CharField(verbose_name='转录本ID', max_length=20)
    chrom = models.CharField(verbose_name='染色体', max_length=10)
    strand = models.CharField(verbose_name='正负链', max_length=1)
    tx_start = models.PositiveIntegerField(verbose_name='起始位置')
    tx_end = models.PositiveIntegerField(verbose_name='终止位置')
    cds_start = models.PositiveIntegerField(verbose_name='CDS起始位置')
    cds_end = models.PositiveIntegerField(verbose_name='CDS终止位置')
    exon_count = models.PositiveSmallIntegerField(verbose_name='外显子个数')
    exon_starts = models.TextField(verbose_name='各外显子起始位置')
    exon_ends = models.TextField(verbose_name='各外显子终止位置')

    class Meta:
        verbose_name = 'RefGene的位置'
        verbose_name_plural = 'RefGene的位置'


class Mutation(models.Model):
    gene_name = models.CharField(verbose_name='基因名称', max_length=20)
    mutation_position = models.CharField(verbose_name='突变位置描述', max_length=50)
    mutation_hgvs = models.CharField(verbose_name='突变HGVS命名', max_length=20)
    driver_tag = models.BooleanField(verbose_name='是否Driver突变', default=False)
    benign_tag = models.BooleanField(verbose_name='是否良性突变', default=False)
    blacklist_tag = models.BooleanField(verbose_name='是否在黑名单中', default=False)
    whitelist_tag = models.BooleanField(verbose_name='是否在白名单中', default=False)
    core_panel_only_tag = models.BooleanField(
        verbose_name='是否仅在核心Panel中', default=False)
    BRCA_recheck_tag = models.BooleanField(
        verbose_name='是否需要BRCA校正', default=False)
    mnp_benign_tag = models.BooleanField(
        verbose_name='是否mnp良性突变', default=False)
    panel_abbr_specific = models.CharField(
        verbose_name='针对的Panle简称', max_length=50)

    class Meta:
        verbose_name = '突变信息'
        verbose_name_plural = '突变信息'


class Fusion(models.Model):
    host_gene_name = models.CharField(verbose_name='Host基因名', max_length=20)
    partner_gene_name = models.CharField(
        verbose_name='Partner基因名', max_length=20)
    source = models.TextField(verbose_name='信息来源')

    class Meta:
        verbose_name = '融合基因'
        verbose_name_plural = '融合基因'


class OncoKB(models.Model):
    isoform = models.CharField(verbose_name='ENST编号', max_length=50)
    refseq = models.CharField(verbose_name='转录本编号', max_length=50)
    entrez_gene_id = models.PositiveSmallIntegerField(
        verbose_name='Entrez基因ID')
    gene_name = models.CharField(verbose_name='基因名称', max_length=20)
    alteration = models.CharField(verbose_name='突变描述', max_length=100)
    protein_change = models.CharField(verbose_name='蛋白质变化', max_length=50)
    cancer_type = models.CharField(verbose_name='肿瘤类型', max_length=50)
    level = models.CharField(verbose_name='等级', max_length=10)
    drug_name = models.CharField(verbose_name='药物名称', max_length=100)
    drug_article_pmid = models.TextField(verbose_name='药物文章PMID')
    drug_abstract = models.TextField(verbose_name='药物描述')

    class Meta:
        verbose_name = 'OncoKB数据库'
        verbose_name_plural = 'OncoKB数据库'


class OncoKBMutation(models.Model):
    isoform = models.CharField(verbose_name='ENST编号', max_length=50)
    refseq = models.CharField(verbose_name='转录本编号', max_length=50)
    entrez_gene_id = models.PositiveSmallIntegerField(
        verbose_name='Entrez基因ID')
    gene_name = models.CharField(verbose_name='基因名称', max_length=20)
    alteration = models.CharField(verbose_name='突变描述', max_length=100)
    protein_change = models.CharField(verbose_name='蛋白质变化', max_length=50)
    oncogenicity = models.CharField(verbose_name='致癌性', max_length=50)
    mutation_effect = models.CharField(verbose_name='突变效应', max_length=100)
    mutation_effect_article_pmid = models.TextField(verbose_name='突变效应文章PMID')
    mutation_effect_abstract = models.TextField(verbose_name='突变效应描述')

    class Meta:
        verbose_name = 'OncoKB数据库Mutation'
        verbose_name_plural = 'OncoKB数据库Mutation'


class Civic(models.Model):
    gene_name = models.CharField(verbose_name='基因名称', max_length=20)
    entrez_id = models.PositiveSmallIntegerField(verbose_name='Entrez编号')
    variant = models.CharField(verbose_name='突变名称-氨基酸变化', max_length=20)
    disease = models.CharField(verbose_name='肿瘤类型', max_length=50)
    doid = models.PositiveSmallIntegerField(verbose_name='doid')
    phenotypes = models.TextField(verbose_name='表型')
    drugs = models.CharField(verbose_name='药物名', max_length=100)
    drug_iteraction_type = models.CharField(
        verbose_name='药物作用类型', max_length=100)
    evidence_type = models.CharField(verbose_name='证据类型', max_length=20)
    evidence_direction = models.CharField(verbose_name='证据方向', max_length=20)
    evidence_level = models.CharField(verbose_name='证据等级', max_length=20)
    clinical_significance = models.CharField(
        verbose_name='临床重要性', max_length=20)
    evidence_statement = models.TextField(verbose_name='证据描述')
    citation_id = models.CharField(verbose_name='引用的ID', max_length=20)
    source_type = models.CharField(verbose_name='引用的源', max_length=20)
    asco_abstract_id = models.CharField(verbose_name='ASCO摘要ID', max_length=20)
    citation = models.TextField(verbose_name='引用')
    nct_ids = models.TextField(verbose_name='nct_ids')
    rating = models.PositiveSmallIntegerField(verbose_name='Rating')
    evidence_status = models.CharField(verbose_name='证据状态', max_length=20)
    evidence_id = models.CharField(verbose_name='证据ID', max_length=20)
    variant_id = models.CharField(verbose_name='突变ID', max_length=20)
    gene_id = models.CharField(verbose_name='基因ID', max_length=20)
    chrom = models.CharField(verbose_name='染色体', max_length=10)
    start = models.PositiveIntegerField(verbose_name='突变起始位置')
    end = models.PositiveIntegerField(verbose_name='突变终止位置')
    reference_base = models.CharField(verbose_name='参考碱基', max_length=20)
    variant_base = models.CharField(verbose_name='突变碱基', max_length=20)
    representive_transcript = models.CharField(
        verbose_name='ENST编号', max_length=30)
    chrom2 = models.CharField(verbose_name='染色体2', max_length=10)
    start2 = models.PositiveIntegerField(verbose_name='突变起始位置2')
    end2 = models.PositiveIntegerField(verbose_name='突变终止位置2')
    representive_transcript2 = models.CharField(
        verbose_name='ENST编号2', max_length=30)
    ensembl_version = models.CharField(verbose_name='ensembl版本', max_length=5)
    reference_build = models.CharField(
        verbose_name='reference版本', max_length=10)
    variant_summary = models.TextField(verbose_name='突变统计')
    variant_origin = models.CharField(
        verbose_name='突变来源', max_length=10, default='Somatic')
    last_review = models.DateField(verbose_name='review日期')
    evidence_civic_url = models.CharField(
        verbose_name='civic证据链接', max_length=200)
    variant_civic_url = models.CharField(
        verbose_name='civic突变链接', max_length=200)
    gene_civic_url = models.CharField(
        verbose_name='civic基因链接', max_length=200)

    class Meta:
        verbose_name = 'Civic数据库'
        verbose_name_plural = 'Civic数据库'


class PharmGKB(models.Model):
    drug_name = models.CharField(verbose_name='药品名称', max_length=50)
    gene_name = models.CharField(verbose_name='基因名称', max_length=20)
    rs_id = models.CharField(verbose_name='rs ID', max_length=20)
    geno_type = models.CharField(verbose_name='基因型', max_length=50)
    geno_typ_cn = models.CharField(verbose_name='基因型中文', max_length=10)
    clinical_type = models.CharField(verbose_name='临床类型', max_length=50)
    clinical_guide = models.CharField(verbose_name='临床作用', max_length=20)
    evidence_weight = models.IntegerField(verbose_name='证据等级', default=0)
    therapeutic_weight = models.IntegerField(verbose_name='疗效等级', default=0)
    side_effect_weight = models.IntegerField(verbose_name='副作用等级', default=0)
    metabolism = models.CharField(verbose_name='代谢等级', max_length=10)
    cds_strand = models.CharField(verbose_name='链方向', max_length=10)
    transcript_id = models.CharField(verbose_name='转录本ID', max_length=20)
    chrom = models.CharField(verbose_name='染色体', max_length=10)
    start = models.PositiveIntegerField(verbose_name='起始位置')
    end = models.PositiveIntegerField(verbose_name='终止位置')
    pharmgkb_panel = models.TextField(verbose_name='pharmGKB Panel')

    class Meta:
        verbose_name = 'PharmGKB数据库'
        verbose_name_plural = 'PharmGKB数据库'


class Hereditary(models.Model):
    gene_name = models.CharField(verbose_name='基因名称', max_length=20)
    evidence = models.CharField(verbose_name='证据等级', max_length=20)
    risk_level = models.CharField(verbose_name='风险等级', max_length=20)
    cancer_type_cn = models.CharField(verbose_name='肿瘤类型', max_length=20)
    hereditary_model = models.CharField(verbose_name='遗传类型', max_length=20)
    omim_id = models.CharField(verbose_name='OMIM ID', max_length=20)
    description = models.TextField(verbose_name='描述')
    disease_description = models.TextField(verbose_name='疾病描述')
    tumor_profiles = models.TextField(verbose_name='肿瘤profile')

    class Meta:
        verbose_name = '遗传信息'
        verbose_name_plural = '遗传信息'


class ClinicalTrials(models.Model):
    nct_num = models.CharField(verbose_name='NCT编号', max_length=20)
    phase = models.CharField(verbose_name='Phase', max_length=20)
    brief_title = models.CharField(verbose_name='标题', max_length=20)
    intervention_name = models.CharField(verbose_name='干预名称', max_length=20)
    intervention_type = models.CharField(verbose_name='干预类型', max_length=20)
    condition = models.CharField(verbose_name='适应症', max_length=20)
    country = models.CharField(verbose_name='国家', max_length=20)
    overall_status = models.CharField(verbose_name='进度', max_length=20)
    study_first_posted = models.DateField(verbose_name='发布日期')
    brief_summary = models.TextField(verbose_name='介绍')

    class Meta:
        verbose_name = 'ClinicalTrials数据库'
        verbose_name_plural = 'ClinicalTrials数据库'


class ImmunityReport(models.Model):
    gene_name = models.CharField(verbose_name='基因名称', max_length=20)
    clinical_guide = models.TextField(verbose_name='临床指导')
    result = models.CharField(verbose_name='检测结果', max_length=100)
    effect = models.CharField(verbose_name='作用', max_length=20)
    data_info = models.CharField(verbose_name='DataInfo', max_length=10)
    panel = models.CharField(verbose_name='Panel', max_length=20)

    class Meta:
        verbose_name = '报告中免疫信息'
        verbose_name_plural = '报告中免疫信息'
